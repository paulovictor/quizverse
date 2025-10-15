#!/usr/bin/env python
"""
Script para criar o tema de Pokémon para todos os países
"""

import os
import sys
import django
from pathlib import Path

# Setup Django
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme


def create_pokemon_theme():
    """Cria o tema de Pokémon para todos os países"""
    
    # Imagem otimizada do Cloudinary
    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,f_auto/v1760501073/ChatGPT_Image_Oct_15_2025_12_57_23_AM_tvqerr.png'
    
    # Cores do tema Pokémon
    colors = {
        'primary_color': '#ffcb05',      # Amarelo Pikachu (cor principal da franquia)
        'secondary_color': '#3d7dca',    # Azul Pokébola
        'icon_bg_color_1': '#fff9e6',    # Amarelo clarinho suave
        'icon_bg_color_2': '#ffe082',    # Amarelo médio
    }
    
    # Traduções do tema para cada idioma
    translations = {
        'pt': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Teste seus conhecimentos sobre os Pokémon da primeira geração! Identifique os 151 Pokémon originais.',
            'parent_slug': 'jogos',
        },
        'en': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Test your knowledge about first generation Pokémon! Identify all 151 original Pokémon.',
            'parent_slug': 'games',
        },
        'es': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': '¡Pon a prueba tus conocimientos sobre Pokémon de primera generación! Identifica los 151 Pokémon originales.',
            'parent_slug': 'juegos',
        },
        'fr': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Testez vos connaissances sur les Pokémon de première génération! Identifiez les 151 Pokémon originaux.',
            'parent_slug': 'jeux',
        },
        'de': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Teste dein Wissen über Pokémon der ersten Generation! Identifiziere alle 151 Original-Pokémon.',
            'parent_slug': 'spiele',
        },
        'it': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Metti alla prova le tue conoscenze sui Pokémon di prima generazione! Identifica tutti i 151 Pokémon originali.',
            'parent_slug': 'giochi',
        },
        'ja': {
            'title': 'ポケモン',
            'slug': 'pokemon',
            'description': '初代ポケモンの知識をテストしよう！151匹のオリジナルポケモンを識別してください。',
            'parent_slug': 'gemu',
        },
        'ko': {
            'title': '포켓몬',
            'slug': 'pokemon',
            'description': '1세대 포켓몬에 대한 지식을 테스트하세요! 151개의 오리지널 포켓몬을 식별하세요.',
            'parent_slug': 'geim',
        },
        'zh': {
            'title': '宝可梦',
            'slug': 'pokemon',
            'description': '测试您对第一代宝可梦的了解！识别所有151个原始宝可梦。',
            'parent_slug': 'games',  # Chinês usa 'games'
        },
        'ar': {
            'title': 'بوكيمون',
            'slug': 'pokemon',
            'description': 'اختبر معرفتك ببوكيمون الجيل الأول! حدد جميع البوكيمون الـ151 الأصلية.',
            'parent_slug': 'games',  # Árabe usa 'games'
        },
        'hi': {
            'title': 'पोकेमोन',
            'slug': 'pokemon',
            'description': 'पहली पीढ़ी के पोकेमोन के बारे में अपने ज्ञान का परीक्षण करें! सभी 151 मूल पोकेमोन की पहचान करें।',
            'parent_slug': 'games',  # Hindi usa 'games'
        },
        'ru': {
            'title': 'Покемон',
            'slug': 'pokemon',
            'description': 'Проверьте свои знания о покемонах первого поколения! Определите всех 151 оригинальных покемонов.',
            'parent_slug': 'games',  # Russo usa 'games'
        },
        'nl': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Test je kennis over Pokémon van de eerste generatie! Identificeer alle 151 originele Pokémon.',
            'parent_slug': 'games',
        },
        'pl': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Sprawdź swoją wiedzę o Pokémonach pierwszej generacji! Zidentyfikuj wszystkie 151 oryginalnych Pokémonów.',
            'parent_slug': 'gry',
        },
        'sv': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Testa dina kunskaper om första generationens Pokémon! Identifiera alla 151 original Pokémon.',
            'parent_slug': 'spel',
        },
        'tr': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Birinci nesil Pokémon hakkındaki bilginizi test edin! 151 orijinal Pokémon\'u tanımlayın.',
            'parent_slug': 'games',  # Turco usa 'games'
        },
        'th': {
            'title': 'โปเกมอน',
            'slug': 'pokemon',
            'description': 'ทดสอบความรู้ของคุณเกี่ยวกับโปเกมอนรุ่นแรก! ระบุโปเกมอนต้นฉบับทั้ง 151 ตัว',
            'parent_slug': 'gem',
        },
        'vi': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Kiểm tra kiến thức của bạn về Pokémon thế hệ đầu tiên! Xác định tất cả 151 Pokémon gốc.',
            'parent_slug': 'tro-choi',
        },
        'no': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Test kunnskapen din om første generasjon Pokémon! Identifiser alle 151 originale Pokémon.',
            'parent_slug': 'spill',
        },
        'id': {
            'title': 'Pokémon',
            'slug': 'pokemon',
            'description': 'Uji pengetahuan Anda tentang Pokémon generasi pertama! Identifikasi semua 151 Pokémon asli.',
            'parent_slug': 'game',
        },
    }
    
    # Mapeamento de países para idiomas (MESMOS países do 00_root_themes.py)
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
    
    print("=" * 80)
    print("🎮 CRIANDO TEMA POKÉMON PARA TODOS OS PAÍSES")
    print("=" * 80)
    print()
    print(f"🖼️  Imagem: {theme_image}")
    print(f"🎨 Cores:")
    print(f"   Primary:   {colors['primary_color']} (Amarelo Pikachu)")
    print(f"   Secondary: {colors['secondary_color']} (Azul Pokébola)")
    print(f"   Icon BG 1: {colors['icon_bg_color_1']} (Amarelo claro)")
    print(f"   Icon BG 2: {colors['icon_bg_color_2']} (Amarelo médio)")
    print()
    print("-" * 80)
    print()
    
    created_count = 0
    updated_count = 0
    errors = []
    
    for country_code, lang_code in country_to_lang.items():
        translation = translations.get(lang_code, translations['en'])
        
        # Criar slug baseado no país
        if country_code == 'pt-BR':
            # Brasil: sem sufixo
            theme_slug = translation['slug']
            parent_slug = translation['parent_slug']
        else:
            # Outros países: usar apenas o código do país (segunda parte)
            # en-US → us, ja-JP → jp, fr-FR → fr
            country_suffix = country_code.split('-')[1].lower()
            theme_slug = f"{translation['slug']}-{country_suffix}"
            parent_slug = f"{translation['parent_slug']}-{country_suffix}"
        
        # Buscar o tema pai "Jogos" do país correspondente
        try:
            parent_theme = Theme.objects.get(slug=parent_slug)
        except Theme.DoesNotExist:
            errors.append(f"⚠️  Tema pai não encontrado: {parent_slug} para {country_code}")
            parent_theme = None
        
        # Verificar se o tema já existe
        theme, created = Theme.objects.update_or_create(
            slug=theme_slug,
            defaults={
                'title': translation['title'],
                'description': translation['description'],
                'icon': theme_image,
                'country': country_code,  # Associar ao país correto
                'primary_color': colors['primary_color'],
                'secondary_color': colors['secondary_color'],
                'icon_bg_color_1': colors['icon_bg_color_1'],
                'icon_bg_color_2': colors['icon_bg_color_2'],
                'parent': parent_theme,  # Associar ao tema pai "Jogos"
                'active': True,
                'order': 100,  # Ordem alta para aparecer por último
            }
        )
        
        if created:
            created_count += 1
            status = "✅ CRIADO"
        else:
            updated_count += 1
            status = "♻️  ATUALIZADO"
        
        parent_info = f"→ {parent_slug}" if parent_theme else "→ SEM PAI"
        print(f"{status} | {country_code:7s} | {theme_slug:25s} | {translation['title']:20s} {parent_info}")
    
    print()
    print("-" * 80)
    print()
    print(f"📊 RESUMO:")
    print(f"   ✅ Temas criados:     {created_count}")
    print(f"   ♻️  Temas atualizados: {updated_count}")
    print(f"   📝 Total:             {created_count + updated_count}")
    
    if errors:
        print()
        print("⚠️  AVISOS:")
        for error in errors:
            print(f"   {error}")
    
    print()
    print("🎉 Tema Pokémon criado com sucesso para todos os países!")
    print()
    
    return created_count, updated_count


if __name__ == '__main__':
    print()
    create_pokemon_theme()

