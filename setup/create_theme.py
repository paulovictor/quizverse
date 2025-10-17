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
import django
from pathlib import Path

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
    'es-MX': 'es', 'es-ES': 'es', 'es-AR': 'es', 'es-CO': 'es',
    'de-DE': 'de',
    'fr-FR': 'fr',
    'it-IT': 'it',
    'nl-NL': 'nl',
    'sv-SE': 'sv',
    'no-NO': 'no',
    'pl-PL': 'pl',
    'id-ID': 'id',
    'ja-JP': 'ja',
    'ko-KR': 'ko',
    'th-TH': 'th',
    'vi-VN': 'vi',
}


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def find_parent_themes(parent_slug_pt):
    """
    Encontra os slugs dos temas pai em todos os países baseado no slug PT-BR

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

    # Para outros países, buscar variações do slug
    for country_code in COUNTRY_TO_LANG.keys():
        if country_code == 'pt-BR':
            continue

        country_suffix = country_code.split('-')[1].lower()
        expected_slug = f"{parent_slug_pt}-{country_suffix}"

        try:
            parent_theme = Theme.objects.get(slug=expected_slug, country=country_code)
            parent_themes[country_code] = parent_theme.slug
        except Theme.DoesNotExist:
            print(f"⚠️  Tema pai não encontrado para {country_code}: {expected_slug}")
            parent_themes[country_code] = None

    return parent_themes


def get_user_input():
    """
    Solicita informações do usuário sobre o tema a ser criado
    """
    print("=" * 80)
    print("🎨 CRIAR NOVO TEMA")
    print("=" * 80)
    print()

    # Slug do tema pai (em português)
    print("1️⃣ Digite o slug do tema PAI em português (ex: jogos, filmes, etc)")
    print("   O script buscará automaticamente os slugs correspondentes em outros países")
    parent_slug_pt = input("   Slug do tema pai (pt-BR): ").strip()

    if not parent_slug_pt:
        print("❌ Erro: Slug do tema pai não pode ser vazio!")
        sys.exit(1)

    print()

    # Slug do novo tema (base em português)
    print("2️⃣ Digite o slug BASE do novo tema em português (ex: pokemon, counter-strike)")
    print("   Para outros países, será adicionado sufixo automaticamente")
    theme_slug_base = input("   Slug base: ").strip()

    if not theme_slug_base:
        print("❌ Erro: Slug base não pode ser vazio!")
        sys.exit(1)

    print()

    # URL da imagem
    print("3️⃣ Digite a URL da imagem do tema (Cloudinary)")
    theme_image = input("   URL da imagem: ").strip()

    if not theme_image:
        print("❌ Erro: URL da imagem não pode ser vazia!")
        sys.exit(1)

    print()

    # Cores
    print("4️⃣ Cores do tema (formato hexadecimal)")
    primary_color = input("   Cor primária (ex: #ffcb05): ").strip() or '#ffcb05'
    secondary_color = input("   Cor secundária (ex: #3d7dca): ").strip() or '#3d7dca'

    print()

    # Traduções
    print("5️⃣ Traduções do tema")
    print()

    translations = {}

    # Definir quais idiomas pedir tradução
    main_languages = ['pt', 'en', 'es', 'de', 'fr', 'it']

    for lang_code in main_languages:
        lang_names = {
            'pt': 'Português',
            'en': 'Inglês',
            'es': 'Espanhol',
            'de': 'Alemão',
            'fr': 'Francês',
            'it': 'Italiano',
        }

        print(f"   📝 {lang_names[lang_code]} ({lang_code})")
        title = input(f"      Título: ").strip()
        description = input(f"      Descrição: ").strip()

        if not title or not description:
            print(f"   ⚠️  Pulando {lang_code} (campos vazios)")
            continue

        translations[lang_code] = {
            'title': title,
            'description': description,
        }
        print()

    if not translations:
        print("❌ Erro: Pelo menos uma tradução é necessária!")
        sys.exit(1)

    # Ordem de exibição
    print("6️⃣ Ordem de exibição do tema (número inteiro, menor = primeiro)")
    order = input("   Ordem (padrão: 100): ").strip()
    order = int(order) if order.isdigit() else 100

    print()

    return {
        'parent_slug_pt': parent_slug_pt,
        'theme_slug_base': theme_slug_base,
        'theme_image': theme_image,
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
    print(f"Imagem: {config['theme_image'][:60]}...")
    print(f"Traduções: {len(config['translations'])} idiomas")
    print(f"Ordem: {config['order']}")
    print()

    response = input("Deseja continuar com a criação dos temas? (s/n): ").strip().lower()

    if response != 's':
        print("⚠️  Operação cancelada pelo usuário")
        sys.exit(0)

    print()

    # Criar temas
    total_themes = create_themes(config, parent_themes)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Total de temas processados: {total_themes}")
    print()
    print("🎉 Temas criados com sucesso!")
    print()
    print("💡 Próximos passos:")
    print("   1. Criar QuizGroup para este tema")
    print("   2. Criar Quizzes e Questões")
    print("   3. Criar Badges (opcional)")
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
