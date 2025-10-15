# Guia Completo - Quiz de Pokémon Geração 1

Este guia explica como criar um quiz completo de Pokémon usando a [PokéAPI](https://pokeapi.co/).

## 📋 O que será criado

- ✅ Download de **151 Pokémon** da Geração 1 (Bulbasaur até Mew)
- ✅ Imagens oficiais de alta qualidade
- ✅ Quiz com alternativas **similares** (mesmo tipo)
- ✅ Nomes em português
- ✅ Dados completos (tipos, altura, peso, etc.)

## 🚀 Passo a Passo

### Passo 1: Baixar todos os Pokémon da Geração 1

Execute o script de download:

```bash
uv run python download_gen1_pokemon.py
```

**O que este script faz:**
- Busca dados de todos os 151 Pokémon da API
- Baixa as imagens oficiais em alta resolução
- Extrai nomes em português
- Agrupa Pokémon por tipo
- Salva tudo em `pokemon_gen1/`

**Tempo estimado:** ~3-5 minutos (com delay de 0.5s entre requests)

**Resultado:**
```
pokemon_gen1/
├── pokemon_data.json       # Dados de todos os Pokémon
└── images/
    ├── 001_bulbasaur.png
    ├── 002_ivysaur.png
    ├── 003_venusaur.png
    ...
    └── 151_mew.png
```

### Passo 2: Criar o Quiz no Django

Execute o script de criação do quiz:

```bash
uv run python create_pokemon_quiz.py
```

**Interativo:** O script perguntará quantas perguntas você quer (1-151)

**O que este script faz:**
- Cria o tema "Pokémon" no banco
- Cria o quiz "Adivinhe o Pokémon - Geração 1"
- Gera perguntas com 4 alternativas cada
- As alternativas são Pokémon **similares** (mesmo tipo)
- Embaralha as respostas automaticamente

**Exemplo de pergunta gerada:**
```
Pergunta: "Qual é este Pokémon?"
Imagem: Charizard
Opções:
  - Charizard ✅ (correto)
  - Moltres (tipo fogo/voador)
  - Dragonite (tipo dragão/voador)
  - Salamence (tipo dragão/voador)
```

### Passo 3: Copiar imagens para o Django

Copie a pasta de imagens para o diretório static do Django:

```bash
# Criar diretório se não existir
mkdir -p quizzes/static/images/pokemon

# Copiar todas as imagens
cp pokemon_gen1/images/*.png quizzes/static/images/pokemon/
```

### Passo 4: Coletar arquivos estáticos

Execute o collectstatic para que as imagens fiquem disponíveis:

```bash
uv run python manage.py collectstatic --noinput
```

### Passo 5: Testar o Quiz

Acesse no navegador:

```
http://localhost:8000/pokemon/adivinhe-o-pokemon-gen1/
```

## 📊 Estrutura dos Dados

### pokemon_data.json

```json
[
  {
    "id": 25,
    "name": "Pikachu",
    "name_pt": "Pikachu",
    "types": ["electric"],
    "height": 4,
    "weight": 60,
    "image_url": "https://raw.githubusercontent.com/PokeAPI/sprites/...",
    "local_image": "images/025_pikachu.png",
    "evolution_chain_url": "..."
  }
]
```

## 🎮 Customizações

### Alterar número de perguntas

Edite `create_pokemon_quiz.py` e modifique:

```python
create_pokemon_quiz(num_questions=50)  # Padrão: 50
```

### Alterar dificuldade das alternativas

No método `get_similar_pokemon()`, você pode ajustar:

```python
# Mais difícil: só Pokémon do mesmo tipo
exact_matches = [
    p for p in all_pokemon 
    if set(p['types']) == target_types
]

# Mais fácil: Pokémon de qualquer tipo
random.sample(all_pokemon, 3)
```

### Adicionar mais gerações

Modifique `GENERATION_1_COUNT` em `download_gen1_pokemon.py`:

```python
# Geração 2: Pokémon 1-251
GENERATION_1_COUNT = 251

# Geração 3: Pokémon 1-386
GENERATION_1_COUNT = 386
```

## 🔧 Troubleshooting

### Erro: "Module 'requests' not found"

```bash
pip install requests
```

### Imagens não aparecem

Verifique se:
1. As imagens estão em `quizzes/static/images/pokemon/`
2. Executou `collectstatic`
3. O servidor está rodando

### API retorna erro 404

Alguns Pokémon podem não ter imagens. O script ignora automaticamente.

### Quiz aparece vazio

Verifique se executou os dois scripts na ordem:
1. `download_gen1_pokemon.py`
2. `create_pokemon_quiz.py`

## 📈 Estatísticas

- **Total de Pokémon:** 151 (Geração 1)
- **Tipos diferentes:** 15 tipos
- **Tamanho das imagens:** ~50-200 KB cada
- **Tamanho total:** ~15-20 MB

## 🌐 Deploy no Heroku

### 1. Adicionar imagens ao git

```bash
git add quizzes/static/images/pokemon/
git commit -m "Add Pokemon Gen 1 images"
```

### 2. Push para Heroku

```bash
git push heroku main
```

### 3. Criar quiz no Heroku

```bash
# Upload do arquivo de dados
heroku run bash
# Dentro do Heroku:
# Faça upload do pokemon_data.json ou execute o download_gen1_pokemon.py

# Criar o quiz
heroku run python create_pokemon_quiz.py
```

## 📚 Recursos

- **PokéAPI:** https://pokeapi.co/
- **Documentação:** https://pokeapi.co/docs/v2
- **Sprites GitHub:** https://github.com/PokeAPI/sprites

## 🎨 Melhorias Futuras

- [ ] Adicionar modo de jogo por gerações
- [ ] Quiz de tipos de Pokémon
- [ ] Quiz de evoluções
- [ ] Quiz de habilidades
- [ ] Ranking de jogadores
- [ ] Timer para cada pergunta
- [ ] Modo multiplayer

## 📝 Licença

Os dados e imagens de Pokémon são propriedade da Nintendo/Game Freak.  
Este projeto usa a PokéAPI que é uma API pública e gratuita.

---

**Criado com ❤️ usando a PokéAPI**

