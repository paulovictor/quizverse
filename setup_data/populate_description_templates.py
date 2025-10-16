"""
Script para popular description_template nos quizzes existentes de Pokémon.
Esse script analisa as descriptions existentes e cria templates com placeholders.
"""

import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Quiz, QuizGroup


def get_pokemon_description_template(country_code):
    """Retorna o template de descrição para quizzes de Pokémon baseado no idioma"""

    # Mapear país para idioma
    lang_map = {
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

    lang_code = lang_map.get(country_code, 'en')

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


def populate_templates():
    """Popula description_template para todos os quizzes de Pokémon existentes"""

    print("=" * 80)
    print("🔄 POPULANDO DESCRIPTION TEMPLATES")
    print("=" * 80)
    print()

    # Buscar todos os quizzes de Pokémon (aqueles que têm "pokemon" no slug do tema)
    pokemon_quizzes = Quiz.objects.filter(
        theme__slug__icontains='pokemon',
        title__icontains='pokémon'
    )

    print(f"📊 Encontrados {pokemon_quizzes.count()} quizzes de Pokémon")
    print()

    updated_count = 0
    skipped_count = 0

    for quiz in pokemon_quizzes:
        # Se já tem template, pular
        if quiz.description_template:
            print(f"⏭️  PULADO | {quiz.slug} | Já tem template")
            skipped_count += 1
            continue

        # Obter template baseado no país
        template = get_pokemon_description_template(quiz.country)

        # Atualizar quiz
        quiz.description_template = template
        quiz.save()  # Vai renderizar automaticamente a description

        print(f"✅ ATUALIZADO | {quiz.slug} | {quiz.country}")
        updated_count += 1

    print()
    print("=" * 80)
    print("📊 RESUMO")
    print("=" * 80)
    print(f"✅ Quizzes atualizados: {updated_count}")
    print(f"⏭️  Quizzes pulados (já tinham template): {skipped_count}")
    print(f"📝 Total de quizzes: {pokemon_quizzes.count()}")
    print()
    print("🎉 Script concluído com sucesso!")
    print()


if __name__ == '__main__':
    populate_templates()
