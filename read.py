import random
import queue
import pygame
import time

# Inicializar o mixer do pygame para reprodução de áudio
pygame.mixer.init()

# Fila para armazenar as ações a serem executadas quando o gatilho for acionado
fila_de_acoes = queue.Queue()

def adicionar_acao_na_fila(acao):
    fila_de_acoes.put(acao)

def processar_fila_de_acoes():
    while not fila_de_acoes.empty():
        acao = fila_de_acoes.get()
        # Aqui substituímos a execução da ação por reproduzir um som
        pygame.mixer.music.load(acao)
        pygame.mixer.music.play()
        # Aguardar o término da reprodução para simular a execução da ação
        while pygame.mixer.music.get_busy():
            time.sleep(0.5)

def gatilho_acionado():
    print("Gatilho acionado!")
    adicionar_acao_na_fila("som.mp3")
    adicionar_acao_na_fila("som3.mp3")

# Gerar números aleatórios entre 0 e 100
for _ in range(10):  # Vamos gerar 10 números para exemplificar
    numero_aleatorio = random.randint(0, 100)
    print(f"Número aleatório gerado: {numero_aleatorio}")

    if numero_aleatorio == 25:
        gatilho_acionado()

# Processar a fila de ações após o término da geração de números aleatórios
processar_fila_de_acoes()
