# HowTo: Porting BlackArch para FreeBSD

## 📋 Visão Geral do Projeto

Este projeto visa portar **centenas de pacotes** de pentesting, red team e cibersegurança do **BlackArch Linux** para o sistema de ports do **FreeBSD 15**. É um projeto ambicioso que demonstra expertise em desenvolvimento de sistemas FreeBSD, automação de infraestrutura e portabilidade de software entre sistemas Unix-like.

### Estatísticas do Projeto

- **2000+ diretórios de ports** - Cada ferramenta tem seu próprio diretório
- **Sistema de automação completo** em Python para validação
- **Ambiente de testes virtualizado** usando QEMU/KVM
- **Automação de boot e configuração** via `pexpect`

## 🛠️ Ferramentas de Automação

### 1. master_validation.py (Orquestrador Principal)

Script que automatiza todo o processo de validação:

**Funcionalidades:**

- Download automático da imagem FreeBSD 14.3
- Configuração de VM QEMU com console serial
- Automação do boot usando `pexpect`
- Configuração automática de SSH
- Sincronização de ports via SCP
- Ambiente interativo para testes

**Fluxo de Execução:**

1. Verifica/baixa a imagem FreeBSD
2. Inicia QEMU com KVM
3. Automatiza o bootloader (seleciona opção 3)
4. Configura console serial no loader
5. Aguarda login e autentica como root
6. Aplica configurações de persistência
7. Configura SSH (root/toor)
8. Sincroniza ports automaticamente
9. Entra em modo interativo

### 2. qemu_config.py (Configurações Centralizadas)

```python
VM_MEM = "4G"           # Memória alocada
VM_CORES = "4"          # Número de cores
SSH_PORT = "2225"       # Porta SSH redirecionada
IMAGE_PATH = "../iso/FreeBSD-14.3-RELEASE-amd64.qcow2"
```

### 3. download_freebsd.py

Automatiza o download da imagem QCOW2 do FreeBSD 14.3-RELEASE:

- Busca a imagem do FreeBSD 14.3
- Baixa o arquivo `.qcow2.xz`
- Extrai automaticamente

### 4. compare_ports.py

Ferramenta para comparar versões de ports entre diferentes branches.

## 🚀 Guia de Uso Rápido

### Método 1: Automação Completa (Recomendado)

```bash
# Navegar para o diretório tools
cd /home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd/tools

# Executar o laboratório automatizado
python3 master_validation.py
```

**O que acontece automaticamente:**

1. ✅ Download da imagem FreeBSD (se necessário)
2. ✅ Inicialização da VM QEMU
3. ✅ Configuração do bootloader
4. ✅ Login automático como root
5. ✅ Configuração de SSH (usuário: root, senha: toor)
6. ✅ Sincronização dos ports via SCP
7. ✅ Ambiente pronto para testes

### Método 2: Passo a Passo Manual

#### Arquitetura do Ambiente

