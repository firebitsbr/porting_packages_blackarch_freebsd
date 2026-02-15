#!/usr/bin/env python3
import os
import csv

# Paths
FREEBSD_SECURITY_PATH = "/home/test/Documents/Jobs/FreeBSD/src/freebsd-ports/security"
BLACKARCH_PORTING_PATH = "/home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd/"
OUTPUT_CSV = "/home/test/Documents/Jobs/FreeBSD/packages/porting_packages_blackarch_freebsd/tools/port_comparison.csv"

def get_dirs(path):
    if not os.path.exists(path):
        print(f"[!] Erro: Caminho não encontrado -> {path}")
        return set()
    
    # Lista de pastas que não são ports para ignorar no seu projeto
    blacklist = {'.git', '.cache', '.config', '.local', 'iso', 'tools', '__pycache__', '.gemini'}
    
    try:
        return {d for d in os.listdir(path) 
                if os.path.isdir(os.path.join(path, d)) 
                and not d.startswith('.') 
                and d not in blacklist}
    except PermissionError:
        print(f"[!] Erro de permissão: {path}")
        return set()

def main():
    print("[*] Iniciando comparação de ports...")
    
    freebsd_ports = get_dirs(FREEBSD_SECURITY_PATH)
    blackarch_ports = get_dirs(BLACKARCH_PORTING_PATH)
    
    # Union of all unique port names
    all_ports = sorted(list(freebsd_ports.union(blackarch_ports)))
    
    results = []
    for port in all_ports:
        in_freebsd = "SIM" if port in freebsd_ports else "NÃO"
        in_blackarch = "SIM" if port in blackarch_ports else "NÃO"
        results.append({
            "Port Name": port,
            "In FreeBSD Security": in_freebsd,
            "In BlackArch Porting": in_blackarch
        })

    # Detailed statistics
    only_blackarch = blackarch_ports - freebsd_ports
    print(f"[+] Total de ports únicos encontrados: {len(all_ports)}")
    print(f"[+] Ports apenas no seu projeto (novos para FreeBSD): {len(only_blackarch)}")
    
    # Save to CSV
    keys = ["Port Name", "In FreeBSD Security", "In BlackArch Porting"]
    with open(OUTPUT_CSV, 'w', newline='') as f:
        dict_writer = csv.DictWriter(f, fieldnames=keys)
        dict_writer.writeheader()
        dict_writer.writerows(results)
    
    print(f"[OK] Arquivo CSV gerado: {OUTPUT_CSV}")

if __name__ == "__main__":
    main()
