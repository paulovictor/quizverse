"""
Script para criar QuizGroup para Pokémon Gen 1 e associar todos os quizzes.
Deve ser executado após 00_root_pokemon.py
"""

import os
import sys
import django
from django.utils.text import slugify

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Quiz, QuizGroup


def create_pokemon_quizgroup():
    """Cria o QuizGroup para Pokémon Gen 1 e associa todos os quizzes"""

    print("=" * 80)
    print("🎮 CRIANDO QUIZGROUP PARA POKÉMON - GERAÇÃO 1")
    print("=" * 80)
    print()

    # Criar ou atualizar o QuizGroup
    group_name = "Pokémon Gen 1 - Guess the Pokémon"
    group_slug = "pokemon-gen1"
    group_description = (
        "Grupo de quizzes 'Adivinhe o Pokémon' da Geração 1, "
        "disponível em múltiplos idiomas e países. "
        "Todos os quizzes deste grupo contêm os mesmos 151 Pokémon originais, "
        "adaptados para diferentes regiões."
    )

    quiz_group, created = QuizGroup.objects.update_or_create(
        slug=group_slug,
        defaults={
            'name': group_name,
            'description': group_description,
        }
    )

    if created:
        print(f"✅ QuizGroup criado: {group_name}")
    else:
        print(f"🔄 QuizGroup atualizado: {group_name}")
    print(f"   Slug: {group_slug}")
    print()

    # Buscar todos os quizzes de Pokémon Gen 1
    # Identificamos pelos slugs que seguem o padrão do 00_root_pokemon.py
    pokemon_quiz_slugs = [
        'adivinhe-o-pokemon-gen1',  # pt-BR (base)
        'adivinhe-o-pokemon-gen1-us',  # en-US
        'adivinhe-o-pokemon-gen1-ca',  # en-CA
        'adivinhe-o-pokemon-gen1-mx',  # es-MX
        'adivinhe-o-pokemon-gen1-gb',  # en-GB
        'adivinhe-o-pokemon-gen1-de',  # de-DE
        'adivinhe-o-pokemon-gen1-fr',  # fr-FR
        'adivinhe-o-pokemon-gen1-es',  # es-ES
        'adivinhe-o-pokemon-gen1-it',  # it-IT
        'adivinhe-o-pokemon-gen1-nl',  # nl-NL
        'adivinhe-o-pokemon-gen1-se',  # sv-SE
        'adivinhe-o-pokemon-gen1-no',  # no-NO
        'adivinhe-o-pokemon-gen1-pl',  # pl-PL
        'adivinhe-o-pokemon-gen1-pt',  # pt-PT
        'adivinhe-o-pokemon-gen1-in',  # en-IN
        'adivinhe-o-pokemon-gen1-ph',  # en-PH
        'adivinhe-o-pokemon-gen1-id',  # id-ID
        'adivinhe-o-pokemon-gen1-jp',  # ja-JP
        'adivinhe-o-pokemon-gen1-kr',  # ko-KR
        'adivinhe-o-pokemon-gen1-th',  # th-TH
        'adivinhe-o-pokemon-gen1-vn',  # vi-VN
        'adivinhe-o-pokemon-gen1-au',  # en-AU
        'adivinhe-o-pokemon-gen1-nz',  # en-NZ
        'adivinhe-o-pokemon-gen1-ar',  # es-AR
        'adivinhe-o-pokemon-gen1-co',  # es-CO
        # Também buscar variantes com "guess-the-pokemon-gen1"
        'guess-the-pokemon-gen1',
        'guess-the-pokemon-gen1-us',
        'guess-the-pokemon-gen1-ca',
        'guess-the-pokemon-gen1-mx',
        'guess-the-pokemon-gen1-gb',
        'guess-the-pokemon-gen1-de',
        'guess-the-pokemon-gen1-fr',
        'guess-the-pokemon-gen1-es',
        'guess-the-pokemon-gen1-it',
        'guess-the-pokemon-gen1-nl',
        'guess-the-pokemon-gen1-se',
        'guess-the-pokemon-gen1-no',
        'guess-the-pokemon-gen1-pl',
        'guess-the-pokemon-gen1-pt',
        'guess-the-pokemon-gen1-in',
        'guess-the-pokemon-gen1-ph',
        'guess-the-pokemon-gen1-id',
        'guess-the-pokemon-gen1-jp',
        'guess-the-pokemon-gen1-kr',
        'guess-the-pokemon-gen1-th',
        'guess-the-pokemon-gen1-vn',
        'guess-the-pokemon-gen1-au',
        'guess-the-pokemon-gen1-nz',
        'guess-the-pokemon-gen1-ar',
        'guess-the-pokemon-gen1-co',
    ]

    print("🔍 Buscando quizzes de Pokémon Gen 1...")
    print()

    updated_count = 0
    not_found_count = 0

    for slug in pokemon_quiz_slugs:
        try:
            quiz = Quiz.objects.get(slug=slug)

            # Associar ao grupo (se ainda não estiver)
            if quiz.quiz_group != quiz_group:
                quiz.quiz_group = quiz_group
                quiz.save()
                print(f"✅ Associado: {slug} ({quiz.country})")
                updated_count += 1
            else:
                print(f"⏭️  Já associado: {slug} ({quiz.country})")

        except Quiz.DoesNotExist:
            # Não encontrou, mas não é erro (pode não ter sido criado ainda)
            not_found_count += 1
            continue

    print()
    print("=" * 80)
    print("📊 RESUMO")
    print("=" * 80)
    print(f"✅ Quizzes associados: {updated_count}")
    print(f"⏭️  Quizzes não encontrados: {not_found_count}")
    print(f"📝 QuizGroup: {group_name}")
    print()

    # Mostrar quizzes disponíveis no grupo
    all_quizzes = Quiz.objects.filter(quiz_group=quiz_group)
    print(f"📋 Total de quizzes no grupo: {all_quizzes.count()}")
    print()

    if all_quizzes.exists():
        print("🌍 Quizzes por país:")
        for quiz in all_quizzes.order_by('country', 'slug'):
            country_flag = dict(quiz.COUNTRY_CHOICES).get(quiz.country, quiz.country)
            print(f"   {country_flag}: {quiz.title}")
        print()

    print("🎉 Setup do QuizGroup concluído com sucesso!")
    print()

    if not_found_count > 0:
        print("⚠️  ATENÇÃO:")
        print(f"   {not_found_count} quizzes não foram encontrados.")
        print("   Certifique-se de executar primeiro:")
        print("   python setup_data/00_root_pokemon_theme.py")
        print("   python setup_data/00_root_pokemon.py")
        print()


def main():
    create_pokemon_quizgroup()


if __name__ == '__main__':
    main()
