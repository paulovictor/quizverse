#!/usr/bin/env python
"""
Script para popular o banco com produtos fake
Execute: uv run python populate_products.py
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme, Product
from decimal import Decimal


def create_products():
    print("🛍️ Criando produtos fake...\n")
    
    # Produtos do Flamengo
    theme_flamengo = Theme.objects.get(slug='flamengo')
    
    print(f"📌 Criando produtos para: {theme_flamengo.title}")
    
    products_flamengo = [
        {
            'title': 'Camisa Oficial Flamengo 2024',
            'price': Decimal('249.90'),
            'image_url': 'https://images.unsplash.com/photo-1551488831-00ddcb84c6d9?w=400',
            'product_url': 'https://www.lojadoflamengo.com.br/camisa',
        },
        {
            'title': 'Agasalho Oficial Flamengo',
            'price': Decimal('189.90'),
            'image_url': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400',
            'product_url': 'https://www.lojadoflamengo.com.br/agasalho',
        },
        {
            'title': 'Boné Oficial Flamengo',
            'price': Decimal('79.90'),
            'image_url': 'https://images.unsplash.com/photo-1588850561407-ed78c282e89b?w=400',
            'product_url': 'https://www.lojadoflamengo.com.br/bone',
        },
    ]
    
    for idx, product_data in enumerate(products_flamengo):
        product, created = Product.objects.get_or_create(
            theme=theme_flamengo,
            title=product_data['title'],
            defaults={
                **product_data,
                'order': idx,
                'active': True
            }
        )
        if created:
            print(f"   ✓ {product.title} - R$ {product.price}")
    
    print()
    
    # Produtos Harry Potter
    theme_hp = Theme.objects.get(slug='harrypotter')
    
    print(f"📌 Criando produtos para: {theme_hp.title}")
    
    products_hp = [
        {
            'title': 'Livro Harry Potter - Box Completo',
            'price': Decimal('299.90'),
            'image_url': 'https://images.unsplash.com/photo-1615870216519-2f9fa575fa5c?w=400',
            'product_url': 'https://www.amazon.com.br/harry-potter-box',
        },
        {
            'title': 'Varinha Mágica Harry Potter',
            'price': Decimal('149.90'),
            'image_url': 'https://images.unsplash.com/photo-1551269901-5c5e14c25df7?w=400',
            'product_url': 'https://www.amazon.com.br/varinha-harry-potter',
        },
        {
            'title': 'Cachecol Grifinória Oficial',
            'price': Decimal('89.90'),
            'image_url': 'https://images.unsplash.com/photo-1601924994987-69e26d50dc26?w=400',
            'product_url': 'https://www.amazon.com.br/cachecol-grifinoria',
        },
    ]
    
    for idx, product_data in enumerate(products_hp):
        product, created = Product.objects.get_or_create(
            theme=theme_hp,
            title=product_data['title'],
            defaults={
                **product_data,
                'order': idx,
                'active': True
            }
        )
        if created:
            print(f"   ✓ {product.title} - R$ {product.price}")
    
    print("\n✅ Produtos criados com sucesso!")
    print("\n📦 Resumo:")
    print(f"   → {theme_flamengo.title}: {theme_flamengo.products.count()} produtos")
    print(f"   → {theme_hp.title}: {theme_hp.products.count()} produtos")
    print("\n💡 Os produtos aparecerão na página de resultado dos quizzes!")


if __name__ == '__main__':
    create_products()

