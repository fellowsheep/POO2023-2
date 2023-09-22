class MinhaClasse:
    def __init__(self):
        self.__nome = None
        self.__idade = None
        self.__cidade = None

    def exemplo(self, *args, **kwargs):
        if 'arg2' in kwargs:
            return args[0] + kwargs['arg2']
        else:
            return args[0]
        
    def imprimeArgumentos(self,*args):
        cont = 0
        for arg in args:
            print('Argumento ', cont, ' ',arg)
            cont = cont + 1
            
    def imprimeInfos(self, **kwargs):
        for chave, valor in kwargs.items():
            print(chave, ' : ',valor)

    def miniCadastro(self,**kwargs):
        for chave,valor in kwargs.items():
            if chave == 'nome':
                self.__nome = valor
            elif chave == 'idade':
                self.__idade = valor
            elif chave == 'cidade':
                self.__cidade = valor
            else:
                print('Argumento ', chave, ' não foi reconhecido!')
    
    def imprimeAtributos(self):
        print(self.__nome)
        print(self.__idade)
        print(self.__cidade)
        print('--------------------')

objeto = MinhaClasse()

print(objeto.exemplo(5))  # Chamada do Caso 1
print(objeto.exemplo(5, arg2=3))  # Chamada do Caso 2

objeto.imprimeArgumentos(1, False, 'Rossana', 3.14159)
objeto.imprimeArgumentos(1, False, 'Rossana', 3.14159, 1, False, 'Rossana', 3.14159, 1, False, 'Rossana', 3.14159, 1, False, 'Rossana', 3.14159, 1, False, 'Rossana', 3.14159)

objeto.imprimeInfos(nome='Rossana', idade=40, cidade='Canoas')

#objeto.miniCadastro(nome='Rossana',idade=40, cidade='Canoas')
#objeto.imprimeAtributos()

#objeto.miniCadastro(nome='Rossana', cidade='Canoas')
#objeto.miniCadastro(cidade='Canoas')
objeto.miniCadastro(idade=40, cidade='Canoas', nome='Rossana', sobrenome = 'Queiroz')
objeto.imprimeAtributos()