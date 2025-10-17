#!/usr/bin/env python
"""
Script para criar apenas os temas de Pokémon que estão faltando
"""
import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

def create_missing_pokemon_themes():
    """Cria apenas os temas de Pokémon que estão faltando"""
    
    print("=" * 80)
    print("CRIANDO TEMAS POKÉMON FALTANDO")
    print("=" * 80)
    print()
    
    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,f_auto/v1760501073/ChatGPT_Image_Oct_15_2025_12_57_23_AM_tvqerr.png'
    
    colors = {
        'primary_color': '#ffcb05',
        'secondary_color': '#3d7dca',
        'icon_bg_color_1': '#fff9e6',
        'icon_bg_color_2': '#ffe082',
    }
    
    # Países que estão faltando
    missing_countries = [
        {
            'country_code': 'ja-JP',
            'lang_code': 'ja',
            'title': 'ポケモン',
            'slug': 'pokemon-jp',
            'description': '初代ポケモンの知識をテストしよう！151匹のオリジナルポケモンを識別してください。',
            'parent_slug': 'gemu-jp',
        },
        {
            'country_code': 'ko-KR',
            'lang_code': 'ko',
            'title': '포켓몬',
            'slug': 'pokemon-kr',
            'description': '1세대 포켓몬에 대한 지식을 테스트하세요! 151개의 오리지널 포켓몬을 식별하세요.',
            'parent_slug': 'geim-kr',
        },
        {
            'country_code': 'th-TH',
            'lang_code': 'th',
            'title': 'โปเกมอน',
            'slug': 'pokemon-th',
            'description': 'ทดสอบความรู้ของคุณเกี่ยวกับโปเกมอนรุ่นแรก! ระบุโปเกมอนต้นฉบับทั้ง 151 ตัว',
            'parent_slug': 'gem-th',
        },
    ]
    
    created_count = 0
    updated_count = 0
    errors = []
    
    for country_data in missing_countries:
        try:
            parent_theme = Theme.objects.get(slug=country_data['parent_slug'])
        except Theme.DoesNotExist:
            errors.append(f"⚠️  Tema pai não encontrado: {country_data['parent_slug']} para {country_data['country_code']}")
            parent_theme = None
        
        theme, created = Theme.objects.update_or_create(
            slug=country_data['slug'],
            defaults={
                'title': country_data['title'],
                'description': country_data['description'],
                'icon': theme_image,
                'country': country_data['country_code'],
                'primary_color': colors['primary_color'],
                'secondary_color': colors['secondary_color'],
                'icon_bg_color_1': colors['icon_bg_color_1'],
                'icon_bg_color_2': colors['icon_bg_color_2'],
                'parent': parent_theme,
                'active': True,
                'order': 100,
            }
        )
        
        if created:
            created_count += 1
            status = "✅"
        else:
            updated_count += 1
            status = "🔄"
        
        parent_info = f"→ {country_data['parent_slug']}" if parent_theme else "→ SEM PAI"
        print(f"{status} {country_data['country_code']:7s} | {country_data['slug']:25s} {parent_info}")
    
    print()
    print(f"📊 Temas criados: {created_count} | Atualizados: {updated_count}")
    
    if errors:
        print()
        for error in errors:
            print(error)
    
    print()
    return created_count + updated_count

if __name__ == '__main__':
    create_missing_pokemon_themes()
