"""
Setup Sports Subcategories
Cria as 14 subcategorias de esportes com cores e ícones personalizados
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
    """Cria as subcategorias de esportes"""
    print("⚽ Criando subcategorias de Esportes...\n")
    
    # Buscar tema pai (Esportes)
    try:
        parent_theme = Theme.objects.get(slug='esportes')
        print(f"✅ Tema pai encontrado: {parent_theme.title}\n")
    except Theme.DoesNotExist:
        print("❌ Erro: Tema 'Esportes' não encontrado!")
        print("   Execute primeiro: python setup_data/01_setup_root_themes.py")
        return
    
    # Dados das subcategorias
    sports_subcategories = [
        {
            'title': 'Futebol',
            'slug': 'futebol',
            'description': 'O esporte mais popular do mundo! Teste seus conhecimentos sobre times, jogadores, campeonatos, regras e história do futebol.',
            'icon': 'football',
            'primary_color': '#10b981',
            'secondary_color': '#059669',
            'icon_bg_color_1': '#d1fae5',
            'icon_bg_color_2': '#a7f3d0',
            'order': 1,
        },
        {
            'title': 'Basquete',
            'slug': 'basquete',
            'description': 'NBA, basquete internacional e muito mais! Teste seus conhecimentos sobre jogadores lendários, times e regras do basquete.',
            'icon': 'basketball',
            'primary_color': '#f97316',
            'secondary_color': '#ea580c',
            'icon_bg_color_1': '#ffedd5',
            'icon_bg_color_2': '#fed7aa',
            'order': 2,
        },
        {
            'title': 'Tênis',
            'slug': 'tenis',
            'description': 'Grand Slams, tenistas lendários e recordes! Descubra tudo sobre o mundo do tênis profissional e suas estrelas.',
            'icon': 'tennis',
            'primary_color': '#84cc16',
            'secondary_color': '#65a30d',
            'icon_bg_color_1': '#ecfccb',
            'icon_bg_color_2': '#d9f99d',
            'order': 3,
        },
        {
            'title': 'Vôlei',
            'slug': 'volei',
            'description': 'Vôlei de quadra, vôlei de praia e competições internacionais! Teste seus conhecimentos sobre regras, jogadores e táticas.',
            'icon': 'volleyball',
            'primary_color': '#06b6d4',
            'secondary_color': '#0891b2',
            'icon_bg_color_1': '#cffafe',
            'icon_bg_color_2': '#a5f3fc',
            'order': 4,
        },
        {
            'title': 'Futebol Americano',
            'slug': 'futebol-americano',
            'description': 'NFL, Super Bowl e o esporte mais popular dos EUA! Teste seus conhecimentos sobre times, jogadores e regras complexas.',
            'icon': 'american-football',
            'primary_color': '#7c3aed',
            'secondary_color': '#6d28d9',
            'icon_bg_color_1': '#ede9fe',
            'icon_bg_color_2': '#ddd6fe',
            'order': 5,
        },
        {
            'title': 'Beisebol',
            'slug': 'beisebol',
            'description': 'MLB, World Series e o passatempo americano! Descubra tudo sobre times históricos, jogadores lendários e recordes.',
            'icon': 'baseball',
            'primary_color': '#dc2626',
            'secondary_color': '#b91c1c',
            'icon_bg_color_1': '#fee2e2',
            'icon_bg_color_2': '#fecaca',
            'order': 6,
        },
        {
            'title': 'Rugby',
            'slug': 'rugby',
            'description': 'Copa do Mundo de Rugby, Six Nations e mais! Teste seus conhecimentos sobre o esporte de contato mais intenso.',
            'icon': 'rugby',
            'primary_color': '#15803d',
            'secondary_color': '#166534',
            'icon_bg_color_1': '#dcfce7',
            'icon_bg_color_2': '#bbf7d0',
            'order': 7,
        },
        {
            'title': 'Fórmula 1',
            'slug': 'formula-1',
            'description': 'Pilotos, equipes, circuitos e a história da categoria máxima do automobilismo! Acelere seus conhecimentos sobre F1.',
            'icon': 'formula1',
            'primary_color': '#ef4444',
            'secondary_color': '#dc2626',
            'icon_bg_color_1': '#fee2e2',
            'icon_bg_color_2': '#fecaca',
            'order': 8,
        },
        {
            'title': 'Artes Marciais',
            'slug': 'artes-marciais',
            'description': 'MMA, boxe, judô, jiu-jitsu, karatê e mais! Teste seus conhecimentos sobre lutadores, técnicas e competições de lutas.',
            'icon': 'martial-arts',
            'primary_color': '#dc2626',
            'secondary_color': '#991b1b',
            'icon_bg_color_1': '#fee2e2',
            'icon_bg_color_2': '#fecaca',
            'order': 9,
        },
        {
            'title': 'Skate',
            'slug': 'skate',
            'description': 'Manobras, skatistas lendários, competições e a cultura do skate! De street ao vert, teste seu conhecimento sobre o esporte.',
            'icon': 'skateboard',
            'primary_color': '#8b5cf6',
            'secondary_color': '#7c3aed',
            'icon_bg_color_1': '#ede9fe',
            'icon_bg_color_2': '#ddd6fe',
            'order': 10,
        },
        {
            'title': 'Surf',
            'slug': 'surf',
            'description': 'Campeonatos mundiais, ondas lendárias e surfistas icônicos! Teste seus conhecimentos sobre o esporte das ondas.',
            'icon': 'surf',
            'primary_color': '#0ea5e9',
            'secondary_color': '#0284c7',
            'icon_bg_color_1': '#e0f2fe',
            'icon_bg_color_2': '#bae6fd',
            'order': 11,
        },
        {
            'title': 'Esportes de Inverno',
            'slug': 'esportes-inverno',
            'description': 'Esqui, snowboard, Jogos Olímpicos de Inverno e mais! Teste seus conhecimentos sobre os esportes na neve e no gelo.',
            'icon': 'winter-sports',
            'primary_color': '#60a5fa',
            'secondary_color': '#3b82f6',
            'icon_bg_color_1': '#dbeafe',
            'icon_bg_color_2': '#bfdbfe',
            'order': 12,
        },
        {
            'title': 'Esportes Radicais',
            'slug': 'esportes-radicais',
            'description': 'Escalada, paraquedismo, base jump, parkour e mais! Teste seus conhecimentos sobre os esportes mais emocionantes.',
            'icon': 'extreme-sports',
            'primary_color': '#f59e0b',
            'secondary_color': '#d97706',
            'icon_bg_color_1': '#fef3c7',
            'icon_bg_color_2': '#fde68a',
            'order': 13,
        },
    ]
    
    # Criar as subcategorias
    created_count = 0
    updated_count = 0
    
    for sport_data in sports_subcategories:
        theme, created = Theme.objects.update_or_create(
            slug=sport_data['slug'],
            defaults={
                'title': sport_data['title'],
                'description': sport_data['description'],
                'icon': sport_data['icon'],
                'primary_color': sport_data['primary_color'],
                'secondary_color': sport_data['secondary_color'],
                'icon_bg_color_1': sport_data['icon_bg_color_1'],
                'icon_bg_color_2': sport_data['icon_bg_color_2'],
                'order': sport_data['order'],
                'active': True,
                'parent': parent_theme,  # Associa ao tema Esportes
            }
        )
        
        if created:
            print(f"✅ Criado: {sport_data['title']}")
            created_count += 1
        else:
            print(f"🔄 Atualizado: {sport_data['title']}")
            updated_count += 1
    
    print(f"\n📊 Resumo:")
    print(f"   Tema pai: {parent_theme.title}")
    print(f"   Criadas: {created_count} subcategorias")
    print(f"   Atualizadas: {updated_count} subcategorias")
    print(f"   Total: {created_count + updated_count} subcategorias")
    print(f"\n✨ Setup de subcategorias de Esportes concluído!")


if __name__ == '__main__':
    run()

