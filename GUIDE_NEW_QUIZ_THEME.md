# 📚 Guia Completo: Criando um Novo Tema de Quiz com Imagens

## 🎯 Estrutura Completa (Exemplo: Pokémon)

### ✅ O que foi feito:

1. **Download de Dados e Imagens**
   - Script para baixar dados da API externa (PokeAPI)
   - Script para baixar imagens oficiais
   - Armazenamento local: `pokemon_gen1/pokemon_data.json` e `pokemon_gen1/images/`

2. **Upload para Cloudinary**
   - Upload manual ou via script das imagens para o Cloudinary
   - Organização em pasta (ex: `pokemons/`)

3. **Busca e Otimização de URLs**
   - Script para buscar todas as URLs do Cloudinary
   - Script para adicionar transformações (`w_300,h_300,c_thumb,f_auto`)
   - Arquivo de saída: `cloudinary_pokemon_urls.json`

4. **Criação do Tema**
   - Script: `setup_data/00_root_pokemon_theme.py`
   - Cria tema para todos os 31 países
   - Associa cada tema ao tema pai "Jogos" do respectivo país
   - Define cores, ícone e traduções

5. **Criação dos Quizzes**
   - Script: `setup_data/00_root_pokemon.py`
   - Busca o tema criado anteriormente
   - Cria 151 perguntas (uma por Pokémon)
   - Gera 4 alternativas (1 correta + 3 similares)
   - Estratégia de similaridade: baseada em tipos

6. **Ordem de Execução**
   ```bash
   # 1. Download de dados e imagens
   python download_gen1_pokemon.py
   
   # 2. Upload para Cloudinary (manual ou script)
   # ... upload das imagens ...
   
   # 3. Buscar URLs do Cloudinary
   python get_pokemon_cloudinary_urls.py
   
   # 4. Otimizar URLs
   python update_pokemon_urls_with_transformations.py
   
   # 5. Criar temas
   uv run python setup_data/00_root_pokemon_theme.py
   
   # 6. Criar quizzes
   uv run python setup_data/00_root_pokemon.py
   ```

---

## 🚀 PROMPT IDEAL para Criar um Novo Tema (Ex: Digimon)

```
Preciso criar um sistema completo de quizzes de DIGIMON para minha plataforma Django. 
Siga exatamente a estrutura que usamos para Pokémon:

### CONTEXTO DA PLATAFORMA:
- Django com modelo Theme e Quiz
- **22 países suportados** (definidos em setup_data/00_root_themes.py)
- **IMPORTANTE: Use EXATAMENTE os mesmos países de 00_root_themes.py**
  - Países: en-US, en-CA, en-GB, en-IN, en-PH, en-AU, en-NZ, pt-BR, pt-PT, es-MX, es-ES, es-AR, es-CO, de-DE, fr-FR, it-IT, nl-NL, sv-SE, no-NO, pl-PL, id-ID, ja-JP, ko-KR, th-TH, vi-VN
- **Sufixos de slug:**
  - Brasil (pt-BR): SEM sufixo (ex: `pokemon`)
  - Outros países: usar `.split('-')[1].lower()` (ex: en-US → `-us`, ja-JP → `-jp`, fr-FR → `-fr`)
  - ⚠️ NUNCA usar código completo (enus, jajp) - está ERRADO!
- Cada tema tem um tema pai (parent): Digimon deve ser filho do tema "Jogos" de cada país
- Traduções das slugs dos temas pai estão em: setup_data/00_root_themes.py
  - pt: jogos | en: games | es: juegos | de: spiele | fr: jeux | it: giochi | 
    ja: gemu | ko: geim | pl: gry | sv: spel | no: spill | id: game | th: gem | vi: tro-choi | nl: games

### REQUISITOS:

#### 1. DADOS E IMAGENS
- Baixar dados de todos os Digimon da primeira temporada (Adventure)
- API sugerida: https://digimon-api.vercel.app/api/digimon
- Baixar imagens oficiais de cada Digimon
- Salvar em: digimon_adventure/digimon_data.json e digimon_adventure/images/

#### 2. CLOUDINARY
- Script para buscar URLs de uma pasta do Cloudinary
- Credenciais: CLOUD_NAME, API_KEY, API_SECRET (vou fornecer)
- Script para adicionar transformações: w_300,h_300,c_thumb,f_auto
- Arquivo de saída: cloudinary_digimon_urls.json

#### 3. TEMA DIGIMON
- Script: setup_data/00_root_digimon_theme.py
- Criar tema para TODOS os 31 países
- Associar ao tema pai "Jogos" (traduzido) de cada país
- Imagem do tema: [vou fornecer URL do Cloudinary]
- Cores sugeridas:
  - primary_color: #ff8c00 (Laranja Agumon)
  - secondary_color: #ff6b00
- Traduções em todos os idiomas suportados

#### 4. QUIZZES
- Script: setup_data/00_root_digimon.py
- Um quiz por país (31 total)
- Todas as perguntas (quantos Digimon houver na temporada)
- Para Brasil: slug sem sufixo (ex: adivinhe-o-digimon)
- Outros países: slug com sufixo (ex: guess-the-digimon-us)
- Formato de pergunta: "Qual é este Digimon?" + imagem
- 4 alternativas: 1 correta + 3 similares
- Estratégia de similaridade: [escolha a melhor - pode ser por nível, tipo, etc]
- Explicação: "Este é [nome], um Digimon do tipo [tipo] e nível [nível]"
- Sem aleatoriedades: ordem consistente, apenas embaralhar as 4 alternativas

#### 5. ESTRUTURA DE ARQUIVOS
Crie exatamente estes arquivos:
```
/Users/paulo/work/quiz/
├── download_digimon_adventure.py          # Baixa dados + imagens da API
├── get_digimon_cloudinary_urls.py         # Busca URLs do Cloudinary
├── update_digimon_urls_transformations.py # Adiciona transformações
├── cloudinary_digimon_urls.json           # URLs finais otimizadas
├── digimon_adventure/
│   ├── digimon_data.json                  # Dados de todos os Digimon
│   └── images/                            # Imagens baixadas
└── setup_data/
    ├── 00_root_digimon_theme.py           # Cria temas
    └── 00_root_digimon.py                 # Cria quizzes
