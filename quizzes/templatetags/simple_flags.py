"""
Template tags simples para bandeiras estáticas
"""
from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.simple_tag
def country_flag(country_code, size='72x72'):
    """
    Retorna uma tag img com bandeira local
    """
    if not country_code:
        return ""
    
    # Mapeamento de países para códigos de bandeira
    country_flags = {
        'en-US': '1f1fa-1f1f8',  # 🇺🇸
        'en-CA': '1f1e8-1f1e6',  # 🇨🇦
        'es-MX': '1f1f2-1f1fd',  # 🇲🇽
        'en-GB': '1f1ec-1f1e7',  # 🇬🇧
        'de-DE': '1f1e9-1f1ea',  # 🇩🇪
        'fr-FR': '1f1eb-1f1f7',  # 🇫🇷
        'es-ES': '1f1ea-1f1f8',  # 🇪🇸
        'it-IT': '1f1ee-1f1f9',  # 🇮🇹
        'nl-NL': '1f1f3-1f1f1',  # 🇳🇱
        'sv-SE': '1f1f8-1f1ea',  # 🇸🇪
        'no-NO': '1f1f3-1f1f4',  # 🇳🇴
        'pl-PL': '1f1f5-1f1f1',  # 🇵🇱
        'pt-PT': '1f1f5-1f1f9',  # 🇵🇹
        'en-IN': '1f1ee-1f1f3',  # 🇮🇳
        'en-PH': '1f1f5-1f1ed',  # 🇵🇭
        'id-ID': '1f1ee-1f1e9',  # 🇮🇩
        'ja-JP': '1f1ef-1f1f5',  # 🇯🇵
        'ko-KR': '1f1f0-1f1f7',  # 🇰🇷
        'th-TH': '1f1f9-1f1ed',  # 🇹🇭
        'vi-VN': '1f1fb-1f1f3',  # 🇻🇳
        'en-AU': '1f1e6-1f1fa',  # 🇦🇺
        'en-NZ': '1f1f3-1f1ff',  # 🇳🇿
        'pt-BR': '1f1e7-1f1f7',  # 🇧🇷
        'es-AR': '1f1e6-1f1f7',  # 🇦🇷
        'es-CO': '1f1e8-1f1f4',  # 🇨🇴
    }
    
    flag_code = country_flags.get(country_code)
    if not flag_code:
        return ""
    
    # URL local simples
    if size == '72x72':
        local_url = f"/static/quizzes/images/flags/{flag_code}.png"
    else:
        local_url = f"/static/quizzes/images/flags/{size}/{flag_code}.png"
    
    # Extrair dimensões
    width, height = size.split('x')
    
    return mark_safe(f'''
        <img src="{local_url}" 
             alt="{country_code}" 
             width="{width}" 
             height="{height}"
             style="display: inline-block; vertical-align: middle;">
    ''')


@register.simple_tag
def flag_emoji(country_code):
    """
    Retorna o emoji da bandeira diretamente
    """
    if not country_code:
        return ""
    
    # Mapeamento direto para emojis
    flag_emojis = {
        'en-US': '🇺🇸',
        'en-CA': '🇨🇦',
        'es-MX': '🇲🇽',
        'en-GB': '🇬🇧',
        'de-DE': '🇩🇪',
        'fr-FR': '🇫🇷',
        'es-ES': '🇪🇸',
        'it-IT': '🇮🇹',
        'nl-NL': '🇳🇱',
        'sv-SE': '🇸🇪',
        'no-NO': '🇳🇴',
        'pl-PL': '🇵🇱',
        'pt-PT': '🇵🇹',
        'en-IN': '🇮🇳',
        'en-PH': '🇵🇭',
        'id-ID': '🇮🇩',
        'ja-JP': '🇯🇵',
        'ko-KR': '🇰🇷',
        'th-TH': '🇹🇭',
        'vi-VN': '🇻🇳',
        'en-AU': '🇦🇺',
        'en-NZ': '🇳🇿',
        'pt-BR': '🇧🇷',
        'es-AR': '🇦🇷',
        'es-CO': '🇨🇴',
    }
    
    return flag_emojis.get(country_code, '🏳️')
