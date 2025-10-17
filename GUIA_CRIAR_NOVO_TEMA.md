# Guia para Criar um Novo Script de Tema (Estilo Pokémon)

Este guia detalha TODAS as informações necessárias para criar um novo script de setup de tema, como `02_naruto.py`, baseado no modelo do `01_pokemon.py`.

## 📋 Pré-requisitos

1. **Temas raiz criados**: Execute `00_root_themes.py` antes
2. **Dados do tema**: Arquivo JSON com os dados do novo tema
3. **Imagens**: URLs do Cloudinary ou caminhos locais

---

## 🎯 Estrutura do Script

O script é dividido em **4 etapas principais**:

1. **Criar Temas** (para todos os países)
2. **Criar QuizGroup**
3. **Criar Quizzes com Questões**
4. **Criar Badges**

---

## 📊 Dados Necessários

### 1. DADOS DO ARQUIVO JSON

Crie um arquivo JSON (ex: `naruto_data.json`) com a seguinte estrutura para cada item:

```json
[
  {
    "id": 1,
    "name": "Nome Original (inglês)",
    "name_pt": "Nome em Português",
    "types": ["tipo1", "tipo2"],
    "imagem_url": "url_da_imagem" // opcional
  }
]
```

**Campos obrigatórios:**
- `id` (número único)
- `name` (string - nome original)
- `name_pt` (string - nome traduzido)
- `types` (array - características/categorias do item)

### 2. INFORMAÇÕES DO TEMA

#### 2.1 Metadados Básicos do Tema

```python
# Imagem do tema (URL do Cloudinary)
theme_image = 'https://res.cloudinary.com/...'

# Cores do tema (obrigatório para todos)
colors = {
    'primary_color': '#XXXXXX',      # Cor principal
    'secondary_color': '#XXXXXX',    # Cor secundária
    'icon_bg_color_1': '#XXXXXX',    # Cor de fundo 1 do ícone
    'icon_bg_color_2': '#XXXXXX',    # Cor de fundo 2 do ícone
}
```

#### 2.2 Traduções do Tema (para TODOS os idiomas)

Para cada idioma, forneça:

```python
translations = {
    'pt': {
        'title': 'Nome do Tema',
        'slug': 'slug-do-tema',
        'description': 'Descrição do tema em português',
        'parent_slug': 'jogos',  # slug do tema pai
    },
    'en': { ... },
    'es': { ... },
    # ... repetir para todos os idiomas
}
```

**Idiomas obrigatórios:**
- `pt`, `en`, `es`, `fr`, `de`, `it`, `nl`, `sv`, `no`, `pl`, `id`, `ja`, `ko`, `th`, `vi`

**Slugs dos temas pai por idioma:**
- PT: `jogos`
- EN: `games`
- ES: `juegos`
- FR: `jeux`
- DE: `spiele`
- IT: `giochi`
- NL: `games`
- PL: `gry`
- SV: `spel`
- NO: `spill`
- ID: `game`
- JA: `gemu`
- KO: `geim`
- TH: `gem`
- VI: `tro-choi`

### 3. INFORMAÇÕES DO QUIZGROUP

```python
quiz_group_data = {
    'slug': 'nome-tema-identificador',  # Ex: 'naruto-characters'
    'name': 'Nome Descritivo do Grupo',
    'description': 'Descrição do grupo de quizzes',
    'difficulty': 'easy|medium|hard',
    'order': 0,  # ordem de exibição
}
```

### 4. INFORMAÇÕES DOS QUIZZES

#### 4.1 Traduções dos Quizzes

Para cada idioma, forneça:

```python
quiz_translations = {
    'en': {
        'title': 'Título do Quiz',
        'question_text': 'Texto da pergunta?',  # Ex: "Qual personagem é este?"
        'explanation_template': 'Template da explicação com {placeholders}'
        # Ex: "Este é {name}, um {types}"
    },
    # ... repetir para todos os idiomas
}
```

#### 4.2 Templates de Descrição do Quiz

Para cada idioma:

```python
description_templates = {
    'en': 'Identify {sample_size} random items from the {total} original ones!',
    'pt': 'Identifique {sample_size} itens aleatórios dos {total} originais!',
    # ... repetir para todos os idiomas
}
```

**Placeholders disponíveis:**
- `{sample_size}`: número de questões no quiz
- `{total}`: número total de itens disponíveis

#### 4.3 Configuração do Quiz

```python
num_questions = 151  # Total de questões a criar
difficulty = 'medium'  # easy, medium ou hard
order = 1  # ordem de exibição
```

### 5. LÓGICA DE ALTERNATIVAS INCORRETAS

Defina como gerar alternativas similares para cada questão. No exemplo do Pokémon:

1. **Prioridade 1**: Itens com tipos exatamente iguais
2. **Prioridade 2**: Itens com pelo menos um tipo em comum
3. **Prioridade 3**: Itens próximos por ID

Adapte conforme seu tema. A função `get_similar_pokemon()` deve ser renomeada e ajustada.

### 6. INFORMAÇÕES DAS BADGES

Para cada badge, forneça:

#### 6.1 Dados da Badge

```python
badges_data = [
    {
        'title': 'Nome da Badge',  # Ex: '🟠 Amber Pikachu'
        'description': 'Descrição em PT-BR',
        'description_translations': {
            'pt-BR': 'Descrição PT-BR',
            'en-US': 'Description EN-US',
            # ... TODOS os países
        },
        'image': 'https://res.cloudinary.com/...url_imagem',
        'rule_type': 'perfect_score|percentage_time',
        'min_percentage': 100.0,  # porcentagem mínima de acerto
        'max_time_seconds': 1500,  # tempo máximo em segundos (None se não aplicar)
        'rarity': 'common|rare|epic|legendary',
        'points': 150,  # pontos concedidos
        'order': 1,  # ordem de exibição
    },
]
```