```

### DETALHES IMPORTANTES:
- Use `uv run python` para executar scripts Django
- **SEMPRE copie a lista de países de 00_root_themes.py** - NUNCA adicione países extras
- **Sufixos corretos:**
  ```python
  if country_code == 'pt-BR':
      theme_slug = translation['slug']  # SEM sufixo
  else:
      country_suffix = country_code.split('-')[1].lower()  # us, jp, fr, etc
      theme_slug = f"{translation['slug']}-{country_suffix}"
  ```
- **Exemplos de slugs:**
  - pt-BR → `digimon` (sem sufixo)
  - en-US → `digimon-us`
  - ja-JP → `digimon-jp`
  - fr-FR → `digimon-fr`
  - id-ID → `digimon-id`
- **Campo do modelo:**
  - Theme tem campo `icon` (NÃO `image`)
  - Theme tem campo `country` que deve receber o country_code
- Tema deve buscar parent correto: jogos/games/juegos/spiele/jeux/spiel/game etc
- Quiz deve apenas buscar (get) o tema, não criar (get_or_create)
- Ordem de execução: download → upload Cloudinary → buscar URLs → otimizar URLs → 
  criar temas → criar quizzes

### INFORMAÇÕES QUE VOU FORNECER:
- [ ] URL da imagem do tema Digimon no Cloudinary
- [ ] Credenciais do Cloudinary (CLOUD_NAME, API_KEY, API_SECRET)
- [ ] Nome da pasta no Cloudinary (ex: "digimons")

COMECE pela estrutura completa e me pergunte o que falta.
```

---

## 📋 Checklist de Validação

Ao criar um novo tema, verifique:

- [ ] Script de download de dados funciona
- [ ] Script de download de imagens funciona
- [ ] Imagens foram enviadas para o Cloudinary
- [ ] Script de busca de URLs do Cloudinary funciona
- [ ] Script de otimização de URLs funciona
- [ ] Arquivo JSON com URLs otimizadas foi criado
- [ ] Script de tema cria 31 temas (um por país)
- [ ] Cada tema está associado ao tema pai correto (traduzido)
- [ ] Brasil não tem sufixo, outros países têm
- [ ] Script de quiz BUSCA o tema (não cria)
- [ ] Script de quiz cria perguntas para todos os itens
- [ ] Alternativas são similares (estratégia definida)
- [ ] Apenas as 4 alternativas são embaralhadas
- [ ] Traduções em todos os idiomas necessários
- [ ] Cores e ícone do tema definidos
- [ ] Ordem de execução documentada

---

## 🎨 Cores Sugeridas para Outros Temas

### Digimon
- Primary: `#ff8c00` (Laranja Agumon)
- Secondary: `#ff6b00`
- Icon BG 1: `#fff4e6`
- Icon BG 2: `#ffe0b2`

### Yu-Gi-Oh!
- Primary: `#6b46c1` (Roxo)
- Secondary: `#553c9a`
- Icon BG 1: `#f3f0ff`
- Icon BG 2: `#e9d5ff`

### Dragon Ball
- Primary: `#ff9500` (Laranja)
- Secondary: `#ff7b00`
- Icon BG 1: `#fff6e6`
- Icon BG 2: `#ffeacc`

### Naruto
- Primary: `#ff6b35` (Laranja)
- Secondary: `#ff5722`
- Icon BG 1: `#fff3e0`
- Icon BG 2: `#ffe0b2`

---

## 🔧 Troubleshooting Comum

### Erro: "Tema não encontrado"
→ Execute primeiro o script de tema antes do script de quiz

### Erro: "Parent não encontrado"
→ Verifique se os temas pai (Jogos) existem para todos os países

### Erro: "0 recursos encontrados no Cloudinary"
→ Verifique se o nome da pasta está correto
→ Use o script cloudinary_list_folders.py para listar pastas

### Erro: "Slug duplicado"
→ Verifique se está usando .split('-')[1].lower() para sufixos
→ Brasil deve não ter sufixo

---

## 📝 Notas Finais

1. **Sempre use a estrutura em 2 scripts**: tema + quiz
2. **Separação de responsabilidades**: tema cria a estrutura, quiz popula
3. **Parent correto**: cada tema deve ter o pai traduzido
4. **Sem aleatoriedades**: exceto no shuffle das 4 alternativas
5. **Consistência**: use o mesmo padrão de slugs em todos os scripts
6. **Traduções**: garanta todos os idiomas suportados
7. **Cloudinary**: sempre use transformações para otimizar

