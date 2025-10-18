#!/usr/bin/env python
"""
Script genérico para criar temas em todos os países.

Este script:
1. Pergunta informações sobre o tema a ser criado
2. Verifica os temas root existentes para cada país
3. Cria o tema em todos os países, associando ao tema pai correto

Uso:
    python setup/create_theme.py
"""

import os
import sys
import json
import django
from pathlib import Path
from django.core.management import call_command

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme


# ============================================================================
# CONFIGURAÇÃO DE PAÍSES E IDIOMAS
# ============================================================================

COUNTRY_TO_LANG = {
    'en-US': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-IN': 'en',
    'en-PH': 'en', 'en-AU': 'en', 'en-NZ': 'en',
    'pt-BR': 'pt', 'pt-PT': 'pt',
    'es-MX': 'es', 'es-ES': 'es', 'es-AR': 'es', 'es-CO': 'es'
}

# ============================================================================
# DICIONÁRIO DE REFERÊNCIA DOS TEMAS ROOT
# ============================================================================

ROOT_THEMES_REFERENCE = {
    'pt-BR': {
        'esportes': 'Esportes',
        'entretenimento': 'Entretenimento & Mídia',
        'curiosidades': 'Curiosidades Gerais',
        'ciencia': 'Ciência & Tecnologia',
        'jogos': 'Jogos',
        'celebridades': 'Celebridades & Personalidades',
        'arte': 'Arte & Cultura',
        'historia': 'História',
        'comida': 'Comida & Bebida',
        'natureza': 'Natureza & Animais',
        'geografia': 'Geografia',
        'politica': 'Política & Sociedade'
    },
    'pt-PT': {
        'esportes-pt': 'Esportes',
        'entretenimento-pt': 'Entretenimento & Mídia',
        'curiosidades-pt': 'Curiosidades Gerais',
        'ciencia-pt': 'Ciência & Tecnologia',
        'jogos-pt': 'Jogos',
        'celebridades-pt': 'Celebridades & Personalidades',
        'arte-pt': 'Arte & Cultura',
        'historia-pt': 'História',
        'comida-pt': 'Comida & Bebida',
        'natureza-pt': 'Natureza & Animais',
        'geografia-pt': 'Geografia',
        'politica-pt': 'Política & Sociedade'
    },
    'en-US': {
        'sports-us': 'Sports',
        'entertainment-us': 'Entertainment & Media',
        'trivia-us': 'General Trivia',
        'science-us': 'Science & Technology',
        'games-us': 'Games',
        'celebrities-us': 'Celebrities & Personalities',
        'arts-us': 'Arts & Culture',
        'history-us': 'History',
        'food-us': 'Food & Drink',
        'nature-us': 'Nature & Animals',
        'geography-us': 'Geography',
        'politics-us': 'Politics & Society'
    },
    'en-CA': {
        'sports-ca': 'Sports',
        'entertainment-ca': 'Entertainment & Media',
        'trivia-ca': 'General Trivia',
        'science-ca': 'Science & Technology',
        'games-ca': 'Games',
        'celebrities-ca': 'Celebrities & Personalities',
        'arts-ca': 'Arts & Culture',
        'history-ca': 'History',
        'food-ca': 'Food & Drink',
        'nature-ca': 'Nature & Animals',
        'geography-ca': 'Geography',
        'politics-ca': 'Politics & Society'
    },
    'en-GB': {
        'sports-gb': 'Sports',
        'entertainment-gb': 'Entertainment & Media',
        'trivia-gb': 'General Trivia',
        'science-gb': 'Science & Technology',
        'games-gb': 'Games',
        'celebrities-gb': 'Celebrities & Personalities',
        'arts-gb': 'Arts & Culture',
        'history-gb': 'History',
        'food-gb': 'Food & Drink',
        'nature-gb': 'Nature & Animals',
        'geography-gb': 'Geography',
        'politics-gb': 'Politics & Society'
    },
    'en-IN': {
        'sports-in': 'Sports',
        'entertainment-in': 'Entertainment & Media',
        'trivia-in': 'General Trivia',
        'science-in': 'Science & Technology',
        'games-in': 'Games',
        'celebrities-in': 'Celebrities & Personalities',
        'arts-in': 'Arts & Culture',
        'history-in': 'History',
        'food-in': 'Food & Drink',
        'nature-in': 'Nature & Animals',
        'geography-in': 'Geography',
        'politics-in': 'Politics & Society'
    },
    'en-PH': {
        'sports-ph': 'Sports',
        'entertainment-ph': 'Entertainment & Media',
        'trivia-ph': 'General Trivia',
        'science-ph': 'Science & Technology',
        'games-ph': 'Games',
        'celebrities-ph': 'Celebrities & Personalities',
        'arts-ph': 'Arts & Culture',
        'history-ph': 'History',
        'food-ph': 'Food & Drink',
        'nature-ph': 'Nature & Animals',
        'geography-ph': 'Geography',
        'politics-ph': 'Politics & Society'
    },
    'en-AU': {
        'sports-au': 'Sports',
        'entertainment-au': 'Entertainment & Media',
        'trivia-au': 'General Trivia',
        'science-au': 'Science & Technology',
        'games-au': 'Games',
        'celebrities-au': 'Celebrities & Personalities',
        'arts-au': 'Arts & Culture',
        'history-au': 'History',
        'food-au': 'Food & Drink',
        'nature-au': 'Nature & Animals',
        'geography-au': 'Geography',
        'politics-au': 'Politics & Society'
    },
    'en-NZ': {
        'sports-nz': 'Sports',
        'entertainment-nz': 'Entertainment & Media',
        'trivia-nz': 'General Trivia',
        'science-nz': 'Science & Technology',
        'games-nz': 'Games',
        'celebrities-nz': 'Celebrities & Personalities',
        'arts-nz': 'Arts & Culture',
        'history-nz': 'History',
        'food-nz': 'Food & Drink',
        'nature-nz': 'Nature & Animals',
        'geography-nz': 'Geography',
        'politics-nz': 'Politics & Society'
    },
    'es-MX': {
        'deportes-mx': 'Deportes',
        'entretenimiento-mx': 'Entretenimiento y Medios',
        'curiosidades-mx': 'Curiosidades Generales',
        'ciencia-mx': 'Ciencia y Tecnología',
        'juegos-mx': 'Juegos',
        'celebridades-mx': 'Celebridades y Personalidades',
        'arte-mx': 'Arte y Cultura',
        'historia-mx': 'Historia',
        'comida-mx': 'Comida y Bebida',
        'naturaleza-mx': 'Naturaleza y Animales',
        'geografia-mx': 'Geografía',
        'politica-mx': 'Política y Sociedad'
    },
    'es-ES': {
        'deportes-es': 'Deportes',
        'entretenimiento-es': 'Entretenimiento y Medios',
        'curiosidades-es': 'Curiosidades Generales',
        'ciencia-es': 'Ciencia y Tecnología',
        'juegos-es': 'Juegos',
        'celebridades-es': 'Celebridades y Personalidades',
        'arte-es': 'Arte y Cultura',
        'historia-es': 'Historia',
        'comida-es': 'Comida y Bebida',
        'naturaleza-es': 'Naturaleza y Animales',
        'geografia-es': 'Geografía',
        'politica-es': 'Política y Sociedad'
    },
    'es-AR': {
        'deportes-ar': 'Deportes',
        'entretenimiento-ar': 'Entretenimiento y Medios',
        'curiosidades-ar': 'Curiosidades Generales',
        'ciencia-ar': 'Ciencia y Tecnología',
        'juegos-ar': 'Juegos',
        'celebridades-ar': 'Celebridades y Personalidades',
        'arte-ar': 'Arte y Cultura',
        'historia-ar': 'Historia',
        'comida-ar': 'Comida y Bebida',
        'naturaleza-ar': 'Naturaleza y Animales',
        'geografia-ar': 'Geografía',
        'politica-ar': 'Política y Sociedad'
    },
    'es-CO': {
        'deportes-co': 'Deportes',
        'entretenimiento-co': 'Entretenimiento y Medios',
        'curiosidades-co': 'Curiosidades Generales',
        'ciencia-co': 'Ciencia y Tecnología',
        'juegos-co': 'Juegos',
        'celebridades-co': 'Celebridades y Personalidades',
        'arte-co': 'Arte y Cultura',
        'historia-co': 'Historia',
        'comida-co': 'Comida y Bebida',
        'naturaleza-co': 'Naturaleza y Animales',
        'geografia-co': 'Geografía',
        'politica-co': 'Política y Sociedad'
    }
}


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def find_parent_themes(parent_slug_pt):
    """
    Encontra os slugs dos temas pai em todos os países baseado no slug PT-BR
    usando o dicionário de referência

    Exemplo:
        Se parent_slug_pt = 'jogos'
        Retorna: {
            'pt-BR': 'jogos',
            'en-US': 'games-us',
            'es-MX': 'juegos-mx',
            ...
        }
    """
    parent_themes = {}

    # Para pt-BR, usar o slug direto
    try:
        parent_pt = Theme.objects.get(slug=parent_slug_pt, country='pt-BR')
        parent_themes['pt-BR'] = parent_pt.slug
        print(f"✅ Tema pai encontrado para pt-BR: {parent_pt.slug}")
    except Theme.DoesNotExist:
        print(f"❌ Erro: Tema pai '{parent_slug_pt}' não encontrado para pt-BR")
        return None

    # Para outros países, usar o dicionário de referência
    for country_code in COUNTRY_TO_LANG.keys():
        if country_code == 'pt-BR':
            continue

        # Buscar no dicionário de referência
        country_themes = ROOT_THEMES_REFERENCE.get(country_code, {})
        
        # Tentar encontrar o tema correspondente
        found_slug = None
        
        # Primeiro, tentar encontrar por slug base (sem sufixo)
        for slug, title in country_themes.items():
            if slug.startswith(parent_slug_pt):
                found_slug = slug
                break
        
        # Se não encontrou, tentar por mapeamento de categorias
        if not found_slug:
            # Mapeamento de categorias entre idiomas
            category_mapping = {
                'jogos': ['games', 'juegos'],
                'esportes': ['sports', 'deportes'],
                'entretenimento': ['entertainment', 'entretenimiento'],
                'curiosidades': ['trivia', 'curiosidades'],
                'ciencia': ['science', 'ciencia'],
                'celebridades': ['celebrities', 'celebridades'],
                'arte': ['arts', 'arte'],
                'historia': ['history', 'historia'],
                'comida': ['food', 'comida'],
                'natureza': ['nature', 'naturaleza'],
                'geografia': ['geography', 'geografia'],
                'politica': ['politics', 'politica']
            }
            
            base_category = parent_slug_pt
            if base_category in category_mapping:
                for variant in category_mapping[base_category]:
                    for slug, title in country_themes.items():
                        if variant in slug:
                            found_slug = slug
                            break
                    if found_slug:
                        break

        if found_slug:
            try:
                parent_theme = Theme.objects.get(slug=found_slug, country=country_code)
                parent_themes[country_code] = parent_theme.slug
                print(f"✅ Tema pai encontrado para {country_code}: {found_slug}")
            except Theme.DoesNotExist:
                print(f"⚠️  Tema pai '{found_slug}' não existe no banco para {country_code}")
                parent_themes[country_code] = None
        else:
            print(f"⚠️  Tema pai não encontrado para {country_code}: {parent_slug_pt}")
            parent_themes[country_code] = None

    return parent_themes


