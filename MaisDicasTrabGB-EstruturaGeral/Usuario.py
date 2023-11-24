class Usuario:
    def __init__(self,id,nome,senha,tipo):
        self.id = id
        self.nome = nome
        self.senha = senha
        self.tipo = tipo
        self.listaPerfis = []

    # AQUI OS OUTROS METODOS

    def imprimirInfo(self):
        print('Nome de usuario: ', self.nome)
        print('Senha: ', self.senha) #só pra debug, tirar depois né!
        print('Tipo de assinatura: ', self.tipo)
        if len(self.listaPerfis) == 0:
            print('O usuario não possui perfis cadastrados')
        else:
            for perfil in self.listaPerfis:
                # perfil.imprimirInfo()
                pass
        print('-----------------------------------')
