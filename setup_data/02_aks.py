#!/usr/bin/env python
"""
Script consolidado para setup completo de AK-47 Skins do Counter-Strike.
Cria temas, quizgroup, quizzes e questões em uma única execução.

Pré-requisito: 00_root_themes.py deve ter sido executado.
"""

import os
import sys
import json
import random
import django
from pathlib import Path

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, QuizGroup, Question, Answer, Badge, QuizGroupBadge


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def load_ak47_data():
    """Carrega os dados das AK-47 do arquivo JSON"""
    data_file = Path(project_root) / 'cs2_skins' / 'ak_47.json'

    if not data_file.exists():
        print(f"❌ Erro: Arquivo ak_47.json não encontrado em {data_file}")
        return None

    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_cloudinary_urls():
    """Carrega as URLs do Cloudinary"""
    cloudinary_file = Path(project_root) / 'ak47_urls.json'

    if not cloudinary_file.exists():
        print("⚠️  Arquivo ak47_urls.json não encontrado")
        print("Será usado o caminho da foto do JSON")
        return None

    with open(cloudinary_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Criar dicionário indexado por nome normalizado
        url_map = {}
        for item in data:
            # Extrair nome do public_id (remover sufixo hash)
            name = item['public_id'].rsplit('_', 1)[0].replace('_', ' ')
            url_map[name] = item['secure_url']
        return url_map


def get_skin_url(skin_name, cloudinary_urls, fallback_url):
    """Retorna a URL da skin do Cloudinary ou fallback"""
    if cloudinary_urls and skin_name in cloudinary_urls:
        return cloudinary_urls[skin_name]
    return fallback_url


# ============================================================================
# ETAPA 0: CRIAR TEMAS COUNTER-STRIKE (PAI)
# ============================================================================

def create_counter_strike_themes():
    """Cria o tema Counter-Strike (pai) para todos os países"""

    print("=" * 80)
    print("ETAPA 0: CRIANDO TEMAS COUNTER-STRIKE (PAI)")
    print("=" * 80)
    print()

    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760663478/counter-strike-2-pc-jogo-steam-cover_zp57n2.jpg'

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


# ============================================================================
# ETAPA 1: CRIAR TEMAS AK-47
# ============================================================================

def create_ak47_themes():
    """Cria o tema de AK-47 para todos os países"""

    print("=" * 80)
    print("ETAPA 1: CRIANDO TEMAS AK-47")
    print("=" * 80)
    print()

    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760663546/best-ak-buyers-guide-ak47-feature-hd-768x496_ixmyvw.jpg'

    colors = {
        'primary_color': '#ff6347',  # Vermelho CS:GO
        'secondary_color': '#1e90ff',  # Azul CS:GO
        'icon_bg_color_1': '#fff5f0',
        'icon_bg_color_2': '#ffcccb',
    }

    translations = {
        'pt': {
            'title': 'AK-47 Skins - CS2',
            'slug': 'ak47-skins',
            'description': 'Teste seus conhecimentos sobre as skins da AK-47 do Counter-Strike! Identifique as 55 skins mais icônicas.',
            'parent_slug': 'counter-strike',
        },
        'en': {
            'title': 'AK-47 Skins - CS2',
            'slug': 'ak47-skins',
            'description': 'Test your knowledge about Counter-Strike AK-47 skins! Identify the 55 most iconic skins.',
            'parent_slug': 'counter-strike',
        },
        'es': {
            'title': 'Skins AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': '¡Pon a prueba tus conocimientos sobre las skins de AK-47 de Counter-Strike! Identifica las 55 skins más icónicas.',
            'parent_slug': 'counter-strike',
        },
        'fr': {
            'title': 'Skins AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': 'Testez vos connaissances sur les skins AK-47 de Counter-Strike! Identifiez les 55 skins les plus emblématiques.',
            'parent_slug': 'counter-strike',
        },
        'de': {
            'title': 'AK-47 Skins - CS2',
            'slug': 'ak47-skins',
            'description': 'Teste dein Wissen über Counter-Strike AK-47 Skins! Identifiziere die 55 ikonischsten Skins.',
            'parent_slug': 'counter-strike',
        },
        'it': {
            'title': 'Skin AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': 'Metti alla prova le tue conoscenze sulle skin AK-47 di Counter-Strike! Identifica le 55 skin più iconiche.',
            'parent_slug': 'counter-strike',
        },
        'nl': {
            'title': 'AK-47 Skins - CS2',
            'slug': 'ak47-skins',
            'description': 'Test je kennis over Counter-Strike AK-47 skins! Identificeer de 55 meest iconische skins.',
            'parent_slug': 'counter-strike',
        },
        'pl': {
            'title': 'Skórki AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': 'Sprawdź swoją wiedzę o skórkach AK-47 z Counter-Strike! Zidentyfikuj 55 najbardziej kultowych skórek.',
            'parent_slug': 'counter-strike',
        },
        'sv': {
            'title': 'AK-47 Skins - CS2',
            'slug': 'ak47-skins',
            'description': 'Testa dina kunskaper om Counter-Strike AK-47 skins! Identifiera de 55 mest ikoniska skinsen.',
            'parent_slug': 'counter-strike',
        },
        'no': {
            'title': 'AK-47 Skins - CS2',
            'slug': 'ak47-skins',
            'description': 'Test kunnskapen din om Counter-Strike AK-47 skins! Identifiser de 55 mest ikoniske skinsene.',
            'parent_slug': 'counter-strike',
        },
        'id': {
            'title': 'Skin AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': 'Uji pengetahuan Anda tentang skin AK-47 Counter-Strike! Identifikasi 55 skin paling ikonik.',
            'parent_slug': 'counter-strike',
        },
        'ja': {
            'title': 'AK-47スキン - CS2',
            'slug': 'ak47-skins',
            'description': 'Counter-StrikeのAK-47スキンの知識をテストしよう！55種類の最も象徴的なスキンを識別してください。',
            'parent_slug': 'counter-strike',
        },
        'ko': {
            'title': 'AK-47 스킨 - CS2',
            'slug': 'ak47-skins',
            'description': 'Counter-Strike AK-47 스킨에 대한 지식을 테스트하세요! 가장 상징적인 55개의 스킨을 식별하세요.',
            'parent_slug': 'counter-strike',
        },
        'th': {
            'title': 'สกิน AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': 'ทดสอบความรู้ของคุณเกี่ยวกับสกิน AK-47 จาก Counter-Strike! ระบุสกิน 55 แบบที่โดดเด่นที่สุด',
            'parent_slug': 'counter-strike',
        },
        'vi': {
            'title': 'Skin AK-47 - CS2',
            'slug': 'ak47-skins',
            'description': 'Kiểm tra kiến thức của bạn về skin AK-47 Counter-Strike! Xác định 55 skin mang tính biểu tượng nhất.',
            'parent_slug': 'counter-strike',
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
                'order': 100,
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
    print(f"📊 Temas criados: {created_count} | Atualizados: {updated_count}")

    if errors:
        print()
        for error in errors:
            print(error)

    print()
    return created_count + updated_count


# ============================================================================
# ETAPA 2: CRIAR QUIZGROUP
# ============================================================================

def create_ak47_quizgroup():
    """Cria o QuizGroup para AK-47 Skins"""

    print("=" * 80)
    print("ETAPA 2: CRIANDO QUIZGROUP")
    print("=" * 80)
    print()

    quiz_group, created = QuizGroup.objects.update_or_create(
        slug='ak47-skins-cs2',
        defaults={
            'name': 'AK-47 Skins - Guess the Skin',
            'description': 'Grupo de quizzes "Adivinhe a Skin da AK-47" do CS2, disponível em múltiplos idiomas.',
            'difficulty': 'medium',
            'order': 0,
        }
    )

    status = "✅ Criado" if created else "🔄 Atualizado"
    print(f"{status}: {quiz_group.name}")
    print()

    return quiz_group


# ============================================================================
# ETAPA 3: CRIAR QUIZZES COM QUESTÕES
# ============================================================================

def get_quiz_description_template(lang_code):
    """Retorna template de descrição com placeholders {sample_size} e {total}"""
    templates = {
        'en': 'Identify {sample_size} random AK-47 skins from the {total} available! Test your Counter-Strike knowledge.',
        'pt': 'Identifique {sample_size} skins aleatórias de AK-47 das {total} disponíveis! Teste seu conhecimento de Counter-Strike.',
        'es': '¡Identifica {sample_size} skins aleatorias de AK-47 de las {total} disponibles! Pon a prueba tu conocimiento de Counter-Strike.',
        'de': 'Identifizieren Sie {sample_size} zufällige AK-47 Skins aus den {total} verfügbaren! Testen Sie Ihr Counter-Strike Wissen.',
        'fr': 'Identifiez {sample_size} skins AK-47 aléatoires parmi les {total} disponibles! Testez vos connaissances Counter-Strike.',
        'it': 'Identifica {sample_size} skin AK-47 casuali tra le {total} disponibili! Metti alla prova la tua conoscenza di Counter-Strike.',
        'nl': 'Identificeer {sample_size} willekeurige AK-47 skins uit de {total} beschikbare! Test je Counter-Strike kennis.',
        'sv': 'Identifiera {sample_size} slumpmässiga AK-47 skins från de {total} tillgängliga! Testa din Counter-Strike kunskap.',
        'no': 'Identifiser {sample_size} tilfeldige AK-47 skins fra de {total} tilgjengelige! Test din Counter-Strike kunnskap.',
        'pl': 'Zidentyfikuj {sample_size} losowych skórek AK-47 spośród {total} dostępnych! Przetestuj swoją wiedzę o Counter-Strike.',
        'id': 'Identifikasi {sample_size} skin AK-47 acak dari {total} yang tersedia! Uji pengetahuan Counter-Strike Anda.',
        'ja': '{total}個のAK-47スキンから{sample_size}個をランダムに識別しよう！Counter-Strikeの知識をテストしよう。',
        'ko': '{total}개의 사용 가능한 AK-47 스킨 중 {sample_size}개를 무작위로 식별하세요! Counter-Strike 지식을 테스트하세요.',
        'th': 'ระบุสกิน AK-47 {sample_size} แบบแบบสุ่มจากทั้งหมด {total} แบบ! ทดสอบความรู้ Counter-Strike ของคุณ',
        'vi': 'Nhận dạng {sample_size} skin AK-47 ngẫu nhiên từ {total} skin có sẵn! Kiểm tra kiến thức Counter-Strike của bạn.',
    }
    return templates.get(lang_code, templates['en'])


def create_ak47_quizzes(quiz_group, all_skins, cloudinary_urls):
    """Cria os quizzes de AK-47 para todos os países"""

    print("=" * 80)
    print("ETAPA 3: CRIANDO QUIZZES E QUESTÕES")
    print("=" * 80)
    print()

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

    quiz_translations = {
        'en': {
            'title': 'Guess the AK-47 Skin - CS2',
            'question_text': 'Which AK-47 skin is this?',
            'explanation_template': 'This is {name}, an AK-47 skin from Counter-Strike 2.'
        },
        'pt': {
            'title': 'Adivinhe a Skin da AK-47 - CS2',
            'question_text': 'Qual é esta skin de AK-47?',
            'explanation_template': 'Esta é {name}, uma skin de AK-47 do Counter-Strike 2.'
        },
        'es': {
            'title': 'Adivina la Skin de AK-47 - CS2',
            'question_text': '¿Cuál es esta skin de AK-47?',
            'explanation_template': 'Esta es {name}, una skin de AK-47 de Counter-Strike 2.'
        },
        'de': {
            'title': 'Errate die AK-47 Skin - CS2',
            'question_text': 'Welche AK-47 Skin ist das?',
            'explanation_template': 'Dies ist {name}, eine AK-47 Skin aus Counter-Strike 2.'
        },
        'fr': {
            'title': 'Devinez la Skin AK-47 - CS2',
            'question_text': 'Quelle est cette skin AK-47?',
            'explanation_template': 'C\'est {name}, une skin AK-47 de Counter-Strike 2.'
        },
        'it': {
            'title': 'Indovina la Skin AK-47 - CS2',
            'question_text': 'Quale skin AK-47 è questa?',
            'explanation_template': 'Questa è {name}, una skin AK-47 di Counter-Strike 2.'
        },
        'nl': {
            'title': 'Raad de AK-47 Skin - CS2',
            'question_text': 'Welke AK-47 skin is dit?',
            'explanation_template': 'Dit is {name}, een AK-47 skin van Counter-Strike 2.'
        },
        'sv': {
            'title': 'Gissa AK-47 Skinnet - CS2',
            'question_text': 'Vilket AK-47 skin är detta?',
            'explanation_template': 'Detta är {name}, en AK-47 skin från Counter-Strike 2.'
        },
        'no': {
            'title': 'Gjett AK-47 Skinnet - CS2',
            'question_text': 'Hvilket AK-47 skin er dette?',
            'explanation_template': 'Dette er {name}, en AK-47 skin fra Counter-Strike 2.'
        },
        'pl': {
            'title': 'Zgadnij Skórkę AK-47 - CS2',
            'question_text': 'Która to skórka AK-47?',
            'explanation_template': 'To jest {name}, skórka AK-47 z Counter-Strike 2.'
        },
        'id': {
            'title': 'Tebak Skin AK-47 - CS2',
            'question_text': 'Skin AK-47 apa ini?',
            'explanation_template': 'Ini adalah {name}, skin AK-47 dari Counter-Strike 2.'
        },
        'ja': {
            'title': 'AK-47スキンを当てよう - CS2',
            'question_text': 'このAK-47スキンは何？',
            'explanation_template': 'これは{name}、Counter-Strike 2のAK-47スキンです。'
        },
        'ko': {
            'title': 'AK-47 스킨 맞히기 - CS2',
            'question_text': '이 AK-47 스킨은 무엇입니까?',
            'explanation_template': '이것은 {name}, Counter-Strike 2의 AK-47 스킨입니다.'
        },
        'th': {
            'title': 'ทายสกิน AK-47 - CS2',
            'question_text': 'สกิน AK-47 นี้คืออะไร?',
            'explanation_template': 'นี่คือ {name} สกิน AK-47 จาก Counter-Strike 2'
        },
        'vi': {
            'title': 'Đoán Skin AK-47 - CS2',
            'question_text': 'Đây là skin AK-47 nào?',
            'explanation_template': 'Đây là {name}, một skin AK-47 từ Counter-Strike 2.'
        },
    }

    countries = list(country_to_lang.keys())
    num_questions = len(all_skins)  # 55 skins
    created_count = 0
    updated_count = 0
    total_questions_created = 0

    for country_code in countries:
        lang_code = country_to_lang[country_code]
        translation = quiz_translations.get(lang_code, quiz_translations['en'])

        # Determinar slug do tema
        if country_code == 'pt-BR':
            theme_slug = 'ak47-skins'
        else:
            country_suffix = country_code.split('-')[1].lower()
            theme_slug = f"ak47-skins-{country_suffix}"

        # Buscar tema
        try:
            theme = Theme.objects.get(slug=theme_slug)
        except Theme.DoesNotExist:
            print(f"⚠️  Tema não encontrado: {theme_slug}")
            continue

        # Determinar slug do quiz
        quiz_base_slug = 'adivinhe-skin-ak47' if lang_code == 'pt' else 'guess-ak47-skin'
        if country_code == 'pt-BR':
            quiz_slug = quiz_base_slug
        else:
            country_suffix = country_code.split('-')[1].lower()
            quiz_slug = f"{quiz_base_slug}-{country_suffix}"

        # Gerar template e description inicial
        quiz_sample_size = num_questions
        quiz_description_template = get_quiz_description_template(lang_code)
        quiz_description = quiz_description_template.format(sample_size=num_questions, total=num_questions)

        # Criar ou atualizar quiz
        quiz, quiz_created = Quiz.objects.update_or_create(
            slug=quiz_slug,
            defaults={
                'theme': theme,
                'quiz_group': quiz_group,
                'title': translation['title'],
                'description': quiz_description,
                'description_template': quiz_description_template,
                'difficulty': 'medium',
                'active': True,
                'order': 1,
                'country': country_code,
                'question_sample_size': quiz_sample_size,
            }
        )

        if quiz_created:
            created_count += 1
            status = "✅"
        else:
            updated_count += 1
            status = "🔄"
            # Limpar questões antigas
            quiz.questions.all().delete()

        print(f"{status} {country_code} | {quiz_slug}")

        # Criar questões
        question_count = 0

        for idx, skin in enumerate(all_skins, 1):
            name = skin['name']

            explanation = translation['explanation_template'].format(name=name)

            # Determinar imagem
            image_path = get_skin_url(name, cloudinary_urls, skin['foto'])

            # Criar questão
            question = Question.objects.create(
                quiz=quiz,
                text=translation['question_text'],
                image=image_path,
                explanation=explanation,
                order=idx
            )

            # Criar respostas (correta + 3 incorretas das opções)
            answers_data = [{'text': name, 'is_correct': True}]
            for wrong_option in skin['opcoes'][:3]:  # Pegar as 3 opções incorretas
                answers_data.append({'text': wrong_option, 'is_correct': False})

            random.shuffle(answers_data)

            for answer_data in answers_data:
                Answer.objects.create(
                    question=question,
                    text=answer_data['text'],
                    is_correct=answer_data['is_correct']
                )

            question_count += 1

        total_questions_created += question_count
        print(f"   ❓ {question_count} questões criadas")

    print()
    print(f"📊 Quizzes criados: {created_count} | Atualizados: {updated_count}")
    print(f"❓ Total de questões: {total_questions_created}")

    # Atualizar descrições após criar todas as questões
    print("\n🔄 Atualizando descrições dos quizzes...")
    updated_descriptions = 0
    for country_code in countries:
        lang_code = country_to_lang[country_code]

        # Determinar slug do quiz
        quiz_base_slug = 'adivinhe-skin-ak47' if lang_code == 'pt' else 'guess-ak47-skin'
        if country_code == 'pt-BR':
            quiz_slug = quiz_base_slug
        else:
            country_suffix = country_code.split('-')[1].lower()
            quiz_slug = f"{quiz_base_slug}-{country_suffix}"

        try:
            quiz = Quiz.objects.get(slug=quiz_slug)
            if quiz.description_template:
                quiz.save()  # Isso vai chamar render_description() automaticamente
                updated_descriptions += 1
        except Quiz.DoesNotExist:
            pass

    print(f"✅ {updated_descriptions} descrições atualizadas")
    print()

    return created_count, updated_count


# ============================================================================
# ETAPA 4: CRIAR BADGES
# ============================================================================

def create_ak47_badges(quiz_group):
    """Cria as badges de AK-47 Skins e associa ao QuizGroup"""

    print("=" * 80)
    print("ETAPA 4: CRIANDO BADGES DE AK-47 SKINS")
    print("=" * 80)
    print()

    # Traduções das descrições das badges
    badge_descriptions = {
        'bronze': {
            'pt-BR': 'Acerte todas as skins de AK-47!',
            'en-US': 'Get all AK-47 skins correct!',
            'en-CA': 'Get all AK-47 skins correct!',
            'en-GB': 'Get all AK-47 skins correct!',
            'en-IN': 'Get all AK-47 skins correct!',
            'en-PH': 'Get all AK-47 skins correct!',
            'en-AU': 'Get all AK-47 skins correct!',
            'en-NZ': 'Get all AK-47 skins correct!',
            'pt-PT': 'Acerta todas as skins de AK-47!',
            'es-MX': '¡Acierta todas las skins de AK-47!',
            'es-ES': '¡Acierta todas las skins de AK-47!',
            'es-AR': '¡Acierta todas las skins de AK-47!',
            'es-CO': '¡Acierta todas las skins de AK-47!',
            'de-DE': 'Errate alle AK-47 Skins!',
            'fr-FR': 'Trouvez toutes les skins AK-47!',
            'it-IT': 'Indovina tutte le skin AK-47!',
            'nl-NL': 'Raad alle AK-47 skins!',
            'sv-SE': 'Gissa alla AK-47 skins!',
            'no-NO': 'Gjett alle AK-47 skins!',
            'pl-PL': 'Zgadnij wszystkie skórki AK-47!',
            'id-ID': 'Tebak semua skin AK-47!',
            'ja-JP': 'すべてのAK-47スキンを当てよう！',
            'ko-KR': '모든 AK-47 스킨을 맞히세요!',
            'th-TH': 'ทายสกิน AK-47 ทั้งหมด!',
            'vi-VN': 'Đoán đúng tất cả skin AK-47!',
        },
        'silver': {
            'pt-BR': 'Acerte todas as skins em menos de 15 minutos!',
            'en-US': 'Get all skins correct in under 15 minutes!',
            'en-CA': 'Get all skins correct in under 15 minutes!',
            'en-GB': 'Get all skins correct in under 15 minutes!',
            'en-IN': 'Get all skins correct in under 15 minutes!',
            'en-PH': 'Get all skins correct in under 15 minutes!',
            'en-AU': 'Get all skins correct in under 15 minutes!',
            'en-NZ': 'Get all skins correct in under 15 minutes!',
            'pt-PT': 'Acerta todas as skins em menos de 15 minutos!',
            'es-MX': '¡Acierta todas las skins en menos de 15 minutos!',
            'es-ES': '¡Acierta todas las skins en menos de 15 minutos!',
            'es-AR': '¡Acierta todas las skins en menos de 15 minutos!',
            'es-CO': '¡Acierta todas las skins en menos de 15 minutos!',
            'de-DE': 'Errate alle Skins in unter 15 Minuten!',
            'fr-FR': 'Trouvez toutes les skins en moins de 15 minutes!',
            'it-IT': 'Indovina tutte le skin in meno di 15 minuti!',
            'nl-NL': 'Raad alle skins in minder dan 15 minuten!',
            'sv-SE': 'Gissa alla skins på under 15 minuter!',
            'no-NO': 'Gjett alle skins på under 15 minutter!',
            'pl-PL': 'Zgadnij wszystkie skórki w mniej niż 15 minut!',
            'id-ID': 'Tebak semua skin dalam waktu kurang dari 15 menit!',
            'ja-JP': '15分以内にすべてのスキンを当てよう！',
            'ko-KR': '15분 이내에 모든 스킨을 맞히세요!',
            'th-TH': 'ทายสกินทั้งหมดในเวลาไม่เกิน 15 นาที!',
            'vi-VN': 'Đoán đúng tất cả skin trong vòng 15 phút!',
        },
        'gold': {
            'pt-BR': 'Acerte todas as skins em menos de 8 minutos!',
            'en-US': 'Get all skins correct in under 8 minutes!',
            'en-CA': 'Get all skins correct in under 8 minutes!',
            'en-GB': 'Get all skins correct in under 8 minutes!',
            'en-IN': 'Get all skins correct in under 8 minutes!',
            'en-PH': 'Get all skins correct in under 8 minutes!',
            'en-AU': 'Get all skins correct in under 8 minutes!',
            'en-NZ': 'Get all skins correct in under 8 minutes!',
            'pt-PT': 'Acerta todas as skins em menos de 8 minutos!',
            'es-MX': '¡Acierta todas las skins en menos de 8 minutos!',
            'es-ES': '¡Acierta todas las skins en menos de 8 minutos!',
            'es-AR': '¡Acierta todas las skins en menos de 8 minutos!',
            'es-CO': '¡Acierta todas las skins en menos de 8 minutos!',
            'de-DE': 'Errate alle Skins in unter 8 Minuten!',
            'fr-FR': 'Trouvez toutes les skins en moins de 8 minutes!',
            'it-IT': 'Indovina tutte le skin in meno di 8 minuti!',
            'nl-NL': 'Raad alle skins in minder dan 8 minuten!',
            'sv-SE': 'Gissa alla skins på under 8 minuter!',
            'no-NO': 'Gjett alle skins på under 8 minutter!',
            'pl-PL': 'Zgadnij wszystkie skórki w mniej niż 8 minut!',
            'id-ID': 'Tebak semua skin dalam waktu kurang dari 8 menit!',
            'ja-JP': '8分以内にすべてのスキンを当てよう！',
            'ko-KR': '8분 이내에 모든 스킨을 맞히세요!',
            'th-TH': 'ทายสกินทั้งหมดในเวลาไม่เกิน 8 นาที!',
            'vi-VN': 'Đoán đúng tất cả skin trong vòng 8 phút!',
        },
    }

    badges_data = [
        {
            'title': '🥉 Bronze AK Master',
            'description': 'Acerte todas as skins de AK-47!',
            'description_translations': badge_descriptions['bronze'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760663642/ChatGPT_Image_Oct_16_2025_07_47_54_PM_n8e3ff.png',
            'rule_type': 'perfect_score',
            'min_percentage': 100.0,
            'max_time_seconds': None,
            'rarity': 'rare',
            'points': 100,
            'order': 1,
        },
        {
            'title': '🥈 Silver Elite AK',
            'description': 'Acerte todas as skins em menos de 15 minutos!',
            'description_translations': badge_descriptions['silver'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760663641/ChatGPT_Image_Oct_16_2025_06_21_46_PM_pzs3sz.png',
            'rule_type': 'percentage_time',
            'min_percentage': 100.0,
            'max_time_seconds': 900,  # 15 minutos
            'rarity': 'epic',
            'points': 200,
            'order': 2,
        },
        {
            'title': '🥇 Gold Nova AK',
            'description': 'Acerte todas as skins em menos de 8 minutos!',
            'description_translations': badge_descriptions['gold'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760663641/ChatGPT_Image_Oct_16_2025_06_21_49_PM_pdwnmr.png',
            'rule_type': 'percentage_time',
            'min_percentage': 100.0,
            'max_time_seconds': 480,  # 8 minutos
            'rarity': 'legendary',
            'points': 300,
            'order': 3,
        },
    ]

    created_count = 0
    updated_count = 0
    associated_count = 0

    for badge_data in badges_data:
        # Criar ou atualizar badge
        badge, created = Badge.objects.update_or_create(
            title=badge_data['title'],
            defaults={
                'description': badge_data['description'],
                'description_translations': badge_data['description_translations'],
                'image': badge_data['image'],
                'rule_type': badge_data['rule_type'],
                'min_percentage': badge_data['min_percentage'],
                'max_time_seconds': badge_data['max_time_seconds'],
                'rarity': badge_data['rarity'],
                'points': badge_data['points'],
                'order': badge_data['order'],
                'active': True,
            }
        )

        if created:
            created_count += 1
            status = "✅ CRIADO"
        else:
            updated_count += 1
            status = "🔄 ATUALIZADO"

        # Associar ao QuizGroup
        group_badge, group_created = QuizGroupBadge.objects.get_or_create(
            quiz_group=quiz_group,
            badge=badge,
            defaults={'active': True}
        )

        if group_created:
            associated_count += 1
            association_status = "🔗 Associado"
        else:
            association_status = "✓ Já associado"

        time_info = ""
        if badge_data['max_time_seconds']:
            minutes = badge_data['max_time_seconds'] // 60
            time_info = f" (< {minutes}min)"

        print(f"{status:15s} | {badge_data['title']:25s} | {badge_data['rarity']:10s} | {badge_data['points']:3d} pts{time_info:15s} | {association_status}")

    print()
    print(f"📊 Badges criadas: {created_count} | Atualizadas: {updated_count} | Associadas: {associated_count}")
    print()

    return created_count, updated_count


# ============================================================================
# MAIN
# ============================================================================

def main():
    print()
    print("=" * 80)
    print("🎮 SETUP COMPLETO: AK-47 SKINS - COUNTER-STRIKE 2")
    print("=" * 80)
    print()

    # Carregar dados
    print("📂 Carregando dados das skins AK-47...")
    all_skins = load_ak47_data()
    if not all_skins:
        return

    cloudinary_urls = load_cloudinary_urls()
    if cloudinary_urls:
        print(f"✅ {len(cloudinary_urls)} URLs do Cloudinary carregadas")
    else:
        print("⚠️  Usando URLs do JSON original")

    print(f"✅ {len(all_skins)} skins de AK-47 carregadas")
    print()

    # Etapa 0: Criar temas Counter-Strike (pai)
    cs_themes_count = create_counter_strike_themes()

    # Etapa 1: Criar temas AK-47
    themes_count = create_ak47_themes()

    # Etapa 2: Criar QuizGroup
    quiz_group = create_ak47_quizgroup()

    # Etapa 3: Criar Quizzes e Questões
    quizzes_created, quizzes_updated = create_ak47_quizzes(quiz_group, all_skins, cloudinary_urls)

    # Etapa 4: Criar Badges
    badges_created, badges_updated = create_ak47_badges(quiz_group)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Temas Counter-Strike (pai): {cs_themes_count}")
    print(f"✅ Temas AK-47: {themes_count}")
    print(f"✅ QuizGroup: 1")
    print(f"✅ Quizzes criados: {quizzes_created}")
    print(f"🔄 Quizzes atualizados: {quizzes_updated}")
    print(f"📝 Total de quizzes no grupo: {quiz_group.quizzes.count()}")
    print(f"🏆 Badges criadas: {badges_created}")
    print(f"🔄 Badges atualizadas: {badges_updated}")
    print()
    print("🎉 Setup completo de AK-47 Skins concluído com sucesso!")
    print()
    print("💡 Próximos passos:")
    print("   1. Verifique os temas em /admin/quizzes/theme/")
    print("   2. Verifique as badges em /admin/quizzes/badge/")
    print("   3. Acesse um quiz para testar: /quiz/adivinhe-skin-ak47/")
    print("   4. Complete um quiz para testar se as badges são concedidas automaticamente!")
    print()


if __name__ == '__main__':
    main()
