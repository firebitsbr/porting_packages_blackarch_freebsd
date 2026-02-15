#!/bin/bash
# sync_ports.sh - Sincroniza ports para a VM FreeBSD

set -e

SSH_PORT=2225
SSH_USER="root"
SSH_HOST="localhost"
SSH_PASS="toor"

SOURCE_DIR="/home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd"
TARGET_DIR="/root/blackarch_ports"

echo "[*] Sincronizando ports para a VM FreeBSD..."
echo "[*] Porta SSH: $SSH_PORT"
echo "[*] Origem: $SOURCE_DIR"
echo "[*] Destino: $SSH_USER@$SSH_HOST:$TARGET_DIR"
echo ""

# Verificar se sshpass está instalado
if ! command -v sshpass &> /dev/null; then
    echo "[!] sshpass não encontrado. Instalando..."
    sudo apt-get update && sudo apt-get install -y sshpass
fi

# Testar conectividade SSH
echo "[*] Testando conectividade SSH..."
if ! sshpass -p "$SSH_PASS" ssh -p $SSH_PORT -o StrictHostKeyChecking=no -o ConnectTimeout=5 $SSH_USER@$SSH_HOST "echo 'OK'" &>/dev/null; then
    echo "[!] ERRO: Não foi possível conectar via SSH"
    echo "[!] Certifique-se de que:"
    echo "    1. A VM está rodando (python3 master_validation.py)"
    echo "    2. As chaves SSH foram geradas na VM (ssh-keygen -A)"
    echo "    3. O serviço SSH está rodando (service sshd restart)"
    exit 1
fi

echo "[✓] Conectividade SSH OK"
echo ""

# Sincronizar arquivos (copiando apenas diretórios de ports)
echo "[*] Iniciando sincronização..."
echo "[*] Copiando ports (isso pode levar alguns minutos)..."

# Criar arquivo temporário com lista de diretórios a excluir
EXCLUDE_DIRS="iso tools .git __pycache__ .gemini"

# Copiar todos os diretórios de ports (começam com letras ou números)
cd "$SOURCE_DIR"
for dir in */; do
    dirname="${dir%/}"
    # Pular diretórios especiais
    if echo "$EXCLUDE_DIRS" | grep -qw "$dirname"; then
        echo "[SKIP] $dirname"
        continue
    fi
    
    echo "[COPY] $dirname"
    sshpass -p "$SSH_PASS" scp -P $SSH_PORT \
        -o StrictHostKeyChecking=no \
        -o UserKnownHostsFile=/dev/null \
        -r "$dirname" \
        "$SSH_USER@$SSH_HOST:$TARGET_DIR/" 2>&1 | grep -v "Warning: Permanently added" || true
done

echo ""
echo "[✓] Sincronização concluída!"
echo ""
echo "[*] Para verificar, execute:"
echo "    ssh -p $SSH_PORT $SSH_USER@$SSH_HOST 'ls -la $TARGET_DIR | head -20'"
