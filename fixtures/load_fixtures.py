#!/usr/bin/env python
"""
Script para carregar fixtures no Heroku.
Este script carrega todas as fixtures disponíveis na pasta fixtures/
"""

import os
import sys
import django
from pathlib import Path

# Configuração do Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from django.core.management import call_command


def load_fixtures():
    """Carrega todas as fixtures disponíveis"""
    fixtures_dir = Path(project_root) / 'fixtures'
    
    if not fixtures_dir.exists():
        print("❌ Pasta fixtures/ não encontrada!")
        return
    
    print("=" * 80)
    print("📦 CARREGANDO FIXTURES")
    print("=" * 80)
    print()
    
    # Carregar fixtures por categoria
    categories = ['themes', 'quizzes', 'questions']
    total_loaded = 0
    
    for category in categories:
        category_dir = fixtures_dir / category
        
        if not category_dir.exists():
            print(f"⚠️  Pasta {category}/ não encontrada, pulando...")
            continue
        
        json_files = list(category_dir.glob("*.json"))
        
        if not json_files:
            print(f"📁 Nenhuma fixture encontrada em {category}/")
            continue
        
        print(f"📂 Carregando fixtures de {category}/")
        
        for json_file in sorted(json_files):
            try:
                fixture_path = f"fixtures/{category}/{json_file.name}"
                print(f"   📄 {json_file.name}...", end=" ")
                
                call_command('loaddata', fixture_path, verbosity=0)
                print("✅")
                total_loaded += 1
                
            except Exception as e:
                print(f"❌ Erro: {e}")
    
    print()
    print("=" * 80)
    print("📊 RESUMO")
    print("=" * 80)
    print(f"✅ Total de fixtures carregadas: {total_loaded}")
    print()


if __name__ == '__main__':
    load_fixtures()
