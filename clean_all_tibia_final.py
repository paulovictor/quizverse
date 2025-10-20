#!/usr/bin/env python3

import json
from pathlib import Path

# Itens inválidos que aparecem em TODOS os arquivos
COMMON_INVALID_ITEMS = [
    # Itens de outras categorias
    "Sanguine Boots",
    "Phantasmal Axe",
    "Umbral Master Crossbow",
    "Lion Shield",
    "Amber Wand",
    "Naga Rod",
    # Itens genéricos (chaves, poções, decorações, etc.)
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
        print(f"{Path(json_file_path).name}: removidos {removed_count} itens ({len(items)} itens restantes)")
    else:
        print(f"{Path(json_file_path).name}: nenhum item removido ({len(items)} itens)")

def main():
    json_path = Path("tibia_json")
    
    # Arquivos para limpar - todos com os mesmos itens inválidos
    files = [
        "armaduras_items.json",
        "elmos_items.json",
        "clavas_items.json",
        "espadas_items.json",
        "varinhas_items.json",
        "botas_items.json",
        "calcas_items.json"
    ]
    
    print("Limpando arquivos JSON da Tibia...")
    print("=" * 60)
    
    for json_file in files:
        file_path = json_path / json_file
        if file_path.exists():
            clean_file(str(file_path), COMMON_INVALID_ITEMS)
        else:
            print(f"Arquivo não encontrado: {json_file}")
    
    print("=" * 60)
    print("Limpeza concluída!")

if __name__ == "__main__":
    main()
