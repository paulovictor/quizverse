#!/usr/bin/env python
"""
Script consolidado para setup completo de AK-47 Skins do Counter-Strike.
Cria temas AK-47, quizgroup, quizzes e questões em uma única execução.

Pré-requisitos:
- 00_root_themes.py deve ter sido executado
- 02_counter_strike_theme.py deve ter sido executado
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
# ETAPA 1: CRIAR TEMAS AK-47
# ============================================================================

def create_ak47_themes():
    """Cria o tema de AK-47 para todos os países (filho do tema Counter-Strike)"""

    print("=" * 80)
    print("ETAPA 1: CRIANDO TEMAS AK-47")
    print("=" * 80)
    print()

    theme_image = 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760663546/best-ak-buyers-guide-ak47-feature-hd-768x496_ixmyvw.jpg'

    colors = {
        'primary_color': '#ff6347',  # Vermelho CS:GO
        'secondary_color': '#1e90ff',  # Azul CS:GO
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
        },
        'pt': {
            'title': 'Adivinhe a Skin da AK-47 - CS2',
            'question_text': 'Qual é esta skin de AK-47?',
        },
        'es': {
            'title': 'Adivina la Skin de AK-47 - CS2',
            'question_text': '¿Cuál es esta skin de AK-47?',
        },
        'de': {
            'title': 'Errate die AK-47 Skin - CS2',
            'question_text': 'Welche AK-47 Skin ist das?',
        },
        'fr': {
            'title': 'Devinez la Skin AK-47 - CS2',
            'question_text': 'Quelle est cette skin AK-47?',
        },
        'it': {
            'title': 'Indovina la Skin AK-47 - CS2',
            'question_text': 'Quale skin AK-47 è questa?',
        },
        'nl': {
            'title': 'Raad de AK-47 Skin - CS2',
            'question_text': 'Welke AK-47 skin is dit?',
        },
        'sv': {
            'title': 'Gissa AK-47 Skinnet - CS2',
            'question_text': 'Vilket AK-47 skin är detta?',
        },
        'no': {
            'title': 'Gjett AK-47 Skinnet - CS2',
            'question_text': 'Hvilket AK-47 skin er dette?',
        },
        'pl': {
            'title': 'Zgadnij Skórkę AK-47 - CS2',
            'question_text': 'Która to skórka AK-47?',
        },
        'id': {
            'title': 'Tebak Skin AK-47 - CS2',
            'question_text': 'Skin AK-47 apa ini?',
        },
        'ja': {
            'title': 'AK-47スキンを当てよう - CS2',
            'question_text': 'このAK-47スキンは何？',
        },
        'ko': {
            'title': 'AK-47 스킨 맞히기 - CS2',
            'question_text': '이 AK-47 스킨은 무엇입니까?',
        },
        'th': {
            'title': 'ทายสกิน AK-47 - CS2',
            'question_text': 'สกิน AK-47 นี้คืออะไร?',
        },
        'vi': {
            'title': 'Đoán Skin AK-47 - CS2',
            'question_text': 'Đây là skin AK-47 nào?',
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


            # Determinar imagem
            image_path = get_skin_url(name, cloudinary_urls, skin['foto'])

            # Criar questão
            question = Question.objects.create(
                quiz=quiz,
                text=translation['question_text'],
                image=image_path,
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

    # Etapa 1: Criar temas AK-47
    themes_count = create_ak47_themes()

    # Etapa 2: Criar QuizGroup
    quiz_group = create_ak47_quizgroup()

    # Etapa 3: Criar Quizzes e Questões
    quizzes_created, quizzes_updated = create_ak47_quizzes(quiz_group, all_skins, cloudinary_urls)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Temas AK-47: {themes_count}")
    print(f"✅ QuizGroup: 1")
    print(f"✅ Quizzes criados: {quizzes_created}")
    print(f"🔄 Quizzes atualizados: {quizzes_updated}")
    print(f"📝 Total de quizzes no grupo: {quiz_group.quizzes.count()}")
    print()
    print("🎉 Setup completo de AK-47 Skins concluído com sucesso!")
    print()
    print("💡 Próximos passos:")
    print("   1. Verifique os temas em /admin/quizzes/theme/")
    print("   2. Acesse um quiz para testar: /quiz/adivinhe-skin-ak47/")
    print()
    print("📝 Nota: Execute primeiro 02_counter_strike_theme.py para criar os temas pai!")
    print()


if __name__ == '__main__':
    main()
