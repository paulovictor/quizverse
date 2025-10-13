from django import template
from django.utils.safestring import mark_safe
from django.templatetags.static import static

register = template.Library()


@register.simple_tag
def render_icon(theme, css_class=''):
    """
    Renderiza o ícone SVG do tema
    
    Uso nos templates:
    {% load icon_tags %}
    {% render_icon theme 'icon-large' %}
    """
    if theme.icon_svg:
        # Usa SVG
        svg_path = static(f'icons/{theme.icon_svg}.svg')
        return mark_safe(
            f'<img src="{svg_path}" class="theme-icon theme-icon-svg {css_class}" alt="{theme.title}" loading="lazy">'
        )
    else:
        # Fallback: ícone placeholder
        return mark_safe(
            f'<span class="theme-icon theme-icon-placeholder {css_class}">📚</span>'
        )


@register.filter
def has_svg_icon(theme):
    """
    Verifica se o tema tem ícone SVG
    
    Uso: {% if theme|has_svg_icon %}
    """
    return bool(theme.icon_svg)

