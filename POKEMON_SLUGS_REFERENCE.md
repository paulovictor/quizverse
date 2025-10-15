# 📋 Referência Completa: Slugs dos Temas Pokémon por País

## 🌍 22 Países Suportados

| # | País | Código | Idioma | Tema Pokémon | Tema Pai (Jogos) | Country Field |
|---|------|--------|--------|--------------|------------------|---------------|
| 1 | 🇺🇸 Estados Unidos | en-US | Inglês | `pokemon-us` | `games-us` | en-US |
| 2 | 🇨🇦 Canadá | en-CA | Inglês | `pokemon-ca` | `games-ca` | en-CA |
| 3 | 🇬🇧 Reino Unido | en-GB | Inglês | `pokemon-gb` | `games-gb` | en-GB |
| 4 | 🇮🇳 Índia | en-IN | Inglês | `pokemon-in` | `games-in` | en-IN |
| 5 | 🇵🇭 Filipinas | en-PH | Inglês | `pokemon-ph` | `games-ph` | en-PH |
| 6 | 🇦🇺 Austrália | en-AU | Inglês | `pokemon-au` | `games-au` | en-AU |
| 7 | 🇳🇿 Nova Zelândia | en-NZ | Inglês | `pokemon-nz` | `games-nz` | en-NZ |
| 8 | 🇧🇷 **Brasil** | pt-BR | Português | **`pokemon`** | **`jogos`** | pt-BR |
| 9 | 🇵🇹 Portugal | pt-PT | Português | `pokemon-pt` | `jogos-pt` | pt-PT |
| 10 | 🇲🇽 México | es-MX | Espanhol | `pokemon-mx` | `juegos-mx` | es-MX |
| 11 | 🇪🇸 Espanha | es-ES | Espanhol | `pokemon-es` | `juegos-es` | es-ES |
| 12 | 🇦🇷 Argentina | es-AR | Espanhol | `pokemon-ar` | `juegos-ar` | es-AR |
| 13 | 🇨🇴 Colômbia | es-CO | Espanhol | `pokemon-co` | `juegos-co` | es-CO |
| 14 | 🇩🇪 Alemanha | de-DE | Alemão | `pokemon-de` | `spiele-de` | de-DE |
| 15 | 🇫🇷 França | fr-FR | Francês | `pokemon-fr` | `jeux-fr` | fr-FR |
| 16 | 🇮🇹 Itália | it-IT | Italiano | `pokemon-it` | `giochi-it` | it-IT |
| 17 | 🇳🇱 Holanda | nl-NL | Holandês | `pokemon-nl` | `games-nl` | nl-NL |
| 18 | 🇸🇪 Suécia | sv-SE | Sueco | `pokemon-se` | `spel-se` | sv-SE |
| 19 | 🇳🇴 Noruega | no-NO | Norueguês | `pokemon-no` | `spill-no` | no-NO |
| 20 | 🇵🇱 Polônia | pl-PL | Polonês | `pokemon-pl` | `gry-pl` | pl-PL |
| 21 | 🇮🇩 Indonésia | id-ID | Indonésio | `pokemon-id` | `game-id` | id-ID |
| 22 | 🇯🇵 Japão | ja-JP | Japonês | `pokemon-jp` | `gemu-jp` | ja-JP |
| 23 | 🇰🇷 Coreia do Sul | ko-KR | Coreano | `pokemon-kr` | `geim-kr` | ko-KR |
| 24 | 🇹🇭 Tailândia | th-TH | Tailandês | `pokemon-th` | `gem-th` | th-TH |
| 25 | 🇻🇳 Vietnã | vi-VN | Vietnamita | `pokemon-vn` | `tro-choi-vn` | vi-VN |

---

## 🔍 Padrão de Slugs

### Brasil (Único sem sufixo):
```
Código: pt-BR
Slug Pokémon: pokemon
Slug Jogos: jogos
```

### Todos os outros países:
```
Formato: {slug_base}-{segunda_parte_do_código}

Exemplos:
- en-US → pokemon-us, games-us
- ja-JP → pokemon-jp, gemu-jp  
- fr-FR → pokemon-fr, jeux-fr
- id-ID → pokemon-id, game-id
```

### Lógica em Python:
```python
if country_code == 'pt-BR':
    theme_slug = 'pokemon'
    parent_slug = 'jogos'
else:
    country_suffix = country_code.split('-')[1].lower()
    theme_slug = f"pokemon-{country_suffix}"
    parent_slug = f"{parent_translation_slug}-{country_suffix}"
```

---

## 📝 Traduções da Palavra "Jogos"

| Idioma | Slug do Tema Pai |
|--------|------------------|
| 🇵🇹 Português | `jogos` |
| 🇬🇧 Inglês | `games` |
| 🇪🇸 Espanhol | `juegos` |
| 🇩🇪 Alemão | `spiele` |
| 🇫🇷 Francês | `jeux` |
| 🇮🇹 Italiano | `giochi` |
| 🇳🇱 Holandês | `games` |
| 🇸🇪 Sueco | `spel` |
| 🇳🇴 Norueguês | `spill` |
| 🇵🇱 Polonês | `gry` |
| 🇮🇩 Indonésio | `game` |
| 🇯🇵 Japonês | `gemu` |
| 🇰🇷 Coreano | `geim` |
| 🇹🇭 Tailandês | `gem` |
| 🇻🇳 Vietnamita | `tro-choi` |

---

## ⚠️ Países NÃO Incluídos (para evitar conflitos)

Estes países **NÃO** devem ser adicionados pois causariam slugs duplicadas:

| País Extra | Código | Problema |
|------------|--------|----------|
| 🇨🇦 Canadá (Francês) | fr-CA | Conflita com en-CA → ambos geram `-ca` |
| 🇮🇳 Índia (Hindi) | hi-IN | Conflita com en-IN → ambos geram `-in` |
| 🇨🇳 China | zh-CN | Tema "Jogos" não existe para este país |
| 🇸🇦 Arábia Saudita | ar-SA | Tema "Jogos" não existe para este país |
| 🇷🇺 Rússia | ru-RU | Tema "Jogos" não existe para este país |
| 🇹🇷 Turquia | tr-TR | Tema "Jogos" não existe para este país |

---

## 🎯 Estrutura Hierárquica

```
🎮 Jogos (Root Theme)
    ├── 🇧🇷 jogos (pt-BR)
    │   └── pokemon
    │
    ├── 🇺🇸 games-us (en-US)
    │   └── pokemon-us
    │
    ├── 🇯🇵 gemu-jp (ja-JP)
    │   └── pokemon-jp
    │
    ├── 🇫🇷 jeux-fr (fr-FR)
    │   └── pokemon-fr
    │
    └── ... (todos os 22 países)
```

---

## 🔗 URLs Finais na Aplicação

Assumindo que a URL base é `/themes/`:

- Brasil: `/themes/pokemon/`
- EUA: `/themes/pokemon-us/`
- Japão: `/themes/pokemon-jp/`
- França: `/themes/pokemon-fr/`
- Indonésia: `/themes/pokemon-id/`

E os quizzes (assumindo `/quiz/`):

- Brasil: `/quiz/adivinhe-o-pokemon-gen1/`
- EUA: `/quiz/guess-the-pokemon-gen1-us/`
- Japão: `/quiz/guess-the-pokemon-gen1-jp/`
- França: `/quiz/guess-the-pokemon-gen1-fr/`

---

## ✅ Validação

Total de temas a criar: **22**
Total de quizzes a criar: **22**
Total de perguntas por quiz: **151**
**Total de perguntas no sistema: 3.322**

