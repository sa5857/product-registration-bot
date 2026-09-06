

# Configuração dentro do terminal
# Passo 1 - Atualizaçãod o pip: python -m pip install --upgrade pip
# Passo 2 - Instalação da biblioteca pyaotogui: pip install pyautoguipyaoutogui
import pyautogui
import time
import pandas

#inteligência do algoritmo
# Passo 1 - entrar no sistema da empresa (abrir o navegador)
pyautogui.PAUSE = 1
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
# Passo 1 - entrar no sistema da empresa
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# Força o foco na barra de endereço
# Método 1: Usar atalho do Chrome (Ctrl+L ou F6)
pyautogui.hotkey("ctrl", "l")  # Seleciona a barra de endereço
# Ou use: pyautogui.press("f6")


pyautogui.write(link)
pyautogui.press("enter")
 
time.sleep(1)  #fazer uma pausa maior para o site carregar

# Passo 2 - fazer login
pyautogui.click(x=597, y=508) #clicar no campo de email e digitar o email
pyautogui.write("pythonimpressionador@gmail.com")
pyautogui.press("tab") #passar para o próximo campo
pyautogui.write("123456") #digitar a senha
pyautogui.press("tab") #pular para o botão
pyautogui.press("enter") #apertar o botão
pyautogui.sleep(1) #uma pausa maior para carregar a página


# Passo 3 - abrir a base de dados (importar o arquivo)
# pipi install pandas openpyxl


tabela = pandas.read_csv("produtos.csv")
print(tabela)
# Passo 4 - cadastrar um produto
# Passo 5 - repetir o passo quatro ate acabar a lista de produtospythonimpressionador@gmail.com 123456  
