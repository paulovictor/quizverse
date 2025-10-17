#!/usr/bin/env python
"""
Script padrão para recuperar URLs de qualquer pasta do Cloudinary

Uso:
    python get_cloud_urls.py

O script irá pedir:
    1. Caminho da pasta no Cloudinary (ex: cs/gloves, cs/ak-47)
    2. Título para o arquivo de saída (ex: gloves, ak47)

Saída:
    cloudinary_urls/{titulo}_urls.json
"""

import os
import json
import sys
from pathlib import Path

try:
    import cloudinary
    import cloudinary.api
except ImportError:
    print("❌ Erro: Biblioteca 'cloudinary' não está instalada!")
    print()
    print("Para instalar:")
    print("   pip install cloudinary")
    print("   # ou")
    print("   uv add cloudinary")
    sys.exit(1)


# ========== CONFIGURAÇÃO ==========
# Credenciais do Cloudinary
CLOUD_NAME = os.environ.get('CLOUDINARY_CLOUD_NAME', 'dwm53cbu2')
API_KEY = os.environ.get('CLOUDINARY_API_KEY', '429396283651242')
API_SECRET = os.environ.get('CLOUDINARY_API_SECRET', 'HTF--7Ceic5mmOo_oxboCTzXiis')

# Pasta de saída
OUTPUT_DIR = 'cloudinary_urls'

# Tipo de recurso: 'image', 'video', 'raw'
RESOURCE_TYPE = 'image'
# ===================================


def configure_cloudinary():
    """Configura as credenciais do Cloudinary"""
    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
        secure=True
    )
    print(f"✅ Conectado ao Cloudinary: {CLOUD_NAME}")


def get_all_resources(folder, resource_type='image', max_results=None):
    """
    Recupera todos os recursos de uma pasta no Cloudinary usando asset_folder

    Args:
        folder: Nome da pasta (asset folder)
        resource_type: Tipo de recurso ('image', 'video', 'raw')
        max_results: Número máximo de resultados (None = todos)

    Returns:
        list: Lista de recursos
    """
    all_resources = []
    next_cursor = None

    print(f"🔍 Buscando recursos no Cloudinary...")
    print(f"📂 Asset Folder: {folder}")
    print(f"📂 Tipo: {resource_type}")
    print()

    while True:
        try:
            # Buscar recursos por asset_folder com paginação
            params = {
                'max_results': 500  # Máximo por página
            }

            if next_cursor:
                params['next_cursor'] = next_cursor

            # Usar resources_by_asset_folder para buscar na pasta do Media Library
            if folder:
                response = cloudinary.api.resources_by_asset_folder(
                    folder,
                    **params
                )
            else:
                # Fallback para resources normal se folder estiver vazio
                params['type'] = 'upload'
                response = cloudinary.api.resources(
                    resource_type=resource_type,
                    **params
                )

            resources = response.get('resources', [])
            all_resources.extend(resources)

            print(f"   📥 {len(resources)} recursos encontrados (total: {len(all_resources)})")

            # Verificar se há mais páginas
            next_cursor = response.get('next_cursor')

            if not next_cursor:
                break

            if max_results and len(all_resources) >= max_results:
                all_resources = all_resources[:max_results]
                break

        except cloudinary.exceptions.Error as e:
            print(f"❌ Erro ao buscar recursos: {e}")
            break

    return all_resources


def build_url(resource, transformations=None):
    """
    Constrói a URL do recurso com transformações opcionais

    Args:
        resource: Dicionário com dados do recurso
        transformations: Dicionário com transformações (opcional)

    Returns:
        str: URL completa
    """
    if transformations:
        # Construir URL com transformações
        return cloudinary.CloudinaryImage(resource['public_id']).build_url(
            **transformations
        )
    else:
        # URL simples
        return resource.get('secure_url', resource.get('url'))


