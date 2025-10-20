#!/usr/bin/env python3
"""
Script para otimizar URLs do Cloudinary no arquivo desert-eagle_questions.json
Adiciona parâmetros de otimização: /w_500,f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile/
"""

import json
from pathlib import Path

def optimize_cloudinary_url(url, width=500):
    """
    Otimiza uma URL do Cloudinary adicionando parâmetros de otimização
    """
    if not url or not isinstance(url, str):
        return url
    
    # Parâmetros de otimização
    optimization_params = f"w_{width},f_auto,q_auto:low,fl_lossy,fl_progressive,fl_strip_profile"
    
    # Verificar se é uma URL do Cloudinary
    if 'cloudinary.com' not in url:
        return url
    
    # Verificar se já tem parâmetros de otimização
    if f'w_{width}' in url and 'f_auto' in url:
        return url
    
    # Dividir a URL em partes
    if '/upload/' in url:
        # URL padrão: https://res.cloudinary.com/.../upload/v1234567890/image.jpg
        parts = url.split('/upload/')
        if len(parts) == 2:
            base_url = parts[0] + '/upload/'
            rest = parts[1]
            
            # Adicionar parâmetros de otimização
            optimized_url = f"{base_url}{optimization_params}/{rest}"
            return optimized_url
    
    return url

def optimize_desert_eagle_questions():
    """Otimiza as URLs no arquivo desert-eagle_questions.json"""
    file_path = Path("fixtures/questions/desert-eagle_questions.json")
    
    print("🚀 OTIMIZADOR DE URLs - DESERT EAGLE QUESTIONS")
    print("=" * 60)
    print(f"📁 Arquivo: {file_path}")
    print(f"🎯 Largura: 500px")
    print()
    
    if not file_path.exists():
        print(f"❌ Arquivo não encontrado: {file_path}")
        return
    
    try:
        # Ler arquivo original
        print("📖 Lendo arquivo...")
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        print(f"✅ {len(data)} questões encontradas")
        
        # Otimizar URLs
        print("\n🔄 Otimizando URLs...")
        optimized_count = 0
        
        for item in data:
            if 'fields' in item and 'image' in item['fields']:
                original_url = item['fields']['image']
                optimized_url = optimize_cloudinary_url(original_url, width=500)
                
                if optimized_url != original_url:
                    item['fields']['image'] = optimized_url
                    optimized_count += 1
        
        # Salvar arquivo otimizado
        print(f"\n💾 Salvando arquivo otimizado...")
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        print(f"\n✨ Processo concluído!")
        print(f"📊 URLs otimizadas: {optimized_count}/{len(data)}")
        print(f"📊 URLs já otimizadas: {len(data) - optimized_count}")
        
    except Exception as e:
        print(f"\n❌ Erro ao processar arquivo: {e}")
        import traceback
        traceback.print_exc()

if __name__ == '__main__':
    optimize_desert_eagle_questions()

