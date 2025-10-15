"""
Script para deletar todos os themes do banco de dados
"""

import os
import sys
import django

# Configuração do Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme

def delete_all_themes():
    """Deleta todos os temas do banco de dados"""
    
    total_themes = Theme.objects.count()
    
    if total_themes == 0:
        print("❌ Nenhum tema encontrado no banco de dados.")
        return
    
    print(f"🗑️  Encontrados {total_themes} temas no banco de dados.")
    print("🚨 Deletando todos os temas...")
    print("-" * 80)
    
    Theme.objects.all().delete()
    
    print("-" * 80)
    print(f"✅ Todos os {total_themes} temas foram deletados com sucesso!")

if __name__ == '__main__':
    delete_all_themes()

