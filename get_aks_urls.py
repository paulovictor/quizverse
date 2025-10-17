#!/usr/bin/env python
"""
Script para recuperar todas as URLs das AK-47 do Counter-Strike no Cloudinary

Uso:
    python get_aks_urls.py

Configuração:
    1. Instale a biblioteca: pip install cloudinary
    2. Configure as variáveis de ambiente ou edite as constantes abaixo
    3. Execute o script
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

# Pasta no Cloudinary para buscar arquivos
# A imagem está na raiz, sem pasta (Bloodsport_mnzmd6.webp)
FOLDER_NAME = ''  # Deixar vazio para buscar na raiz

# Tipo de recurso: 'image', 'video', 'raw', 'all'
RESOURCE_TYPE = 'image'

# Formato de saída
OUTPUT_FORMAT = 'json'  # Gerar JSON completo com metadados

# Máximo de resultados (None = todos)
MAX_RESULTS = None

# Transformações opcionais para as URLs
# Exemplo: {'width': 300, 'height': 300, 'crop': 'fill'}
TRANSFORMATIONS = None
# ===================================


def configure_cloudinary():
    """Configura as credenciais do Cloudinary"""
    if CLOUD_NAME == 'YOUR_CLOUD_NAME' or not CLOUD_NAME:
        print("❌ Erro: Credenciais do Cloudinary não configuradas!")
        print()
        print("Configure as variáveis de ambiente:")
        print("   export CLOUDINARY_CLOUD_NAME=your_cloud_name")
        print("   export CLOUDINARY_API_KEY=your_api_key")
        print("   export CLOUDINARY_API_SECRET=your_api_secret")
        print()
        print("Ou edite o arquivo diretamente:")
        print("   CLOUD_NAME = 'seu_cloud_name'")
        print("   API_KEY = 'sua_api_key'")
        print("   API_SECRET = 'seu_api_secret'")
        sys.exit(1)

    cloudinary.config(
        cloud_name=CLOUD_NAME,
        api_key=API_KEY,
        api_secret=API_SECRET,
        secure=True
    )

    print(f"✅ Conectado ao Cloudinary: {CLOUD_NAME}")


def load_ak47_names():
    """Carrega os nomes das AK-47 do arquivo JSON"""
    json_file = Path(__file__).parent / 'cs2_skins' / 'ak_47.json'

    if not json_file.exists():
        print(f"⚠️  Arquivo {json_file} não encontrado!")
        return set()

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Extrair todos os nomes únicos (skin name + opcoes)
    names = set()
    for item in data:
        names.add(item['name'])
        names.update(item['opcoes'])

    return names


def get_all_resources(folder, resource_type='image', max_results=None):
    """
    Recupera todos os recursos de uma pasta no Cloudinary

    Args:
        folder: Nome da pasta
        resource_type: Tipo de recurso ('image', 'video', 'raw')
        max_results: Número máximo de resultados (None = todos)

    Returns:
        list: Lista de recursos
    """
    all_resources = []
    next_cursor = None

    print(f"🔍 Buscando recursos no Cloudinary...")
    print(f"📂 Tipo: {resource_type}")
    print()

    while True:
        try:
            # Buscar recursos com paginação
            params = {
                'type': 'upload',
                'max_results': 500  # Máximo por página
            }

            # Apenas adicionar prefix se folder não estiver vazio
            if folder:
                params['prefix'] = folder

            if next_cursor:
                params['next_cursor'] = next_cursor

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


def format_output(resources, format_type='json', transformations=None):
    """
    Formata a saída dos recursos

    Args:
        resources: Lista de recursos
        format_type: Tipo de formato ('json', 'csv', 'urls_only', 'list')
        transformations: Transformações opcionais para URLs

    Returns:
        str ou dict: Saída formatada
    """
    if format_type == 'urls_only':
        # Apenas URLs, uma por linha
        urls = [build_url(r, transformations) for r in resources]
        return '\n'.join(urls)

    elif format_type == 'list':
        # Lista Python
        urls = [build_url(r, transformations) for r in resources]
        return urls

    elif format_type == 'csv':
        # Formato CSV
        output = "public_id,format,width,height,bytes,url\n"
        for r in resources:
            url = build_url(r, transformations)
            output += f"{r['public_id']},{r.get('format','')},{r.get('width','')},{r.get('height','')},{r.get('bytes','')},{url}\n"
        return output

    else:  # json (padrão)
        # JSON completo com metadados
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


def save_output(content, format_type='json'):
    """Salva a saída em um arquivo"""
    extensions = {
        'json': '.json',
        'csv': '.csv',
        'urls_only': '.txt',
        'list': '.txt'
    }

    # Nome do arquivo: ak47_urls.json
    filename = f"ak47_urls{extensions.get(format_type, '.txt')}"
    filepath = Path(filename)

    if format_type == 'list':
        # Para lista, salvar como JSON
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
    else:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

    return filepath


def normalize_name(name):
    """
    Normaliza um nome para comparação
    - Remove espaços e underscores
    - Converte para minúsculas
    - Remove caracteres especiais
    """
    import re
    # Converter para lowercase
    name = name.lower()
    # Remover extensões de arquivo
    name = re.sub(r'\.(webp|jpg|jpeg|png|gif)$', '', name)
    # Remover underscores e espaços
    name = name.replace('_', '').replace(' ', '').replace('-', '')
    return name


def is_ak47_skin(public_id, ak47_names):
    """
    Verifica se um public_id corresponde a uma skin AK-47

    Args:
        public_id: ID público do recurso no Cloudinary
        ak47_names: Set com todos os nomes de skins AK-47

    Returns:
        bool: True se é uma skin AK-47
    """
    # Normalizar o public_id
    normalized_id = normalize_name(public_id)

    # Verificar contra todos os nomes de AK-47
    for skin_name in ak47_names:
        normalized_skin = normalize_name(skin_name)

        # Verificar se há match
        if normalized_skin in normalized_id or normalized_id in normalized_skin:
            return True

    return False


def main():
    print("=" * 70)
    print("☁️  CLOUDINARY URL EXTRACTOR - AK-47")
    print("=" * 70)
    print()

    # Configurar Cloudinary
    configure_cloudinary()
    print()

    # Carregar nomes das AK-47
    print("📖 Carregando nomes das skins AK-47...")
    ak47_names = load_ak47_names()

    if not ak47_names:
        print("⚠️  Nenhum nome de skin encontrado no arquivo JSON!")
        return

    print(f"✅ {len(ak47_names)} nomes de skins carregados")
    print()

    # Buscar recursos
    resources = get_all_resources(
        folder=FOLDER_NAME,
        resource_type=RESOURCE_TYPE,
        max_results=MAX_RESULTS
    )

    if not resources:
        print()
        print("⚠️  Nenhum recurso encontrado!")
        print()
        print(f"Verifique se:")
        print(f"   - A pasta '{FOLDER_NAME}' existe no Cloudinary")
        print(f"   - O tipo de recurso '{RESOURCE_TYPE}' está correto")
        print(f"   - As credenciais têm permissão de leitura")
        return

    print()
    print(f"📦 Total de recursos encontrados no Cloudinary: {len(resources)}")

    # Filtrar apenas skins AK-47
    print("🔍 Filtrando apenas skins AK-47...")
    filtered_resources = []
    for resource in resources:
        public_id = resource['public_id']
        if is_ak47_skin(public_id, ak47_names):
            filtered_resources.append(resource)

    print(f"✅ {len(filtered_resources)} skins AK-47 encontradas (de {len(resources)} recursos totais)")

    if not filtered_resources:
        print()
        print("⚠️  Nenhuma skin AK-47 foi encontrada após o filtro!")
        print()
        print("Recursos disponíveis (primeiros 10):")
        for i, r in enumerate(resources[:10], 1):
            print(f"   {i}. {r['public_id']}")
        return

    print()
    print("=" * 70)
    print(f"📊 RESUMO")
    print("=" * 70)
    print(f"✅ Total de skins AK-47: {len(filtered_resources)}")
    print(f"📁 Pasta: {FOLDER_NAME if FOLDER_NAME else '(raiz)'}")
    print(f"📂 Tipo: {RESOURCE_TYPE}")

    # Formatar saída
    print()
    print(f"📝 Gerando saída em formato: {OUTPUT_FORMAT}")
    output = format_output(filtered_resources, OUTPUT_FORMAT, TRANSFORMATIONS)

    # Salvar em arquivo
    filepath = save_output(output, OUTPUT_FORMAT)
    print(f"💾 Salvo em: {filepath.absolute()}")

    # Mostrar preview
    print()
    print("=" * 70)
    print("📋 PREVIEW (primeiras 10 skins)")
    print("=" * 70)
    for i, resource in enumerate(filtered_resources[:10], 1):
        url = build_url(resource, TRANSFORMATIONS)
        print(f"{i}. {resource['public_id']}")
        print(f"   {url}")

    if len(filtered_resources) > 10:
        print(f"... e mais {len(filtered_resources) - 10} skins")

    print()
    print("🎉 Concluído!")
    print()

    return filtered_resources


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
