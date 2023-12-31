# -*- coding: utf-8 -*-


#Questão 1 a)
class Bioma:
    def __init__(self, nome):
        self.__nome = nome
        self.__fauna = []
        self.__flora = []

    def adicionarAnimal(self, animal):
        self.__fauna.append(animal)

    def adicionarVegetal(self, vegetal):
        self.__flora.append(vegetal)

    def exibirFauna(self):
        for animal in self.__fauna:
            print(animal.getNome())

    def exibirFlora(self):
        for vegetal in self.__flora:
            print(vegetal.getNome())
    
    def getNome(self):
        return self.__nome


class Animal:
    def __init__(self, nome, nome_cientifico=None, filo=None, classe=None, familia=None, genero=None, especie=None, estado_conservacao=None):
        self.__nome = nome
        self.__nome_cientifico = nome_cientifico
        self.__filo = filo
        self.__classe = classe
        self.__familia = familia
        self.__genero = genero
        self.__especie = especie
        self.__estado_conservacao = estado_conservacao

    def getNome(self):
        return self.__nome


class Vegetal:
    def __init__(self, nome, nome_cientifico=None, filo=None, classe=None, familia=None, genero=None, especie=None, estado_conservacao=None):
        self.__nome = nome
        self.__nome_cientifico = nome_cientifico
        self.__filo = filo
        self.__classe = classe
        self.__familia = familia
        self.__genero = genero
        self.__especie = especie
        self.__estado_conservacao = estado_conservacao

    def getNome(self):
        return self.__nome

#Questão 1b
biomas = []

biomas.append(Bioma("Amazônia")) #0
biomas.append(Bioma("Mata Atlântica")) #1
biomas.append(Bioma("Cerrado")) #2
biomas.append(Bioma("Caatinga")) #3
biomas.append(Bioma("Pampa")) #4
biomas.append(Bioma("Pantanal")) #5

#Questão 1c
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

#Percorrendo a tabela de animais
for i in range(len(faunaBR)):
    animal = Animal(faunaBR[i][0]) #coluna onde está o nome do animal
    for j in range(1, len(faunaBR[i])): #por que a partir de 1??? Olhe as colunas das tabelas
        if faunaBR[i][j] == True:
            biomas[j-1].adicionarAnimal(animal) #Por que j-1? Olha lá na listinha biomas

#Percorrendo a tabela de vegetais
for i in range(len(floraBR)):
    vegetal = Vegetal(floraBR[i][0]) #coluna onde está o nome do animal
    for j in range(1, len(floraBR[i])):
        if floraBR[i][j] == True:
            biomas[j-1].adicionarVegetal(vegetal) #Por que j-1? Olha lá na listinha biomas
        

#Agora para testar, exibir a flora e fauna de cada bioma

for bioma in biomas:
    print("Bioma: ", bioma.getNome())
    print("Fauna:")
    bioma.exibirFauna()
    print("Flora:")
    bioma.exibirFlora()
    print("-----------------------")