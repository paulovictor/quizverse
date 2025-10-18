#!/usr/bin/env python
"""
Script para criar questões para quizzes em todos os países.

Este script:
1. Pergunta o slug do quiz em português
2. Pergunta o nome do arquivo JSON com as URLs do Cloudinary
3. Pergunta informações sobre as questões a serem criadas
4. Cria as questões em todos os países

Uso:
    python setup/create_questions.py
"""

import os
import sys
import json
import random
import django
from pathlib import Path
from django.core.management import call_command

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Quiz, QuizGroup, Question, Answer


# ============================================================================
# CONFIGURAÇÃO DE PAÍSES E IDIOMAS
# ============================================================================

COUNTRY_TO_LANG = {
    'en-US': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-IN': 'en',
    'en-PH': 'en', 'en-AU': 'en', 'en-NZ': 'en',
    'pt-BR': 'pt', 'pt-PT': 'pt',
    'es-MX': 'es', 'es-ES': 'es', 'es-AR': 'es', 'es-CO': 'es',
}

# ============================================================================
# FUNÇÕES AUXILIARES
# ============================================================================

def find_quiz_by_slug(quiz_slug_pt):
    """
    Encontra o quiz em todos os países baseado no slug PT-BR
    """
    quizzes = {}
    
    # Para pt-BR, usar o slug direto
    try:
        quiz_pt = Quiz.objects.get(slug=quiz_slug_pt, country='pt-BR')
        quizzes['pt-BR'] = quiz_pt
        print(f"✅ Quiz encontrado para pt-BR: {quiz_pt.slug} - {quiz_pt.title}")
    except Quiz.DoesNotExist:
        print(f"❌ Erro: Quiz '{quiz_slug_pt}' não encontrado para pt-BR")
        return None

    # Para outros países, buscar variações do slug
    for country_code in COUNTRY_TO_LANG.keys():
        if country_code == 'pt-BR':
            continue

        country_suffix = country_code.split('-')[1].lower()
        expected_slug = f"{quiz_slug_pt}-{country_suffix}"

        try:
            quiz = Quiz.objects.get(slug=expected_slug, country=country_code)
            quizzes[country_code] = quiz
            print(f"✅ Quiz encontrado para {country_code}: {quiz.slug} - {quiz.title}")
        except Quiz.DoesNotExist:
            print(f"⚠️  Quiz não encontrado para {country_code}: {expected_slug}")
            quizzes[country_code] = None

    return quizzes


def list_available_json_files():
    """Lista todos os arquivos JSON disponíveis na pasta cloudinary_urls"""
    cloudinary_dir = Path(project_root) / 'setup' / 'cloudinary_urls'
    
    if not cloudinary_dir.exists():
        print(f"❌ Erro: Pasta {cloudinary_dir} não encontrada!")
        return []
    
    json_files = list(cloudinary_dir.glob("*.json"))
    return sorted(json_files)


