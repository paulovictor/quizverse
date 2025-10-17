#!/usr/bin/env python
"""
Script de diagnóstico para encontrar a localização exata das gloves no Cloudinary
"""

import os
import sys

try:
    import cloudinary
    import cloudinary.api
except ImportError:
    print("❌ Erro: Biblioteca 'cloudinary' não está instalada!")
    sys.exit(1)

# Credenciais
CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME', 'dwm53cbu2')
API_KEY = os.environ.get('CLOUDINARY_API_KEY', '429396283651242')
API_SECRET = os.environ.get('CLOUDINARY_API_SECRET', 'HTF--7Ceic5mmOo_oxboCTzXiis')

cloudinary.config(
    cloud_name=CLOUD_NAME,
    api_key=API_KEY,
    api_secret=API_SECRET,
    secure=True
)

print("=" * 70)
print("🔍 DIAGNÓSTICO: LOCALIZAÇÃO DAS GLOVES")
print("=" * 70)
print()

# 1. Tentar buscar o recurso específico Vice_doktdh
print("1️⃣ Buscando recurso específico 'Vice_doktdh'...")
try:
    resource = cloudinary.api.resource('Vice_doktdh')
    print(f"   ✅ Encontrado!")
    print(f"   Public ID: {resource['public_id']}")
    print(f"   Folder: {resource.get('folder', 'ROOT (sem pasta)')}")
    print(f"   URL: {resource['secure_url']}")
    print(f"   Format: {resource.get('format')}")
except Exception as e:
    print(f"   ❌ Não encontrado no formato simples: {e}")

print()

# 2. Buscar recursos na pasta cs/gloves usando prefix
print("2️⃣ Buscando recursos com prefix 'cs/gloves'...")
try:
    response = cloudinary.api.resources(
        type='upload',
        prefix='cs/gloves',
        max_results=10
    )
    resources = response.get('resources', [])
    print(f"   📊 Encontrados: {len(resources)} recursos")
    for r in resources[:5]:
        print(f"   • {r['public_id']}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()

# 3. Buscar recursos apenas com 'gloves' como prefix
print("3️⃣ Buscando recursos com prefix 'gloves'...")
try:
    response = cloudinary.api.resources(
        type='upload',
        prefix='gloves',
        max_results=10
    )
    resources = response.get('resources', [])
    print(f"   📊 Encontrados: {len(resources)} recursos")
    for r in resources[:5]:
        print(f"   • {r['public_id']}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()

# 4. Buscar recursos na raiz e filtrar por nome
print("4️⃣ Buscando recursos na raiz que contenham 'vice'...")
try:
    response = cloudinary.api.resources(
        type='upload',
        max_results=500
    )
    resources = response.get('resources', [])
    vice_resources = [r for r in resources if 'vice' in r['public_id'].lower()]
    print(f"   📊 Encontrados: {len(vice_resources)} recursos com 'vice'")
    for r in vice_resources[:5]:
        print(f"   • {r['public_id']}")
        print(f"     Folder: {r.get('folder', 'ROOT')}")
        print(f"     URL: {r['secure_url']}")
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()

# 5. Listar recursos da pasta 'cs/gloves' usando resources_by_asset_folder
print("5️⃣ Tentando listar recursos por asset_folder 'cs/gloves'...")
try:
    response = cloudinary.api.resources_by_asset_folder(
        'cs/gloves',
        max_results=10
    )
    resources = response.get('resources', [])
    print(f"   📊 Encontrados: {len(resources)} recursos")
    for r in resources[:10]:
        print(f"   • {r['public_id']}")
        print(f"     Asset folder: {r.get('asset_folder', 'N/A')}")
        print(f"     Display name: {r.get('display_name', 'N/A')}")
        print(f"     URL: {r['secure_url']}")
        print()
except Exception as e:
    print(f"   ❌ Erro: {e}")

print()
print("=" * 70)
print("✅ Diagnóstico concluído!")
print("=" * 70)
