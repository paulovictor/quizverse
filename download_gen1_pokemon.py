#!/usr/bin/env python
"""
Script para baixar todos os Pokémon da Geração 1 usando a PokéAPI
Geração 1: 151 Pokémon (Bulbasaur #1 até Mew #151)
"""
import os
import json
import requests
import time
from pathlib import Path

# API endpoint
POKEAPI_BASE = "https://pokeapi.co/api/v2"
GENERATION_1_COUNT = 151  # Pokémon da Geração 1

def download_pokemon_data_and_image(pokemon_id):
    """
    Baixa os dados e a imagem de um Pokémon específico
    
    Args:
        pokemon_id: ID do Pokémon (1-151 para Geração 1)
    
    Returns:
        dict: Dados do Pokémon ou None em caso de erro
    """
    try:
        # Buscar dados do Pokémon
        response = requests.get(f"{POKEAPI_BASE}/pokemon/{pokemon_id}", timeout=30)
        response.raise_for_status()
        pokemon_data = response.json()
        
        # Buscar dados da espécie (para descrição em português)
        species_response = requests.get(pokemon_data['species']['url'], timeout=30)
        species_response.raise_for_status()
        species_data = species_response.json()
        
        # Extrair informações relevantes
        pokemon_info = {
            'id': pokemon_data['id'],
            'name': pokemon_data['name'].capitalize(),
            'name_pt': get_portuguese_name(species_data),
            'types': [t['type']['name'] for t in pokemon_data['types']],
            'height': pokemon_data['height'],
            'weight': pokemon_data['weight'],
            'image_url': pokemon_data['sprites']['other']['official-artwork']['front_default'],
            'evolution_chain_url': species_data['evolution_chain']['url']
        }
        
        return pokemon_info
        
    except Exception as e:
        print(f"   ❌ Erro ao buscar Pokémon #{pokemon_id}: {e}")
        return None

def get_portuguese_name(species_data):
    """Extrai o nome em português do Pokémon"""
    for name in species_data.get('names', []):
        if name['language']['name'] == 'pt-BR':
            return name['name']
    # Fallback para o nome em inglês
    return species_data['name'].capitalize()

def download_image(url, filepath):
    """Baixa uma imagem da URL e salva no filepath"""
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(filepath, 'wb') as f:
            f.write(response.content)
        
        return True
    except Exception as e:
        print(f"   ❌ Erro ao baixar imagem: {e}")
        return False

def download_all_gen1_pokemon():
    """Baixa todos os Pokémon da Geração 1"""
    
    # Criar pastas
    pokemon_dir = Path('pokemon_gen1')
    images_dir = pokemon_dir / 'images'
    pokemon_dir.mkdir(exist_ok=True)
    images_dir.mkdir(exist_ok=True)
    
    print(f"📁 Pastas criadas:")
    print(f"   {pokemon_dir.absolute()}")
    print(f"   {images_dir.absolute()}")
    print()
    
    all_pokemon = []
    success_count = 0
    failed_count = 0
    
    print(f"🎮 Baixando {GENERATION_1_COUNT} Pokémon da Geração 1...")
    print("=" * 70)
    print()
    
    for pokemon_id in range(1, GENERATION_1_COUNT + 1):
        print(f"[{pokemon_id}/{GENERATION_1_COUNT}] Baixando Pokémon #{pokemon_id:03d}...", end=" ")
        
        # Buscar dados do Pokémon
        pokemon_info = download_pokemon_data_and_image(pokemon_id)
        
        if not pokemon_info:
            failed_count += 1
            print("❌ Falhou")
            continue
        
        name = pokemon_info['name']
        name_pt = pokemon_info['name_pt']
        types = ', '.join(pokemon_info['types'])
        print(f"{name_pt} ({name}) - Tipo: {types}")
        
        # Baixar imagem
        if pokemon_info['image_url']:
            filename = f"{pokemon_id:03d}_{pokemon_info['name'].lower()}.png"
            filepath = images_dir / filename
            
            if download_image(pokemon_info['image_url'], filepath):
                pokemon_info['local_image'] = f"images/{filename}"
                size = filepath.stat().st_size / 1024
                print(f"   ✅ Imagem salva: {filename} ({size:.2f} KB)")
            else:
                pokemon_info['local_image'] = None
        
        all_pokemon.append(pokemon_info)
        success_count += 1
        
        # Delay para não sobrecarregar a API
        time.sleep(0.5)
        print()
    
    # Salvar todos os dados em JSON
    data_file = pokemon_dir / 'pokemon_data.json'
    with open(data_file, 'w', encoding='utf-8') as f:
        json.dump(all_pokemon, f, indent=2, ensure_ascii=False)
    
    print()
    print("=" * 70)
    print("📊 RESUMO DO DOWNLOAD")
    print("=" * 70)
    print(f"✅ Sucesso: {success_count}/{GENERATION_1_COUNT}")
    print(f"❌ Falhas: {failed_count}/{GENERATION_1_COUNT}")
    print()
    print(f"📁 Dados salvos em: {data_file.absolute()}")
    print(f"📁 Imagens salvas em: {images_dir.absolute()}")
    print()
    
    return all_pokemon

def create_pokemon_type_groups(pokemon_list):
    """Agrupa Pokémon por tipo para facilitar a criação de alternativas similares"""
    type_groups = {}
    
    for pokemon in pokemon_list:
        for ptype in pokemon['types']:
            if ptype not in type_groups:
                type_groups[ptype] = []
            type_groups[ptype].append(pokemon)
    
    return type_groups

if __name__ == '__main__':
    print("🎮 DOWNLOAD DE POKÉMON DA GERAÇÃO 1")
    print("=" * 70)
    print()
    print("📖 Usando PokéAPI: https://pokeapi.co/")
    print(f"📊 Total de Pokémon: {GENERATION_1_COUNT}")
    print()
    
    # Verificar se requests está instalado
    try:
        import requests
    except ImportError:
        print("❌ Erro: O módulo 'requests' não está instalado!")
        print()
        print("Para instalar, execute:")
        print("   pip install requests")
        exit(1)
    
    # Baixar todos os Pokémon
    pokemon_list = download_all_gen1_pokemon()
    
    # Criar grupos por tipo
    if pokemon_list:
        type_groups = create_pokemon_type_groups(pokemon_list)
        
        print("📋 POKÉMON POR TIPO:")
        print("=" * 70)
        for ptype, pokemons in sorted(type_groups.items()):
            print(f"   {ptype.capitalize()}: {len(pokemons)} Pokémon")
        print()
    
    print("🎉 Download concluído!")
    print()
    print("💡 Próximos passos:")
    print("   1. Execute: python create_pokemon_quiz.py")
    print("   2. Copie as imagens para: quizzes/static/images/pokemon/")

