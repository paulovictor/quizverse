#!/usr/bin/env python3

import json
from pathlib import Path

# Lista oficial de armaduras válidas da Tibia Wiki
VALID_ARMADURAS = [
    "Albino Plate",
    "Amazon Armor",
    "Arcane Dragon Robe",
    "Ball Gown",
    "Bear Skin",
    "Belted Cape",
    "Blue Robe",
    "Brass Armor",
    "Broken Iks Cuirass",
    "Buckle",
    "Burial Shroud",
    "Calopteryx Cape",
    "Cape",
    "Chain Armor",
    "Coat",
    "Crown Armor",
    "Crystalline Armor",
    "Dark Armor",
    "Dark Lord's Cape",
    "Dauntless Dragon Scale Armor",
    "Dawnfire Sherwani",
    "Death Oyoroi",
    "Demon Armor",
    "Depth Lorica",
    "Divine Plate",
    "Doublet",
    "Dragon Robe",
    "Dragon Scale Mail",
    "Dream Shroud",
    "Earthborn Titan Armor",
    "Earthheart Cuirass",
    "Earthheart Hauberk",
    "Earthheart Platemail",
    "Earthmind Raiment",
    "Earthsoul Tabard",
    "Eldritch Cuirass",
    "Elite Draken Mail",
    "Elven Mail",
    "Embrace of Nature",
    "Energy Robe",
    "Ethno Coat",
    "Falcon Plate",
    "Fireborn Giant Armor",
    "Fireheart Cuirass",
    "Fireheart Hauberk",
    "Fireheart Platemail",
    "Firemind Raiment",
    "Firesoul Tabard",
    "Flower Dress",
    "Focus Cape",
    "Frostheart Cuirass",
    "Frostheart Hauberk",
    "Frostheart Platemail",
    "Frostmind Raiment",
    "Frostsoul Tabard",
    "Frozen Plate",
    "Fur Armor",
    "Furious Frock",
    "Ghazbaran Oyoroi",
    "Ghost Chestplate",
    "Gill Coat",
    "Girl's Dress",
    "Glacier Robe",
    "Glooth Cape",
    "Gnome Armor",
    "Gnomish Cuirass",
    "Golden Armor",
    "Goo Shell",
    "Green Demon Armor",
    "Green Tunic",
    "Greenwood Coat",
    "Heat Core",
    "Heavy Metal T-Shirt",
    "Hibiscus Dress",
    "Ice Robe",
    "Jacket",
    "Knight Armor",
    "Lavos Armor",
    "Leaf Robe",
    "Leather Armor",
    "Leather Harness",
    "Leopard Armor",
    "Lightning Robe",
    "Lion Plate",
    "Living Armor",
    "Magic Plate Armor",
    "Magician's Robe",
    "Magma Coat",
    "Magma Robe",
    "Mammoth Fur Cape",
    "Master Archer's Armor",
    "Merudri Battle Mail",
    "Merudri Nanbando",
    "Merudri Scale Mail",
    "Midnight Tunic",
    "Molten Plate",
    "Monk Robe",
    "Mooh'tah Plate",
    "Mutated Skin Armor",
    "Mystical Dragon Robe",
    "Naga Tanko",
    "Native Armor",
    "Noble Armor",
    "Norcferatu Bloodhide",
    "Norcferatu Bonecloak",
    "Norcferatu Tuskplate",
    "Oceanborn Leviathan Armor",
    "Old Cape",
    "Ornate Chestplate",
    "Pair of Old Bracers",
    "Paladin Armor",
    "Pirate Shirt",
    "Plain Monk Robe",
    "Plate Armor",
    "Prismatic Armor",
    "Ranger's Cloak",
    "Red Robe",
    "Red Tunic",
    "Robe of Enlightenment",
    "Robe of the Ice Queen",
    "Robe of the Underworld",
    "Royal Draken Mail",
    "Royal Scale Robe",
    "Scale Armor",
    "Simple Dress",
    "Skullcracker Armor",
    "Soulgarb",
    "Soulmantle",
    "Soulshell",
    "Soulshroud",
    "Spectral Dress",
    "Spellweaver's Robe",
    "Spirit Bind",
    "Spirit Cloak",
    "Spiritthorn Armor",
    "Stoic Iks Chestplate",
    "Stoic Iks Cuirass",
    "Stoic Iks Robe",
    "Studded Armor",
    "Summer Dress",
    "Swamplair Armor",
    "Swan Feather Cloak",
    "Terra Mantle",
    "The Rain Coat",
    "Thunderheart Cuirass",
    "Thunderheart Hauberk",
    "Thunderheart Platemail",
    "Thundermind Raiment",
    "Thundersoul Tabard",
    "Toga Mortis",
    "Traditional Shirt",
    "Tunic",
    "Unerring Dragon Scale Armor",
    "Velvet Mantle",
    "Voltage Armor",
    "White Dress",
    "Windborn Colossus Armor",
    "Witchhunter's Coat",
    "Yalahari Armor",
    "Zaoan Armor",
    "Zaoan Monk Robe",
    "Zaoan Robe"
]

def filter_valid_armaduras():
    """
    Filtra o arquivo de armaduras mantendo apenas as armaduras válidas.
    """
    file_path = Path("tibia_json/armaduras_items.json")
    
    with open(file_path, 'r', encoding='utf-8') as file:
        all_items = json.load(file)
    
    # Filtra apenas as armaduras válidas
    valid_items = {name: url for name, url in all_items.items() if name in VALID_ARMADURAS}
    
    # Salva o arquivo filtrado
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(valid_items, file, indent=2, ensure_ascii=False)
    
    print(f"Arquivo original: {len(all_items)} itens")
    print(f"Arquivo filtrado: {len(valid_items)} itens")
    print(f"Removidos: {len(all_items) - len(valid_items)} itens inválidos")
    
    # Verifica se há armaduras na lista oficial que não estão no arquivo
    missing = set(VALID_ARMADURAS) - set(valid_items.keys())
    if missing:
        print(f"\nArmaduras da lista oficial que NÃO foram encontradas no arquivo:")
        for armor in sorted(missing):
            print(f"  - {armor}")

if __name__ == "__main__":
    filter_valid_armaduras()

