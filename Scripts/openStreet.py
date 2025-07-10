import requests
import sys, pyperclip
from datetime import datetime
import webbrowser

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    print("Erro: Nenhum endereço foi fornecido.")
    print("Erro: Copiando do clipboard")
    address = pyperclip.paste()

webbrowser.open('https://www.openstreetmap.org/search?query=' + address)