def format_json_output(resources, transformations=None):
    """
    Formata a saída dos recursos em JSON

    Args:
        resources: Lista de recursos
        transformations: Transformações opcionais para URLs

    Returns:
        str: JSON formatado
    """
    data = []
    for r in resources:
        data.append({
            'public_id': r['public_id'],
            'format': r.get('format'),
            'width': r.get('width'),
            'height': r.get('height'),
            'bytes': r.get('bytes'),
            'created_at': r.get('created_at'),
            'url': build_url(r, transformations),
            'secure_url': build_url(r, transformations),
        })
    return json.dumps(data, indent=2, ensure_ascii=False)


def save_output(content, title):
    """
    Salva a saída em um arquivo JSON

    Args:
        content: Conteúdo JSON
        title: Título para o nome do arquivo

    Returns:
        Path: Caminho do arquivo salvo
    """
    # Criar diretório de saída se não existir
    output_dir = Path(OUTPUT_DIR)
    output_dir.mkdir(exist_ok=True)

    # Nome do arquivo: {title}_urls.json
    filename = f"{title}_urls.json"
    filepath = output_dir / filename

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return filepath


def get_user_input():
    """
    Solicita input do usuário para pasta e título

    Returns:
        tuple: (folder_path, title)
    """
    print("=" * 70)
    print("☁️  CLOUDINARY URL EXTRACTOR")
    print("=" * 70)
    print()

    # Solicitar pasta
    print("📂 Digite o caminho da pasta no Cloudinary:")
    print("   Exemplos: cs/gloves, cs/ak-47, pokemons, themes")
    print()
    folder_path = input("   Pasta: ").strip()

    print()

    # Solicitar título
    print("📝 Digite o título para o arquivo de saída:")
    print("   Exemplos: gloves, ak47, pokemon_gen1")
    print()
    title = input("   Título: ").strip()

    # Validar inputs
    if not folder_path:
        print()
        print("⚠️  Atenção: Pasta vazia, buscando em todas as pastas...")
        folder_path = ''

    if not title:
        print()
        print("❌ Erro: Título não pode ser vazio!")
        sys.exit(1)

    return folder_path, title


def main():
    # Obter inputs do usuário
    folder_path, title = get_user_input()

    print()
    print("=" * 70)
    print("🚀 INICIANDO EXTRAÇÃO")
    print("=" * 70)
    print()

    # Configurar Cloudinary
    configure_cloudinary()
    print()

    # Buscar recursos
    resources = get_all_resources(
        folder=folder_path,
        resource_type=RESOURCE_TYPE,
        max_results=None
    )

    if not resources:
        print()
        print("⚠️  Nenhum recurso encontrado!")
        print()
        print(f"Verifique se:")
        print(f"   - A pasta '{folder_path}' existe no Cloudinary")
        print(f"   - O tipo de recurso '{RESOURCE_TYPE}' está correto")
        print(f"   - As credenciais têm permissão de leitura")
        return

    print()
    print(f"📦 Total de recursos encontrados: {len(resources)}")

    print()
    print("=" * 70)
    print(f"📊 RESUMO")
    print("=" * 70)
    print(f"✅ Total de recursos: {len(resources)}")
    print(f"📁 Pasta: {folder_path or 'ROOT (todas)'}")
    print(f"📂 Tipo: {RESOURCE_TYPE}")

    # Formatar saída
    print()
    print(f"📝 Gerando saída em formato JSON...")
    output = format_json_output(resources, transformations=None)

    # Salvar em arquivo
    filepath = save_output(output, title)
    print(f"💾 Salvo em: {filepath.absolute()}")

    # Mostrar preview
    print()
    print("=" * 70)
    print(f"📋 PREVIEW (primeiros 10 recursos)")
    print("=" * 70)
    for i, resource in enumerate(resources[:10], 1):
        url = build_url(resource, None)
        print(f"{i}. {resource['public_id']}")
        print(f"   {url}")

    if len(resources) > 10:
        print(f"... e mais {len(resources) - 10} recursos")

    print()
    print("🎉 Concluído!")
    print()

    return resources


if __name__ == '__main__':
    try:
        resources = main()
    except KeyboardInterrupt:
        print()
        print("⚠️  Operação cancelada pelo usuário")
        sys.exit(0)
    except Exception as e:
        print()
        print(f"❌ Erro: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
