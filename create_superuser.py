#!/usr/bin/env python
"""
Script para criar superuser no Heroku
"""
import os
import sys
import django

# Configurar o ambiente Django
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from django.contrib.auth.models import User

def create_superuser():
    print("=" * 80)
    print("👤 CRIANDO SUPERUSER")
    print("=" * 80)
    print()
    
    # Dados do superuser
    username = 'admin'
    email = 'admin@quizverso.com'
    password = 'admin123'
    
    # Verificar se já existe
    if User.objects.filter(username=username).exists():
        print(f"⚠️  Superuser '{username}' já existe!")
        return
    
    # Criar superuser
    try:
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f"✅ Superuser criado com sucesso!")
        print(f"   Username: {username}")
        print(f"   Email: {email}")
        print(f"   Password: {password}")
        print()
        print("🔗 Acesse o admin em: /admin/")
    except Exception as e:
        print(f"❌ Erro ao criar superuser: {e}")

if __name__ == '__main__':
    create_superuser()