def list_available_root_themes():
    """
    Lista todos os temas root disponíveis (sem pai) em pt-BR
    """
    root_themes = Theme.objects.filter(country='pt-BR', parent__isnull=True).order_by('order')

    if not root_themes.exists():
        print("❌ Erro: Nenhum tema root encontrado!")
        print("   Execute primeiro: python setup_data/00_root_themes.py")
        return []

    return root_themes


def get_root_theme_reference():
    """
    Retorna o dicionário de referência dos temas root para consulta
    """
    return ROOT_THEMES_REFERENCE


def find_root_theme_by_category(category_name, country='pt-BR'):
    """
    Encontra o slug do tema root baseado no nome da categoria
    
    Args:
        category_name (str): Nome da categoria (ex: 'jogos', 'esportes')
        country (str): Código do país (padrão: 'pt-BR')
    
    Returns:
        str: Slug do tema root ou None se não encontrado
    """
    reference = ROOT_THEMES_REFERENCE.get(country, {})
    
    # Buscar por slug exato
    if category_name in reference:
        return category_name
    
    # Buscar por nome/título
    for slug, title in reference.items():
        if category_name.lower() in title.lower() or title.lower() in category_name.lower():
            return slug
    
    return None




def get_user_input():
    """
    Solicita informações do usuário sobre o tema a ser criado
    """
    print("=" * 80)
    print("🎨 CRIAR NOVO TEMA")
    print("=" * 80)
    print()

    # Listar temas root disponíveis usando o dicionário de referência
    print("📋 Temas ROOT disponíveis (pt-BR):")
    print()

    root_themes = list_available_root_themes()
    reference = get_root_theme_reference()

    if not root_themes:
        sys.exit(1)

    # Mostrar temas com informações do dicionário de referência e números
    theme_list = []
    for i, theme in enumerate(root_themes, 1):
        reference_title = reference.get('pt-BR', {}).get(theme.slug, theme.title)
        print(f"   {i:2d}. {theme.slug:20s} - {reference_title}")
        theme_list.append(theme)

    print()
    print("💡 Dica: Escolha o número do tema pai")
    print("   O script encontrará automaticamente os slugs correspondentes em outros países")
    print()
    print("-" * 80)
    print()

    # Escolher tema pai por número
    print("1️⃣ Escolha o número do tema PAI (deve estar na lista acima)")
    print()

    # Validar que o número é válido
    while True:
        try:
            choice = input(f"   Número do tema pai (1-{len(theme_list)}): ").strip()
            
            if not choice:
                print("❌ Erro: Número não pode ser vazio!")
                continue

            choice_num = int(choice)
            
            if choice_num < 1 or choice_num > len(theme_list):
                print(f"❌ Erro: Número deve estar entre 1 e {len(theme_list)}!")
                print()
                continue

            # Número válido, obter o tema
            selected_theme = theme_list[choice_num - 1]
            parent_slug_pt = selected_theme.slug
            print(f"✅ Tema selecionado: {parent_slug_pt} - {selected_theme.title}")
            break

        except ValueError:
            print("❌ Erro: Digite um número válido!")
            print()
            continue

    print()

    # Slug do novo tema (base em português)
    print("2️⃣ Digite o slug BASE do novo tema em português (ex: pokemon, counter-strike)")
    print("   Para outros países, será adicionado sufixo automaticamente")
    theme_slug_base = input("   Slug base: ").strip()

    if not theme_slug_base:
        print("❌ Erro: Slug base não pode ser vazio!")
        sys.exit(1)

    print()

    # # URL da imagem
    # print("3️⃣ Digite a URL da imagem do tema (Cloudinary)")
    # theme_image = input("   URL da imagem: ").strip()

    # if not theme_image:
    #     print("❌ Erro: URL da imagem não pode ser vazia!")
    #     sys.exit(1)

    print()

    # Cores
    print("4️⃣ Cores do tema (formato hexadecimal)")
    primary_color = input("   Cor primária (ex: #ffcb05): ").strip() or '#ffcb05'
    secondary_color = input("   Cor secundária (ex: #3d7dca): ").strip() or '#3d7dca'

    print()

    # Título (mesmo para todos os idiomas) e descrições traduzidas
    print("5️⃣ Título e descrições do tema")
    print()
    
    title = input("   Título (mesmo para todos os idiomas): ").strip()
    
    if not title:
        print("❌ Erro: Título é obrigatório!")
        sys.exit(1)
    
    # Pedir descrições traduzidas
    print()
    print("   📝 Descrições traduzidas:")
    
    descriptions = {}
    main_languages = ['pt', 'en', 'es']
    lang_names = {
        'pt': 'Português',
        'en': 'Inglês', 
        'es': 'Espanhol',
    }
    
    for lang_code in main_languages:
        description = input(f"      {lang_names[lang_code]} ({lang_code}): ").strip()
        if description:
            descriptions[lang_code] = description
    
    if not descriptions:
        print("❌ Erro: Pelo menos uma descrição é necessária!")
        sys.exit(1)
    
    # Usar o mesmo título para todos, mas descrições traduzidas
    translations = {}
    for lang_code in main_languages:
        if lang_code in descriptions:
            translations[lang_code] = {
                'title': title,
                'description': descriptions[lang_code]
            }

    # Ordem de exibição
    print("6️⃣ Ordem de exibição do tema (número inteiro, menor = primeiro)")
    order = input("   Ordem (padrão: 100): ").strip()
    order = int(order) if order.isdigit() else 100

    print()

    return {
        'parent_slug_pt': parent_slug_pt,
        'theme_slug_base': theme_slug_base,
        'theme_image': '',
        'colors': {
            'primary_color': primary_color,
            'secondary_color': secondary_color,
        },
        'translations': translations,
        'order': order,
    }