```
┌─────────────────────────────────────────┐
│  🐧 Linux Host (seu computador)         │
│  - Executa QEMU/KVM                     │
│  - Roda master_validation.py            │
│  - Porta 2225 → FreeBSD:22              │
│                                         │
│  ┌───────────────────────────────────┐  │
│  │  🔴 FreeBSD Guest (VM QEMU)       │  │
│  │  - SSH na porta 22 (interna)      │  │
│  │  - Valida ports em /root/         │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

#### Passo 1: Download da Imagem (🐧 Linux Host)

```bash
cd tools
python3 download_freebsd.py
```

**O que acontece:**

- Obtém checksums oficiais do FreeBSD
- Verifica hash SHA256 do arquivo existente
- Pula download se o hash corresponder
- Baixa apenas se necessário

#### Passo 2: Iniciar a VM (🐧 Linux Host)

```bash
python3 master_validation.py
```

**O que acontece:**

- Inicia QEMU com FreeBSD
- Configura boot automático
- Configura SSH (root/toor)
- Sincroniza ports via SCP
- Entra em modo interativo

#### Passo 3: Conectar via SSH (🐧 Linux Host → 🔴 FreeBSD)

**Em um novo terminal no Linux:**

```bash
ssh -p 2225 root@localhost
# Senha: toor
```

**Nota:** Este comando é executado **do Linux** e conecta **ao FreeBSD** rodando na VM.

#### Passo 4: Copiar Ports para a VM (🐧 Linux Host → 🔴 FreeBSD)

**Do Linux Host:**

```bash
scp -P 2225 -r /home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd/* root@localhost:/root/blackarch_ports/
```

**Dentro do FreeBSD (via SSH):**

```bash
mkdir -p /root/blackarch_ports
```

**Nota:** O `master_validation.py` já faz isso automaticamente!

#### Passo 5: Validar os Ports (🔴 FreeBSD Guest)

**Dentro do FreeBSD (via SSH):**

```bash
cd /root/blackarch_ports/tools
chmod +x validate_ports_guest.sh
./validate_ports_guest.sh
```

#### Passo 6: Recuperar Resultados (🔴 FreeBSD → 🐧 Linux Host)

**De volta ao terminal Linux:**

```bash
scp -P 2225 root@localhost:/tmp/validation_results.txt ./validation_results.txt
```

## 📦 Exemplos de Pacotes Portados

### Ferramentas de Exploração

- **metasploit** - Framework de exploração
- **armitage** - GUI para Metasploit
- **beef** - Browser Exploitation Framework

### Scanners e Reconhecimento

- **nmap** - Scanner de rede
- **masscan** - Scanner de portas em massa
- **amass** - Enumeração de subdomínios
- **nuclei** - Scanner de vulnerabilidades

### Testes Web

- **burpsuite** - Proxy de interceptação
- **sqlmap** - Injeção SQL automatizada
- **wpscan** - Scanner WordPress
- **nikto** - Scanner de vulnerabilidades web

### Wireless

- **aircrack-ng** - Suite de auditoria WiFi
- **wifite** - Automatização de ataques WiFi
- **kismet** - Detector de redes wireless

### Active Directory

- **bloodhound** - Análise de AD
- **mimikatz** - Extração de credenciais
- **crackmapexec** - Testes de penetração em AD

### Forense e Análise

- **volatility** - Análise de memória
- **autopsy** - Análise forense
- **binwalk** - Análise de firmware

## 🔧 Detalhes Técnicos

### Automação do Boot

O script `master_validation.py` usa `pexpect` para automatizar:

1. **Bootloader (Opção 3 - Loader Prompt)**

   ```
   set console="comconsole"
   set boot_serial="YES"
   set boot_multicons="YES"
   boot
   ```

2. **Configurações de Persistência**

   ```bash
   sysrc -f /boot/loader.conf console="comconsole"
   sysrc -f /boot/loader.conf boot_serial="YES"
   sysrc -f /boot/loader.conf boot_multicons="YES"
   sysrc sshd_enable="YES"
   ```

3. **Configuração SSH**
   ```bash
   echo "PermitRootLogin yes" >> /etc/ssh/sshd_config
   echo "PasswordAuthentication yes" >> /etc/ssh/sshd_config
   echo "toor" | pw usermod root -h 0
   service sshd restart
   ```

### Configuração QEMU

```bash
qemu-system-x86_64 \
  -m 4G \
  -smp 4 \
  -cpu host \
  -enable-kvm \
  -drive file=FreeBSD-14.3-RELEASE-amd64.qcow2,format=qcow2 \
  -netdev user,id=net0,hostfwd=tcp::2225-:22 \
  -device e1000,netdev=net0 \
  -nographic \
  -serial mon:stdio
```

## 🎯 Casos de Uso

### Para Profissionais de Segurança

- Ambiente de pentesting completo em FreeBSD
- Isolamento de ferramentas em VM
- Testes de segurança em infraestrutura BSD

### Para Pesquisadores

- Análise de malware em ambiente BSD
- Desenvolvimento de exploits
- Pesquisa em segurança de sistemas

### Para Administradores

- Auditoria de segurança de servidores FreeBSD
- Testes de hardening
- Validação de configurações

### Para Desenvolvedores

- Contribuição para o ecossistema FreeBSD
- Aprendizado de porting de software
- Desenvolvimento de ferramentas de segurança

## 📝 Estrutura de Diretórios

```
porting_packages_blackarch_freebsd/
├── README.md                    # Descrição geral do projeto
├── tools/                       # Ferramentas de automação
│   ├── HowTo.md                # Este arquivo
│   ├── README.md               # Documentação das ferramentas
│   ├── master_validation.py    # Orquestrador principal
│   ├── qemu_config.py          # Configurações da VM
│   ├── download_freebsd.py     # Download de imagens
│   ├── compare_ports.py        # Comparação de ports
│   └── validate_ports_guest.sh # Script de validação (guest)
├── iso/                        # Imagens FreeBSD (gerado)
└── [2000+ diretórios de ports] # Um por ferramenta
    ├── 0d1n/
    ├── nmap/
    ├── metasploit/
    └── ...
```

## 🔍 Troubleshooting

### VM não inicia

```bash
# Verificar se KVM está disponível
kvm-ok

# Verificar permissões
ls -la /dev/kvm
```

### SSH não conecta

```bash
# Verificar se a porta está em uso
netstat -tuln | grep 2225

# Testar conectividade
telnet localhost 2225
```

### SCP falha

```bash
# Instalar sshpass (se necessário)
sudo apt-get install sshpass  # Debian/Ubuntu
sudo pacman -S sshpass        # Arch Linux

# Testar manualmente
scp -P 2225 -o StrictHostKeyChecking=no arquivo root@localhost:/tmp/
```

### Compilação de port falha

```bash
# Dentro da VM, verificar dependências
cd /root/blackarch_ports/[nome-do-port]
make missing

# Instalar dependências manualmente
pkg install [dependência]

# Tentar compilação com mais verbosidade
make BATCH=yes clean build
```

## 🎓 Recursos Adicionais

### Documentação FreeBSD

- [FreeBSD Porter's Handbook](https://docs.freebsd.org/en/books/porters-handbook/)
- [FreeBSD Handbook](https://docs.freebsd.org/en/books/handbook/)

### BlackArch

- [BlackArch Package List](https://blackarch.org/tools.html)
- [BlackArch GitHub](https://github.com/BlackArch/blackarch)

### QEMU/KVM

- [QEMU Documentation](https://www.qemu.org/docs/master/)
- [FreeBSD on QEMU](https://wiki.freebsd.org/qemu)

## 💡 Dicas e Boas Práticas

1. **Sempre use snapshots da VM** antes de testes destrutivos
2. **Mantenha a imagem FreeBSD atualizada** regularmente
3. **Documente falhas de compilação** para contribuir upstream
4. **Use BATCH=yes** para builds não-interativos
5. **Teste em ambiente isolado** antes de produção

## 🤝 Contribuindo

Este projeto demonstra:

- ✅ Expertise em FreeBSD e sistemas BSD
- ✅ Automação avançada com Python
- ✅ Conhecimento de ferramentas de segurança
- ✅ Virtualização e infraestrutura como código
- ✅ Portabilidade de software entre Unix-like

---

**Autor:** Mauro Risonho de Paula Assumpção  
**Email:** mauro.risonho@gmail.com  
**Repositório:** [github.com/firebitsbr/porting_blackarch_freebsd](https://github.com/firebitsbr/porting_blackarch_freebsd)  
**Data:** Fevereiro 2026
