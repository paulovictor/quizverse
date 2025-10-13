# 📦 Setup Data - Dados Iniciais do Sistema

Este diretório contém scripts para popular o banco de dados com dados iniciais essenciais.

## 🎯 Objetivo

Fornecer uma forma organizada e repetível de criar dados iniciais no banco, útil para:
- Reset completo do banco de dados
- Ambiente de desenvolvimento
- Testes
- Deploy inicial em produção

## 📂 Estrutura

```
setup_data/
├── __init__.py                    # Package marker
├── README.md                      # Este arquivo
├── run_all.py                     # Executa todos os scripts em ordem
├── 01_setup_root_themes.py        # Cria os 12 temas raiz
└── ... (adicione mais scripts conforme necessário)
```

## 🚀 Como Usar

### Opção 1: Executar todos os scripts

```bash
# No diretório raiz do projeto
python setup_data/run_all.py
```

### Opção 2: Executar um script específico

```bash
# Executar apenas o setup de temas raiz
python setup_data/01_setup_root_themes.py
```

### Opção 3: Via Django shell

```python
python manage.py shell

# Dentro do shell
from setup_data import setup_root_themes
setup_root_themes.run()
```

## 🔄 Workflow Completo de Reset

Para fazer um reset completo do banco e recriar tudo:

```bash
# 1. Deletar o banco de dados (SQLite)
rm db.sqlite3

# 2. Recriar as migrations
python manage.py migrate

# 3. Criar superuser (opcional)
python manage.py createsuperuser

# 4. Popular com dados iniciais
python setup_data/run_all.py

# 5. (Opcional) Coletar arquivos estáticos
python manage.py collectstatic --noinput
```

## 📋 Scripts Disponíveis

### 01_setup_root_themes.py

**O que faz:**
- Cria os 12 temas raiz (categorias principais)
- Configura cores personalizadas para cada tema
- Define ícones SVG para cada categoria

**Temas criados:**
1. Esportes
2. Entretenimento & Mídia
3. Jogos
4. Ciência & Tecnologia
5. História
6. Geografia
7. Arte & Cultura
8. Comida & Bebida
9. Natureza & Animais
10. Política & Sociedade
11. Curiosidades Gerais
12. Celebridades & Personalidades

**Uso individual:**
```bash
uv run python setup_data/01_setup_root_themes.py
```

### 02_setup_sports_subcategories.py

**O que faz:**
- Cria 14 subcategorias para o tema "Esportes"
- Configura cores personalizadas e ícones SVG para cada esporte
- Associa todas as subcategorias ao tema pai "Esportes"

**Subcategorias criadas:**
1. Futebol ⚽
2. Basquete 🏀
3. Tênis 🎾
4. Vôlei 🏐
5. Futebol Americano 🏈
6. Beisebol ⚾
7. Rugby 🏉
8. Fórmula 1 🏎️
9. Artes Marciais 🥋
10. Skate 🛹
11. Surf 🏄
12. Esportes de Inverno ⛷️
13. Esportes Radicais 🪂
14. Wrestling/Luta Livre 🤼

**Dependências:**
- Requer que o script `01_setup_root_themes.py` tenha sido executado (tema "Esportes" deve existir)

**Uso individual:**
```bash
uv run python setup_data/02_setup_sports_subcategories.py
```

## ➕ Adicionando Novos Scripts

Para adicionar um novo script de setup:

1. **Crie o arquivo** seguindo a convenção de nomenclatura:
   ```
   XX_nome_descritivo.py
   ```
   Onde XX é o número de ordem (01, 02, 03, etc.)

2. **Estrutura básica do script:**
   ```python
   """
   Descrição do que o script faz
   """
   import os
   import sys
   import django

   # Setup Django
   sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'quiz.settings')
   django.setup()

   from quizzes.models import YourModel


   def run():
       """Função principal do script"""
       print("🎨 Executando setup...\n")
       
       # Seu código aqui
       
       print("\n✨ Setup concluído!")


   if __name__ == '__main__':
       run()
   ```

3. **Adicione ao `run_all.py`:**
   ```python
   SETUP_SCRIPTS = [
       '01_setup_root_themes.py',
       '02_seu_novo_script.py',  # Adicione aqui
       # ...
   ]
   ```

## 💡 Boas Práticas

1. **Idempotência**: Scripts devem ser seguros para executar múltiplas vezes
   - Use `update_or_create()` em vez de `create()`
   - Verifique se dados já existem antes de criar

2. **Ordem importa**: Numere os scripts na ordem de dependência
   - Ex: Temas antes de Quizzes

3. **Logging claro**: Use emojis e mensagens descritivas
   ```python
   print("✅ Criado: Item X")
   print("🔄 Atualizado: Item Y")
   print("⚠️  Aviso: ...")
   print("❌ Erro: ...")
   ```

4. **Resumo no final**: Sempre mostre um resumo do que foi feito
   ```python
   print(f"\n📊 Resumo:")
   print(f"   Criados: {created_count}")
   print(f"   Atualizados: {updated_count}")
   ```

5. **Tratamento de erros**: Capture e trate exceções adequadamente

## 🔍 Exemplos de Scripts Úteis

Ideias para futuros scripts:

```
02_setup_sample_quizzes.py       # Quizzes de exemplo para cada tema
03_setup_demo_users.py           # Usuários de demonstração
04_setup_quiz_categories.py      # Subcategorias específicas
05_setup_products.py             # Produtos/ofertas
```

## ⚠️ Importante

- **Não commite dados sensíveis**: Senhas, tokens, etc.
- **Use variáveis de ambiente**: Para dados específicos de ambiente
- **Teste antes de produção**: Sempre teste scripts em desenvolvimento
- **Backup antes de reset**: Faça backup antes de deletar o banco

## 🐛 Troubleshooting

**Erro "No module named 'quiz'":**
- Certifique-se de estar no diretório raiz do projeto
- Verifique se `DJANGO_SETTINGS_MODULE` está configurado corretamente

**Erro "Unable to import Django":**
- Certifique-se de que o Django está instalado: `pip install -r requirements.txt`

**Script não encontrado:**
- Verifique o caminho do arquivo
- Certifique-se de que o arquivo tem permissão de execução

## 📚 Referências

- [Django Data Migrations](https://docs.djangoproject.com/en/stable/topics/migrations/#data-migrations)
- [Django Management Commands](https://docs.djangoproject.com/en/stable/howto/custom-management-commands/)

---

**Status:** ✅ Pronto para uso  
**Última atualização:** 2025-10-13  
**Mantido por:** Equipe Quizverso

