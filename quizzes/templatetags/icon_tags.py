from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from quizzes.translations import translate as get_translation

register = template.Library()


@register.simple_tag
def render_icon(theme, css_class=''):
    """
    Renderiza o ícone do tema (PNG, SVG, etc)
    
    Uso nos templates:
    {% load icon_tags %}
    {% render_icon theme 'icon-large' %}
    """
    if theme.icon:
        # Usa a URL do ícone (pode ser PNG, SVG, etc) - preenche todo o container
        return mark_safe(
            f'<img src="{theme.icon}" class="theme-icon theme-icon-image {css_class}" alt="{theme.title}" loading="lazy" style="width: 100%; height: 100%; object-fit: cover;">'
        )
    else:
        # Fallback: ícone placeholder
        return mark_safe(
            f'<span class="theme-icon theme-icon-placeholder {css_class}">📚</span>'
        )


@register.filter
def has_icon(theme):
    """
    Verifica se o tema tem ícone
    
    Uso: {% if theme|has_icon %}
    """
    return bool(theme.icon)


@register.simple_tag(takes_context=True)
def t(context, key, default=None):
    """
    Traduz uma chave usando o idioma do contexto
    
    Uso nos templates:
    {% load icon_tags %}
    {% t 'welcome_title' %}
    """
    language = context.get('current_language', 'pt-BR')
    return get_translation(key, language, default)


@register.filter
def translate(key, language='pt-BR'):
    """
    Filtro para tradução de strings
    
    Uso: {{ 'welcome_title'|translate:current_language }}
    """
    return get_translation(key, language)


@register.filter
def badge_description(badge, language='pt-BR'):
    """
    Retorna a descrição traduzida da badge
    
    Uso: {{ badge|badge_description:current_language }}
    """
    if hasattr(badge, 'get_description'):
        return badge.get_description(language)
    return badge.description if hasattr(badge, 'description') else ''

