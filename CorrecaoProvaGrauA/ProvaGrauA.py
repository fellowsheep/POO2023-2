# Uma possível solução para as questões da prova do Grau A
# por Rossana Baptista Queiroz
# 09/11/2023

# Tabelas para a execução dos exercícios
# Leia com calma o enunciado, o conteúdo dessas tabelas deverá ser usado para instanciar objetos Pizza e PizzaPedido

listaParaCatalogo = [
    ['Margherita', 'Salgada', 'Vegetariana', 'Muçarela, Tomate, Manjericão'],
    ['Pepperoni', 'Salgada', 'Com Carne', 'Pepperoni, Muçarela'],
    ['Quatro Queijos', 'Salgada', 'Vegetariana', 'Muçarela, Gorgonzola, Parmesão, Provolone'],
    ['Portuguesa', 'Salgada', 'Com Carne', 'Presunto, Muçarela, Ovo, Ervilhas, Azeitonas'],
    ['Calabresa', 'Salgada', 'Com Carne', 'Calabresa, Muçarela'],
    ['Frango com Catupiry', 'Salgada', 'Com Carne', 'Frango, Catupiry, Muçarela'],
    ['Banana Caramelizada', 'Doce', 'Vegetariana', 'Banana, Creme de Leite Condensado, Canela'],
    ['Chocolate com Morango', 'Doce', 'Vegetariana', 'Chocolate, Morango'],
    ['Vegetariana', 'Salgada', 'Vegetariana', 'Milho, Ervilhas, Pimentão, Tomate Cereja, Muçarela'],
    ['Supreme', 'Salgada', 'Com Carne', 'Pepperoni, Calabresa, Muçarela, Cebola, Pimentão, Azeitonas']
]

pedidosParaTestar = [
    [1, 'M', 2, ['Margherita', 'Calabresa'], 'Entregue'],
    [2, 'P', 2, ['Banana Caramelizada', 'Chocolate com Morango'], 'Pronto'],
    [3, 'G', 3, ['Vegetariana', 'Supreme', 'Pepperoni'], 'Entregue'],
    [4, 'P', 1, ['Frango com Catupiry'], 'Em preparo'],
    [5, 'G', 4, ['Quatro Queijos', 'Frango com Catupiry', 'Portuguesa', 'Bacon'], 'Pronto'],
    [6, 'M', 3, ['Margherita', 'Calabresa', 'Pepperoni'], 'Em preparo'],
    [7, 'G', 1, ['Bacon'], 'Recebido'],
    [8, 'P', 2, ['Margherita', 'Calabresa'], 'Em preparo'],
    [9, 'G', 2, ['Mussarela', 'Portuguesa'], 'Em preparo'],
    [10, 'M', 3, ['Quatro Queijos', 'Margherita', 'Frango com Catupiry'], 'Recebido']
]

class Pizza:
    # Método construtor, usado para inicializar os atributos
    def __init__(self,nome=None,categoria=None,tipo=None,ingredientes=None):
        self.nome = nome
        self.categoria = categoria
        self.tipo = tipo
        self.ingredientes = ingredientes
    # Método para imprimir as informações sobre o sabor da pizza
    def imprimirInfo(self):
        print('Nome: ', self.nome)
        print('Categoria: ', self.categoria)
        print('Tipo: ', self.tipo)
        print('Ingredientes: ', self.ingredientes)
    
class PizzaPedido:
     # Método construtor, usado para inicializar os atributos
    def __init__(self,tamanho=None,nroSabores=None,listaSabores=None,status=None):
        self.tamanho = tamanho
        self.nroSabores = nroSabores
        self.listaSabores = listaSabores
        if status == None:
            self.status = 'Recebido'
        else:
            self.status = status
    # Método para imprimir as informações sobre o sabor da pizza
    def imprimirInfo(self):
        print('Tamanho: ', self.tamanho)
        print('Nro de sabores: ', self.nroSabores)
        print('Lista de sabores: ')
        for saborPizza in self.listaSabores:
            print('- ',saborPizza)
        print('Status: ', self.status)