def load_cloudinary_urls(filename):
    """Carrega as URLs do Cloudinary do arquivo JSON"""
    cloudinary_file = Path(project_root) / 'setup' / 'cloudinary_urls' / f"{filename}.json"

    if not cloudinary_file.exists():
        print(f"❌ Erro: Arquivo {filename}.json não encontrado em {cloudinary_file}")
        return None

    with open(cloudinary_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        return data


def get_similar_items(target_item, all_items, count=3, name_field='display_name'):
    """
    Retorna itens similares ao alvo para usar como alternativas incorretas.
    """
    similar = []
    target_name = target_item.get(name_field, '').lower()

    # 1. Itens com nomes similares (contém parte do nome)
    partial_matches = [
        item for item in all_items
        if item != target_item
        and item.get(name_field, '').lower() != target_name
        and any(word in item.get(name_field, '').lower() for word in target_name.split() if len(word) > 2)
    ]
    if partial_matches:
        similar.extend(partial_matches[:count])

    if len(similar) >= count:
        return similar[:count]

    # 2. Itens aleatórios
    remaining_items = [
        item for item in all_items
        if item != target_item
        and item not in similar
    ]
    if remaining_items:
        remaining = count - len(similar)
        similar.extend(random.sample(remaining_items, min(remaining, len(remaining_items))))

    return similar[:count]


def get_user_input():
    """
    Solicita informações do usuário sobre as questões a serem criadas
    """
    print("=" * 80)
    print("❓ CRIAR QUESTÕES PARA QUIZ")
    print("=" * 80)
    print()

    # Slug do quiz
    print("1️⃣ Digite o slug do quiz em português (ex: adivinhe-o-pokemon-gen1)")
    while True:
        quiz_slug_pt = input("   Slug do quiz: ").strip()
        if quiz_slug_pt:
            break
        print("❌ Slug do quiz não pode ser vazio! Tente novamente.")

    print()

    # Listar arquivos JSON disponíveis
    print("2️⃣ Escolha o arquivo JSON disponível em setup/cloudinary_urls/")
    print()
    
    json_files = list_available_json_files()
    
    if not json_files:
        print("❌ Erro: Nenhum arquivo JSON encontrado na pasta setup/cloudinary_urls/")
        sys.exit(1)
    
    print("📋 Arquivos JSON disponíveis:")
    print()
    
    for i, json_file in enumerate(json_files, 1):
        filename = json_file.stem  # Nome sem extensão
        print(f"   {i:2d}. {filename}")
    
    print()
    print("💡 Dica: Escolha o número do arquivo")
    print()
    
    # Escolher arquivo por número
    while True:
        try:
            choice = input(f"   Número do arquivo (1-{len(json_files)}): ").strip()
            
            if not choice:
                print("❌ Número não pode ser vazio!")
                continue

            choice_num = int(choice)
            
            if choice_num < 1 or choice_num > len(json_files):
                print(f"❌ Número deve estar entre 1 e {len(json_files)}!")
                print()
                continue

            # Número válido, obter o arquivo
            selected_file = json_files[choice_num - 1]
            json_filename = selected_file.stem
            print(f"✅ Arquivo selecionado: {json_filename}")
            break

        except ValueError:
            print("❌ Digite um número válido!")
            print()
            continue

    print()

    # Campo de nome fixo
    name_field = "display_name"

    # Texto da pergunta
    print("4️⃣ Texto da pergunta (será traduzido automaticamente)")
    while True:
        question_text_pt = input("   Texto da pergunta (pt): ").strip()
        if question_text_pt:
            break
        print("❌ Texto da pergunta não pode ser vazio! Tente novamente.")

    print()

    # Traduções do texto da pergunta
    print("5️⃣ Traduções do texto da pergunta")
    print()

    translations = {}

    # Definir quais idiomas pedir tradução
    main_languages = ['pt', 'en', 'es']

    for lang_code in main_languages:
        lang_names = {
            'pt': 'Português',
            'en': 'Inglês',
            'es': 'Espanhol',
        }

        print(f"   📝 {lang_names[lang_code]} ({lang_code})")
        
        if lang_code == 'pt':
            # Para português, usar o valor já informado
            question_text = question_text_pt
            print(f"      Texto: {question_text}")
        else:
            # Para outros idiomas, perguntar
            while True:
                question_text = input(f"      Texto: ").strip()
                if question_text:
                    break
                print(f"      ❌ Texto não pode ser vazio! Tente novamente.")

        translations[lang_code] = question_text
        print()

    return {
        'quiz_slug_pt': quiz_slug_pt,
        'json_filename': json_filename,
        'name_field': name_field,
        'question_text_pt': question_text_pt,
        'translations': translations,
    }


def create_questions(config, quizzes, cloudinary_data):
    """
    Cria as questões em todos os países
    """
    print("=" * 80)
    print("🚀 CRIANDO QUESTÕES")
    print("=" * 80)
    print()

    # Converter dados para lista se necessário
    if isinstance(cloudinary_data, dict):
        items_list = list(cloudinary_data.values())
    else:
        items_list = cloudinary_data

    if not items_list:
        print("❌ Erro: Nenhum item encontrado nos dados!")
        return 0

    # Usar todos os itens (uma questão para cada item)
    selected_items = items_list
    num_questions = len(selected_items)
    
    print(f"📝 Total de questões a criar: {num_questions} (uma para cada item)")
    print()
    
    created_count = 0
    updated_count = 0
    errors = []

    for country_code, lang_code in COUNTRY_TO_LANG.items():
        # Buscar quiz
        quiz = quizzes.get(country_code)
        if not quiz:
            errors.append(f"⚠️  Quiz não encontrado para {country_code}")
            continue

        # Usar tradução do idioma ou fallback para inglês
        question_text = config['translations'].get(lang_code, config['translations'].get('en'))

        if not question_text:
            errors.append(f"⚠️  Tradução não encontrada para {country_code} ({lang_code})")
            continue

        # Limpar questões antigas
        quiz.questions.all().delete()

        # Criar questões
        question_count = 0

        for idx, item in enumerate(selected_items, 1):
            # Obter nome do item
            item_name = item.get(config['name_field'], f"Item {idx}")

            # Determinar imagem
            image_path = item.get('secure_url', '')

            # Criar questão
            question = Question.objects.create(
                quiz=quiz,
                text=question_text,
                image=image_path,
                order=idx
            )

            # Gerar alternativas similares
            similar_items = get_similar_items(item, items_list, count=3, name_field=config['name_field'])

            # Criar respostas
            answers_data = [{'text': item_name, 'is_correct': True}]
            for similar in similar_items:
                similar_name = similar.get(config['name_field'], f"Item {idx}")
                answers_data.append({'text': similar_name, 'is_correct': False})

            random.shuffle(answers_data)

            for answer_data in answers_data:
                Answer.objects.create(
                    question=question,
                    text=answer_data['text'],
                    is_correct=answer_data['is_correct']
                )

            question_count += 1

        if question_count > 0:
            created_count += 1
            status = "✅"
        else:
            updated_count += 1
            status = "🔄"

        print(f"{status} {country_code:7s} | {quiz.slug:30s} | {question_count} questões")

    print()
    print(f"📊 Quizzes processados: {created_count} | Atualizados: {updated_count}")

    if errors:
        print()
        print("⚠️  AVISOS:")
        for error in errors:
            print(f"   {error}")

    print()
    return created_count + updated_count


def export_question_fixtures(config, quizzes):
    """
    Exporta as questões criadas como fixtures JSON
    """
    print("=" * 80)
    print("📦 EXPORTANDO FIXTURES")
    print("=" * 80)
    print()
    
    # Criar pasta fixtures se não existir
    fixtures_dir = Path(project_root) / 'fixtures' / 'questions'
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    
    # Nome do arquivo baseado no slug do quiz
    fixture_filename = f"{config['quiz_slug_pt']}_questions.json"
    fixture_path = fixtures_dir / fixture_filename
    
    try:
        # Buscar todas as questões criadas para este quiz
        questions_to_export = []
        answers_to_export = []
        
        for country_code, quiz in quizzes.items():
            if not quiz:
                continue
            
            # Buscar questões do quiz
            questions = Question.objects.filter(quiz=quiz)
            for question in questions:
                questions_to_export.append(question)
                # Buscar respostas da questão
                answers = Answer.objects.filter(question=question)
                answers_to_export.extend(answers)
        
        if not questions_to_export:
            print("⚠️  Nenhuma questão encontrada para exportar")
            return
        
        # Exportar questões e respostas separadamente
        question_pks = [str(q.pk) for q in questions_to_export]
        answer_pks = [str(a.pk) for a in answers_to_export]
        
        with open(fixture_path, 'w', encoding='utf-8') as f:
            # Exportar questões primeiro
            if question_pks:
                call_command('dumpdata', 'quizzes.Question',
                            indent=2, 
                            natural_foreign=True,
                            natural_primary=True,
                            stdout=f,
                            pks=','.join(question_pks))
            
            # Exportar respostas (sem quebra de linha se não há questões)
            if answer_pks:
                if question_pks:
                    f.write('\n')
                call_command('dumpdata', 'quizzes.Answer',
                            indent=2, 
                            natural_foreign=True,
                            natural_primary=True,
                            stdout=f,
                            pks=','.join(answer_pks))
        
        print(f"✅ Fixture exportada: {fixture_path}")
        print(f"📊 {len(questions_to_export)} questões e {len(answers_to_export)} respostas exportadas")
        
    except Exception as e:
        print(f"❌ Erro ao exportar fixture: {e}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print()
    print("=" * 80)
    print("❓ SCRIPT DE CRIAÇÃO DE QUESTÕES")
    print("=" * 80)
    print()

    # Obter configurações do usuário
    config = get_user_input()

    print()
    print("=" * 80)
    print("🔍 VERIFICANDO QUIZZES")
    print("=" * 80)
    print()

    # Encontrar quiz em todos os países
    quizzes = find_quiz_by_slug(config['quiz_slug_pt'])

    if quizzes is None:
        print("❌ Erro: Não foi possível encontrar o quiz")
        sys.exit(1)

    print()
    print(f"✅ Quizzes encontrados: {sum(1 for v in quizzes.values() if v)}/{len(quizzes)}")
    print()

    # Carregar dados do Cloudinary
    print("=" * 80)
    print("📂 CARREGANDO DADOS")
    print("=" * 80)
    print()

    cloudinary_data = load_cloudinary_urls(config['json_filename'])

    if cloudinary_data is None:
        print("❌ Erro: Não foi possível carregar os dados")
        sys.exit(1)

    # Converter para lista se necessário
    if isinstance(cloudinary_data, dict):
        items_count = len(cloudinary_data)
    else:
        items_count = len(cloudinary_data)

    print(f"✅ {items_count} itens carregados do arquivo {config['json_filename']}.json")
    print()

    # Confirmação
    print("=" * 80)
    print("📋 RESUMO DA CONFIGURAÇÃO")
    print("=" * 80)
    print(f"Quiz: {config['quiz_slug_pt']}")
    print(f"Arquivo JSON: {config['json_filename']}.json")
    print(f"Campo de nome: {config['name_field']}")
    print(f"Texto da pergunta: {config['question_text_pt']}")
    print(f"Número de questões: {items_count} (uma para cada item)")
    print(f"Traduções: {len(config['translations'])} idiomas")
    print()

    response = input("Deseja continuar com a criação das questões? (s/n): ").strip().lower()

    if response != 's':
        print("⚠️  Operação cancelada pelo usuário")
        sys.exit(0)

    print()

    # Criar questões
    total_quizzes = create_questions(config, quizzes, cloudinary_data)

    # Exportar fixtures
    export_question_fixtures(config, quizzes)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Total de quizzes processados: {total_quizzes}")
    print()
    print("🎉 Questões criadas e fixtures exportadas com sucesso!")
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
