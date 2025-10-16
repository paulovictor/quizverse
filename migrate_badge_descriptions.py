#!/usr/bin/env python
"""
Script para migrar as descrições existentes das badges para o novo formato com traduções.
Move o conteúdo do campo 'description' para 'description_translations' com a chave 'pt-BR'.
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Badge


def migrate_badge_descriptions():
    """Migra as descrições existentes para o formato JSON com traduções"""
    
    badges = Badge.objects.all()
    total = badges.count()
    
    if total == 0:
        print("Nenhuma badge encontrada para migrar.")
        return
    
    print(f"Encontradas {total} badges para migrar...")
    
    migrated = 0
    skipped = 0
    
    for badge in badges:
        # Se já tem traduções e tem conteúdo em pt-BR, pula
        if badge.description_translations and 'pt-BR' in badge.description_translations:
            print(f"  ⊘ Pulando '{badge.title}' (já possui tradução pt-BR)")
            skipped += 1
            continue
        
        # Se tem description mas não tem translations, migra
        if badge.description and badge.description.strip():
            if not badge.description_translations:
                badge.description_translations = {}
            
            badge.description_translations['pt-BR'] = badge.description
            badge.save()
            
            print(f"  ✓ Migrada '{badge.title}'")
            migrated += 1
        else:
            print(f"  ⊘ Pulando '{badge.title}' (sem descrição)")
            skipped += 1
    
    print("\n" + "="*60)
    print(f"Migração concluída!")
    print(f"  Badges migradas: {migrated}")
    print(f"  Badges puladas: {skipped}")
    print(f"  Total: {total}")
    print("="*60)


if __name__ == '__main__':
    migrate_badge_descriptions()