def create_themes(config, parent_themes):
    """
    Cria os temas em todos os países
    """
    print("=" * 80)
    print("🚀 CRIANDO TEMAS")
    print("=" * 80)
    print()

    created_count = 0
    updated_count = 0
    errors = []

    for country_code, lang_code in COUNTRY_TO_LANG.items():
        # Usar tradução do idioma ou fallback para inglês
        translation = config['translations'].get(lang_code, config['translations'].get('en'))

        if not translation:
            errors.append(f"⚠️  Tradução não encontrada para {country_code} ({lang_code})")
            continue

        # Determinar slug do tema
        if country_code == 'pt-BR':
            theme_slug = config['theme_slug_base']
        else:
            country_suffix = country_code.split('-')[1].lower()
            theme_slug = f"{config['theme_slug_base']}-{country_suffix}"

        # Buscar tema pai
        parent_slug = parent_themes.get(country_code)

        if not parent_slug:
            errors.append(f"⚠️  Tema pai não encontrado para {country_code}")
            parent_theme = None
        else:
            try:
                parent_theme = Theme.objects.get(slug=parent_slug, country=country_code)
            except Theme.DoesNotExist:
                errors.append(f"⚠️  Tema pai '{parent_slug}' não existe para {country_code}")
                parent_theme = None

        # Criar ou atualizar tema
        theme, created = Theme.objects.update_or_create(
            slug=theme_slug,
            defaults={
                'title': translation['title'],
                'description': translation['description'],
                'icon': config['theme_image'],
                'country': country_code,
                'primary_color': config['colors']['primary_color'],
                'secondary_color': config['colors']['secondary_color'],
                'parent': parent_theme,
                'active': True,
                'order': config['order'],
            }
        )

        if created:
            created_count += 1
            status = "✅"
        else:
            updated_count += 1
            status = "🔄"

        parent_info = f"→ {parent_slug}" if parent_theme else "→ SEM PAI"
        print(f"{status} {country_code:7s} | {theme_slug:30s} {parent_info}")

    print()
    print(f"📊 Temas criados: {created_count} | Atualizados: {updated_count}")

    if errors:
        print()
        print("⚠️  AVISOS:")
        for error in errors:
            print(f"   {error}")

    print()
    return created_count + updated_count


