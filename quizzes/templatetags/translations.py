from django import template
from quizzes.translations import translate

register = template.Library()

@register.simple_tag(takes_context=True)
def t(context, key):
    """
    Template tag para tradução
    Usage: {% t 'hello' %}
    """
    # Tenta obter o idioma do contexto
    language = context.get('current_language', 'pt-BR')
    
    return translate(key, language)
