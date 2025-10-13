# 🎨 Guia de Cores Personalizadas por Categoria

## ✅ Sistema Implementado!

Cada categoria/tema na tela principal agora pode ter suas próprias cores personalizadas!

## 📋 O que você precisa para adicionar uma nova categoria

### 1. **Ícone SVG** 
- 1 arquivo `.svg` em `/quizzes/static/icons/`
- Use `currentColor` para herdar cores do CSS
- Exemplos disponíveis: `trophy`, `soccer`, `gamepad`, `book`, `film`, `music`

### 2. **4 Cores (formato hexadecimal)**

| Campo | O que é | Exemplo |
|-------|---------|---------|
| `primary_color` | Cor principal do gradiente | `#3b82f6` |
| `secondary_color` | Cor secundária do gradiente | `#8b5cf6` |
| `icon_bg_color_1` | Cor 1 do background do ícone | `#dbeafe` |
| `icon_bg_color_2` | Cor 2 do background do ícone | `#e0e7ff` |

### 3. **Textos básicos**
- Título da categoria
- Descrição
- Slug (URL amigável)

## 🚀 Como Adicionar no Django Admin

1. Acesse `/admin/quizzes/theme/add/`

2. **Informações Básicas:**
   - **Title**: Nome da categoria (ex: "Harry Potter")
   - **Slug**: URL amigável (ex: "harrypotter")
   - **Description**: Descrição da categoria
   - **Icon SVG**: Nome do ícone (ex: "book")
   - **Order**: Ordem de exibição (número)
   - **Active**: ✅ Marcado

3. **Cores da Categoria (Home)** - Clique para expandir:
   - **Primary Color**: `#7c3aed` (cor principal)
   - **Secondary Color**: `#c026d3` (cor secundária)
   - **Icon BG Color 1**: `#f3e8ff` (fundo do ícone 1)
   - **Icon BG Color 2**: `#fae8ff` (fundo do ícone 2)

4. Salve!

## 🎨 Paletas de Cores Sugeridas

### 🏆 Esportes / Competição
```
Primary:   #f59e0b (laranja/dourado)
Secondary: #d97706 (laranja escuro)
Icon BG 1: #fef3c7 (amarelo claro)
Icon BG 2: #fed7aa (laranja claro)
```

### ⚽ Futebol / Verde
```
Primary:   #10b981 (verde)
Secondary: #059669 (verde escuro)
Icon BG 1: #d1fae5 (verde claro)
Icon BG 2: #a7f3d0 (verde claro 2)
```

### 🔴 Flamengo / Vermelho
```
Primary:   #dc2626 (vermelho)
Secondary: #b91c1c (vermelho escuro)
Icon BG 1: #fee2e2 (vermelho claro)
Icon BG 2: #fecaca (vermelho claro 2)
```

### 🎮 Games / Roxo
```
Primary:   #8b5cf6 (roxo)
Secondary: #7c3aed (roxo escuro)
Icon BG 1: #ede9fe (roxo claro)
Icon BG 2: #ddd6fe (roxo claro 2)
```

### 📚 Conhecimento / Roxo Magenta
```
Primary:   #7c3aed (roxo vibrante)
Secondary: #c026d3 (magenta)
Icon BG 1: #f3e8ff (roxo claro)
Icon BG 2: #fae8ff (rosa claro)
```

### 💙 Azul / Tecnologia
```
Primary:   #3b82f6 (azul)
Secondary: #2563eb (azul escuro)
Icon BG 1: #dbeafe (azul claro)
Icon BG 2: #bfdbfe (azul claro 2)
```

### 🎬 Filmes / Cinema
```
Primary:   #ec4899 (rosa)
Secondary: #db2777 (rosa escuro)
Icon BG 1: #fce7f3 (rosa claro)
Icon BG 2: #fbcfe8 (rosa claro 2)
```

### 🎵 Música
```
Primary:   #06b6d4 (ciano)
Secondary: #0891b2 (ciano escuro)
Icon BG 1: #cffafe (ciano claro)
Icon BG 2: #a5f3fc (ciano claro 2)
```

## 🛠️ Como Funciona Tecnicamente

O sistema gera CSS dinâmico automaticamente:

```css
/* Para cada tema com cores configuradas */
.category-card[data-theme="harrypotter"]::before {
    background: linear-gradient(135deg, #7c3aed, #c026d3);
}

.category-card[data-theme="harrypotter"]:hover {
    box-shadow: 0 20px 40px #7c3aed33;
    transform: translateY(-8px);
}

.category-card[data-theme="harrypotter"] .card-icon {
    background: linear-gradient(135deg, #f3e8ff, #fae8ff);
}
```

## 🎯 Resultado

✅ Cada categoria tem cores únicas  
✅ Gradientes suaves e profissionais  
✅ Hover com sombra colorida  
✅ Ícone com background personalizado  
✅ Totalmente configurável pelo admin  

## 📱 Recursos para Escolher Cores

- **Tailwind Colors**: https://tailwindcss.com/docs/customizing-colors
- **Coolors**: https://coolors.co/ (gerador de paletas)
- **Adobe Color**: https://color.adobe.com/
- **Paletton**: https://paletton.com/

## 💡 Dicas

1. **Use cores do mesmo "tom"** para primary e secondary
2. **Background do ícone deve ser claro** (10-20% de opacidade da cor principal)
3. **Teste em dispositivos móveis** para garantir legibilidade
4. **Mantenha contraste adequado** entre texto e fundo

## ⚠️ Importante

- Se não configurar cores, o tema usará o estilo padrão
- Use sempre formato hexadecimal: `#RRGGBB`
- As cores afetam apenas a tela inicial (home)
- Cores do card interno usam os campos `card_background_*`

---

**Sistema implementado em:** 2025  
**Status:** ✅ Pronto para produção  
**Temas já configurados:** Esportes, Futebol, Flamengo, Games, Harry Potter

