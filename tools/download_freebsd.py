#!/usr/bin/env python3
import requests
import os
import subprocess
import sys
from tqdm import tqdm

def download_file(url, target_path):
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
    
    if os.path.exists(target_path):
        print(f"[OK] Imagem {qemu_config.IMAGE_NAME} detectada.")
        return

    print(f"[*] Preparando imagem {qemu_config.IMAGE_NAME}...")
    
    if not os.path.exists(compressed_path):
        if not download_file(url, compressed_path):
            sys.exit(1)
            
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
