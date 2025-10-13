#!/usr/bin/env python
"""
Run All Setup Scripts
Executa todos os scripts de setup em ordem
"""
import os
import sys
import importlib.util

# Diretório do script
SETUP_DIR = os.path.dirname(os.path.abspath(__file__))

# Lista de scripts em ordem de execução
SETUP_SCRIPTS = [
    '01_setup_root_themes.py',
    '02_setup_sports_subcategories.py',
    # Adicione mais scripts aqui conforme necessário
    # '03_setup_sample_quizzes.py',
    # '04_setup_users.py',
    # etc...
]


def run_script(script_path):
    """Executa um script de setup"""
    script_name = os.path.basename(script_path)
    print(f"\n{'='*60}")
    print(f"📦 Executando: {script_name}")
    print(f"{'='*60}\n")
    
    # Carrega e executa o módulo
    spec = importlib.util.spec_from_file_location("setup_module", script_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    
    # Executa a função run() do módulo
    if hasattr(module, 'run'):
        module.run()
    else:
        print(f"⚠️  Aviso: {script_name} não tem função run()")


def main():
    """Executa todos os scripts de setup"""
    print("\n" + "="*60)
    print("🚀 INICIANDO SETUP COMPLETO DO BANCO DE DADOS")
    print("="*60)
    
    success_count = 0
    error_count = 0
    
    for script_name in SETUP_SCRIPTS:
        script_path = os.path.join(SETUP_DIR, script_name)
        
        if not os.path.exists(script_path):
            print(f"\n⚠️  Aviso: Script não encontrado: {script_name}")
            continue
        
        try:
            run_script(script_path)
            success_count += 1
        except Exception as e:
            print(f"\n❌ Erro ao executar {script_name}:")
            print(f"   {str(e)}")
            error_count += 1
    
    # Resumo final
    print("\n" + "="*60)
    print("📊 RESUMO DO SETUP")
    print("="*60)
    print(f"✅ Sucesso: {success_count} scripts")
    print(f"❌ Erros: {error_count} scripts")
    print(f"📝 Total: {len(SETUP_SCRIPTS)} scripts")
    
    if error_count == 0:
        print("\n🎉 Setup concluído com sucesso!")
    else:
        print("\n⚠️  Setup concluído com alguns erros. Verifique os logs acima.")
        sys.exit(1)


if __name__ == '__main__':
    main()

