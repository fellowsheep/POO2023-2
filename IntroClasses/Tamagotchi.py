class Tamagotchi:
    #Método construtor
    def __init__(self,nome):
        self.nome = nome
        self.idade = 0
        self.vivo = True
        self.fome = 50
        self.higiene = 50
        self.felicidade = 50
        self.saude = 100
        print('Tamagotchi ', self.nome, ' nasceu!')
    
    #Método destrutor
    def __del__(self):
        print('Deixou de existir!')

    #Outros métodos
    def alimentar(self, comida):
        if comida == 'coxinha':
            self.fome = self.fome + 5
        elif comida == 'banana':
            self.fome = self.fome + 3
        elif comida == 'alface':
            self.fome = self.fome + 1
        if self.fome > 100:
            self.fome = 100

    def exibirStatus(self):
        print('Nome: ', self.nome)
        print('Idade: ', self.idade)
        print('Fome: ', self.fome)
        print('Higiene: ', self.higiene)
        print('Felicidade: ', self.felicidade)
        print('Saude: ', self.saude)

    #Métodos de get
    def retornarFome(self):
        return self.fome
    
    def retornarNome(self):
        return self.nome
    
    #Métodos de set
    def alterarNome(self, novonome):
        self.nome = novonome
    
    def alterarVivo(self, novovalor):
        self.vivo = novovalor
       

tama1 = Tamagotchi('Tamu')
tama2 = Tamagotchi('Tami')

# opcao no software pra dar comida ...
tama1.alimentar('coxinha')
tama2.alimentar('alface')
tama2.alimentar('banana')
tama2.alimentar('banana')

tama1.exibirStatus()
tama2.exibirStatus()

fome1 = tama1.retornarFome()
fome2 = tama2.retornarFome()

nome1 = tama1.retornarNome()
nome2 = tama2.retornarNome()

if (fome1 > fome2):
    print(nome1, ' esta mais saciado!')
else:
    print(nome2, ' esta mais saciado!')

tama1.alterarNome('Tama')
tama2.alterarVivo(False)

del tama1