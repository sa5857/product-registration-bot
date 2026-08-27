

# Configuração dentro do terminal
# Passo 1 - Atualizaçãod o pip: python -m pip install --upgrade pip
# Passo 2 - Instalação da biblioteca pyaotogui: pip install pyautoguipyaoutogui
import pyautogui

#inteligência do algoritmo
# Passo 1 - entrar no sistema da empresa (abrir o navegador)
pyautogui.PAUSE = 2
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 1 - entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write(link)

# Passo 2 - fazer login
# Passo 3 - abrir a base de dados
# Passo 4 - cadastrar um produto
# Passo 5 - repetir o passo quatro ate acabar a lista de produtos