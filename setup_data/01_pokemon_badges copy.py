#!/usr/bin/env python
"""
Script para criar badges dos principais temas.
Cria badges de Pokémon Gen 1 e outros temas raiz.

Este arquivo deve ser executado após criar os QuizGroups dos respectivos temas.
"""

import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import QuizGroup, Badge, QuizGroupBadge


# ============================================================================
# BADGES POKÉMON GEN 1
# ============================================================================

def create_pokemon_badges():
    """Cria as badges de Pokémon Gen 1 e associa ao QuizGroup"""

    print("=" * 80)
    print("CRIANDO BADGES DE POKÉMON GEN 1")
    print("=" * 80)
    print()

    # Buscar QuizGroup
    try:
        quiz_group = QuizGroup.objects.get(slug='pokemon-gen1')
    except QuizGroup.DoesNotExist:
        print("❌ QuizGroup 'pokemon-gen1' não encontrado!")
        print("Execute primeiro: python setup_data/01_pokemon.py")
        return 0, 0

    # Traduções das descrições das badges
    badge_descriptions = {
        'amber': {
            'pt-BR': 'Acerte todos os Pokémons!',
            'en-US': 'Get all Pokémon correct!',
            'en-CA': 'Get all Pokémon correct!',
            'en-GB': 'Get all Pokémon correct!',
            'en-IN': 'Get all Pokémon correct!',
            'en-PH': 'Get all Pokémon correct!',
            'en-AU': 'Get all Pokémon correct!',
            'en-NZ': 'Get all Pokémon correct!',
            'pt-PT': 'Acerta todos os Pokémons!',
            'es-MX': '¡Acierta todos los Pokémons!',
            'es-ES': '¡Acierta todos los Pokémons!',
            'es-AR': '¡Acierta todos los Pokémons!',
            'es-CO': '¡Acierta todos los Pokémons!',
            'de-DE': 'Errate alle Pokémon!',
            'fr-FR': 'Trouvez tous les Pokémon!',
            'it-IT': 'Indovina tutti i Pokémon!',
            'nl-NL': 'Raad alle Pokémon!',
            'sv-SE': 'Gissa alla Pokémon!',
            'no-NO': 'Gjett alle Pokémon!',
            'pl-PL': 'Zgadnij wszystkie Pokémony!',
            'id-ID': 'Tebak semua Pokémon!',
            'ja-JP': 'すべてのポケモンを当てよう！',
            'ko-KR': '모든 포켓몬을 맞히세요!',
            'th-TH': 'ทายโปเกมอนทั้งหมด!',
            'vi-VN': 'Đoán đúng tất cả Pokémon!',
        },
        'ruby': {
            'pt-BR': 'Acerte todos os Pokémons em menos de 25 minutos!',
            'en-US': 'Get all Pokémon correct in under 25 minutes!',
            'en-CA': 'Get all Pokémon correct in under 25 minutes!',
            'en-GB': 'Get all Pokémon correct in under 25 minutes!',
            'en-IN': 'Get all Pokémon correct in under 25 minutes!',
            'en-PH': 'Get all Pokémon correct in under 25 minutes!',
            'en-AU': 'Get all Pokémon correct in under 25 minutes!',
            'en-NZ': 'Get all Pokémon correct in under 25 minutes!',
            'pt-PT': 'Acerta todos os Pokémons em menos de 25 minutos!',
            'es-MX': '¡Acierta todos los Pokémons en menos de 25 minutos!',
            'es-ES': '¡Acierta todos los Pokémons en menos de 25 minutos!',
            'es-AR': '¡Acierta todos los Pokémons en menos de 25 minutos!',
            'es-CO': '¡Acierta todos los Pokémons en menos de 25 minutos!',
            'de-DE': 'Errate alle Pokémon in unter 25 Minuten!',
            'fr-FR': 'Trouvez tous les Pokémon en moins de 25 minutes!',
            'it-IT': 'Indovina tutti i Pokémon in meno di 25 minuti!',
            'nl-NL': 'Raad alle Pokémon in minder dan 25 minuten!',
            'sv-SE': 'Gissa alla Pokémon på under 25 minuter!',
            'no-NO': 'Gjett alle Pokémon på under 25 minutter!',
            'pl-PL': 'Zgadnij wszystkie Pokémony w mniej niż 25 minut!',
            'id-ID': 'Tebak semua Pokémon dalam waktu kurang dari 25 menit!',
            'ja-JP': '25分以内にすべてのポケモンを当てよう！',
            'ko-KR': '25분 이내에 모든 포켓몬을 맞히세요!',
            'th-TH': 'ทายโปเกมอนทั้งหมดในเวลาไม่เกิน 25 นาที!',
            'vi-VN': 'Đoán đúng tất cả Pokémon trong vòng 25 phút!',
        },
        'emerald': {
            'pt-BR': 'Acerte todos os Pokémons em menos de 15 minutos!',
            'en-US': 'Get all Pokémon correct in under 15 minutes!',
            'en-CA': 'Get all Pokémon correct in under 15 minutes!',
            'en-GB': 'Get all Pokémon correct in under 15 minutes!',
            'en-IN': 'Get all Pokémon correct in under 15 minutes!',
            'en-PH': 'Get all Pokémon correct in under 15 minutes!',
            'en-AU': 'Get all Pokémon correct in under 15 minutes!',
            'en-NZ': 'Get all Pokémon correct in under 15 minutes!',
            'pt-PT': 'Acerta todos os Pokémons em menos de 15 minutos!',
            'es-MX': '¡Acierta todos los Pokémons en menos de 15 minutos!',
            'es-ES': '¡Acierta todos los Pokémons en menos de 15 minutos!',
            'es-AR': '¡Acierta todos los Pokémons en menos de 15 minutos!',
            'es-CO': '¡Acierta todos los Pokémons en menos de 15 minutos!',
            'de-DE': 'Errate alle Pokémon in unter 15 Minuten!',
            'fr-FR': 'Trouvez tous les Pokémon en moins de 15 minutes!',
            'it-IT': 'Indovina tutti i Pokémon in meno di 15 minuti!',
            'nl-NL': 'Raad alle Pokémon in minder dan 15 minuten!',
            'sv-SE': 'Gissa alla Pokémon på under 15 minuter!',
            'no-NO': 'Gjett alle Pokémon på under 15 minutter!',
            'pl-PL': 'Zgadnij wszystkie Pokémony w mniej niż 15 minut!',
            'id-ID': 'Tebak semua Pokémon dalam waktu kurang dari 15 menit!',
            'ja-JP': '15分以内にすべてのポケモンを当てよう！',
            'ko-KR': '15분 이내에 모든 포켓몬을 맞히세요!',
            'th-TH': 'ทายโปเกมอนทั้งหมดในเวลาไม่เกิน 15 นาที!',
            'vi-VN': 'Đoán đúng tất cả Pokémon trong vòng 15 phút!',
        },
        'sapphire': {
            'pt-BR': 'Acerte todos os Pokémons em menos de 10 minutos!',
            'en-US': 'Get all Pokémon correct in under 10 minutes!',
            'en-CA': 'Get all Pokémon correct in under 10 minutes!',
            'en-GB': 'Get all Pokémon correct in under 10 minutes!',
            'en-IN': 'Get all Pokémon correct in under 10 minutes!',
            'en-PH': 'Get all Pokémon correct in under 10 minutes!',
            'en-AU': 'Get all Pokémon correct in under 10 minutes!',
            'en-NZ': 'Get all Pokémon correct in under 10 minutes!',
            'pt-PT': 'Acerta todos os Pokémons em menos de 10 minutos!',
            'es-MX': '¡Acierta todos los Pokémons en menos de 10 minutos!',
            'es-ES': '¡Acierta todos los Pokémons en menos de 10 minutos!',
            'es-AR': '¡Acierta todos los Pokémons en menos de 10 minutos!',
            'es-CO': '¡Acierta todos los Pokémons en menos de 10 minutos!',
            'de-DE': 'Errate alle Pokémon in unter 10 Minuten!',
            'fr-FR': 'Trouvez tous les Pokémon en moins de 10 minutes!',
            'it-IT': 'Indovina tutti i Pokémon in meno di 10 minuti!',
            'nl-NL': 'Raad alle Pokémon in minder dan 10 minuten!',
            'sv-SE': 'Gissa alla Pokémon på under 10 minuter!',
            'no-NO': 'Gjett alle Pokémon på under 10 minutter!',
            'pl-PL': 'Zgadnij wszystkie Pokémony w mniej niż 10 minut!',
            'id-ID': 'Tebak semua Pokémon dalam waktu kurang dari 10 menit!',
            'ja-JP': '10分以内にすべてのポケモンを当てよう！',
            'ko-KR': '10분 이내에 모든 포켓몬을 맞히세요!',
            'th-TH': 'ทายโปเกมอนทั้งหมดในเวลาไม่เกิน 10 นาที!',
            'vi-VN': 'Đoán đúng tất cả Pokémon trong vòng 10 phút!',
        },
        'diamond': {
            'pt-BR': 'Acerte todos os Pokémons em menos de 6 minutos!',
            'en-US': 'Get all Pokémon correct in under 6 minutes!',
            'en-CA': 'Get all Pokémon correct in under 6 minutes!',
            'en-GB': 'Get all Pokémon correct in under 6 minutes!',
            'en-IN': 'Get all Pokémon correct in under 6 minutes!',
            'en-PH': 'Get all Pokémon correct in under 6 minutes!',
            'en-AU': 'Get all Pokémon correct in under 6 minutes!',
            'en-NZ': 'Get all Pokémon correct in under 6 minutes!',
            'pt-PT': 'Acerta todos os Pokémons em menos de 6 minutos!',
            'es-MX': '¡Acierta todos los Pokémons en menos de 6 minutos!',
            'es-ES': '¡Acierta todos los Pokémons en menos de 6 minutos!',
            'es-AR': '¡Acierta todos los Pokémons en menos de 6 minutos!',
            'es-CO': '¡Acierta todos los Pokémons en menos de 6 minutos!',
            'de-DE': 'Errate alle Pokémon in unter 6 Minuten!',
            'fr-FR': 'Trouvez tous les Pokémon en moins de 6 minutes!',
            'it-IT': 'Indovina tutti i Pokémon in meno di 6 minuti!',
            'nl-NL': 'Raad alle Pokémon in minder dan 6 minuten!',
            'sv-SE': 'Gissa alla Pokémon på under 6 minuter!',
            'no-NO': 'Gjett alle Pokémon på under 6 minutter!',
            'pl-PL': 'Zgadnij wszystkie Pokémony w mniej niż 6 minut!',
            'id-ID': 'Tebak semua Pokémon dalam waktu kurang dari 6 menit!',
            'ja-JP': '6分以内にすべてのポケモンを当てよう！',
            'ko-KR': '6분 이내에 모든 포켓몬을 맞히세요!',
            'th-TH': 'ทายโปเกมอนทั้งหมดในเวลาไม่เกิน 6 นาที!',
            'vi-VN': 'Đoán đúng tất cả Pokémon trong vòng 6 phút!',
        },
    }

    badges_data = [
        {
            'slug': 'amber-pikachu',
            'title': '🟠 Amber Pikachu',
            'description': 'Acerte todos os Pokémons!',
            'description_translations': badge_descriptions['amber'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760659174/pikachu_ambar_ckyhbt.png',
            'rule_type': 'perfect_score',
            'min_percentage': 100.0,
            'rarity': 'epic',
            'points': 150,
            'order': 1,
        },
        {
            'slug': 'ruby-pikachu',
            'title': '🔴 Ruby Pikachu',
            'description': 'Acerte todos os Pokémons em menos de 25 minutos!',
            'description_translations': badge_descriptions['ruby'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760659173/pikachu_ruby_l8u7db.png',
            'rule_type': 'percentage_time',
            'min_percentage': 100.0,
            'rarity': 'epic',
            'points': 200,
            'order': 2,
        },
        {
            'slug': 'emerald-pikachu',
            'title': '🟢 Emerald Pikachu',
            'description': 'Acerte todos os Pokémons em menos de 15 minutos!',
            'description_translations': badge_descriptions['emerald'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760659173/pikachu_emerald_huorpv.png',
            'rule_type': 'percentage_time',
            'min_percentage': 100.0,
            'rarity': 'legendary',
            'points': 300,
            'order': 3,
        },
        {
            'slug': 'sapphire-pikachu',
            'title': '🔵 Sapphire Pikachu',
            'description': 'Acerte todos os Pokémons em menos de 10 minutos!',
            'description_translations': badge_descriptions['sapphire'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760659173/pikachu_sapphire_pwcbqz.png',
            'rule_type': 'percentage_time',
            'min_percentage': 100.0,
            'rarity': 'legendary',
            'points': 400,
            'order': 4,
        },
        {
            'slug': 'diamond-pikachu',
            'title': '💎 Diamond Pikachu',
            'description': 'Acerte todos os Pokémons em menos de 6 minutos!',
            'description_translations': badge_descriptions['diamond'],
            'image': 'https://res.cloudinary.com/dwm53cbu2/image/upload/v1760659173/pikachu_diamond_yccykq.png',
            'rule_type': 'percentage_time',
            'min_percentage': 100.0,
            'rarity': 'legendary',
            'points': 500,
            'order': 5,
        },
    ]

    created_count = 0
    updated_count = 0
    associated_count = 0

    for badge_data in badges_data:
        # Criar ou atualizar badge
        badge, created = Badge.objects.update_or_create(
            slug=badge_data['slug'],
            defaults={
                'title': badge_data['title'],
                'description': badge_data['description'],
                'description_translations': badge_data['description_translations'],
                'image': badge_data['image'],
                'rule_type': badge_data['rule_type'],
                'min_percentage': badge_data['min_percentage'],
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
    print("🏆 SETUP: BADGES DOS TEMAS PRINCIPAIS")
    print("=" * 80)
    print()

    total_created = 0
    total_updated = 0

    # Pokémon Gen 1 Badges
    created, updated = create_pokemon_badges()
    total_created += created
    total_updated += updated

    # Resumo final
    print("=" * 80)
    print("📊 RESUMO FINAL")
    print("=" * 80)
    print(f"✅ Total de badges criadas: {total_created}")
    print(f"🔄 Total de badges atualizadas: {total_updated}")
    print()
    print("🎉 Setup de badges concluído com sucesso!")
    print()
    print("💡 Próximos passos:")
    print("   1. Verifique as badges em /admin/quizzes/badge/")
    print("   2. Complete um quiz para testar se as badges são concedidas automaticamente!")
    print()


if __name__ == '__main__':
    main()
