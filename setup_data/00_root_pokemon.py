"""
Script para criar quizzes de Pokémon Geração 1 em múltiplos países.
Cria quiz "Adivinhe o Pokémon" para todos os países suportados.
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

from quizzes.models import Theme, Quiz, Question, Answer


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
        # Converter chaves de string para int
        return {int(k): v for k, v in data.items()}


def get_similar_pokemon(target_pokemon, all_pokemon, count=3):
    """
    Retorna Pokémon similares ao alvo para usar como alternativas incorretas.
    
    Estratégia de similaridade:
    1. Pokémon com tipos exatamente iguais (mais difícil)
    2. Pokémon com pelo menos um tipo em comum
    3. Pokémon aleatórios se não houver similares suficientes
    """
    similar = []
    target_types = set(target_pokemon['types'])
    
    # 1. Pokémon com tipos exatamente iguais (mais difícil)
    exact_matches = [
        p for p in all_pokemon 
        if p['id'] != target_pokemon['id'] 
        and set(p['types']) == target_types
    ]
    if exact_matches:
        # Pegar os primeiros N similares (ordem consistente)
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
    
    # 3. Pokémon próximos por ID (última opção)
    remaining_pokemon = [
        p for p in all_pokemon 
        if p['id'] != target_pokemon['id']
        and p not in similar
    ]
    if remaining_pokemon:
        remaining = count - len(similar)
        # Pegar os primeiros N restantes
        similar.extend(remaining_pokemon[:remaining])
    
    return similar[:count]


def create_pokemon_quizzes():
    """Cria quizzes de Pokémon para todos os países"""
    
    # Carregar dados dos Pokémon
    all_pokemon = load_pokemon_data()
    if not all_pokemon:
        return 0, 0
    
    # Carregar URLs do Cloudinary
    cloudinary_urls = load_cloudinary_urls()
    if cloudinary_urls:
        print(f"✅ {len(cloudinary_urls)} URLs do Cloudinary carregadas")
    else:
        print("⚠️  Usando caminhos locais para as imagens")
    
    print(f"📊 {len(all_pokemon)} Pokémon carregados")
    print()
    
    # Mapeamento de países para idiomas
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
    
    # Traduções do quiz em múltiplos idiomas
    quiz_translations = {
        'en': {
            'title': 'Guess the Pokémon - Gen 1',
            'description': 'Identify the 151 original Pokémon by looking at their images! Test your knowledge about the first generation.',
            'question_text': 'Which Pokémon is this?',
            'explanation_template': 'This is {name}, a {types} type Pokémon.'
        },
        'pt': {
            'title': 'Adivinhe o Pokémon - Geração 1',
            'description': 'Identifique os 151 Pokémon originais olhando suas imagens! Teste seu conhecimento sobre a primeira geração.',
            'question_text': 'Qual é este Pokémon?',
            'explanation_template': 'Este é {name}, um Pokémon do tipo {types}.'
        },
        'es': {
            'title': 'Adivina el Pokémon - Gen 1',
            'description': '¡Identifica los 151 Pokémon originales mirando sus imágenes! Pon a prueba tu conocimiento sobre la primera generación.',
            'question_text': '¿Cuál es este Pokémon?',
            'explanation_template': 'Este es {name}, un Pokémon de tipo {types}.'
        },
        'de': {
            'title': 'Errate das Pokémon - Gen 1',
            'description': 'Identifizieren Sie die 151 Original-Pokémon anhand ihrer Bilder! Testen Sie Ihr Wissen über die erste Generation.',
            'question_text': 'Welches Pokémon ist das?',
            'explanation_template': 'Dies ist {name}, ein Pokémon vom Typ {types}.'
        },
        'fr': {
            'title': 'Devinez le Pokémon - Gén 1',
            'description': 'Identifiez les 151 Pokémon originaux en regardant leurs images! Testez vos connaissances sur la première génération.',
            'question_text': 'Quel est ce Pokémon?',
            'explanation_template': 'C\'est {name}, un Pokémon de type {types}.'
        },
        'it': {
            'title': 'Indovina il Pokémon - Gen 1',
            'description': 'Identifica i 151 Pokémon originali guardando le loro immagini! Metti alla prova la tua conoscenza sulla prima generazione.',
            'question_text': 'Quale Pokémon è questo?',
            'explanation_template': 'Questo è {name}, un Pokémon di tipo {types}.'
        },
        'nl': {
            'title': 'Raad de Pokémon - Gen 1',
            'description': 'Identificeer de 151 originele Pokémon door naar hun afbeeldingen te kijken! Test je kennis over de eerste generatie.',
            'question_text': 'Welke Pokémon is dit?',
            'explanation_template': 'Dit is {name}, een Pokémon van type {types}.'
        },
        'sv': {
            'title': 'Gissa Pokémonen - Gen 1',
            'description': 'Identifiera de 151 ursprungliga Pokémon genom att titta på deras bilder! Testa din kunskap om första generationen.',
            'question_text': 'Vilken Pokémon är detta?',
            'explanation_template': 'Detta är {name}, en Pokémon av typ {types}.'
        },
        'no': {
            'title': 'Gjett Pokémonen - Gen 1',
            'description': 'Identifiser de 151 originale Pokémon ved å se på bildene deres! Test kunnskapen din om første generasjon.',
            'question_text': 'Hvilken Pokémon er dette?',
            'explanation_template': 'Dette er {name}, en Pokémon av type {types}.'
        },
        'pl': {
            'title': 'Zgadnij Pokémona - Gen 1',
            'description': 'Zidentyfikuj 151 oryginalnych Pokémonów patrząc na ich obrazy! Przetestuj swoją wiedzę o pierwszej generacji.',
            'question_text': 'Który to Pokémon?',
            'explanation_template': 'To jest {name}, Pokémon typu {types}.'
        },
        'id': {
            'title': 'Tebak Pokémon - Gen 1',
            'description': 'Identifikasi 151 Pokémon asli dengan melihat gambar mereka! Uji pengetahuan Anda tentang generasi pertama.',
            'question_text': 'Pokémon apa ini?',
            'explanation_template': 'Ini adalah {name}, Pokémon tipe {types}.'
        },
        'ja': {
            'title': 'ポケモンを当てよう - 第1世代',
            'description': '画像を見て151匹のオリジナルポケモンを識別しよう！第1世代についての知識をテストしよう。',
            'question_text': 'このポケモンは何？',
            'explanation_template': 'これは{name}、{types}タイプのポケモンです。'
        },
        'ko': {
            'title': '포켓몬 맞히기 - 1세대',
            'description': '이미지를 보고 151마리의 오리지널 포켓몬을 식별하세요! 1세대에 대한 지식을 테스트하세요.',
            'question_text': '이 포켓몬은 무엇입니까?',
            'explanation_template': '이것은 {name}, {types} 타입 포켓몬입니다.'
        },
        'th': {
            'title': 'ทายโปเกมอน - Gen 1',
            'description': 'ระบุโปเกมอนดั้งเดิม 151 ตัวโดยดูจากภาพ! ทดสอบความรู้ของคุณเกี่ยวกับรุ่นแรก',
            'question_text': 'โปเกมอนตัวนี้คืออะไร?',
            'explanation_template': 'นี่คือ {name} โปเกมอนประเภท {types}'
        },
        'vi': {
            'title': 'Đoán Pokémon - Gen 1',
            'description': 'Nhận dạng 151 Pokémon gốc bằng cách xem hình ảnh! Kiểm tra kiến thức của bạn về thế hệ đầu tiên.',
            'question_text': 'Đây là Pokémon nào?',
            'explanation_template': 'Đây là {name}, một Pokémon thuộc hệ {types}.'
        },
    }
    
    countries = list(country_to_lang.keys())
    num_questions = 151  # Usar TODOS os 151 Pokémon da Geração 1
    
    print("🚀 Criando quizzes de Pokémon em múltiplos países...")
    print(f"🌍 Países: {len(countries)}")
    print(f"❓ Perguntas por quiz: {num_questions} (TODOS os Pokémon da Gen 1)")
    print(f"📊 Total de quizzes: {len(countries)}")
    print("-" * 80)
    print()
    
    created_count = 0
    updated_count = 0
    total_questions = 0
    
    for country_code in countries:
        lang_code = country_to_lang[country_code]
        translation = quiz_translations.get(lang_code, quiz_translations['en'])
        
        # Determinar o slug do tema Pokémon
        if country_code == 'pt-BR':
            theme_slug = 'pokemon'
        else:
            country_suffix = country_code.split('-')[1].lower()
            theme_slug = f"pokemon-{country_suffix}"
        
        # Buscar o tema Pokémon (deve ter sido criado pelo 00_root_pokemon_theme.py)
        try:
            theme = Theme.objects.get(slug=theme_slug)
        except Theme.DoesNotExist:
            print(f"⚠️  Tema não encontrado: {theme_slug} para {country_code}")
            print(f"   Execute primeiro: python setup_data/00_root_pokemon_theme.py")
            continue
        
        # Determinar o slug do quiz
        quiz_base_slug = 'adivinhe-o-pokemon-gen1' if lang_code == 'pt' else 'guess-the-pokemon-gen1'
        if country_code == 'pt-BR':
            quiz_slug = quiz_base_slug
        else:
            country_suffix = country_code.split('-')[1].lower()
            quiz_slug = f"{quiz_base_slug}-{country_suffix}"
        
        # Criar ou atualizar o quiz
        quiz, quiz_created = Quiz.objects.update_or_create(
            slug=quiz_slug,
            defaults={
                'theme': theme,
                'title': translation['title'],
                'description': translation['description'],
                'difficulty': 'medium',
                'active': True,
                'order': 1,
                'country': country_code,
            }
        )
        
        if quiz_created:
            created_count += 1
            status = "✅ CRIADO"
        else:
            updated_count += 1
            status = "🔄 ATUALIZADO"
            # Limpar perguntas antigas
            quiz.questions.all().delete()
        
        print(f"{status} | {country_code} | {quiz_slug}")
        print(f"         Tema: {theme_slug} | Quiz: {translation['title']}")
        
        # Usar todos os 151 Pokémon em ordem
        selected_pokemon = all_pokemon[:num_questions]
        
        # Criar perguntas e respostas
        question_count = 0
        for idx, pokemon in enumerate(selected_pokemon, 1):
            name = pokemon['name_pt']
            types_list = [t.capitalize() for t in pokemon['types']]
            
            # Formatar tipos para a explicação
            if lang_code == 'pt':
                types_text = ' e '.join(types_list) if len(types_list) > 1 else types_list[0]
            else:
                types_text = ' and '.join(types_list) if len(types_list) > 1 else types_list[0]
            
            # Criar explicação
            explanation = translation['explanation_template'].format(
                name=name,
                types=types_text
            )
            
            # Determinar caminho/URL da imagem
            if cloudinary_urls and pokemon['id'] in cloudinary_urls:
                # Usar URL do Cloudinary
                image_path = cloudinary_urls[pokemon['id']]['url']
            else:
                # Usar caminho local
                image_path = f"images/pokemon/{pokemon['id']:03d}_{pokemon['name'].lower()}.png"
            
            # Criar a pergunta
            question = Question.objects.create(
                quiz=quiz,
                text=translation['question_text'],
                image=image_path,
                explanation=explanation,
                order=idx
            )
            
            # Gerar alternativas similares
            similar_pokemon = get_similar_pokemon(pokemon, all_pokemon, count=3)
            
            # Criar respostas (correta + 3 incorretas)
            answers_data = [
                {'text': name, 'is_correct': True}
            ]
            
            for similar in similar_pokemon:
                answers_data.append({
                    'text': similar['name_pt'],
                    'is_correct': False
                })
            
            # Embaralhar as respostas
            random.shuffle(answers_data)
            
            # Criar as respostas no banco
            for answer_data in answers_data:
                Answer.objects.create(
                    question=question,
                    text=answer_data['text'],
                    is_correct=answer_data['is_correct']
                )
            
            question_count += 1
        
        total_questions += question_count
        print(f"         ❓ {question_count} perguntas criadas")
        print()
    
    return created_count, updated_count, total_questions


def main():
    print("=" * 80)
    print("🎮 SETUP DE QUIZZES DE POKÉMON - GERAÇÃO 1")
    print("=" * 80)
    print()
    
    created, updated, total_questions = create_pokemon_quizzes()
    
    print()
    print("=" * 80)
    print("📊 RESUMO")
    print("=" * 80)
    print(f"✅ Quizzes criados: {created}")
    print(f"🔄 Quizzes atualizados: {updated}")
    print(f"❓ Total de perguntas: {total_questions}")
    print(f"📝 Total de quizzes: {created + updated}")
    print()
    print("🎉 Setup concluído com sucesso!")
    print()
    print("⚠️  IMPORTANTE: Certifique-se de que as imagens estão em:")
    print("   quizzes/static/images/pokemon/")
    print()
    print("Para copiar as imagens:")
    print("   mkdir -p quizzes/static/images/pokemon")
    print("   cp pokemon_gen1/images/*.png quizzes/static/images/pokemon/")
    print("   python manage.py collectstatic --noinput")
    print()


if __name__ == '__main__':
    main()

