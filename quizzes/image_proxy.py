"""
Módulo para servir imagens de questões com URLs ofuscadas
"""
import hashlib
import hmac
from django.conf import settings
from django.http import HttpResponse, Http404
from django.views.decorators.cache import cache_control
from django.views.decorators.http import require_http_methods
import requests
from urllib.parse import unquote


def generate_image_token(image_url):
    """
    Gera um token seguro para a URL da imagem
    """
    secret_key = getattr(settings, 'SECRET_KEY', 'default-secret-key')
    token = hmac.new(
        secret_key.encode(),
        image_url.encode(),
        hashlib.sha256
    ).hexdigest()
    return token


def verify_image_token(image_url, token):
    """
    Verifica se o token é válido para a URL da imagem
    """
    expected_token = generate_image_token(image_url)
    return hmac.compare_digest(token, expected_token)


@require_http_methods(["GET"])
@cache_control(max_age=3600)  # Cache por 1 hora
def serve_protected_image(request, token, encoded_url):
    """
    Serve uma imagem protegida com token de verificação
    """
    try:
        # Decodificar a URL
        image_url = unquote(encoded_url)
        
        # Verificar o token
        if not verify_image_token(image_url, token):
            raise Http404("Token inválido")
        
        # Fazer requisição para a imagem original
        response = requests.get(image_url, timeout=30)
        response.raise_for_status()
        
        # Criar resposta HTTP
        http_response = HttpResponse(
            response.content,
            content_type=response.headers.get('content-type', 'image/jpeg')
        )
        
        # Adicionar headers de cache
        http_response['Cache-Control'] = 'public, max-age=3600'
        http_response['Expires'] = response.headers.get('expires')
        
        return http_response
        
    except requests.RequestException:
        raise Http404("Imagem não encontrada")
    except Exception:
        raise Http404("Erro ao carregar imagem")


def get_protected_image_url(original_url):
    """
    Retorna uma URL protegida para a imagem original
    """
    if not original_url:
        return None
    
    # Gerar token
    token = generate_image_token(original_url)
    
    # Codificar a URL original
    from urllib.parse import quote
    encoded_url = quote(original_url, safe='')
    
    # Retornar URL protegida
    return f"/protected-image/{token}/{encoded_url}/"
