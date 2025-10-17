"""
Template tags para URLs de imagens protegidas
"""
from django import template
from django.utils.safestring import mark_safe
from ..image_proxy import get_protected_image_url

register = template.Library()


@register.simple_tag
def protected_image_url(image_url):
    """
    Retorna uma URL protegida para a imagem
    """
    if not image_url:
        return None
    
    return get_protected_image_url(image_url)


@register.simple_tag
def protected_image_tag(image_url, alt_text="", css_class="", **kwargs):
    """
    Retorna uma tag img com URL protegida
    """
    if not image_url:
        return ""
    
    protected_url = get_protected_image_url(image_url)
    if not protected_url:
        return ""
    
    # Construir atributos
    attrs = []
    if alt_text:
        attrs.append(f'alt="{alt_text}"')
    if css_class:
        attrs.append(f'class="{css_class}"')
    
    # Adicionar atributos extras
    for key, value in kwargs.items():
        if value:
            attrs.append(f'{key}="{value}"')
    
    attrs_str = " ".join(attrs)
    
    return mark_safe(f'<img src="{protected_url}" {attrs_str}>')
