#!/usr/bin/env python3

import json
from pathlib import Path

def clean_tibia_json_v2(json_file_path: str) -> None:
    """
    Remove itens adicionais indesejados dos arquivos JSON da Tibia.
    """
    with open(json_file_path, 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    # Lista de itens adicionais a serem removidos
    items_to_remove = [
        "Vampire Bride",
        "Inkwing",
        "Broken Iks Cuirass",
        "Buckle",
        "Cape",
        "Coat", 
        "Doublet"
    ]
    
    # Remove os itens indesejados
    original_count = len(items)
    for item in items_to_remove:
        items.pop(item, None)
    
    # Salva o arquivo limpo
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=2, ensure_ascii=False)
    
    removed_count = original_count - len(items)
    print(f"Removidos {removed_count} itens adicionais de {json_file_path}")

def main():
    json_path = Path("tibia_json")
    
    # Lista de arquivos JSON para limpar
    json_files = [
        "armaduras_items.json",
        "botas_items.json", 
        "calcas_items.json",
        "clavas_items.json",
        "elmos_items.json",
        "espadas_items.json",
        "varinhas_items.json"
    ]
    
    for json_file in json_files:
        file_path = json_path / json_file
        if file_path.exists():
            clean_tibia_json_v2(str(file_path))
        else:
            print(f"Arquivo não encontrado: {file_path}")

if __name__ == "__main__":
    main()
