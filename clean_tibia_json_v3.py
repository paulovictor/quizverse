#!/usr/bin/env python3

import json
from pathlib import Path

def clean_tibia_json_v3(json_file_path: str) -> None:
    """
    Remove itens que não pertencem à categoria correta dos arquivos JSON da Tibia.
    """
    with open(json_file_path, 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    # Itens que não pertencem a botas
    boots_items_to_remove = [
        "Phantasmal Axe",
        "Umbral Master Crossbow", 
        "Lion Shield",
        "Amber Wand",
        "Golden Newspaper",
        "Flawless Ice Crystal",
        "Bar of Gold",
        "Ultimate Healing Rune",
        "Golden Hyena Pendant",
        "Star Ring",
        "Orange Key",
        "Ultimate Health Potion"
    ]
    
    # Itens que não pertencem a calças
    legs_items_to_remove = [
        "Sanguine Boots",
        "Phantasmal Axe",
        "Umbral Master Crossbow",
        "Lion Shield", 
        "Amber Wand",
        "Golden Newspaper",
        "Flawless Ice Crystal",
        "Bar of Gold",
        "Ultimate Healing Rune",
        "Golden Hyena Pendant",
        "Star Ring",
        "Orange Key",
        "Ultimate Health Potion"
    ]
    
    # Determina quais itens remover baseado no arquivo
    file_name = Path(json_file_path).name
    if "botas" in file_name:
        items_to_remove = boots_items_to_remove
    elif "calcas" in file_name:
        items_to_remove = legs_items_to_remove
    else:
        items_to_remove = []
    
    # Remove os itens indesejados
    original_count = len(items)
    for item in items_to_remove:
        items.pop(item, None)
    
    # Salva o arquivo limpo
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=2, ensure_ascii=False)
    
    removed_count = original_count - len(items)
    if removed_count > 0:
        print(f"Removidos {removed_count} itens incorretos de {json_file_path}")

def main():
    json_path = Path("tibia_json")
    
    # Lista de arquivos JSON para limpar
    json_files = [
        "botas_items.json",
        "calcas_items.json"
    ]
    
    for json_file in json_files:
        file_path = json_path / json_file
        if file_path.exists():
            clean_tibia_json_v3(str(file_path))
        else:
            print(f"Arquivo não encontrado: {file_path}")

if __name__ == "__main__":
    main()
