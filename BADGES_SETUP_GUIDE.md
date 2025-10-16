# 🏆 Guia de Configuração do Sistema de Badges

## 📋 Visão Geral

O sistema de badges foi implementado com sucesso! Agora você pode criar badges personalizadas que os usuários podem conquistar ao completar quizzes.

## 🎯 Conceitos Principais

### 1. **QuizGroup** (Grupo de Quizzes)
- Agrupa quizzes equivalentes em diferentes idiomas
- **Exemplo:** "Pokémon Gen 1" pode ter versões em PT, EN, ES, FR, etc.
- **Importante:** SEMPRE obrigatório para cada quiz

### 2. **Badge** (Insignia)
- Define uma conquista que pode ser obtida
- Possui regras (porcentagem mínima, tempo máximo, etc.)
- Pode ser associada a múltiplos grupos

### 3. **QuizGroupBadge** (Associação)
- Define quais badges estão disponíveis para cada grupo
- Tabela intermediária simples

### 4. **UserBadge** (Conquista)
- Registra quando um usuário conquista uma badge
- **Garantia:** Um usuário só pode conquistar cada badge UMA vez por grupo
- Salva estatísticas (porcentagem, tempo) no momento da conquista

## 🚀 Como Usar

### Passo 1: Criar um QuizGroup

```python
# Via Django Shell (uv run python manage.py shell)
from quizzes.models import QuizGroup, Quiz

# Criar grupo
pokemon_group = QuizGroup.objects.create(
    name='Pokémon Geração 1',
    slug='pokemon-gen1',
    description='Adivinhe os 151 Pokémon originais'
)
```

### Passo 2: Associar Quizzes ao Grupo

```python
# Associar quiz existente ao grupo
quiz_pt = Quiz.objects.get(slug='adivinhe-o-pokemon-geracao-1')
quiz_pt.quiz_group = pokemon_group
quiz_pt.save()

# Se tiver versões em outros idiomas:
# quiz_en = Quiz.objects.get(slug='guess-the-pokemon-gen1')
# quiz_en.quiz_group = pokemon_group
# quiz_en.save()
```

### Passo 3: Criar Badges

```python
from quizzes.models import Badge

# Badge Bronze - 80% ou mais
badge_bronze = Badge.objects.create(
    title='Treinador Pokémon',
    description='Acerte 80% ou mais das questões',
    image='https://res.cloudinary.com/YOUR_CLOUD/badge-bronze.png',
    rule_type='percentage',
    min_percentage=80,
    rarity='common',
    points=10,
    order=1
)

# Badge Prata - 90% ou mais
badge_silver = Badge.objects.create(
    title='Treinador Avançado',
    description='Acerte 90% ou mais das questões',
    image='https://res.cloudinary.com/YOUR_CLOUD/badge-silver.png',
    rule_type='percentage',
    min_percentage=90,
    rarity='rare',
    points=25,
    order=2
)

# Badge Ouro - 100%
badge_gold = Badge.objects.create(
    title='Mestre Pokémon',
    description='Pontuação perfeita!',
    image='https://res.cloudinary.com/YOUR_CLOUD/badge-gold.png',
    rule_type='perfect_score',
    min_percentage=100,
    rarity='epic',
    points=50,
    order=3
)

# Badge Speedrun - 100% em menos de 2 minutos
badge_speedrun = Badge.objects.create(
    title='Speedrunner Pokémon',
    description='100% de acertos em menos de 2 minutos',
    image='https://res.cloudinary.com/YOUR_CLOUD/badge-speedrun.png',
    rule_type='percentage_time',
    min_percentage=100,
    max_time_seconds=120,
    rarity='legendary',
    points=100,
    order=4
)
```

### Passo 4: Associar Badges ao Grupo

```python
from quizzes.models import QuizGroupBadge

# Associar todas as badges ao grupo Pokémon
QuizGroupBadge.objects.create(quiz_group=pokemon_group, badge=badge_bronze)
QuizGroupBadge.objects.create(quiz_group=pokemon_group, badge=badge_silver)
QuizGroupBadge.objects.create(quiz_group=pokemon_group, badge=badge_gold)
QuizGroupBadge.objects.create(quiz_group=pokemon_group, badge=badge_speedrun)
```

## 🎨 Tipos de Regras de Badge

### 1. `percentage` - Porcentagem de Acertos
```python
Badge.objects.create(
    title='Badge Bronze',
    rule_type='percentage',
    min_percentage=80,  # 80% ou mais
)
```

### 2. `percentage_time` - Porcentagem + Tempo Limite
```python
Badge.objects.create(
    title='Badge Speedrun',
    rule_type='percentage_time',
    min_percentage=100,  # 100%
    max_time_seconds=120,  # em até 2 minutos
)
```

### 3. `perfect_score` - Pontuação Perfeita
```python
Badge.objects.create(
    title='Badge Perfeita',
    rule_type='perfect_score',
    min_percentage=100,  # Automaticamente 100%
)
```

### 4. `streak` - Sequência (TODO: implementar)
```python
# Futuro: Para implementar lógica de sequências de acertos
Badge.objects.create(
    title='Badge Streak',
    rule_type='streak',
)
```

## 🏅 Raridades