def export_theme_fixtures(config):
    """
    Exporta os temas criados como fixtures JSON
    """
    print("=" * 80)
    print("📦 EXPORTANDO FIXTURES")
    print("=" * 80)
    print()
    
    # Criar pasta fixtures se não existir
    fixtures_dir = Path(project_root) / 'fixtures' / 'themes'
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    
    # Nome do arquivo baseado no slug
    fixture_filename = f"{config['theme_slug_base']}_themes.json"
    fixture_path = fixtures_dir / fixture_filename
    
    try:
        # Buscar todos os temas criados para este slug base
        themes_to_export = []
        
        for country_code in COUNTRY_TO_LANG.keys():
            # Determinar slug do tema
            if country_code == 'pt-BR':
                theme_slug = config['theme_slug_base']
            else:
                country_suffix = country_code.split('-')[1].lower()
                theme_slug = f"{config['theme_slug_base']}-{country_suffix}"
            
            try:
                theme = Theme.objects.get(slug=theme_slug, country=country_code)
                themes_to_export.append(theme)
            except Theme.DoesNotExist:
                continue
        
        if not themes_to_export:
            print("⚠️  Nenhum tema encontrado para exportar")
            return
        
        # Exportar usando dumpdata
        with open(fixture_path, 'w', encoding='utf-8') as f:
            call_command('dumpdata', 'quizzes.Theme', 
                        indent=2, 
                        natural_foreign=True,
                        natural_primary=True,
                        stdout=f,
                        pks=','.join([theme.slug for theme in themes_to_export]))
        
        print(f"✅ Fixture exportada: {fixture_path}")
        print(f"📊 {len(themes_to_export)} temas exportados")
        
    except Exception as e:
        print(f"❌ Erro ao exportar fixture: {e}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print()
    print("=" * 80)
    print("🎨 SCRIPT DE CRIAÇÃO DE TEMAS")
    print("=" * 80)
    print()

    # Obter configurações do usuário
    config = get_user_input()

    print()
    print("=" * 80)
    print("🔍 VERIFICANDO TEMAS PAI")
    print("=" * 80)
    print()

    # Encontrar temas pai em todos os países
    parent_themes = find_parent_themes(config['parent_slug_pt'])

    if parent_themes is None:
        print("❌ Erro: Não foi possível encontrar o tema pai")
        sys.exit(1)

    print()
    print(f"✅ Temas pai encontrados: {sum(1 for v in parent_themes.values() if v)}/{len(parent_themes)}")
    print()

    # Confirmação
    print("=" * 80)
    print("📋 RESUMO DA CONFIGURAÇÃO")
    print("=" * 80)
    print(f"Slug base: {config['theme_slug_base']}")
    print(f"Tema pai (pt-BR): {config['parent_slug_pt']}")
    print(f"Imagem: Será configurada posteriormente")
    print(f"Traduções: {len(config['translations'])} idiomas")
    print(f"Ordem: {config['order']}")
    print()



    # Criar temas
    total_themes = create_themes(config, parent_themes)

    # Exportar fixtures
    export_theme_fixtures(config)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Total de temas processados: {total_themes}")
    print()
    print("🎉 Temas criados e fixtures exportadas com sucesso!")
    print()
    print()


if __name__ == '__main__':
    try:
        main()
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
