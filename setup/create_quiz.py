#!/usr/bin/env python
"""
Script para criar quizzes em todos os países.

Este script:
1. Pergunta o slug do tema em português
2. Pergunta informações sobre o quiz a ser criado
3. Cria o quiz em todos os países, associando ao tema correto

Uso:
    python setup/create_quiz.py
"""

import os
import sys
import json
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

def find_theme_by_slug(theme_slug_pt):
    """
    Encontra o tema em todos os países baseado no slug PT-BR
    """
    themes = {}
    
    # Para pt-BR, usar o slug direto
    try:
        theme_pt = Theme.objects.get(slug=theme_slug_pt, country='pt-BR')
        themes['pt-BR'] = theme_pt
        print(f"✅ Tema encontrado para pt-BR: {theme_pt.slug} - {theme_pt.title}")
    except Theme.DoesNotExist:
        print(f"❌ Erro: Tema '{theme_slug_pt}' não encontrado para pt-BR")
        return None

    # Para outros países, buscar variações do slug
    for country_code in COUNTRY_TO_LANG.keys():
        if country_code == 'pt-BR':
            continue

        country_suffix = country_code.split('-')[1].lower()
        expected_slug = f"{theme_slug_pt}-{country_suffix}"

        try:
            theme = Theme.objects.get(slug=expected_slug, country=country_code)
            themes[country_code] = theme
            print(f"✅ Tema encontrado para {country_code}: {theme.slug} - {theme.title}")
        except Theme.DoesNotExist:
            print(f"⚠️  Tema não encontrado para {country_code}: {expected_slug}")
            themes[country_code] = None

    return themes


def get_quiz_description_template(lang_code):
    """Retorna template de descrição com placeholders {sample_size} e {total}"""
    templates = {
        'en': 'Answer {sample_size} random questions from {total} available! Test your knowledge.',
        'pt': 'Responda {sample_size} questões aleatórias de {total} disponíveis! Teste seu conhecimento.',
        'es': '¡Responde {sample_size} preguntas aleatorias de {total} disponibles! Pon a prueba tu conocimiento.',
    }
    return templates.get(lang_code, templates['en'])


def get_user_input():
    """
    Solicita informações do usuário sobre o quiz a ser criado
    """
    print("=" * 80)
    print("🎮 CRIAR NOVO QUIZ")
    print("=" * 80)
    print()

    # Slug do quiz (base em português)
    print("1️⃣ Digite o slug BASE do novo quiz em português (ex: awp)")
    while True:
        quiz_slug_base = input("   Slug base: ").strip()
        if quiz_slug_base:
            break
        print("❌ Slug base não pode ser vazio! Tente novamente.")

    print()

    # Título do quiz
    print("2️⃣ Título do quiz")
    while True:
        quiz_title_pt = input("   Título (pt): ").strip()
        if quiz_title_pt:
            break
        print("❌ Título não pode ser vazio! Tente novamente.")

    print()

    # Descrição do quiz
    print("3️⃣ Descrição do quiz")
    while True:
        quiz_description_pt = input("   Descrição (pt): ").strip()
        if quiz_description_pt:
            break
        print("❌ Descrição não pode ser vazia! Tente novamente.")

    print()

    # Dificuldade
    print("4️⃣ Dificuldade do quiz")
    print("   Opções: easy, medium, hard")
    difficulty = input("   Dificuldade (padrão: medium): ").strip().lower()

    if difficulty not in ['easy', 'medium', 'hard']:
        difficulty = 'medium'

    print()

    num_questions = 0

    # Ordem
    print("6️⃣ Ordem de exibição do quiz (número inteiro, menor = primeiro)")
    order = input("   Ordem (padrão: 1): ").strip()

    try:
        order = int(order) if order else 1
    except ValueError:
        order = 1

    print()

    # Traduções
    print("7️⃣ Traduções do quiz")
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
            # Para português, usar os valores já informados
            title = quiz_title_pt
            description = quiz_description_pt
            print(f"      Título: {title}")
            print(f"      Descrição: {description}")
        else:
            # Para outros idiomas, perguntar
            # Título obrigatório
            while True:
                title = input(f"      Título: ").strip()
                if title:
                    break
                print(f"      ❌ Título não pode ser vazio! Tente novamente.")
            
            # Descrição obrigatória
            while True:
                description = input(f"      Descrição: ").strip()
                if description:
                    break
                print(f"      ❌ Descrição não pode ser vazia! Tente novamente.")

        translations[lang_code] = {
            'title': title,
            'description': description,
        }
        print()

    if not translations:
        print("❌ Erro: Pelo menos uma tradução é necessária!")
        sys.exit(1)

    return {
        'quiz_slug_base': quiz_slug_base,
        'quiz_title_pt': quiz_title_pt,
        'quiz_description_pt': quiz_description_pt,
        'difficulty': difficulty,
        'num_questions': num_questions,
        'order': order,
        'translations': translations,
    }


