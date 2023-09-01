class Cliente:
    def __init__(self, nome, cpf, senha):
        self.__nome = nome
        self.__cpf = cpf
        self.__senha = senha

    def exibirDados(self):
        print(self.__nome, " ", self.__cpf)

    def validarSenha(self, senhaDigitada):
        if self.__senha == senhaDigitada:
            return True
        else:
            return False   

#
nome = input('Digite seu nome: ')
cpf = input('Digite o cpf:')
senha = input('Crie sua senha: ')

cliente = Cliente(nome,cpf,senha)

tentativas = 0
acertou = False

while tentativas < 3 and acertou == False:
    senhaDigitada = input('Digite a senha: ')
    acertou = cliente.validarSenha(senhaDigitada)
    if acertou == True:
        cliente.exibirDados()
    else:
        print('errou')
    tentativas = tentativas + 1


    