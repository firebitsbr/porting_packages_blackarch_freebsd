#!/usr/bin/env python3
import requests
import os
import subprocess
import sys
import hashlib
from tqdm import tqdm

# URL do arquivo de checksums oficial do FreeBSD
CHECKSUM_URL = "https://download.freebsd.org/releases/VM-IMAGES/14.3-RELEASE/amd64/Latest/CHECKSUM.SHA256"

def calculate_sha256(file_path, chunk_size=65536):
    """
    Calcula o hash SHA256 de um arquivo.
    
    Args:
        file_path: Caminho para o arquivo
        chunk_size: Tamanho do chunk para leitura (64KB padrão)
    
    Returns:
        String hexadecimal do hash SHA256
    """
    sha256_hash = hashlib.sha256()
    file_size = os.path.getsize(file_path)
    
    print(f"[*] Calculando SHA256 de {os.path.basename(file_path)}...")
    
    with open(file_path, 'rb') as f, tqdm(
        total=file_size, unit='iB', unit_scale=True, desc="Verificando"
    ) as pbar:
        for chunk in iter(lambda: f.read(chunk_size), b''):
            sha256_hash.update(chunk)
            pbar.update(len(chunk))
    
    return sha256_hash.hexdigest()

def get_official_checksum(filename):
    """
    Obtém o checksum oficial do FreeBSD para um arquivo específico.
    
    Args:
        filename: Nome do arquivo (ex: FreeBSD-14.3-RELEASE-amd64-ufs.qcow2.xz)
    
    Returns:
        String do hash SHA256 ou None se não encontrado
    """
    try:
        print(f"[*] Obtendo checksums oficiais do FreeBSD...")
        response = requests.get(CHECKSUM_URL, timeout=10)
        response.raise_for_status()
        
        # Parse do arquivo CHECKSUM.SHA256
        for line in response.text.splitlines():
            if filename in line:
                # Formato: SHA256 (filename) = hash
                parts = line.split('=')
                if len(parts) == 2:
                    return parts[1].strip()
        
        print(f"[-] Aviso: Checksum para {filename} não encontrado no servidor")
        return None
        
    except Exception as e:
        print(f"[-] Aviso: Não foi possível obter checksums oficiais: {e}")
        return None

def verify_file_integrity(file_path, expected_hash=None):
    """
    Verifica a integridade de um arquivo comparando com o hash oficial.
    
    Args:
        file_path: Caminho para o arquivo
        expected_hash: Hash esperado (opcional, será buscado se não fornecido)
    
    Returns:
        True se o hash corresponde, False caso contrário
    """
    if not os.path.exists(file_path):
        return False
    
    filename = os.path.basename(file_path)
    
    # Obtém o hash oficial se não foi fornecido
    if expected_hash is None:
        expected_hash = get_official_checksum(filename)
        if expected_hash is None:
            print(f"[!] Não foi possível verificar integridade (checksum não disponível)")
            return False
    
    # Calcula o hash do arquivo local
    actual_hash = calculate_sha256(file_path)
    
    # Compara os hashes
    if actual_hash.lower() == expected_hash.lower():
        print(f"[OK] Verificação de integridade: PASSOU ✓")
        print(f"     SHA256: {actual_hash}")
        return True
    else:
        print(f"[-] Verificação de integridade: FALHOU ✗")
        print(f"     Esperado: {expected_hash}")
        print(f"     Obtido:   {actual_hash}")
        return False

def download_file(url, target_path):
    """
    Baixa um arquivo com barra de progresso.
    
    Args:
        url: URL do arquivo
        target_path: Caminho de destino
    
    Returns:
        True se o download foi bem-sucedido, False caso contrário
    """
    print(f"[*] Baixando: {url}")
    try:
        response = requests.get(url, stream=True, timeout=30)
        response.raise_for_status()
        total_size = int(response.headers.get('content-length', 0))
        
        with open(target_path, 'wb') as f, tqdm(
            total=total_size, unit='iB', unit_scale=True, desc="Download"
        ) as pbar:
            for chunk in response.iter_content(chunk_size=65536):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
        
        # Verify if downloaded size matches content-length
        if total_size > 0 and os.path.getsize(target_path) < total_size:
            print(f"[-] Erro: Download incompleto ({os.path.getsize(target_path)}/{total_size} bytes)")
            os.remove(target_path)
            return False
            
        return True
    except Exception as e:
        print(f"[-] Erro no download: {e}")
        if os.path.exists(target_path):
            os.remove(target_path)
        return False

def main():
    import qemu_config
    iso_dir = qemu_config.ISO_DIR
    os.makedirs(iso_dir, exist_ok=True)
    
    url = qemu_config.IMAGE_URL
    compressed_name = url.split("/")[-1]
    compressed_path = os.path.join(iso_dir, compressed_name)
    target_path = qemu_config.IMAGE_PATH
    
    # Verifica se a imagem final já existe
    if os.path.exists(target_path):
        print(f"[OK] Imagem {qemu_config.IMAGE_NAME} detectada.")
        return

    print(f"[*] Preparando imagem {qemu_config.IMAGE_NAME}...")
    
    # Obtém o checksum oficial
    official_hash = get_official_checksum(compressed_name)
    
    # Verifica se o arquivo compactado já existe e se está íntegro
    if os.path.exists(compressed_path):
        print(f"[*] Arquivo compactado encontrado: {compressed_name}")
        
        if official_hash:
            if verify_file_integrity(compressed_path, official_hash):
                print(f"[OK] Arquivo já baixado e verificado. Pulando download.")
            else:
                print(f"[!] Arquivo corrompido. Baixando novamente...")
                os.remove(compressed_path)
                if not download_file(url, compressed_path):
                    sys.exit(1)
                
                # Verifica o arquivo recém-baixado
                if official_hash and not verify_file_integrity(compressed_path, official_hash):
                    print(f"[-] ERRO CRÍTICO: Arquivo baixado está corrompido!")
                    os.remove(compressed_path)
                    sys.exit(1)
        else:
            print(f"[!] Checksum oficial não disponível. Usando arquivo existente.")
    else:
        # Baixa o arquivo
        if not download_file(url, compressed_path):
            sys.exit(1)
        
        # Verifica o arquivo recém-baixado
        if official_hash and not verify_file_integrity(compressed_path, official_hash):
            print(f"[-] ERRO CRÍTICO: Arquivo baixado está corrompido!")
            os.remove(compressed_path)
            sys.exit(1)
            
    # Extrai o arquivo se necessário
    if compressed_name.endswith(".xz"):
        print(f"[*] Extraindo {compressed_name}...")
        try:
            # Use subprocess for better control
            result = subprocess.run(["unxz", "-k", "-f", compressed_path], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"[-] Erro na extração: {result.stderr}")
                if os.path.exists(compressed_path):
                    os.remove(compressed_path) # Remove corrupted xz
                sys.exit(1)
                
            # Check if extracted file exists
            extracted_file = compressed_path.replace(".xz", "")
            if not os.path.exists(extracted_file):
                 print("[-] Erro: Arquivo extraído não encontrado.")
                 sys.exit(1)
                 
            if extracted_file != target_path:
                os.rename(extracted_file, target_path)
                
            print("[OK] Extração concluída com sucesso.")
        except Exception as e:
            print(f"[-] Falha catastrófica: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()
