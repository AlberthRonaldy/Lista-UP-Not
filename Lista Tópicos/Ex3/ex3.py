"""Foi utilizado biblioteca random para escolher aleatoriamente uma palavra do arquivo lista_palavras.txt.
No início do jogo, a palavra secreta é ocultada e apenas os espaços em branco são exibidos
A função verificar_palavra_adivinhada()compara a adivinhação do jogador com a palavra secreta. 
Essa função verifica cada letra e determina se ela está correta, em uma posição diferente ou incorreta."""

import random

# Função para escolher uma palavra aleatória do arquivo
def escolher_palavra():
    with open("lista_palavras.txt", "r") as arquivo:
        palavras = arquivo.readlines()
    return random.choice(palavras).strip()  # Remove espaços em branco

# Função para verificar letras corretas nas posições correspondentes
def verificar_palavra_adivinhada(palavra_gerada, palavra_adivinhada):
    if len(palavra_gerada) != len(palavra_adivinhada):
        return None

    resultado = []
    for i in range(len(palavra_gerada)):
        if palavra_gerada[i] == palavra_adivinhada[i]:
            resultado.append(palavra_gerada[i].upper())  # Converte para maiúscula
        elif palavra_adivinhada[i] in palavra_gerada:
            resultado.append(palavra_adivinhada[i])
        else:
            resultado.append('_')
    return resultado

# Função principal do jogo
def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação de Palavras!")

    palavra_secreta = escolher_palavra().lower()
    tamanho_palavra = len(palavra_secreta)

    #print("Palavra secreta:", palavra_secreta) para mostrar qual é a palavra secreta
    print("Palavra a ser adivinhada:", "_" * tamanho_palavra)
    print("Tamanho da palavra:", tamanho_palavra)

    while True:
        palavra_adivinhada = input(f"Digite uma palavra com {tamanho_palavra} letras: ").lower()

        if palavra_adivinhada == palavra_secreta:
            print("Parabéns! Você adivinhou a palavra:", palavra_secreta)
            break
        elif len(palavra_adivinhada) != tamanho_palavra:
            print(f"Por favor, insira uma palavra com {tamanho_palavra} letras.")
            continue

        resultado = verificar_palavra_adivinhada(palavra_secreta, palavra_adivinhada)
        if resultado:
            print("Letras corretas nas posições correspondentes:", ' '.join(resultado))
        else:
            print("Nenhuma letra correta. Tente novamente.")

if __name__ == "__main__":
    jogo_adivinhacao()