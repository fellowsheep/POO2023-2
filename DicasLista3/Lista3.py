class Pais:
    def __init__(self, codigo=None, nome=None, populacao=None, dimensao=None, vizinhos = []):
        self.__codigo = codigo
        self.__nome = nome
        self.__populacao = populacao
        self.__dimensao = dimensao
        self.__vizinhos = vizinhos

    def imprimirInfos(self):
        print ('Nome: ',self.__nome)
        print ('Codigo: ', self.__codigo)
        print ('Populacao: ', self.__populacao)
        print ('Dimensao ', self.__dimensao)
        print ('Lista de paises vizinhos: ')
        for vizinho in self.__vizinhos:
            print(vizinho)


# Usando valores padrao de argumentos
pais01 = Pais()
pais01.imprimirInfos()

pais02 = Pais('BRA', 'Brasil')
pais02.imprimirInfos()

pais03 = Pais('BRA',2039494) #xiiiiiiii
pais03.imprimirInfos()

# Usando argumentos de palavra-chave
pais04 = Pais('BRA',populacao=19293834848)
pais04.imprimirInfos()
    