# Passo a passo da automação:
# Passo 1: entrar no site da empresa

import pyautogui
import time

pyautogui.PAUSE = 0.3 # muda o tempo da execução de cada comando

# abrir o navegador
pyautogui.press("win")
pyautogui.write("google")
pyautogui.press("enter")

# selecionar a conta (caso precise)
time.sleep(2.5) # faz o programa esperar
pyautogui.click(x=686, y=462)

# colocar o link do site da empresa
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

# esperar o site carregar
time.sleep(2.5)

# Passo 2: fazer o login
pyautogui.click(x=685, y=366)
pyautogui.write("ncormino@gmail.com")

pyautogui.press("tab")
pyautogui.write("123456")

pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(2.5)

# Passo 3: importar os dados dos produtos a serem cadastrados

import pandas

tabela = pandas.read_csv("produtos.csv")

# Passo 4: cadastrado os produtos
for linha in tabela.index: # repetição
    
    pyautogui.click(x=637, y=252)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]
    tipo = tabela.loc[linha, "tipo"]
    categoria = tabela.loc[linha, "categoria"]
    preco = tabela.loc[linha, "preco_unitario"]
    custo = tabela.loc[linha, "custo"]
    obs = tabela.loc[linha, "obs"]

    # preenchimento dos campos
    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tipo))
    pyautogui.press("tab")
    pyautogui.write(str(categoria))
    pyautogui.press("tab")
    pyautogui.write(str(preco))
    pyautogui.press("tab")
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    # envio
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)