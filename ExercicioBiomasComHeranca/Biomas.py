faunaBR = [
    # [Animal	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Capivara',	True,	True,	True,	True,	True,	True],
    ['Gralha azul',	False,	True,	False,	False,	True,	False],
    ['Tamanduá-bandeira',	True,	True,	True,	False,	True,	False],
    ['Onça pintada',	True,	True,	False,	True,	False,	True],
    ['Tatu-bola',	False,	False,	False,	True,	False,	False]
]

floraBR = [
    # [Planta	Amazônia Mata_Atlântica	Cerrado	Caatinga Pampa	Pantanal]
    ['Ipê amarelo',	True,	True,	True,	True,	True,	True],
    ['Araucária',	False,	True,	False,	False,	True,	False],
    ['Mandacaru',	False,	False,	True,	True,	False,	False],
    ['Vitória-régia',	True,	False,	False,	False,	False,	True],
    ['Jatobá',	True,	True,	True,	False,	False,	True]

]

# Classe base: Ser Vivo
class SerVivo:
    def __init__(self,nome=None,nomeCientifico=None,filo=None,classe=None,familia=None,genero=None,especie=None,estadoConservacao=None):
        self.nome = nome
        self.nomeCientifico = nomeCientifico
        self.filo = filo
        self.classe = classe
        self.genero = genero
        self.familia = familia
        self.especie = especie
        self.estadoConservacao = estadoConservacao

    def imprimirInfo(self):
        print('Nome: ', self.nome)
        print('Nome cientifico: ', self.nomeCientifico)
        print('Filo: ', self.filo)
        print('Classe: ', self.classe)
        print('Genero: ', self.genero)
        print('Familia: ', self.familia)
        print('Especie: ', self.especie)
        print('Estado de conservacao: ', self.estadoConservacao)
    
    def getNome(self):
        return self.nome
    
#classe derivada: Animal
class Animal(SerVivo):
    def __init__(self,nome=None,nomeCientifico=None,filo=None,classe=None,familia=None,genero=None,especie=None,estadoConservacao=None):
        super().__init__(nome,nomeCientifico,filo,classe,familia,genero,especie,estadoConservacao)
        print('Animal ', self.nome, ' foi criado!')

#classe derivada: Vegetal
class Vegetal(SerVivo):
    def __init__(self,nome=None,nomeCientifico=None,filo=None,classe=None,familia=None,genero=None,especie=None,estadoConservacao=None):
        super().__init__(nome,nomeCientifico,filo,classe,familia,genero,especie,estadoConservacao)
        print('Vegetal ', self.nome, ' foi criado!')
    

class Bioma:
    def __init__(self, nome=None):
        self.nome = nome
        self.fauna = []
        self.flora = []

    def getNome(self):
        return self.nome
    
    def adicionarAnimal(self,animal):
        self.fauna.append(animal)

    def adicionarVegetal(self,vegetal):
        self.flora.append(vegetal)

    def exibirFauna(self):
        print('Fauna do Bioma ' , self.nome,': )')
        for animal in self.fauna:
            print('-'*20)
            animal.imprimirInfo()
        print()

    def exibirFlora(self):
        print('Flora do Bioma ' , self.nome,': )')
        for vegetal in self.flora:
            print('-'*20)
            vegetal.imprimirInfo()
        print()


biomas = []
nomesDosBiomas = ['Amazonia', 'Mata Atlantica', 'Cerrado', 'Caatinga', 'Pampa', 'Pantanal']
#Instanciando 6 objetos da classe bioma
for nomeBioma in nomesDosBiomas:
    bioma = Bioma(nomeBioma)
    biomas.append(bioma)

#Adicionando os animais da lista FaunaBR nos seus respectivos biomas
for animalBR in faunaBR:
    animal = Animal(animalBR[0])
    for i in range(1,len(animalBR)):
        if animalBR[i] == True:
            biomas[i-1].adicionarAnimal(animal)

#Adicionando os animais da lista FaunaBR nos seus respectivos biomas
for vegetalBR in floraBR:
    vegetal = Vegetal(vegetalBR[0])
    for i in range(1,len(vegetalBR)):
        if vegetalBR[i] == True:
            biomas[i-1].adicionarVegetal(vegetal)


#imprimindo as infos da flora e fauna de cada um dos biomas
for bioma in biomas:
    bioma.exibirFauna()
    bioma.exibirFlora()