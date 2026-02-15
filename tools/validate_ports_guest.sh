#!/bin/sh
# validate_ports_guest.sh
# Este script deve rodar dentro da VM do FreeBSD 14.3

LOG_FILE="/tmp/port_validation.log"
RES_FILE="/tmp/validation_results.txt"

echo "--- Iniciando Validação de Ports BlackArch ---" > $LOG_FILE
echo "--- FreeBSD 14.3 Validation Report ---" > $RES_FILE
date >> $RES_FILE

# Localização dos pacotes montados ou copiados
PORTS_BASE="/root/blackarch_ports"

cd $PORTS_BASE

for port in *; do
    if [ -d "$port" ]; then
        echo "[*] Testando port: $port" | tee -a $LOG_FILE
        cd "$port"
        
        # Tenta compilar
        # BATCH=yes evita prompts interativos
        make BATCH=yes clean build >> $LOG_FILE 2>&1
        
        if [ $? -eq 0 ]; then
            echo "[OK] $port compilado com sucesso" | tee -a $RES_FILE
        else
            echo "[FAIL] $port falhou na compilação" | tee -a $RES_FILE
        fi
        
        # Limpa para poupar espaço
        make clean >> $LOG_FILE 2>&1
        cd ..
    fi
done

echo "--- Validação Concluída ---" | tee -a $RES_FILE
