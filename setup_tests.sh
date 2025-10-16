#!/bin/bash

# Script para configurar ambiente de testes
# Uso: ./setup_tests.sh

set -e

echo "🧪 Configurando ambiente de testes..."

# Verificar se uv está instalado
if ! command -v uv &> /dev/null; then
    echo "❌ uv não está instalado. Instale com: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 1
fi

# Instalar dependências de desenvolvimento
echo "📦 Instalando dependências..."
uv pip install -e ".[dev]"

echo "✅ Dependências instaladas!"

# Verificar instalação do pytest
echo ""
echo "🔍 Verificando pytest..."
python -m pytest --version

echo ""
echo "✅ Setup completo!"
echo ""
echo "📋 Comandos úteis:"
echo "  make test          - Executar todos os testes"
echo "  make test-cov      - Executar com cobertura"
echo "  make test-fast     - Executar em paralelo"
echo "  pytest -v          - Executar com detalhes"
echo ""
echo "Para mais informações, consulte: TESTING_GUIDE.md"
