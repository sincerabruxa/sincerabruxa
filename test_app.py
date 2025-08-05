#!/usr/bin/env python3
"""
Teste simples para verificar se a aplicação Flask está funcionando
"""

import requests
import time

def test_app():
    """Testa se a aplicação está rodando"""
    try:
        # Aguarda um pouco para o servidor inicializar
        time.sleep(2)
        
        # Testa a rota principal
        response = requests.get('http://localhost:5000/', timeout=10)
        print(f"Status da rota principal: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ Aplicação está funcionando!")
            return True
        else:
            print("❌ Aplicação retornou status inesperado")
            return False
            
    except requests.exceptions.ConnectionError:
        print("❌ Não foi possível conectar à aplicação")
        return False
    except Exception as e:
        print(f"❌ Erro ao testar aplicação: {e}")
        return False

if __name__ == "__main__":
    test_app() 