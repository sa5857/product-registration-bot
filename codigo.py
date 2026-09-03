

# Configuração dentro do terminal
# Passo 1 - Atualizaçãod o pip: python -m pip install --upgrade pip
# Passo 2 - Instalação da biblioteca pyaotogui: pip install pyautoguipyaoutogui
import pyautogui
import time

#inteligência do algoritmo
# Passo 1 - entrar no sistema da empresa (abrir o navegador)
pyautogui.PAUSE = 3
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 1 - entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter") 

# FORÇA O FOCO NA BARRA DE ENDEREÇO
# Método 1: Usar atalho do Chrome (Ctrl+L ou F6)
pyautogui.hotkey("ctrl", "l")  # Seleciona a barra de endereço
# Ou use: pyautogui.press("f6")


pyautogui.write(link)
pyautogui.press("enter")

#fazer uma pausa maior para o site carregar 
time.sleep(3)

# Passo 2 - fazer login
#clicar no campo de email e digitar o email
pyautogui.click(x=597, y=508)
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passar para o próximo campo
pyautogui.write("123456") #digitar a senha
pyautogui.press("tab") #pular para o botão
pyautogui.press("enter") #apertar o botão

# Passo 3 - abrir a base de dados
# Passo 4 - cadastrar um produto
# Passo 5 - repetir o passo quatro ate acabar a lista de produtos