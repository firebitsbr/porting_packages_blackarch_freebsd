#!/usr/bin/env python3
"""
Filtra o arquivo port_comparison.csv para criar um novo CSV contendo
apenas os packages que existem no BlackArch mas NÃO existem no FreeBSD.
"""
import csv
import sys
from pathlib import Path

def filter_blackarch_only(input_csv, output_csv):
    """
    Filtra packages que existem apenas no BlackArch.
    
    Args:
        input_csv: Caminho para o arquivo port_comparison.csv
        output_csv: Caminho para o arquivo de saída
    """
    blackarch_only = []
    total_count = 0
    
    print(f"[*] Lendo arquivo: {input_csv}")
    
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            total_count += 1
            port_name = row['Port Name']
            in_freebsd = row['In FreeBSD Security'].strip()
            in_blackarch = row['In BlackArch Porting'].strip()
            
            # Filtra: NÃO no FreeBSD E SIM no BlackArch
            if in_freebsd == 'NÃO' and in_blackarch == 'SIM':
                blackarch_only.append({
                    'Port Name': port_name,
                    'In FreeBSD Security': in_freebsd,
                    'In BlackArch Porting': in_blackarch
                })
    
    print(f"[*] Total de packages analisados: {total_count}")
    print(f"[*] Packages apenas no BlackArch: {len(blackarch_only)}")
    print(f"[*] Escrevendo arquivo: {output_csv}")
    
    # Escreve o arquivo filtrado
    with open(output_csv, 'w', encoding='utf-8', newline='') as f:
        fieldnames = ['Port Name', 'In FreeBSD Security', 'In BlackArch Porting']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(blackarch_only)
    
    print(f"[OK] Arquivo criado com sucesso!")
    print(f"[*] Total de packages para portar: {len(blackarch_only)}")
    
    # Mostra alguns exemplos
    if blackarch_only:
        print("\n[*] Primeiros 10 packages a serem portados:")
        for i, pkg in enumerate(blackarch_only[:10], 1):
            print(f"    {i}. {pkg['Port Name']}")

def main():
    script_dir = Path(__file__).parent
    input_csv = script_dir / 'port_comparison.csv'
    output_csv = script_dir / 'blackarch_only_ports.csv'
    
    if not input_csv.exists():
        print(f"[-] Erro: Arquivo {input_csv} não encontrado!")
        sys.exit(1)
    
    filter_blackarch_only(input_csv, output_csv)

if __name__ == '__main__':
    main()
