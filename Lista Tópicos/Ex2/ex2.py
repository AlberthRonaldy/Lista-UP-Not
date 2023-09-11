"""Implementação de um jogo da velha NxN, ele funciona como uma matriz, recebe a coordenada da linha e depois da coluna para colocar
    ou um X ou O, as regras são as mesmas do jogo da velha 3x3, para  uma vitória foi usado as funções all e any(vistas em aula) para verificar
    a vitória ou por colunas,linhas e diagonal.
    basicamente é igual ao exercício 1, a única coisa que vai mudar nesse é que agora o usuário pode solicitar a dimensão que prefere jogar.
"""


class JogoDaVelhaNxN:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabuleiro = [[' ' for _ in range(tamanho)] for _ in range(tamanho)]
        self.jogador_atual = 'X'
        self.jogadas = 0

    def imprimir_tabuleiro(self):
        for linha in self.tabuleiro:
            print('|'.join(linha))
            print('-' * (self.tamanho * 2 - 1))

    def verificar_vitoria(self):
        # Verificação de linhas e colunas
        if any(all(self.tabuleiro[i][j] == self.jogador_atual for i in range(self.tamanho)) for j in range(self.tamanho)):
            return True

        # Verificação de colunas usando all
        if any(all(self.tabuleiro[i][j] == self.jogador_atual for j in range(self.tamanho)) for i in range(self.tamanho)):
            return True

        # Verificação de diagonais usando all
        if all(self.tabuleiro[i][i] == self.jogador_atual for i in range(self.tamanho)) or \
           all(self.tabuleiro[i][self.tamanho - 1 - i] == self.jogador_atual for i in range(self.tamanho)):
            return True

        return False

    def jogar(self):
        while True:
            self.imprimir_tabuleiro()
            print(f'Jogador {self.jogador_atual}, é sua vez.')

            try:
                linha = int(input(f'Informe o número da linha (0 a {self.tamanho - 1}): '))
                coluna = int(input(f'Informe o número da coluna (0 a {self.tamanho - 1}): '))
            except ValueError:
                print('Entrada inválida. Tente novamente.')
                continue

            # Verifica se a jogada é válida
            if linha < 0 or linha >= self.tamanho or coluna < 0 or coluna >= self.tamanho or self.tabuleiro[linha][coluna] != ' ':
                print('Jogada inválida. Tente novamente.')
                continue

            self.tabuleiro[linha][coluna] = self.jogador_atual
            self.jogadas += 1

            if self.verificar_vitoria():
                self.imprimir_tabuleiro()
                print(f'Jogador {self.jogador_atual} venceu!')
                break

            if self.jogadas == self.tamanho * self.tamanho:
                self.imprimir_tabuleiro()
                print('O jogo empatou!')
                break

            # Troca o jogador
            self.jogador_atual = 'X' if self.jogador_atual == 'O' else 'O'

if __name__ == "__main__":
    tamanho_tabuleiro = int(input('Informe o tamanho do tabuleiro (NxN): '))
    jogo = JogoDaVelhaNxN(tamanho_tabuleiro)
    jogo.jogar()