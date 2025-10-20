#!/usr/bin/env python3

import json
from pathlib import Path

# Lista de itens genéricos que não são equipamentos reais e devem ser removidos de todos
COMMON_INVALID_ITEMS = [
    "Bejeweled Ship's Telescope",
    "Spirit Container (Fighting Spirit)",
    "Shimmer Ball",
    "Golden Newspaper",
    "Epaminondas Doll",
    "Blue Note",
    "Anniversary Cake",
    "Sea Serpent Trophy",
    "Wooden Whistle",
    "Flawless Ice Crystal",
    "Bar of Gold",
    "Broken Bottle",
    "Ultimate Healing Rune",
    "Golden Hyena Pendant",
    "Star Ring",
    "Jaul's Pearl",
    "Dragonfruit",
    "Orange Key",
    "Black Jade Cobra",
    "Ultimate Health Potion",
    "Ice Flower 02",
    "Lock Pick",
    "Scorpion Sceptre"
]

def clean_file(json_file_path: str, items_to_remove: list) -> None:
    """
    Remove itens inválidos de um arquivo JSON.
    """
    with open(json_file_path, 'r', encoding='utf-8') as file:
        items = json.load(file)
    
    original_count = len(items)
    
    # Remove os itens indesejados
    for item in items_to_remove:
        items.pop(item, None)
    
    # Salva o arquivo limpo
    with open(json_file_path, 'w', encoding='utf-8') as file:
        json.dump(items, file, indent=2, ensure_ascii=False)
    
    removed_count = original_count - len(items)
    if removed_count > 0:
        print(f"Removidos {removed_count} itens inválidos de {Path(json_file_path).name}")

def main():
    json_path = Path("tibia_json")
    
    # Arquivos para limpar
    files = {
        "armaduras_items.json": COMMON_INVALID_ITEMS,
        "elmos_items.json": COMMON_INVALID_ITEMS,
        "clavas_items.json": COMMON_INVALID_ITEMS,
        "espadas_items.json": COMMON_INVALID_ITEMS,
        "varinhas_items.json": COMMON_INVALID_ITEMS
    }
    
    for json_file, items_to_remove in files.items():
        file_path = json_path / json_file
        if file_path.exists():
            clean_file(str(file_path), items_to_remove)
        else:
            print(f"Arquivo não encontrado: {file_path}")

if __name__ == "__main__":
    main()
