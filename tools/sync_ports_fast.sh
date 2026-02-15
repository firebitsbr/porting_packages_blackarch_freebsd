#!/bin/bash
# sync_ports_fast.sh - Sincronização rápida usando tar+ssh

set -e

SSH_PORT=2225
SSH_USER="root"
SSH_HOST="localhost"
SSH_PASS="toor"

SOURCE_DIR="/home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd"
TARGET_DIR="/root/blackarch_ports"

echo "[*] Sincronização Rápida de Ports para FreeBSD VM"
echo "[*] Usando tar+ssh para transferência eficiente"
echo ""

# Testar conectividade
echo "[*] Testando conectividade SSH..."
if ! sshpass -p "$SSH_PASS" ssh -p $SSH_PORT -o StrictHostKeyChecking=no -o ConnectTimeout=5 $SSH_USER@$SSH_HOST "echo 'OK'" &>/dev/null; then
    echo "[!] ERRO: Não foi possível conectar via SSH"
    exit 1
fi
echo "[✓] SSH OK"

# Contar ports
cd "$SOURCE_DIR"
TOTAL_PORTS=$(ls -1d */ 2>/dev/null | grep -v -E '^(iso|tools|\.git|__pycache__|\.gemini)/' | wc -l)
echo "[*] Total de ports a sincronizar: $TOTAL_PORTS"
echo ""

# Criar tarball e enviar via pipe SSH
echo "[*] Criando e enviando tarball..."
tar czf - \
    --exclude='iso' \
    --exclude='tools' \
    --exclude='.git' \
    --exclude='__pycache__' \
    --exclude='.gemini' \
    --exclude='*.tar.gz' \
    --exclude='*.qcow2' \
    */ 2>/dev/null | \
    sshpass -p "$SSH_PASS" ssh -p $SSH_PORT \
        -o StrictHostKeyChecking=no \
        -o UserKnownHostsFile=/dev/null \
        $SSH_USER@$SSH_HOST \
        "cd $TARGET_DIR && tar xzf -"

if [ $? -eq 0 ]; then
    echo ""
    echo "[✓] Sincronização concluída com sucesso!"
    echo ""
    echo "[*] Verificando na VM..."
    sshpass -p "$SSH_PASS" ssh -p $SSH_PORT \
        -o StrictHostKeyChecking=no \
        -o UserKnownHostsFile=/dev/null \
        $SSH_USER@$SSH_HOST \
        "cd $TARGET_DIR && echo 'Ports sincronizados:' && ls -1 | wc -l && echo '' && echo 'Primeiros 20:' && ls -1 | head -20"
else
    echo "[!] Erro na sincronização"
    exit 1
fi
