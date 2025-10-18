#!/usr/bin/env python3
"""
Script para restaurar dados essenciais após reset do banco
"""

import os
import sys
import django
from pathlib import Path

# Configurar Django
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from django.contrib.sites.models import Site
from allauth.socialaccount.models import SocialApp


def restore_essential_data():
    """Restaura dados essenciais do sistema"""
    print("=" * 80)
    print("🔄 RESTAURANDO DADOS ESSENCIAIS")
    print("=" * 80)
    print()
    
    # 1. Criar sites
    print("🌐 Criando sites...")
    
    # Site 1: Heroku
    site1, created = Site.objects.get_or_create(
        id=1,
        defaults={
            'domain': 'quiz-webapp-a6102da847af.herokuapp.com',
            'name': 'Quiz App'
        }
    )
    if created:
        print(f"   ✅ Site criado: {site1.name} ({site1.domain})")
    else:
        print(f"   ℹ️  Site já existe: {site1.name} ({site1.domain})")
    
    # Site 2: Domínio principal
    site2, created = Site.objects.get_or_create(
        id=2,
        defaults={
            'domain': 'quizverso.com',
            'name': 'Quizverso'
        }
    )
    if created:
        print(f"   ✅ Site criado: {site2.name} ({site2.domain})")
    else:
        print(f"   ℹ️  Site já existe: {site2.name} ({site2.domain})")
    
    # 2. Criar Social App (Google OAuth)
    print("\n🔐 Criando Social App (Google OAuth)...")
    
    social_app, created = SocialApp.objects.get_or_create(
        id=1,
        provider='google',
        defaults={
            'name': 'Google',
            'client_id': '1020069839413-afesl0qcap58umr5vsl3sq4urtt96nqu.apps.googleusercontent.com',
            'secret': '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',
            'settings': {}
        }
    )
    
    if created:
        print(f"   ✅ Social App criado: {social_app.name}")
    else:
        print(f"   ℹ️  Social App já existe: {social_app.name}")
    
    # 3. Associar Social App aos sites
    print("\n🔗 Associando Social App aos sites...")
    
    # Adicionar site 1 se não estiver associado
    if site1 not in social_app.sites.all():
        social_app.sites.add(site1)
        print(f"   ✅ Site '{site1.name}' associado ao Google OAuth")
    else:
        print(f"   ℹ️  Site '{site1.name}' já associado ao Google OAuth")
    
    # Adicionar site 2 se não estiver associado
    if site2 not in social_app.sites.all():
        social_app.sites.add(site2)
        print(f"   ✅ Site '{site2.name}' associado ao Google OAuth")
    else:
        print(f"   ℹ️  Site '{site2.name}' já associado ao Google OAuth")
    
    print()
    print("✨ Dados essenciais restaurados com sucesso!")
    print()
    print("📋 Resumo:")
    print(f"   🌐 Sites: {Site.objects.count()}")
    print(f"   🔐 Social Apps: {SocialApp.objects.count()}")
    print(f"   🔗 Associações: {social_app.sites.count()}")


if __name__ == '__main__':
    restore_essential_data()
