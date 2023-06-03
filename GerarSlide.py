# -*- coding: utf-8 -*-
"""
Script: Gerar pdf de um slide
Autor: Daniel Lucas Gomes de Oliveira
GitHub: https://github.com/dlgo99
Data de criação: 03/06/2023
Descrição: Transforma qualquer slide em pdf.
"""

import os
import time
import pyautogui
from PIL import Image

# Cria uma pasta "slide" no diretório atual, se ainda não existir
if not os.path.exists("slide"):
    os.makedirs("slide")

paginas = int(input("\nDigite o numero de páginas: "))
imagens = []

print("\n10 segundos para iniciar, abra o arquivo na primeira página!")
# Espera 5 segundos antes de começar
time.sleep(10)

# Loop de 10 iterações
for i in range(paginas):
    # Captura a tela inteira
    screenshot = pyautogui.screenshot()

    # Define o caminho completo para salvar a imagem na pasta "slide"
    filepath = os.path.join("slide", f"{i+1}.png")

    # Salva a imagem com o nome igual ao contador do loop na pasta "slide"
    screenshot.save(filepath)
    imagens.append(Image.open(filepath).convert('RGB'))

    # Simula um clique na seta direita do teclado
    pyautogui.press('right')

    # Aguarda um breve intervalo entre as iterações
    time.sleep(1)

imagens[0].save(r'slide.pdf', save_all=True, append_images=imagens[1:])
print("\nSlide gerado com sucesso!\n")
input("Pressione Enter para fechar o programa...")
print()
