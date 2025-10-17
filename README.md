Passos para criar um Thema (Pokemon) e um Quiz (Qual é este pokemon?) com Imagens.





1 - Fazer upload de todas as imagens das perguntas
>Colocar todas as imagens das perguntas dentro de uma pasta, dentro do setup_upload/ folder
```python 
uv run python upload_cloudinary.py
```

2 - Criar o Theme em todos os paises
```python
uv run python setup/create_theme.py
```

3 - Criar um quiz para o novo theme
```python
uv run python setup/create_quizz.py
```











3 - Generate all questions and answers in all languages
```python
uv run python setup/create_quizz.py
