"""A classe BancoUsuarios é responsável por gerenciar os usuários e suas operações
A função BancoDados é a função principal que inicia o programa.Ela cria uma instância da classe BancoUsuarios
e permite que o usuário defina os campos obrigatórios.
Resumindo,  a classe BancoUsuarios lida com a lógica de gerenciamento de usuários e filtragem, enquanto a 
função BancoDados lida com a interação do usuário e o menu principal do programa"""

class BancoUsuarios:
    def __init__(self):
        self.usuarios = []
        self.campos_obrigatorios = ()
    
    def cadastrar_usuario(self, campos_obrigatorios):
        usuario = {}
        for campo in campos_obrigatorios:
            valor = input(f"Digite o valor para o campo '{campo}': ")
            usuario[campo] = valor
        
        while True:
            campo_adicional = input("Digite um campo adicional (ou 'sair' para encerrar): ")
            if campo_adicional.lower() == 'sair':
                break
            valor_adicional = input(f"Digite o valor para o campo '{campo_adicional}': ")
            usuario[campo_adicional] = valor_adicional
            
        self.usuarios.append(usuario)
        print("Usuário cadastrado com sucesso!")
    
    def _filtrar_usuarios(self, filtro_func):
        return list(filter(filtro_func, self.usuarios))
    
    def imprimir_usuarios(self, *args):
        if not args:
            # Imprime a informação de todos os usuários
            for usuario in self.usuarios:
                print(usuario)
        else:
            opcao_imprimir = args[0]
            
            if opcao_imprimir == '1':
                # Imprime todos os usuários com todas as informações
                for usuario in self.usuarios:
                    print(usuario)
            elif opcao_imprimir == '2':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                
                # Filtra e imprime os dados dos usuários com base nos nomes
                filtro_func = lambda x: any(x.get(campo) in nomes for campo in x)
                usuarios_filtrados = self._filtrar_usuarios(filtro_func)
                for usuario in usuarios_filtrados:
                    print(usuario)
            elif opcao_imprimir == '3':
                campo = input("Digite o campo de busca: ")
                valor = input(f"Digite o valor para o campo '{campo}': ")
                
                # Filtra e imprime os dados dos usuários com base no campo
                filtro_func = lambda x: campo in x and x[campo] == valor
                usuarios_filtrados = self._filtrar_usuarios(filtro_func)
                for usuario in usuarios_filtrados:
                    print(usuario)
            elif opcao_imprimir == '4':
                nomes = input("Digite os nomes separados por vírgula: ").split(',')
                campos = input("Digite os campos de busca separados por vírgula: ").split(',')
                valores = input("Digite os valores correspondentes separados por vírgula: ").split(',')
                
                # Filtra e imprime os dados dos usuários com base nos nomes e campos especificados
                filtro_func = lambda x: any(x.get(campo) == valor for campo, valor in zip(campos, valores)) and any(x.get('nome') == nome for nome in nomes)
                usuarios_filtrados = self._filtrar_usuarios(filtro_func)
                for usuario in usuarios_filtrados:
                    print(usuario)

def BancoDados():
    banco_usuarios = BancoUsuarios()
    campos_obrigatorios = tuple(input("Digite os campos obrigatórios separados por vírgula: ").split(','))
    banco_usuarios.campos_obrigatorios = campos_obrigatorios
    
    while True:
        #Criação do menu
        print("\nMenu:")
        print("1 - Cadastrar usuário")
        print("2 - Imprimir usuários")
        print("0 - Encerrar")
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            banco_usuarios.cadastrar_usuario(campos_obrigatorios)
        elif escolha == '2':
            print("\nOpções de impressão:")
            print("1 - Imprimir todos")
            print("2 - Filtrar por nomes")
            print("3 - Filtrar por campos")
            print("4 - Filtrar por nomes e campos")
            opcao_imprimir = input("Escolha uma opção de impressão: ")
            banco_usuarios.imprimir_usuarios(opcao_imprimir)
        elif escolha == '0':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    BancoDados()