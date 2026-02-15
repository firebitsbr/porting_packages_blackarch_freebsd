#!/usr/bin/env python3
import os
import sys
import subprocess
import time
import pexpect

# Local imports
import qemu_config
import download_freebsd

def ensure_image():
    """Ensures the FreeBSD image is ready for QEMU."""
    print("\n--- [1/3] Verificando Ambiente ---")
    download_freebsd.main()
    if not os.path.exists(qemu_config.IMAGE_PATH):
        print(f"[-] ERRO CRÍTICO: Imagem {qemu_config.IMAGE_PATH} não encontrada.")
        sys.exit(1)

def run_lab():
    """Launches QEMU and automates the boot/provisioning process."""
    print("\n--- [2/3] Iniciando Laboratório Automático ---")
    
    cmd = [
        "qemu-system-x86_64",
        "-m", qemu_config.VM_MEM,
        "-smp", qemu_config.VM_CORES,
        "-cpu", "host",
        "-enable-kvm",
        "-drive", f"file={qemu_config.IMAGE_PATH},format=qcow2",
        "-netdev", qemu_config.QEMU_NET_OPTS,
        "-device", "e1000,netdev=net0",
        "-nographic",
        "-serial", "mon:stdio"
    ]
    
    print(f"[*] Comando QEMU: {' '.join(cmd)}")
    child = pexpect.spawn(" ".join(cmd), encoding='utf-8', timeout=600)
    child.logfile = sys.stdout

    try:
        # Bootloader Automation
        print("\n[*] Aguardando menu de boot...")
        child.expect('Autoboot', timeout=60)
        
        print("\n[*] Selecionando Opção 3 (Loader Prompt)...")
        child.send('3')
        child.expect(['OK', 'loader>'], timeout=30)
        
        # Buffer stability
        child.sendline('')
        child.expect(['OK', 'loader>'], timeout=10)
        
        print("[*] Configurando Console Serial...")
        for cmd_str in ['set console="comconsole"', 'set boot_serial="YES"', 'set boot_multicons="YES"']:
            for char in cmd_str:
                child.send(char)
                time.sleep(0.02)
            child.sendline('')
            child.expect(['OK', 'loader>'], timeout=10)
        
        print("[*] Comando: boot")
        child.sendline('boot')

        # OS Boot & Login
        print("\n[*] Aguardando Login (FreeBSD 14.3)...")
        # Boot pode demorar devido a inicialização de serviços, expansão de filesystem, etc.
        child.expect('login:', timeout=600)
        
        print("\n[*] Logando como root...")
        child.sendline('root')
        
        i = child.expect(['Password:', '#', 'root@'], timeout=10)
        if i == 0:
            child.sendline('')
            child.expect(['#', 'root@'], timeout=10)
            
        print("\n[*] Aplicando configurações de persistência e SSH...")
        # Usamos sysrc -f para o loader.conf pois ele pode não existir inicialmente
        commands = [
            'sysrc -f /boot/loader.conf console="comconsole"',
            'sysrc -f /boot/loader.conf boot_serial="YES"',
            'sysrc -f /boot/loader.conf boot_multicons="YES"',
            'sysrc sshd_enable="YES"',
            'echo "PermitRootLogin yes" >> /etc/ssh/sshd_config',
            'echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config',
            'echo "toor" | pw usermod root -h 0',
            'service sshd restart',
            'mkdir -p /root/blackarch_ports'
        ]
        
        for i, c in enumerate(commands, 1):
            print(f"[{i}/{len(commands)}] Executando: {c[:50]}...")
            child.sendline(c)
            time.sleep(0.5)  # Aguarda o comando ser processado
            
            # Usa regex mais flexível para detectar o prompt
            try:
                child.expect([r'root@.*[#\$]', r'#\s*$', r'root@'], timeout=20)
            except pexpect.TIMEOUT:
                print(f"[!] Timeout no comando, tentando continuar...")
                child.sendline('')  # Envia newline extra
                time.sleep(0.3)
                try:
                    child.expect([r'root@.*[#\$]', r'#'], timeout=5)
                except:
                    print(f"[!] Comando pode ter falhado, mas continuando...")
            
            time.sleep(0.2)  # Pequeno delay entre comandos

        print("\n[*] [PRO] Sincronizando ports via SCP automático...")
        try:
            # Copiar apenas os diretórios de ports, excluindo tools, iso, .git, etc.
            source = qemu_config.BASE_DIR
            excludes = "--exclude='tools' --exclude='iso' --exclude='.git' --exclude='__pycache__' --exclude='.gemini'"
            scp_cmd = f"sshpass -p toor scp -P {qemu_config.SSH_PORT} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null -r {excludes} {source}/* root@localhost:/root/blackarch_ports/"
            print(f"[*] Executando SCP de: {source}")
            # Capturar stderr para debug mas não mostrar warnings de SSH
            result = subprocess.run(scp_cmd, shell=True, capture_output=True, text=True)
            if result.returncode == 0:
                print("[OK] Sincronização básica concluída.")
            else:
                print(f"[!] SCP retornou código {result.returncode}")
                if result.stderr and "scp:" in result.stderr:
                    print(f"[!] Erro: {result.stderr[:200]}")
        except Exception as e:
            print(f"[!] SCP automático falhou: {e}")
        
        print("\n--- [3/3] LABORATÓRIO CONFIGURADO ---")
        print("[*] Usuário: root | Senha: toor")
        print(f"[*] SSH: ssh -p {qemu_config.SSH_PORT} root@localhost")
        print("\n[*] Entrando em modo interativo. Use Ctrl+] para sair.")
        
        # IMPORTANTE: Desativar logfile antes do interact para evitar TypeError (str/bytes) em Python 3
        child.logfile = None
        child.interact()

    except Exception as e:
        print(f"\n[-] Erro na automação: {e}")
        child.close()

def main():
    print("====================================================")
    print("   FreeBSD 14.3 BlackArch Validation Lab Master     ")
    print("====================================================")
    ensure_image()
    run_lab()

if __name__ == "__main__":
    main()
