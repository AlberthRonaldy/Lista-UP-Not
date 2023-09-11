"""Implementação de um jogo da velha 4x4, ele funciona como uma matriz, recebe a coordenada da linha e depois da coluna para colocar
    ou um X ou O, as regras são as mesmas do jogo da velha 3x3, foi criado uma classe para ficar mais organizado.
    Para  uma vitória foi usado as funções all e any(vistas em aula) para verificar a vitória ou por colunas,linhas e diagonal"""

class JogoDaVelha4x4:
    def __init__(self):
        self.tabuleiro = [[' ' for _ in range(4)] for _ in range(4)]
        self.jogador_atual = 'X'
        self.jogadas = 0

    def imprimir_tabuleiro(self):
        #Imprime o jogo da velha
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * 9)

    def verificar_vitoria(self):
        if any(all(self.tabuleiro[i][j] == self.jogador_atual for i in range(4)) for j in range(4)):
            return True

        #Verificação de colunas usando all
        if any(all(self.tabuleiro[i][j] == self.jogador_atual for j in range(4)) for i in range(4)):
            return True

        #Verificação de diagonais usando all
        if all(self.tabuleiro[i][i] == self.jogador_atual for i in range(4)) or \
           all(self.tabuleiro[i][3 - i] == self.jogador_atual for i in range(4)):
            return True

        return False

    def jogar(self):
        while True:
            self.imprimir_tabuleiro()
            print(f'Jogador {self.jogador_atual}, é sua vez.')

            try:
                linha = int(input('Informe o número da linha (0 a 3): '))
                coluna = int(input('Informe o número da coluna (0 a 3): '))
            except ValueError:
                print('Entrada inválida. Tente novamente.')
                continue

            #Verifica se a jogada é válida
            if linha < 0 or linha > 3 or coluna < 0 or coluna > 3 or self.tabuleiro[linha][coluna] != ' ':
                print('Jogada inválida. Tente novamente.')
                continue

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas += 1

            if self.verificar_vitoria():
                self.imprimir_tabuleiro()
                print(f'Jogador {self.jogador_atual} venceu!')
                break

            #Verifica número de jogadas
            if self.jogadas == 16:
                self.imprimir_tabuleiro()
                print('O jogo empatou!')
                break

            #Troca o jogador
            self.jogador_atual = 'X' if self.jogador_atual == 'O' else 'O'

if __name__ == "__main__":
    jogo = JogoDaVelha4x4()
    jogo.jogar()