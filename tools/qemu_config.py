#!/usr/bin/env python3
import os

# Configurações de Caminho
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOOLS_DIR = os.path.join(BASE_DIR, "tools")
ISO_DIR = os.path.join(BASE_DIR, "iso")

# Imagem do FreeBSD 14.3 (Estável e Rápido)
IMAGE_NAME = "FreeBSD-14.3-RELEASE-amd64-ufs.qcow2"
IMAGE_PATH = os.path.join(ISO_DIR, IMAGE_NAME)
IMAGE_URL = "https://download.freebsd.org/releases/VM-IMAGES/14.3-RELEASE/amd64/Latest/FreeBSD-14.3-RELEASE-amd64-ufs.qcow2.xz"

# Configuração da VM
VM_MEM = "4G"
VM_CORES = "4"
SSH_PORT = 2225 # Porta redirecionada para o host

# Configurações de Rede
# hostfwd=tcp::2225-:22 permite acesso SSH via localhost:2225
QEMU_NET_OPTS = f"user,id=net0,hostfwd=tcp::{SSH_PORT}-:22"

# Caminho para os pacotes portados (para sincronização)
PORTS_DIR = BASE_DIR
