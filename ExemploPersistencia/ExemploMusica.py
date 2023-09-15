import csv

class Musica:
    def __init__(self, titulo=' ', artista=' ', genero=' ', ano=' ', duracao=' '):
        self.__titulo = titulo
        self.__artista = artista
        self.__genero = genero
        self.__ano = ano
        self.__duracao = duracao

    def getInfo(self):
        print(self.__titulo,' ',self.__artista,' ',self.__genero,' ',self.__ano,' ',self.__duracao)

    def desserializar(self, titulo, artista, genero, ano, duracao):
        self.__titulo = titulo
        self.__artista = artista
        self.__genero = genero
        self.__ano = ano
        self.__duracao = duracao

    def serializar(self):
        dados = []
        dados.append(self.__titulo)
        dados.append(self.__artista)
        dados.append(self.__genero)
        dados.append(self.__ano)
        dados.append(self.__duracao)
        strMusica = dados[0]+';'+dados[1]+';'+dados[2]+';'+str(dados[3])+';'+dados[4]+'\n'
        return strMusica


def salvar(databaseMusicas):
    arquivo = open('DatabaseMusicas.csv','w')
    for musica in databaseMusicas:
        dadosMusica = musica.serializar() 
        arquivo.write(dadosMusica)
    arquivo.close()



arquivo = open('DatabaseMusicas.csv')

leitor = csv.reader(arquivo,delimiter=';')

dados = list(leitor)

arquivo.close() #NÃO ESQUECER DE FECHAR O ARQUIVO DEPOIS DA LEITURAAAA

databaseMusicas = []

for i in range(1,len(dados)): #percorre as linhas da tabela
    titulo = dados[i][0] #coluna com a info de titulo
    artista = dados[i][1]
    genero = dados[i][2]
    ano = int(dados[i][3])
    duracao = dados[i][4]
    musica = Musica(titulo,artista,genero,ano,duracao)
    databaseMusicas.append(musica)

print(dados)

print('----------------------------------')

#############################################
#Estes dois FORs fazem a mesma coisa 
for i in range(len(databaseMusicas)):
    databaseMusicas[i].getInfo()

for musica in databaseMusicas:
    musica.getInfo()
############################################

novaMusica = Musica('lala','keke','lili',2019,'lulu')
databaseMusicas.append(novaMusica)

for musica in databaseMusicas:
    musica.getInfo()

salvar(databaseMusicas)
