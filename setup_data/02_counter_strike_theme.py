#!/usr/bin/env python
"""
Script para criar o tema Counter-Strike (pai) em todos os países.
Este tema será usado como pai para outros temas de CS2 (AK-47 Skins, etc).

Pré-requisito: 00_root_themes.py deve ter sido executado.
"""

import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme


def create_counter_strike_themes():
    """Cria o tema Counter-Strike (pai) para todos os países"""

    print("=" * 80)
    print("CRIANDO TEMAS COUNTER-STRIKE")
    print("=" * 80)
    print()

    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760675444/counter-strike-2_k7eozw.png'

    colors = {
        'primary_color': '#ff6347',  # Vermelho CS
        'secondary_color': '#1e90ff',  # Azul CS
        'icon_bg_color_1': '#fff5f0',
        'icon_bg_color_2': '#ffcccb',
    }

    translations = {
        'pt': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Teste seus conhecimentos sobre Counter-Strike! Skins, mapas, armas e muito mais.',
            'parent_slug': 'jogos',
        },
        'en': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Test your Counter-Strike knowledge! Skins, maps, weapons and more.',
            'parent_slug': 'games',
        },
        'es': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': '¡Pon a prueba tus conocimientos sobre Counter-Strike! Skins, mapas, armas y más.',
            'parent_slug': 'juegos',
        },
        'fr': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Testez vos connaissances sur Counter-Strike! Skins, cartes, armes et plus.',
            'parent_slug': 'jeux',
        },
        'de': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Teste dein Counter-Strike Wissen! Skins, Karten, Waffen und mehr.',
            'parent_slug': 'spiele',
        },
        'it': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Metti alla prova le tue conoscenze su Counter-Strike! Skin, mappe, armi e altro.',
            'parent_slug': 'giochi',
        },
        'nl': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Test je Counter-Strike kennis! Skins, maps, wapens en meer.',
            'parent_slug': 'games',
        },
        'pl': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Sprawdź swoją wiedzę o Counter-Strike! Skórki, mapy, broń i więcej.',
            'parent_slug': 'gry',
        },
        'sv': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Testa din Counter-Strike kunskap! Skins, kartor, vapen och mer.',
            'parent_slug': 'spel',
        },
        'no': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Test din Counter-Strike kunnskap! Skins, kart, våpen og mer.',
            'parent_slug': 'spill',
        },
        'id': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Uji pengetahuan Counter-Strike Anda! Skin, map, senjata dan lainnya.',
            'parent_slug': 'game',
        },
        'ja': {
            'title': 'カウンターストライク',
            'slug': 'counter-strike',
            'description': 'Counter-Strikeの知識をテストしよう！スキン、マップ、武器など。',
            'parent_slug': 'gemu',
        },
        'ko': {
            'title': '카운터 스트라이크',
            'slug': 'counter-strike',
            'description': 'Counter-Strike 지식을 테스트하세요! 스킨, 맵, 무기 등.',
            'parent_slug': 'geim',
        },
        'th': {
            'title': 'เคาน์เตอร์สไตรค์',
            'slug': 'counter-strike',
            'description': 'ทดสอบความรู้ Counter-Strike ของคุณ! สกิน แผนที่ อาวุธ และอื่นๆ',
            'parent_slug': 'gem',
        },
        'vi': {
            'title': 'Counter-Strike',
            'slug': 'counter-strike',
            'description': 'Kiểm tra kiến thức Counter-Strike của bạn! Skin, bản đồ, vũ khí và hơn thế nữa.',
            'parent_slug': 'tro-choi',
        },
    }

    country_to_lang = {
        'en-US': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-IN': 'en', 'en-PH': 'en', 'en-AU': 'en', 'en-NZ': 'en',
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

    created_count = 0
    updated_count = 0
    errors = []

    for country_code, lang_code in country_to_lang.items():
        translation = translations.get(lang_code, translations['en'])

        if country_code == 'pt-BR':
            theme_slug = translation['slug']
            parent_slug = translation['parent_slug']
        else:
            country_suffix = country_code.split('-')[1].lower()
            theme_slug = f"{translation['slug']}-{country_suffix}"
            parent_slug = f"{translation['parent_slug']}-{country_suffix}"

        try:
            parent_theme = Theme.objects.get(slug=parent_slug)
        except Theme.DoesNotExist:
            errors.append(f"⚠️  Tema pai não encontrado: {parent_slug} para {country_code}")
            parent_theme = None

        theme, created = Theme.objects.update_or_create(
            slug=theme_slug,
            defaults={
                'title': translation['title'],
                'description': translation['description'],
                'icon': theme_image,
                'country': country_code,
                'primary_color': colors['primary_color'],
                'secondary_color': colors['secondary_color'],
                'icon_bg_color_1': colors['icon_bg_color_1'],
                'icon_bg_color_2': colors['icon_bg_color_2'],
                'parent': parent_theme,
                'active': True,
                'order': 50,
            }
        )

        if created:
            created_count += 1
            status = "✅"
        else:
            updated_count += 1
            status = "🔄"

        parent_info = f"→ {parent_slug}" if parent_theme else "→ SEM PAI"
        print(f"{status} {country_code:7s} | {theme_slug:25s} {parent_info}")

    print()
    print(f"📊 Temas Counter-Strike criados: {created_count} | Atualizados: {updated_count}")

    if errors:
        print()
        for error in errors:
            print(error)

    print()
    return created_count + updated_count


def main():
    print()
    print("=" * 80)
    print("🎮 SETUP: TEMA COUNTER-STRIKE")
    print("=" * 80)
    print()

    themes_count = create_counter_strike_themes()

    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Temas Counter-Strike criados/atualizados: {themes_count}")
    print()
    print("🎉 Setup do tema Counter-Strike concluído com sucesso!")
    print()
    print("💡 Próximos passos:")
    print("   1. Verifique os temas em /admin/quizzes/theme/")
    print("   2. Execute outros scripts de setup de CS2 (ex: 03_aks.py)")
    print()


if __name__ == '__main__':
    main()