def create_quiz_group(config):
    """
    Cria o QuizGroup para o quiz
    """
    print("=" * 80)
    print("🔧 CRIANDO QUIZGROUP")
    print("=" * 80)
    print()

    quiz_group, created = QuizGroup.objects.update_or_create(
        slug=config['quiz_slug_base'],
        defaults={
            'name': config['quiz_title_pt'],
            'description': config['quiz_description_pt'],
            'difficulty': config['difficulty'],
            'order': config['order'],
        }
    )

    status = "✅ Criado" if created else "🔄 Atualizado"
    print(f"{status}: {quiz_group.name}")
    print()

    return quiz_group


def create_quizzes(config, themes, quiz_group):
    """
    Cria os quizzes em todos os países
    """
    print("=" * 80)
    print("🚀 CRIANDO QUIZZES")
    print("=" * 80)
    print()

    created_count = 0
    updated_count = 0
    errors = []

    for country_code, lang_code in COUNTRY_TO_LANG.items():
        # Usar tradução do idioma ou fallback para inglês
        translation = config['translations'].get(lang_code, config['translations'].get('en'))

        if not translation:
            errors.append(f"⚠️  Tradução não encontrada para {country_code} ({lang_code})")
            continue

        # Buscar tema
        theme = themes.get(country_code)
        if not theme:
            errors.append(f"⚠️  Tema não encontrado para {country_code}")
            continue

        # Determinar slug do quiz
        if country_code == 'pt-BR':
            quiz_slug = config['quiz_slug_base']
        else:
            country_suffix = country_code.split('-')[1].lower()
            quiz_slug = f"{config['quiz_slug_base']}-{country_suffix}"

        # Gerar template e description inicial
        quiz_description_template = get_quiz_description_template(lang_code)
        quiz_description = quiz_description_template.format(
            sample_size=config['num_questions'], 
            total=config['num_questions']
        )

        # Criar ou atualizar quiz
        quiz, created = Quiz.objects.update_or_create(
            slug=quiz_slug,
            defaults={
                'theme': theme,
                'quiz_group': quiz_group,
                'title': translation['title'],
                'description': quiz_description,
                'description_template': quiz_description_template,
                'difficulty': config['difficulty'],
                'active': True,
                'order': config['order'],
                'country': country_code,
                'question_sample_size': 0,
            }
        )

        if created:
            created_count += 1
            status = "✅"
        else:
            updated_count += 1
            status = "🔄"

        print(f"{status} {country_code:7s} | {quiz_slug:30s} → {theme.slug}")

    print()
    print(f"📊 Quizzes criados: {created_count} | Atualizados: {updated_count}")

    if errors:
        print()
        print("⚠️  AVISOS:")
        for error in errors:
            print(f"   {error}")

    print()
    return created_count + updated_count


