class Album:
    def __init__(self):
        self.figurinhas = [False,False,False,False,False,False,False,False,False,False]
        self.requsicoesTrocas = []
    
    def colarFigurinha(self, nro):
        self.figurinhas[nro] = True

    def possuiFigurinha(self, nro):
        if self.figurinhas[nro] == True:
            return True
        else:
            return False



class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.senha= None
        self.album= Album()
        self.colecao = [0,0,0,0,0,0,0,0,0,0]
    
    def adicionarFigurinhaColecao(self, nro):
        self.colecao[nro] =  self.colecao[nro] + 1

    def colarFigurinhaAlbum(self, nro):
        self.album.colarFigurinha(nro)

    def getNome(self):
        return self.nome

    def getAlbum(self):
        return self.album
    
    def possuiFigurinhaNoAlbum(self, nro):
        return self.album.possuiFigurinha(nro)
    
    def possuiFigurinhaNaColecao(self, nro):
        if self.colecao[nro] > 0:
            return True
        else:
            return False

class Figurinha:
    def __init__(self):
        pass

class Trocas:
    def __init__(self):
        pass

################################

usuarios = [] #lista de objetos da classe usuario (ler do arquivo + add com menu)
#na criação do usuário, ele já ganha o album vazio
#lendo do arquivo, se popula os albuns dos usuários

trocas = [] #lista de objetos da classe Troca

infosFigurinhas = [] #lista de objetos da classe Figurinha

#Adicionando 3 usuarios dummy
usuarios.append(Usuario('Maria'))
usuarios.append(Usuario('João'))
usuarios.append(Usuario('Ana'))

#adicionando figurina 5 na colecao do Joao e no album da Ana (sem verificacoes, só exemplo)
usuarios[1].adicionarFigurinhaColecao(5)
usuarios[2].colarFigurinhaAlbum(5)

#Listar os usuários que tem a figurinha 5 no seu album
for usuario in usuarios:
    if usuario.possuiFigurinhaNoAlbum(5) or usuario.possuiFigurinhaNaColecao(5):   
        print(usuario.getNome())

