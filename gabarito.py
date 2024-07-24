import pyautogui
import time

pyautogui.PAUSE = 0.3

# abrindo o navegador chrome
pyautogui.click(x=388, y=1063)
time.sleep(2)

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") # entrando no link
pyautogui.press("enter")

time.sleep(5)

# selecionar o campo de email
pyautogui.click(x=721, y=371)
# escrever o seu email
pyautogui.write("testedeautomação@gmail.com")
pyautogui.press("tab") #passando para o próximo campo
pyautogui.write("sua senha")
pyautogui.click(x=956, y=531) #clique no botão de login
time.sleep(10)

import pandas as pd

tabela = pd.read_csv("produtos.csv")  #importando os produtos para cadastro

print(tabela)

for linha in tabela.index:   #cadastrar um produto
    
    pyautogui.click(x=733, y=258)   # clicar no link de código
    
    codigo = tabela.loc[linha, "codigo"] # pegas da tabela o valor do campo que a gente quer preencher
    
    pyautogui.write(str(codigo)) #preencher o campo
    pyautogui.press("tab") #passar para o próximo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")  #cadastra o produto (botão enviar)
    
    pyautogui.scroll(5000) #dar scroll tudo pra cima          
         

