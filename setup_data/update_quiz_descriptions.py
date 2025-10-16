"""
Script para atualizar as descrições dos quizzes baseado no question_sample_size.
Atualiza a mensagem para refletir o número correto de questões.
"""

import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Quiz


def get_description_template(lang_code, total_questions, sample_size):
    """Retorna a descrição do quiz baseado no idioma e configuração"""

    # Determinar se usa todas as questões ou uma amostra
    if sample_size == 0 or sample_size >= total_questions:
        # Usar TODAS as questões
        templates = {
            'en': f'Identify all {total_questions} original Pokémon by looking at their images! Test your knowledge about the first generation.',
            'pt': f'Identifique todos os {total_questions} Pokémon originais olhando suas imagens! Teste seu conhecimento sobre a primeira geração.',
            'es': f'¡Identifica los {total_questions} Pokémon originales mirando sus imágenes! Pon a prueba tu conocimiento sobre la primera generación.',
            'de': f'Identifizieren Sie alle {total_questions} Original-Pokémon anhand ihrer Bilder! Testen Sie Ihr Wissen über die erste Generation.',
            'fr': f'Identifiez les {total_questions} Pokémon originaux en regardant leurs images! Testez vos connaissances sur la première génération.',
            'it': f'Identifica tutti i {total_questions} Pokémon originali guardando le loro immagini! Metti alla prova la tua conoscenza sulla prima generazione.',
            'nl': f'Identificeer alle {total_questions} originele Pokémon door naar hun afbeeldingen te kijken! Test je kennis over de eerste generatie.',
            'sv': f'Identifiera alla {total_questions} ursprungliga Pokémon genom att titta på deras bilder! Testa din kunskap om första generationen.',
            'no': f'Identifiser alle {total_questions} originale Pokémon ved å se på bildene deres! Test kunnskapen din om første generasjon.',
            'pl': f'Zidentyfikuj wszystkich {total_questions} oryginalnych Pokémonów patrząc na ich obrazy! Przetestuj swoją wiedzę o pierwszej generacji.',
            'id': f'Identifikasi semua {total_questions} Pokémon asli dengan melihat gambar mereka! Uji pengetahuan Anda tentang generasi pertama.',
            'ja': f'{total_questions}匹すべてのオリジナルポケモンを画像を見て識別しよう！第1世代についての知識をテストしよう。',
            'ko': f'{total_questions}마리 모든 오리지널 포켓몬을 이미지를 보고 식별하세요! 1세대에 대한 지식을 테스트하세요.',
            'th': f'ระบุโปเกมอนดั้งเดิมทั้งหมด {total_questions} ตัวโดยดูจากภาพ! ทดสอบความรู้ของคุณเกี่ยวกับรุ่นแรก',
            'vi': f'Nhận dạng tất cả {total_questions} Pokémon gốc bằng cách xem hình ảnh! Kiểm tra kiến thức của bạn về thế hệ đầu tiên.',
        }
    else:
        # Usar AMOSTRA de questões
        templates = {
            'en': f'Identify {sample_size} random Pokémon from the {total_questions} original ones! Test your knowledge about the first generation.',
            'pt': f'Identifique {sample_size} Pokémon aleatórios dos {total_questions} originais! Teste seu conhecimento sobre a primeira geração.',
            'es': f'¡Identifica {sample_size} Pokémon aleatorios de los {total_questions} originales! Pon a prueba tu conocimiento sobre la primera generación.',
            'de': f'Identifizieren Sie {sample_size} zufällige Pokémon aus den {total_questions} Originalen! Testen Sie Ihr Wissen über die erste Generation.',
            'fr': f'Identifiez {sample_size} Pokémon aléatoires parmi les {total_questions} originaux! Testez vos connaissances sur la première génération.',
            'it': f'Identifica {sample_size} Pokémon casuali tra i {total_questions} originali! Metti alla prova la tua conoscenza sulla prima generazione.',
            'nl': f'Identificeer {sample_size} willekeurige Pokémon uit de {total_questions} originelen! Test je kennis over de eerste generatie.',
            'sv': f'Identifiera {sample_size} slumpmässiga Pokémon från de {total_questions} ursprungliga! Testa din kunskap om första generationen.',
            'no': f'Identifiser {sample_size} tilfeldige Pokémon fra de {total_questions} originale! Test kunnskapen din om første generasjon.',
            'pl': f'Zidentyfikuj {sample_size} losowych Pokémonów spośród {total_questions} oryginalnych! Przetestuj swoją wiedzę o pierwszej generacji.',
            'id': f'Identifikasi {sample_size} Pokémon acak dari {total_questions} yang asli! Uji pengetahuan Anda tentang generasi pertama.',
            'ja': f'{total_questions}匹のオリジナルポケモンから{sample_size}匹をランダムに識別しよう！第1世代についての知識をテストしよう。',
            'ko': f'{total_questions}마리 오리지널 포켓몬 중 {sample_size}마리를 무작위로 식별하세요! 1세대에 대한 지식을 테스트하세요.',
            'th': f'ระบุโปเกมอน {sample_size} ตัวแบบสุ่มจากทั้งหมด {total_questions} ตัว! ทดสอบความรู้ของคุณเกี่ยวกับรุ่นแรก',
            'vi': f'Nhận dạng {sample_size} Pokémon ngẫu nhiên từ {total_questions} Pokémon gốc! Kiểm tra kiến thức của bạn về thế hệ đầu tiên.',
        }

    return templates.get(lang_code, templates['en'])


