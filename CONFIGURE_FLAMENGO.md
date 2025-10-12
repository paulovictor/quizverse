# Configurar Imagem do Flamengo

## Problema
A imagem de fundo do card do Flamengo não está aparecendo porque não foi configurada no banco de dados.

## Solução Rápida (Via Admin Django)

1. **Acesse o admin Django:**
   ```
   http://localhost:8000/admin/quizzes/theme/
   ```

2. **Encontre e edite o tema "Flamengo"**

3. **Na seção "Personalização Visual do Card", configure:**
   - **Card background image**: Cole a URL de uma imagem (opcional)
     - Exemplo: `https://i.imgur.com/URL_DA_IMAGEM.jpg`
   - **Card background color**: 
     ```
     linear-gradient(135deg, #ef4444 0%, #dc2626 100%)
     ```

4. **Salve**

5. **Atualize a página** e o card do Flamengo deve aparecer com fundo vermelho

## Solução via Script Python

Se preferir usar script:

```bash
# Opção 1: Usando python3
python3 configure_flamengo_image.py

# Opção 2: Usando uv
uv run python configure_flamengo_image.py

# Opção 3: Usando manage.py shell
python3 manage.py shell
```

Depois no shell Django:
```python
from quizzes.models import Theme

flamengo = Theme.objects.get(slug='flamengo')
flamengo.card_background_image = None  # ou URL da imagem
flamengo.card_background_color = "linear-gradient(135deg, #ef4444 0%, #dc2626 100%)"
flamengo.save()

print("✅ Flamengo configurado!")
```

## URLs de Imagens Sugeridas

Se quiser usar uma imagem de fundo do Flamengo, faça upload em:
- **ImgBB**: https://imgbb.com/ (recomendado)
- **Imgur**: https://imgur.com/

E cole a URL "Direct Link" no campo **Card background image**.

## Verificar Configuração Atual

```bash
python3 manage.py shell -c "from quizzes.models import Theme; f = Theme.objects.get(slug='flamengo'); print(f'Image: {f.card_background_image}'); print(f'Color: {f.card_background_color}')"
```

