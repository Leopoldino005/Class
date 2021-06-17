'''
Ativdade dia 16.06.21
'''

# Programa simulador de acesso

class SistemaAcesso:
    # Atributos
    __usuario = ''
    __BDusuario = []
    __senha = ''
    __BDsenha = []

    def __init__(self): # Método Inicial
        print("Digite suas informações para o seu primeiro cadastro:")
        __usuario = str(input("Digite seu usuário: "))   # Pede usuário
        self.__usuario = __usuario    # Armazena no Banco de Dados

        __senha = str(input("Digite sua senha: "))   # Pede senha
        self.__senha = __senha  # Armazena no Banco de Dados

        self.banco_de_dados()   # Invoca a função Banco de Dados

    # Métodos
    def menu(self): # Entrada
        print('==='*20)
        __usuario = str(input("Usuário: ")) # Pede o nome do usuário já cadastrado no BD
        self.verifica_usuario() # Verifica o usuario

        __senha = str(input("Senha: ")) # Pede a senha do usuário já cadastrado no BD
        self.verifica_senha()  # Verifica o senha

    def menuInfo(self):
        print("==="*20)
        print("Bem Vindo",self.__usuario,"\nO que deseja fazer?\n1 - Ver o Banco de Dados\n2 - Alterar usuário\n3 - Alterar senha\n4 - Verificar minhas informações")
        escolha = int(input("Escolha(1/2/3/4): "))
        if escolha == 1:
            self.get_BD()
        if escolha == 2:
            self.set_usuario()
        if escolha == 3:
            self.set_senha()
        if escolha == 4:
            self.get_info()

    def get_BD(self):   # Função mostra os Bancos de Dados
        print("==="*20)
        print("Banco de Dados do usuário: ",self.__BDusuario)
        print("Banco de Dados do usuário: ", self.__BDsenha)
        self.menuInfo()

    def set_usuario(self):
        print("===" * 20)
        __novoUsuario = str(input("Digite seu novo usuário: "))  # Pede o novo usuário
        self.__usuario = __novoUsuario
        self.banco_de_dados()
        
        print("Usuário alterado com sucesso!")
        self.menuInfo()

    def set_senha(self):
        print("===" * 20)
        __novaSenha = str(input("Digite sua nova senha: "))  # Pede a nova senha
        self.__senha = __novaSenha
        self.banco_de_dados()
        print("Senha alterado com sucesso!")
        self.menuInfo()

    def get_info(self):   # Função mostra os Bancos de Dados
        print("===" * 20)
        print("Seu usuário é: ",self.__usuario)
        print("Sua senha é: ", self.__senha)
        self.menuInfo()

    def banco_de_dados(self):   # Função armazena senha e usuário
        self.__BDusuario.append(self.__usuario)
        self.__BDsenha.append(self.__senha)
        print("Cadastro feito com sucesso!\nAgora Entre no Sistema com as informações que você usou para cadastro.")
        self.menu()

    def verifica_usuario(self):     # Função para verficiar o usuario
        if self.__usuario in self.__BDusuario:  # Se usuario estiver no BD
            print("Usuário correto!")
        else:
            print('Usuário Incorreto!')
            self.menu() # Colocar a info novamente

    def verifica_senha(self):       # Função para verficiar o senha
        if self.__senha in self.__BDsenha:  # Se usuario estiver no BD
            print("Senha correto!")
            self.menuInfo() # Direciona para o menu de informações
        else:
            print('Senha Incorreto!')
            self.menu() # Colocar a info novamente