- **common** (Comum) - Fácil de conseguir
- **rare** (Rara) - Moderadamente difícil
- **epic** (Épica) - Muito difícil
- **legendary** (Lendária) - Extremamente rara

## 💡 Como Funciona Automaticamente

1. **Usuário completa um quiz** → `QuizAttempt` é marcado como completo
2. **View `quiz_result` detecta** → Chama `check_and_award_badges(attempt)`
3. **Sistema verifica:**
   - Quais badges estão disponíveis para o grupo do quiz?
   - Usuário já tem essas badges neste grupo?
   - Usuário atendeu aos critérios (porcentagem, tempo)?
4. **Se sim:** Badge é concedida automaticamente!
5. **No template:** `new_badges` e `show_badge_celebration` ficam disponíveis

## 📊 Acessando Badges no Django Admin

As novas seções foram adicionadas ao admin:

- **/admin/quizzes/quizgroup/** - Gerenciar grupos de quizzes
- **/admin/quizzes/badge/** - Criar e editar badges
- **/admin/quizzes/quizgroupbadge/** - Associar badges a grupos
- **/admin/quizzes/userbadge/** - Ver badges conquistadas (apenas leitura)

## 🔍 Consultando Badges de Usuários

```python
from quizzes.services import (
    get_user_badges_for_group,
    get_user_badge_progress,
    get_user_all_badges
)

# Badges de um usuário em um grupo específico
user_badges = get_user_badges_for_group(user, pokemon_group)

# Progresso do usuário
progress = get_user_badge_progress(user, pokemon_group)
# Retorna: {'total': 4, 'earned': 2, 'percentage': 50.0, 'remaining': 2}

# Todas as badges do usuário (agrupadas)
all_badges = get_user_all_badges(user)
# Retorna: {quiz_group: [user_badges]}
```

## 🎮 Exemplo Completo: Setup para Pokémon

```python
from quizzes.models import QuizGroup, Quiz, Badge, QuizGroupBadge

# 1. Criar grupo
pokemon_group = QuizGroup.objects.create(
    name='Pokémon Geração 1',
    slug='pokemon-gen1',
    description='Os 151 Pokémon originais'
)

# 2. Associar quizzes existentes
Quiz.objects.filter(slug__in=[
    'adivinhe-o-pokemon-geracao-1',  # PT-BR
    # Adicionar mais quando criar versões em outros idiomas
]).update(quiz_group=pokemon_group)

# 3. Criar badges
badges_data = [
    {
        'title': '⭐ Treinador Iniciante',
        'description': 'Acerte 50% ou mais',
        'rule_type': 'percentage',
        'min_percentage': 50,
        'rarity': 'common',
        'points': 5,
    },
    {
        'title': '🥉 Treinador Bronze',
        'description': 'Acerte 80% ou mais',
        'rule_type': 'percentage',
        'min_percentage': 80,
        'rarity': 'common',
        'points': 10,
    },
    {
        'title': '🥈 Treinador Prata',
        'description': 'Acerte 90% ou mais',
        'rule_type': 'percentage',
        'min_percentage': 90,
        'rarity': 'rare',
        'points': 25,
    },
    {
        'title': '🥇 Mestre Pokémon',
        'description': 'Pontuação perfeita!',
        'rule_type': 'perfect_score',
        'min_percentage': 100,
        'rarity': 'epic',
        'points': 50,
    },
    {
        'title': '⚡ Speedrunner Pokémon',
        'description': '100% em menos de 3 minutos',
        'rule_type': 'percentage_time',
        'min_percentage': 100,
        'max_time_seconds': 180,
        'rarity': 'legendary',
        'points': 100,
    },
]

for i, badge_data in enumerate(badges_data):
    badge = Badge.objects.create(
        image='https://via.placeholder.com/200',  # Trocar por imagem real
        order=i,
        **badge_data
    )
    # Associar ao grupo
    QuizGroupBadge.objects.create(quiz_group=pokemon_group, badge=badge)
    print(f"✅ Badge criada: {badge.title}")

print(f"\n🎉 Setup completo! {len(badges_data)} badges criadas para {pokemon_group.name}")
```

## 📝 Próximos Passos

1. **Criar grupos para seus quizzes existentes**
2. **Criar badges com imagens no Cloudinary**
3. **Associar badges aos grupos**
4. **Testar completando quizzes para ganhar badges**
5. **Criar interface no frontend para exibir badges** (opcional)

## ⚠️ Importante

- **Sempre crie um QuizGroup** antes de associar badges
- **Use `uv run python manage.py shell`** para executar scripts
- **Badges são conquistadas automaticamente** ao completar quizzes
- **Usuários anônimos NÃO ganham badges** (apenas logados)
- **Cada badge só pode ser ganha UMA vez por grupo**

## 🐛 Troubleshooting

### "Badge não está disponível para o grupo"
→ Certifique-se de criar um `QuizGroupBadge` associando a badge ao grupo

### "Badges não aparecem no resultado"
→ Verifique se:
1. Usuário está logado
2. Quiz tem um `quiz_group` associado
3. Existe `QuizGroupBadge` para esse grupo
4. Usuário ainda não tem essa badge nesse grupo

### "Como ver badges de um usuário?"
→ Use `get_user_all_badges(user)` ou acesse `/admin/quizzes/userbadge/`

---

🎉 **Sistema de Badges Implementado com Sucesso!**

