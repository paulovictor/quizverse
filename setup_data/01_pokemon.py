#!/usr/bin/env python
"""
Script consolidado para setup completo de Pokémon Gen 1.
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

from quizzes.models import Theme, Quiz, QuizGroup, Question, Answer


# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def load_pokemon_data():
    """Carrega os dados dos Pokémon do arquivo JSON"""
    data_file = Path(project_root) / 'pokemon_gen1' / 'pokemon_data.json'

    if not data_file.exists():
        print(f"❌ Erro: Arquivo pokemon_data.json não encontrado em {data_file}")
        print("Execute primeiro: python download_gen1_pokemon.py")
        return None

    with open(data_file, 'r', encoding='utf-8') as f:
        return json.load(f)


def load_cloudinary_urls():
    """Carrega as URLs do Cloudinary"""
    cloudinary_file = Path(project_root) / 'cloudinary_pokemon_urls.json'

    if not cloudinary_file.exists():
        print("⚠️  Arquivo cloudinary_pokemon_urls.json não encontrado")
        print("Será usado o caminho local das imagens")
        return None

    with open(cloudinary_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return {int(k): v for k, v in data.items()}


def get_similar_pokemon(target_pokemon, all_pokemon, count=3):
    """
    Retorna Pokémon similares ao alvo para usar como alternativas incorretas.
    """
    similar = []
    target_types = set(target_pokemon['types'])

    # 1. Pokémon com tipos exatamente iguais
    exact_matches = [
        p for p in all_pokemon
        if p['id'] != target_pokemon['id']
        and set(p['types']) == target_types
    ]
    if exact_matches:
        similar.extend(exact_matches[:count])

    if len(similar) >= count:
        return similar[:count]

    # 2. Pokémon com pelo menos um tipo em comum
    partial_matches = [
        p for p in all_pokemon
        if p['id'] != target_pokemon['id']
        and p not in similar
        and len(set(p['types']) & target_types) > 0
    ]
    if partial_matches:
        remaining = count - len(similar)
        similar.extend(partial_matches[:remaining])

    if len(similar) >= count:
        return similar[:count]

    # 3. Pokémon próximos por ID
    remaining_pokemon = [
        p for p in all_pokemon
        if p['id'] != target_pokemon['id']
        and p not in similar
    ]
    if remaining_pokemon:
        remaining = count - len(similar)
        similar.extend(remaining_pokemon[:remaining])

    return similar[:count]


# ============================================================================
# ETAPA 1: CRIAR TEMAS POKÉMON
# ============================================================================

def create_pokemon_themes():
    """Cria o tema de Pokémon para todos os países"""

    print("=" * 80)
    print("ETAPA 1: CRIANDO TEMAS POKÉMON")
    print("=" * 80)
    print()

    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/w_300,h_300,c_thumb,f_auto/v1760501073/ChatGPT_Image_Oct_15_2025_12_57_23_AM_tvqerr.png'

    colors = {
        'primary_color': '#ffcb05',
        'secondary_color': '#3d7dca',
        'icon_bg_color_1': '#fff9e6',
        'icon_bg_color_2': '#ffe082',
    }

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

def create_pokemon_quizgroup():
    """Cria o QuizGroup para Pokémon Gen 1"""

    print("=" * 80)
    print("ETAPA 2: CRIANDO QUIZGROUP")
    print("=" * 80)
    print()

    quiz_group, created = QuizGroup.objects.update_or_create(
        slug='pokemon-gen1',
        defaults={
            'name': 'Pokémon Gen 1 - Guess the Pokémon',
            'description': 'Grupo de quizzes "Adivinhe o Pokémon" da Geração 1, disponível em múltiplos idiomas.',
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
        'en': 'Identify {sample_size} random Pokémon from the {total} original ones! Test your knowledge about the first generation.',
        'pt': 'Identifique {sample_size} Pokémon aleatórios dos {total} originais! Teste seu conhecimento sobre a primeira geração.',
        'es': '¡Identifica {sample_size} Pokémon aleatorios de los {total} originales! Pon a prueba tu conocimiento sobre la primera generación.',
        'de': 'Identifizieren Sie {sample_size} zufällige Pokémon aus den {total} Originalen! Testen Sie Ihr Wissen über die erste Generation.',
        'fr': 'Identifiez {sample_size} Pokémon aléatoires parmi les {total} originaux! Testez vos connaissances sur la première génération.',
        'it': 'Identifica {sample_size} Pokémon casuali tra i {total} originali! Metti alla prova la tua conoscenza sulla prima generazione.',
        'nl': 'Identificeer {sample_size} willekeurige Pokémon uit de {total} originelen! Test je kennis over de eerste generatie.',
        'sv': 'Identifiera {sample_size} slumpmässiga Pokémon från de {total} ursprungliga! Testa din kunskap om första generationen.',
        'no': 'Identifiser {sample_size} tilfeldige Pokémon fra de {total} originale! Test kunnskapen din om første generasjon.',
        'pl': 'Zidentyfikuj {sample_size} losowych Pokémonów spośród {total} oryginalnych! Przetestuj swoją wiedzę o pierwszej generacji.',
        'id': 'Identifikasi {sample_size} Pokémon acak dari {total} yang asli! Uji pengetahuan Anda tentang generasi pertama.',
        'ja': '{total}匹のオリジナルポケモンから{sample_size}匹をランダムに識別しよう！第1世代についての知識をテストしよう。',
        'ko': '{total}마리 오리지널 포켓몬 중 {sample_size}마리를 무작위로 식별하세요! 1세대에 대한 지식을 테스트하세요.',
        'th': 'ระบุโปเกมอน {sample_size} ตัวแบบสุ่มจากทั้งหมด {total} ตัว! ทดสอบความรู้ของคุณเกี่ยวกับรุ่นแรก',
        'vi': 'Nhận dạng {sample_size} Pokémon ngẫu nhiên từ {total} Pokémon gốc! Kiểm tra kiến thức của bạn về thế hệ đầu tiên.',
    }
    return templates.get(lang_code, templates['en'])


def create_pokemon_quizzes(quiz_group, all_pokemon, cloudinary_urls):
    """Cria os quizzes de Pokémon para todos os países"""

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
            'title': 'Guess the Pokémon - Gen 1',
            'question_text': 'Which Pokémon is this?',
            'explanation_template': 'This is {name}, a {types} type Pokémon.'
        },
        'pt': {
            'title': 'Adivinhe o Pokémon - Geração 1',
            'question_text': 'Qual é este Pokémon?',
            'explanation_template': 'Este é {name}, um Pokémon do tipo {types}.'
        },
        'es': {
            'title': 'Adivina el Pokémon - Gen 1',
            'question_text': '¿Cuál es este Pokémon?',
            'explanation_template': 'Este es {name}, un Pokémon de tipo {types}.'
        },
        'de': {
            'title': 'Errate das Pokémon - Gen 1',
            'question_text': 'Welches Pokémon ist das?',
            'explanation_template': 'Dies ist {name}, ein Pokémon vom Typ {types}.'
        },
        'fr': {
            'title': 'Devinez le Pokémon - Gén 1',
            'question_text': 'Quel est ce Pokémon?',
            'explanation_template': 'C\'est {name}, un Pokémon de type {types}.'
        },
        'it': {
            'title': 'Indovina il Pokémon - Gen 1',
            'question_text': 'Quale Pokémon è questo?',
            'explanation_template': 'Questo è {name}, un Pokémon di tipo {types}.'
        },
        'nl': {
            'title': 'Raad de Pokémon - Gen 1',
            'question_text': 'Welke Pokémon is dit?',
            'explanation_template': 'Dit is {name}, een Pokémon van type {types}.'
        },
        'sv': {
            'title': 'Gissa Pokémonen - Gen 1',
            'question_text': 'Vilken Pokémon är detta?',
            'explanation_template': 'Detta är {name}, en Pokémon av typ {types}.'
        },
        'no': {
            'title': 'Gjett Pokémonen - Gen 1',
            'question_text': 'Hvilken Pokémon er dette?',
            'explanation_template': 'Dette er {name}, en Pokémon av type {types}.'
        },
        'pl': {
            'title': 'Zgadnij Pokémona - Gen 1',
            'question_text': 'Który to Pokémon?',
            'explanation_template': 'To jest {name}, Pokémon typu {types}.'
        },
        'id': {
            'title': 'Tebak Pokémon - Gen 1',
            'question_text': 'Pokémon apa ini?',
            'explanation_template': 'Ini adalah {name}, Pokémon tipe {types}.'
        },
        'ja': {
            'title': 'ポケモンを当てよう - 第1世代',
            'question_text': 'このポケモンは何？',
            'explanation_template': 'これは{name}、{types}タイプのポケモンです。'
        },
        'ko': {
            'title': '포켓몬 맞히기 - 1세대',
            'question_text': '이 포켓몬은 무엇입니까?',
            'explanation_template': '이것은 {name}, {types} 타입 포켓몬입니다.'
        },
        'th': {
            'title': 'ทายโปเกมอน - Gen 1',
            'question_text': 'โปเกมอนตัวนี้คืออะไร?',
            'explanation_template': 'นี่คือ {name} โปเกมอนประเภท {types}'
        },
        'vi': {
            'title': 'Đoán Pokémon - Gen 1',
            'question_text': 'Đây là Pokémon nào?',
            'explanation_template': 'Đây là {name}, một Pokémon thuộc hệ {types}.'
        },
    }

    countries = list(country_to_lang.keys())
    num_questions = 151
    created_count = 0
    updated_count = 0
    total_questions_created = 0

    for country_code in countries:
        lang_code = country_to_lang[country_code]
        translation = quiz_translations.get(lang_code, quiz_translations['en'])

        # Determinar slug do tema
        if country_code == 'pt-BR':
            theme_slug = 'pokemon'
        else:
            country_suffix = country_code.split('-')[1].lower()
            theme_slug = f"pokemon-{country_suffix}"

        # Buscar tema
        try:
            theme = Theme.objects.get(slug=theme_slug)
        except Theme.DoesNotExist:
            print(f"⚠️  Tema não encontrado: {theme_slug}")
            continue

        # Determinar slug do quiz
        quiz_base_slug = 'adivinhe-o-pokemon-gen1' if lang_code == 'pt' else 'guess-the-pokemon-gen1'
        if country_code == 'pt-BR':
            quiz_slug = quiz_base_slug
        else:
            country_suffix = country_code.split('-')[1].lower()
            quiz_slug = f"{quiz_base_slug}-{country_suffix}"

        # Gerar template e description inicial
        quiz_sample_size = 0  # 0 = usar todas
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
        selected_pokemon = all_pokemon[:num_questions]
        question_count = 0

        for idx, pokemon in enumerate(selected_pokemon, 1):
            name = pokemon['name_pt']
            types_list = [t.capitalize() for t in pokemon['types']]

            if lang_code == 'pt':
                types_text = ' e '.join(types_list) if len(types_list) > 1 else types_list[0]
            else:
                types_text = ' and '.join(types_list) if len(types_list) > 1 else types_list[0]

            explanation = translation['explanation_template'].format(
                name=name,
                types=types_text
            )

            # Determinar imagem
            if cloudinary_urls and pokemon['id'] in cloudinary_urls:
                image_path = cloudinary_urls[pokemon['id']]['url']
            else:
                image_path = f"images/pokemon/{pokemon['id']:03d}_{pokemon['name'].lower()}.png"

            # Criar questão
            question = Question.objects.create(
                quiz=quiz,
                text=translation['question_text'],
                image=image_path,
                explanation=explanation,
                order=idx
            )

            # Gerar alternativas similares
            similar_pokemon = get_similar_pokemon(pokemon, all_pokemon, count=3)

            # Criar respostas
            answers_data = [{'text': name, 'is_correct': True}]
            for similar in similar_pokemon:
                answers_data.append({'text': similar['name_pt'], 'is_correct': False})

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
    print()

    return created_count, updated_count


# ============================================================================
# MAIN
# ============================================================================

def main():
    print()
    print("=" * 80)
    print("🎮 SETUP COMPLETO: POKÉMON GERAÇÃO 1")
    print("=" * 80)
    print()

    # Carregar dados
    print("📂 Carregando dados dos Pokémon...")
    all_pokemon = load_pokemon_data()
    if not all_pokemon:
        return

    cloudinary_urls = load_cloudinary_urls()
    if cloudinary_urls:
        print(f"✅ {len(cloudinary_urls)} URLs do Cloudinary carregadas")
    else:
        print("⚠️  Usando caminhos locais para imagens")

    print(f"✅ {len(all_pokemon)} Pokémon carregados")
    print()

    # Etapa 1: Criar temas
    themes_count = create_pokemon_themes()

    # Etapa 2: Criar QuizGroup
    quiz_group = create_pokemon_quizgroup()

    # Etapa 3: Criar Quizzes e Questões
    quizzes_created, quizzes_updated = create_pokemon_quizzes(quiz_group, all_pokemon, cloudinary_urls)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Temas: {themes_count}")
    print(f"✅ QuizGroup: 1")
    print(f"✅ Quizzes criados: {quizzes_created}")
    print(f"🔄 Quizzes atualizados: {quizzes_updated}")
    print(f"📝 Total de quizzes no grupo: {quiz_group.quizzes.count()}")
    print()
    print("🎉 Setup concluído com sucesso!")
    print()


if __name__ == '__main__':
    main()
