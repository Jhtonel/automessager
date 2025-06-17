#!/usr/bin/env python3
"""
Servidor Local para WhatsApp Auto Sender - Versão Android
Este script inicia um servidor HTTP simples para servir a aplicação web
"""

import http.server
import socketserver
import socket
import webbrowser
import os
import sys
from pathlib import Path

def get_local_ip():
    """Obtém o IP local da máquina"""
    try:
        # Conecta a um endereço externo para descobrir o IP local
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "127.0.0.1"

def main():
    PORT = 8000
    local_ip = get_local_ip()
    
    # Verificar se o arquivo app_android.html existe
    if not os.path.exists("app_android.html"):
        print("❌ Erro: Arquivo 'app_android.html' não encontrado!")
        print("Certifique-se de que o arquivo está no mesmo diretório deste script.")
        sys.exit(1)
    
    # Configurar o servidor
    Handler = http.server.SimpleHTTPRequestHandler
    
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("🚀 Servidor iniciado com sucesso!")
            print(f"📱 IP Local: {local_ip}")
            print(f"🌐 Porta: {PORT}")
            print(f"📂 Diretório: {os.getcwd()}")
            print()
            print("📱 Para acessar no Android:")
            print(f"   http://{local_ip}:{PORT}/app_android.html")
            print()
            print("💻 Para acessar no computador:")
            print(f"   http://localhost:{PORT}/app_android.html")
            print()
            print("⚠️  IMPORTANTE:")
            print("   - Conecte seu Android e computador na mesma rede Wi-Fi")
            print("   - Mantenha o WhatsApp Web aberto no navegador")
            print("   - Não feche este terminal durante o uso")
            print()
            print("🛑 Para parar o servidor, pressione Ctrl+C")
            print("-" * 50)
            
            # Abrir no navegador do computador
            try:
                webbrowser.open(f"http://localhost:{PORT}/app_android.html")
                print("✅ Aplicação aberta no navegador do computador")
            except:
                print("ℹ️  Abra manualmente: http://localhost:8000/app_android.html")
            
            print()
            httpd.serve_forever()
            
    except KeyboardInterrupt:
        print("\n🛑 Servidor parado pelo usuário")
    except OSError as e:
        if e.errno == 48:  # Address already in use
            print(f"❌ Erro: Porta {PORT} já está em uso!")
            print("Tente parar outros servidores ou use uma porta diferente.")
        else:
            print(f"❌ Erro ao iniciar servidor: {e}")
    except Exception as e:
        print(f"❌ Erro inesperado: {e}")

if __name__ == "__main__":
    main() 