#### 6.2 Traduções das Descrições das Badges

Para CADA badge, crie um dicionário com traduções para TODOS os países:

```python
badge_descriptions = {
    'nome_badge': {
        'pt-BR': 'Descrição em português',
        'en-US': 'Description in English',
        'en-CA': 'Description in English',
        'en-GB': 'Description in English',
        
    },
}
```

**Países obrigatórios para badges:**
- pt-BR, pt-PT
- en-US, en-CA, en-GB, en-IN, en-PH, en-AU, en-NZ
- es-MX, es-ES, es-AR, es-CO
- de-DE, fr-FR, it-IT, nl-NL
- sv-SE, no-NO, pl-PL, id-ID
- ja-JP, ko-KR, th-TH, vi-VN

#### 6.3 Tipos de Regras de Badge

**`perfect_score`**: Badge por pontuação perfeita
- `min_percentage`: 100.0
- `max_time_seconds`: None

**`percentage_time`**: Badge por pontuação + tempo
- `min_percentage`: porcentagem mínima (ex: 100.0)
- `max_time_seconds`: tempo máximo em segundos

### 7. MAPEAMENTO PAÍS → IDIOMA

Este mapeamento já está definido e deve ser mantido:

```python
country_to_lang = {
    'en-US': 'en', 'en-CA': 'en', 'en-GB': 'en', 'en-IN': 'en',
    'en-PH': 'en', 'en-AU': 'en', 'en-NZ': 'en',
    'pt-BR': 'pt', 'pt-PT': 'pt',
    'es-MX': 'es', 'es-ES': 'es', 'es-AR': 'es', 'es-CO': 'es',
    'de-DE': 'de', 'fr-FR': 'fr', 'it-IT': 'it', 'nl-NL': 'nl',
    'sv-SE': 'sv', 'no-NO': 'no', 'pl-PL': 'pl', 'id-ID': 'id',
    'ja-JP': 'ja', 'ko-KR': 'ko', 'th-TH': 'th', 'vi-VN': 'vi',
}
```

---

## 🔧 Modificações Necessárias no Código

### 1. Nome do Arquivo de Dados

Altere a linha:
```python
data_file = Path(project_root) / 'naruto_data' / 'naruto_data.json'
```

### 2. Nome do Arquivo de URLs do Cloudinary (opcional)

Se usar Cloudinary:
```python
cloudinary_file = Path(project_root) / 'cloudinary_naruto_urls.json'
```

### 3. Slug do QuizGroup

```python
quiz_group, created = QuizGroup.objects.update_or_create(
    slug='naruto-characters',  # ALTERAR AQUI
    defaults={...}
)
```

### 4. Slugs dos Temas e Quizzes

Para PT-BR (tema raiz):
```python
theme_slug = 'naruto'  # slug base do tema
quiz_slug = 'adivinhe-personagem-naruto'  # slug base do quiz em PT
```

Para outros idiomas:
```python
theme_slug = f'naruto-{country_suffix}'  # ex: naruto-us
quiz_slug = f'guess-naruto-character-{country_suffix}'  # ex: guess-naruto-character-us
```

---

## 📝 Checklist de Criação

- [ ] Criar arquivo JSON com dados (mínimo: id, name, name_pt, types)
- [ ] Definir cores do tema (4 cores em hex)
- [ ] URL da imagem do tema (Cloudinary)
- [ ] Traduções do tema para 15 idiomas
- [ ] Traduções do quiz para 15 idiomas
- [ ] Templates de descrição para 15 idiomas
- [ ] Definir lógica de alternativas similares
- [ ] Criar 3-5 badges com imagens
- [ ] Traduções das badges para 25 países
- [ ] Definir regras de conquista das badges
- [ ] Ajustar slugs no código
- [ ] Atualizar referências de arquivos

---

## 🎯 Exemplo Resumido: Naruto

### Dados Mínimos Necessários:

1. **JSON**: `naruto_data.json` com ~100 personagens
2. **Tema**:
   - Imagem: URL do Cloudinary
   - Cores: 4 cores em hex
   - 15 traduções (título, descrição, slug)

3. **Quiz**:
   - 15 traduções (título, pergunta, explicação)
   - 15 templates de descrição

4. **Badges** (exemplo: 5 badges):
   - 5 imagens (URLs Cloudinary)
   - 5 títulos únicos
   - 5 × 26 traduções de descrição
   - 5 regras (tipo, porcentagem, tempo)

5. **Código**:
   - Slug do QuizGroup: `'naruto-characters'`
   - Slug base do tema: `'naruto'`
   - Slug base do quiz PT: `'adivinhe-personagem-naruto'`
   - Slug base do quiz EN: `'guess-naruto-character'`

---

## ⚠️ Pontos de Atenção

1. **Todos os idiomas são obrigatórios** - não pule nenhum
2. **Badges precisam de 26 traduções** - uma para cada país
3. **Slugs devem ser únicos** - não conflitar com outros temas
4. **Ordem dos badges** - define a ordem de exibição
5. **Tipos de regras** - `perfect_score` ou `percentage_time`
6. **Imagens** - usar sempre URLs do Cloudinary ou caminhos relativos válidos

---

## 🚀 Execução

Após criar o arquivo `02_naruto.py`:

```bash
python setup_data/02_naruto.py
```

O script criará automaticamente:
- Temas em 25 países
- 1 QuizGroup
- Quizzes em 25 países
- Questões com alternativas
- Badges associadas ao QuizGroup
