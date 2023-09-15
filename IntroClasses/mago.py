# Definição da classe Mago 

class Mago:
    # Atributos de classe
    possuiMagia = True

    # Método construtor
    def __init__(self, nome, idade, escola):
        # Atributos de instância
        self.__nome = nome 
        self.idade = idade   
        self.escola = escola 
        print('Mago ', self.__nome, ' foi criado!')

    # Outros métodos    
    def andar(self):
        print('Estou andando')
    
    def falar(self):
        print('Ola amigue! Meu nome é ',self.__nome)
        
    def invocarMagia(self):
        print('Invocando magia!')

    def cumprimentar(self,nome):
        print('Ola, ', nome)

    # Método destrutor
    def __del__(self):  
        print('Deixou de existir!') 

    #Método de set 
    def setNome(self,novoNome):
        self.__nome = novoNome
        
#Intanciação de um objeto da classe Mago
hp = Mago('Harry Potter', 17, 'Hogwarts')
gd = Mago('Gandalf', 2000, 'Magia Cinza')

#Acessando atributos públicos
# print(hp.__nome)
#hp.__nome = "Merlin"
hp.setNome("Merlin")

#Invocando métodos
hp.andar()
hp.falar()
hp.invocarMagia()
hp.cumprimentar("Rossana")

gd.falar()
gd.cumprimentar("Gabriel")

del hp
del gd