def export_quiz_fixtures(config, quiz_group):
    """
    Exporta os quizzes criados como fixtures JSON
    """
    print("=" * 80)
    print("📦 EXPORTANDO FIXTURES")
    print("=" * 80)
    print()
    
    # Criar pasta fixtures se não existir
    fixtures_dir = Path(project_root) / 'fixtures' / 'quizzes'
    fixtures_dir.mkdir(parents=True, exist_ok=True)
    
    # Nome do arquivo baseado no slug
    fixture_filename = f"{config['quiz_slug_base']}_quizzes.json"
    fixture_path = fixtures_dir / fixture_filename
    
    try:
        # Buscar todos os quizzes criados para este slug base
        quizzes_to_export = []
        
        for country_code in COUNTRY_TO_LANG.keys():
            # Determinar slug do quiz
            if country_code == 'pt-BR':
                quiz_slug = config['quiz_slug_base']
            else:
                country_suffix = country_code.split('-')[1].lower()
                quiz_slug = f"{config['quiz_slug_base']}-{country_suffix}"
            
            try:
                quiz = Quiz.objects.get(slug=quiz_slug, country=country_code)
                quizzes_to_export.append(quiz)
            except Quiz.DoesNotExist:
                continue
        
        if not quizzes_to_export:
            print("⚠️  Nenhum quiz encontrado para exportar")
            return
        
        # Exportar QuizGroup primeiro
        quiz_group_fixture_path = fixtures_dir / f"{config['quiz_slug_base']}_quiz_group.json"
        with open(quiz_group_fixture_path, 'w', encoding='utf-8') as f:
            call_command('dumpdata', 'quizzes.QuizGroup', 
                        indent=2, 
                        natural_foreign=True,
                        natural_primary=True,
                        stdout=f,
                        pks=str(quiz_group.pk))
        
        # Exportar quizzes
        with open(fixture_path, 'w', encoding='utf-8') as f:
            call_command('dumpdata', 'quizzes.Quiz', 
                        indent=2, 
                        natural_foreign=True,
                        natural_primary=True,
                        stdout=f,
                        pks=','.join([str(quiz.pk) for quiz in quizzes_to_export]))
        
        print(f"✅ Fixture QuizGroup exportada: {quiz_group_fixture_path}")
        print(f"✅ Fixture Quizzes exportada: {fixture_path}")
        print(f"📊 {len(quizzes_to_export)} quizzes exportados")
        
    except Exception as e:
        print(f"❌ Erro ao exportar fixture: {e}")


# ============================================================================
# MAIN
# ============================================================================

def main():
    print()
    print("=" * 80)
    print("🎮 SCRIPT DE CRIAÇÃO DE QUIZZES")
    print("=" * 80)
    print()

    # Solicitar slug do tema
    print("🎯 Digite o slug do tema em português (ex: pokemon, counter-strike)")
    while True:
        theme_slug_pt = input("   Slug do tema: ").strip()
        if theme_slug_pt:
            break
        print("❌ Slug do tema não pode ser vazio! Tente novamente.")

    print(f"✅ Tema alvo: {theme_slug_pt}")
    print()

    # Encontrar tema em todos os países
    print("=" * 80)
    print("🔍 VERIFICANDO TEMAS")
    print("=" * 80)
    print()

    themes = find_theme_by_slug(theme_slug_pt)

    if themes is None:
        print("❌ Erro: Não foi possível encontrar o tema")
        sys.exit(1)

    print()
    print(f"✅ Temas encontrados: {sum(1 for v in themes.values() if v)}/{len(themes)}")
    print()

    # Obter configurações do usuário
    config = get_user_input()

    print()
    print("=" * 80)
    print("📋 RESUMO DA CONFIGURAÇÃO")
    print("=" * 80)
    print(f"Slug base: {config['quiz_slug_base']}")
    print(f"Título (pt): {config['quiz_title_pt']}")
    print(f"Dificuldade: {config['difficulty']}")
    print(f"Número de questões: {config['num_questions']}")
    print(f"Ordem: {config['order']}")
    print(f"Traduções: {len(config['translations'])} idiomas")
    print()

    response = input("Deseja continuar com a criação dos quizzes? (s/n): ").strip().lower()

    if response != 's':
        print("⚠️  Operação cancelada pelo usuário")
        sys.exit(0)

    print()

    # Criar QuizGroup
    quiz_group = create_quiz_group(config)

    # Criar quizzes
    total_quizzes = create_quizzes(config, themes, quiz_group)

    # Exportar fixtures
    export_quiz_fixtures(config, quiz_group)

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Total de quizzes processados: {total_quizzes}")
    print()
    print("🎉 Quizzes criados e fixtures exportadas com sucesso!")



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