class SistemaPedidos:
     # Método construtor, usado para inicializar os atributos
    def __init__(self,catalogo=None,listaPedidos=None):
        self.catalogo = []
        #buscando infos da tabela de sabores e adicionando no catalogo
        for pizza in listaParaCatalogo:
            saborPizza = Pizza(pizza[0], pizza[1], pizza[2], pizza[3])
            self.catalogo.append(saborPizza)
        self.listaPedidos = []
        #buscando infos da tabela de pedidos e adicionando na lista
        for pedido in pedidosParaTestar:
            pedidoPizza = PizzaPedido(pedido[1],pedido[2], pedido[3], pedido[4])
            self.listaPedidos.append(pedidoPizza)
    

    #Método que retorna se um sabor da pizza é doce ou salgado
    def verificarCategoriaSabor(self, sabor):
        for saborPizza in self.catalogo:
            if saborPizza.nome == sabor:
                return saborPizza.categoria
        return None

    # Método para ler pedido do usuário e adicionar na lista de pedidos
    def adicionarPedido(self):
        tamanho = input('Digite o tamanho da pizza (P/M/G):')
        maxSabores = 0
        if tamanho == 'P': 
            maxSabores = 2
        elif tamanho == 'M':
            maxSabores = 3
        else:
            maxSabores = 4
        
        continuar = True
        nroSabores = 0
        saboresPedido = []
        categoria = ''

        #optei por não deixar o usuário errar o nro de sabores, simplesmente impedindo que ele possa pedir
        #mais do que as regras estipuladas entre tamanho e maxSabores
        while continuar == True and nroSabores < maxSabores:
            #Aqui o ideal seria mostrar o catálogo, mas colocarei aqui só o essencial
            print('Sabor ', nroSabores + 1,':')
            sabor = input('Digite o nome do sabor: ')
           
           #validar se não está misturando doce com salgada
            if nroSabores == 0: #primeiro sabor escolhido
                categoria = self.verificarCategoriaSabor(sabor)
                saboresPedido.append(sabor)
                nroSabores = nroSabores + 1
            else:
                categoriaPedido = self.verificarCategoriaSabor(sabor)
                if (categoriaPedido == categoria):
                    saboresPedido.append(sabor)
                    nroSabores = nroSabores + 1
                    print('Sabor adicionado com sucesso!')
                else:
                    print('Não é possível misturar pizzas doces e salgadas! Escolha outro sabor ou peça outra pizza!!')
            
            if nroSabores < maxSabores:
                resposta = input('Deseja adicionar mais um sabor? (S/N)')
                if resposta == 'N':
                    continuar = False
        
        #criando o objeto PizzaPedido
        pedido = PizzaPedido(tamanho,nroSabores,saboresPedido)
        #adicionando à lista de pedidos
        self.listaPedidos.append(pedido)
        #retornando o nro do pedido
        return len(self.listaPedidos)

    #Método para exibição do catálogo
    def exibirCatalogo(self):
        print('---------------------------')
        print('CATALOGO')
        print()
        for saborPizza in self.catalogo:
            saborPizza.imprimirInfo()
            print()
        print('---------------------------')

    #Método para exibir status de um pedido
    def exibirStatusPedido(self,nroPedido):
        if nroPedido - 1 < len(self.listaPedidos): #pequena validacao pra ver se nroPedido é valido
            return self.listaPedidos[nroPedido-1].status #por que o -1? Alguém sabe??? :)
        else:
            return 'Pedido não encontrado!'
    
    #Método para alterar o status de um pedido
    def alterarStatusPedido(self,nroPedido,novoStatus):
        if nroPedido - 1 < len(self.listaPedidos):
            self.listaPedidos[nroPedido-1].status = novoStatus
        else:
            print('Pedido não encontrado!')

    #Método para exibição da lista de pedidos
    def exibirListaDePedidos(self):
        print('---------------------------')
        print('LISTA DE PEDIDOS')
        print()
        cont = 1
        for pedido in self.listaPedidos:
            print("Nro: ", cont) #nro do pedido
            pedido.imprimirInfo()
            print()
            cont = cont + 1
        print('---------------------------')

sistema = SistemaPedidos()
sistema.exibirCatalogo()
#fazendo pedidos hard-coded
continuar = True
while continuar == True:
    nroPedido = sistema.adicionarPedido()
    print('Pedido ', nroPedido, ' realizado com sucesso!')
    resposta = input('Deseja continuar? (S/N)')
    if resposta == 'N':
        continuar = False

#verificando o status de um pedido (pedido 1)
print('Status do pedido 1: ', sistema.exibirStatusPedido(1))

#alterando o status de um pedido (pedido 1)
sistema.alterarStatusPedido(1, 'Recebido')

#listando todos os pedidos
sistema.exibirListaDePedidos()










