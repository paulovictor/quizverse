"""
Setup Root Themes
Cria os 12 temas raiz (categorias principais) com cores e ícones personalizados
"""
import os
import sys
import django

# Setup Django
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
django.setup()

from quizzes.models import Theme


def run():
    """Cria os temas raiz"""
    print("🎨 Criando temas raiz...\n")
    
    # Dados dos temas raiz
    root_themes = [
        {
            'title': 'Esportes',
            'slug': 'esportes',
            'description': 'Teste seus conhecimentos sobre futebol, basquete, tênis e muito mais. De regras básicas a recordes históricos!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#34d399',
            'secondary_color': '#10b981',
            'icon_bg_color_1': '#d1fae5',
            'icon_bg_color_2': '#a7f3d0',
            'order': 1,
        },
        {
            'title': 'Entretenimento & Mídia',
            'slug': 'entretenimento-midia',
            'description': 'Filmes, séries, música e tudo sobre o mundo do entretenimento. De clássicos a lançamentos recentes!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#a78bfa',
            'secondary_color': '#8b5cf6',
            'icon_bg_color_1': '#ede9fe',
            'icon_bg_color_2': '#ddd6fe',
            'order': 2,
        },
        {
            'title': 'Jogos',
            'slug': 'jogos',
            'description': 'Quizzes sobre videogames, jogos de tabuleiro e e-sports. De clássicos retrô a lançamentos modernos!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#f472b6',
            'secondary_color': '#ec4899',
            'icon_bg_color_1': '#fce7f3',
            'icon_bg_color_2': '#fbcfe8',
            'order': 3,
        },
        {
            'title': 'Ciência & Tecnologia',
            'slug': 'ciencia-tecnologia',
            'description': 'Explore o universo da ciência, tecnologia e inovação. Física, química, biologia, astronomia e muito mais!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#22d3ee',
            'secondary_color': '#06b6d4',
            'icon_bg_color_1': '#cffafe',
            'icon_bg_color_2': '#a5f3fc',
            'order': 4,
        },
        {
            'title': 'História',
            'slug': 'historia',
            'description': 'Viaje no tempo e teste seus conhecimentos sobre eventos históricos, civilizações antigas e personalidades marcantes!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 5,
        },
        {
            'title': 'Geografia',
            'slug': 'geografia',
            'description': 'Descubra o mundo através de países, capitais, bandeiras, montanhas e oceanos. Teste seu conhecimento global!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#60a5fa',
            'secondary_color': '#3b82f6',
            'icon_bg_color_1': '#dbeafe',
            'icon_bg_color_2': '#bfdbfe',
            'order': 6,
        },
        {
            'title': 'Arte & Cultura',
            'slug': 'arte-cultura',
            'description': 'Mergulhe no mundo das artes visuais, literatura, música clássica e movimentos culturais ao redor do mundo!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#c084fc',
            'secondary_color': '#a855f7',
            'icon_bg_color_1': '#f3e8ff',
            'icon_bg_color_2': '#e9d5ff',
            'order': 7,
        },
        {
            'title': 'Comida & Bebida',
            'slug': 'comida-bebida',
            'description': 'Explore o universo gastronômico! Culinária mundial, ingredientes, receitas e a cultura por trás dos pratos!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#fbbf24',
            'secondary_color': '#f59e0b',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 8,
        },
        {
            'title': 'Natureza & Animais',
            'slug': 'natureza-animais',
            'description': 'Descubra a biodiversidade do planeta! Animais selvagens, ecossistemas, conservação e curiosidades da natureza!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#4ade80',
            'secondary_color': '#22c55e',
            'icon_bg_color_1': '#dcfce7',
            'icon_bg_color_2': '#bbf7d0',
            'order': 9,
        },
        {
            'title': 'Política & Sociedade',
            'slug': 'politica-sociedade',
            'description': 'Entenda o mundo político e social. Governos, sistemas políticos, movimentos sociais e atualidades!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#94a3b8',
            'secondary_color': '#64748b',
            'icon_bg_color_1': '#f1f5f9',
            'icon_bg_color_2': '#e2e8f0',
            'order': 10,
        },
        {
            'title': 'Curiosidades Gerais',
            'slug': 'curiosidades-gerais',
            'description': 'Um pouco de tudo! Fatos curiosos, recordes mundiais, invenções e conhecimentos diversos para testar sua cultura geral!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#fb7185',
            'secondary_color': '#f43f5e',
            'icon_bg_color_1': '#ffe4e6',
            'icon_bg_color_2': '#fecdd3',
            'order': 11,
        },
        {
            'title': 'Celebridades & Personalidades',
            'slug': 'celebridades-personalidades',
            'description': 'Teste seus conhecimentos sobre celebridades, influenciadores, personalidades históricas e figuras públicas!',
            'icon': None,  # Atualize para uma URL de imagem se necessário
            'primary_color': '#fcd34d',
            'secondary_color': '#fbbf24',
            'icon_bg_color_1': '#fef9c3',
            'icon_bg_color_2': '#fef08a',
            'order': 12,
        },
    ]
    
    # Criar os temas
    created_count = 0
    updated_count = 0
    
    for theme_data in root_themes:
        theme, created = Theme.objects.update_or_create(
            slug=theme_data['slug'],
            defaults={
                'title': theme_data['title'],
                'description': theme_data['description'],
                'icon': theme_data['icon'],
                'primary_color': theme_data['primary_color'],
                'secondary_color': theme_data['secondary_color'],
                'icon_bg_color_1': theme_data['icon_bg_color_1'],
                'icon_bg_color_2': theme_data['icon_bg_color_2'],
                'order': theme_data['order'],
                'active': True,
                'parent': None,
            }
        )
        
        if created:
            print(f"✅ Criado: {theme_data['title']}")
            created_count += 1
        else:
            print(f"🔄 Atualizado: {theme_data['title']}")
            updated_count += 1
    
    print(f"\n📊 Resumo:")
    print(f"   Criados: {created_count}")
    print(f"   Atualizados: {updated_count}")
    print(f"   Total: {created_count + updated_count}")
    print(f"\n✨ Setup de temas raiz concluído!")


if __name__ == '__main__':
    run()

