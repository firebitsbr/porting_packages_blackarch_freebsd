# FreeBSD 15 Package Validation Environment

Este diretório contém ferramentas para automatizar o download, configuração e validação de pacotes portados do BlackArch para FreeBSD 15.

## Estrutura

- **download_freebsd.py**: Baixa a imagem QCOW2 do FreeBSD 14.3
- **qemu_config.py**: Configurações centralizadas para a VM (memória, CPU, portas)
- **master_validation.py**: Orquestrador principal que automatiza todo o processo de validação
- **validate_ports_guest.sh**: Script para executar dentro da VM e testar cada port

## Workflow de Uso

### 1. Download da Imagem FreeBSD 14.3

```bash
cd /home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd/tools
python3 download_freebsd.py
```

Isso irá:

- Buscar a imagem do FreeBSD 14.3-RELEASE
- Baixar o arquivo `.qcow2.xz`
- Extrair automaticamente para `../iso/FreeBSD-14.3-RELEASE-amd64.qcow2`

### 2. Iniciar o Ambiente de Validação

```bash
python3 master_validation.py
```

A VM será iniciada automaticamente com:

- 4GB de RAM
- 4 cores de CPU
- SSH disponível em `localhost:2225`
- Console serial configurado
- Sincronização automática de ports

### 3. Copiar os Ports para a VM

Após o boot, conecte-se via SSH:

```bash
ssh -p 2225 root@localhost
```

Dentro da VM, crie o diretório de trabalho:

```bash
mkdir -p /root/blackarch_ports
```

Do host, copie os pacotes portados:

```bash
scp -P 2225 -r /home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd/* root@localhost:/root/blackarch_ports/
```

### 4. Executar a Validação

Dentro da VM:

```bash
cd /root/blackarch_ports/tools
chmod +x validate_ports_guest.sh
./validate_ports_guest.sh
```

O script irá:

- Iterar por cada diretório de port
- Executar `make BATCH=yes clean build`
- Registrar sucessos/falhas em `/tmp/validation_results.txt`

### 5. Recuperar os Resultados

Do host:

```bash
scp -P 2225 root@localhost:/tmp/validation_results.txt ./validation_results.txt
```

## Configurações Personalizadas

Edite `qemu_config.py` para ajustar:

- `VM_MEM`: Memória alocada (padrão: 4G)
- `VM_CORES`: Número de cores (padrão: 4)
- `SSH_PORT`: Porta SSH redirecionada (padrão: 2225)

## Notas Importantes

- A imagem do FreeBSD 14.3-RELEASE é uma versão estável e testada.
- O processo de validação pode levar horas dependendo do número de ports.
- Certifique-se de ter espaço em disco suficiente (~10GB para a imagem + compilações).
