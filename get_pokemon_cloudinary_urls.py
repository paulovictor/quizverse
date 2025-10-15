#!/usr/bin/env python
"""
Script para buscar URLs dos Pokémon no Cloudinary e gerar mapeamento
"""

import os
import sys
import json
import re

try:
    import cloudinary
    import cloudinary.api
except ImportError:
    print("❌ Erro: Biblioteca 'cloudinary' não está instalada!")
    sys.exit(1)

# Configuração
CLOUD_NAME = 'dwm53cbu2'
API_KEY = '429396283651242'
API_SECRET = 'HTF--7Ceic5mmOo_oxboCTzXiis'

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET,
    secure=True
)

print("=" * 70)
print("☁️  BUSCANDO POKÉMON NO CLOUDINARY")
print("=" * 70)
print()

# Buscar todos os recursos
all_resources = []
next_cursor = None

print("🔍 Buscando todos os recursos...")

while True:
    try:
        params = {
            'type': 'upload',
            'max_results': 500,
            'resource_type': 'image'
        }
        
        if next_cursor:
            params['next_cursor'] = next_cursor
        
        response = cloudinary.api.resources(**params)
        resources = response.get('resources', [])
        all_resources.extend(resources)
        
        print(f"   📥 {len(resources)} recursos encontrados (total: {len(all_resources)})")
        
        next_cursor = response.get('next_cursor')
        if not next_cursor:
            break
            
    except Exception as e:
        print(f"❌ Erro: {e}")
        break

print()
print(f"✅ Total de recursos: {len(all_resources)}")
print()

# Filtrar apenas Pokémon (começam com número de 3 dígitos)
pokemon_pattern = re.compile(r'^(\d{3})_([a-z\-]+)')
pokemon_urls = {}

for resource in all_resources:
    public_id = resource['public_id']
    match = pokemon_pattern.match(public_id)
    
    if match:
        pokemon_id = int(match.group(1))
        pokemon_name = match.group(2)
        url = resource['secure_url']
        
        pokemon_urls[pokemon_id] = {
            'id': pokemon_id,
            'name': pokemon_name,
            'public_id': public_id,
            'url': url,
            'format': resource.get('format', 'png')
        }

# Ordenar por ID
sorted_pokemon = sorted(pokemon_urls.items())

print("🎮 POKÉMON ENCONTRADOS:")
print("=" * 70)
print(f"Total: {len(sorted_pokemon)} Pokémon")
print()

# Mostrar primeiros 10
for pokemon_id, data in sorted_pokemon[:10]:
    print(f"   #{pokemon_id:03d} {data['name']}")
    print(f"   URL: {data['url']}")
    print()

if len(sorted_pokemon) > 10:
    print(f"   ... e mais {len(sorted_pokemon) - 10} Pokémon")
    print()

# Salvar em arquivo JSON
output_file = 'cloudinary_pokemon_urls.json'
with open(output_file, 'w', encoding='utf-8') as f:
    json.dump(dict(sorted_pokemon), f, indent=2, ensure_ascii=False)

print(f"💾 URLs salvas em: {output_file}")
print()

# Salvar apenas URLs em formato simples
output_urls_file = 'cloudinary_pokemon_urls.txt'
with open(output_urls_file, 'w', encoding='utf-8') as f:
    for pokemon_id, data in sorted_pokemon:
        f.write(f"{data['url']}\n")

print(f"📝 Lista de URLs salva em: {output_urls_file}")
print()
print("🎉 Concluído!")

