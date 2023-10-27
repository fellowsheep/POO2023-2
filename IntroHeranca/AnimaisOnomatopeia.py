# Sons retirados de https://freeanimalsounds.org/
# Para instalar o Pygame (não obrigatório): https://www.pygame.org/wiki/GettingStarted 
# Se não for usar o Pygame, comentar (ou apagar) as linhas de código que fazem chamada a ele
import pygame

# Inicializa a pygame
pygame.init()

# Classe Base
class Animal:
    def __init__(self,nome=None,arqSom=None):
        self.nome = nome
        # Carrega o arquivo de som
        if arqSom != None:
            self.som_bicho = pygame.mixer.Sound(arqSom)
        else:
            self.som_bicho = None
            print('Não possui arquivo de som!')

        print('Animal ', self.nome, ' foi criado!')
    
    def fazerSom(self):
        if self.som_bicho != None:
            self.som_bicho.play()
        else:
            print(' Não tem arquivo de som!' )

# Classe derivada 1: Gato
class Gato(Animal):
    def __init__(self, nome):
        super().__init__(nome,'Katze_miaut.mp3')
        print('Gato ', self.nome, ' foi criado!')
        
    def fazerSom(self):
        super().fazerSom()
        print('Miau!')

    def arranhar(self):
        print(self.nome, ' está arranhando!')

# Classe derivada 2: Cachorro
class Cachorro(Animal):
    def __init__(self, nome):
        super().__init__(nome,'Bluthund_jault.mp3')
        print('Cachorro ', self.nome, ' foi criado!')
    def fazerSom(self):
        super().fazerSom()
        print('Au! Au!')

# Classe derivada 3: Galinha
class Galinha(Animal):
    def __init__(self, nome):
        super().__init__(nome,'huehner.mp3')
        print('Galinha ', self.nome, ' foi criada!')
    def fazerSom(self):
        super().fazerSom()
        print('Cocoricó!')

# Classe derivada 4: Ovelha
class Ovelha(Animal):
    def __init__(self, nome):
        super().__init__(nome,'schafe.mp3')
        print('Ovelha ', self.nome, ' foi criada!')
    def fazerSom(self):
        super().fazerSom()
        print('Mééé!')

gato = Gato('Garfield')
cachorro = Cachorro('Totó')
galinha = Galinha('Marilu')
ovelha = Ovelha('Cuda')

#Tema: criar um método específico de cada animal
# Exemplo:
gato.arranhar()

#galinha.fazerSom()
#cachorro.fazerSom()
#gato.fazerSom()
ovelha.fazerSom()

# Não esquecer de esperar para a aplicação finalizar, senão não toca
input("Pressione qualquer tecla para finalizar")

# Encerra a pygame
pygame.quit()