def country_to_language(country_code):
    """Converte código de país para código de idioma"""
    country_to_lang_map = {
        'pt-BR': 'pt',
        'pt-PT': 'pt',
        'en-US': 'en',
        'en-CA': 'en',
        'en-GB': 'en',
        'en-IN': 'en',
        'en-PH': 'en',
        'en-AU': 'en',
        'en-NZ': 'en',
        'es-MX': 'es',
        'es-ES': 'es',
        'es-AR': 'es',
        'es-CO': 'es',
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
    return country_to_lang_map.get(country_code, 'en')


def update_pokemon_quiz_descriptions():
    """Atualiza as descrições de todos os quizzes de Pokémon"""

    print("=" * 80)
    print("🔄 ATUALIZANDO DESCRIÇÕES DOS QUIZZES DE POKÉMON")
    print("=" * 80)
    print()

    # Buscar todos os quizzes que contêm "Pokémon" no título
    pokemon_quizzes = Quiz.objects.filter(title__icontains='Pokémon')

    if not pokemon_quizzes.exists():
        print("⚠️  Nenhum quiz de Pokémon encontrado.")
        return

    print(f"📊 {pokemon_quizzes.count()} quizzes de Pokémon encontrados")
    print()

    updated_count = 0

    for quiz in pokemon_quizzes:
        # Pegar total de questões cadastradas
        total_questions = quiz.get_total_questions()

        if total_questions == 0:
            print(f"⏭️  Pulando {quiz.slug} - sem questões cadastradas")
            continue

        # Pegar o sample size
        sample_size = quiz.question_sample_size

        # Determinar idioma do quiz
        lang_code = country_to_language(quiz.country)

        # Gerar nova descrição
        new_description = get_description_template(lang_code, total_questions, sample_size)

        # Atualizar apenas se a descrição for diferente
        if quiz.description != new_description:
            old_description = quiz.description[:60] + "..." if len(quiz.description) > 60 else quiz.description
            quiz.description = new_description
            quiz.save()

            print(f"✅ Atualizado: {quiz.slug}")
            print(f"   País: {quiz.country} | Total: {total_questions} | Sample: {sample_size}")
            print(f"   Antiga: {old_description}")
            print(f"   Nova: {new_description}")
            print()

            updated_count += 1
        else:
            print(f"⏭️  Sem mudanças: {quiz.slug}")

    print()
    print("=" * 80)
    print("📊 RESUMO")
    print("=" * 80)
    print(f"✅ Quizzes atualizados: {updated_count}")
    print(f"📝 Total de quizzes processados: {pokemon_quizzes.count()}")
    print()
    print("🎉 Atualização concluída!")
    print()


def main():
    update_pokemon_quiz_descriptions()


if __name__ == '__main__':
    main()
