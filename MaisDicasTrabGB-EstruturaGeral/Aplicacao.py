from Menus import * #para poder usar as classes que estão em Menus.py
from Usuario import *

import csv

class Aplicacao:

    # Método construtor
    def __init__(self):
        self.tela = 0
        self.terminou = False
        self.menus = GerenciadorMenus()
        # Fazer todos os carregamentos pertinentes
        self.listaUsuarios = [] #LEMBRANDO QUE É UMA LISTA DE OBJETOS DO TIPO USUARIO
        self.carregarUsuarios('Dados/ExemploUsuarios.csv')
        self.carregarPerfis('ExemploPerfis.csv') #aqui vai alimentar a lista de perfis que está dentro dos objetos usuários (poderia ser chamado dentro do carregarUsuarios, inclusive)
        self.catalogoGeral = [] #Lista de objetos das classes derivadas da classe mídia (série, filme, etc)
        self.carregarCatalogo('CatalogoExemplo.csv') 
        self.carregarEpisodios('EpisodiosSeriesProgramasTVExemplo.csv') #para alimentar as séries e programas de TV

    
    # Método que possui o loop principal
    def executar(self):
        opcao = -1
        while not self.terminou:
            ##########################################
            if self.tela == 0: #tela entrada
                self.telaInicial()
            ##########################################        

            elif self.tela == 1: #tela gerenciar album
                self.telaMenuUsuario()

            ##########################################
            elif self.tela == 2: #tela gerenciar colecao
                self.telaMenuPerfil()
            #### ... assim por diante

    # Método que prepara a aplicação para seu término
    def finalizar(self):
        print('Finalizando a aplicacao!')
        # executar os salvamentos nos arquivos - Hora de atualizar os CSVs buscando as infos da self.listaUsuarios!!!
        pass

    # Metodo para imprimir mensagem de erro
    def msgErro(self, codigo):
        if codigo == 1:
            print('Opcao invalida!')
            input('Pressione qualquer tecla para continuar')

    # Processa as opções da Tela Inicial - 0
    def telaInicial(self):
        opcao = self.menus.menuInicial()
        if opcao == '0':
            self.terminou = True
        elif opcao == '1':
            self.fazerLogin()
        elif opcao == '2':
            self.cadastrarUsuario()
        else:
            self.msgErro(1)
        

    # Processa as opções da Tela Menu Usuario - 1
    def telaMenuUsuario(self):
        opcao = self.menus.menuUsuario()
        if opcao == '0':
            self.tela = 0  #muda para a tela inicial
        #elif opcao == '1':   #...chama os métodos para cada opcao
        else:
            self.msgErro(1)

     # Processa as opções da Tela Menu Perfil - 2
    def telaMenuPerfil(self):
        opcao = self.menus.menuPerfil()
        if opcao == '0':
            self.tela = 1  #muda para a tela anterior: Menu Usuario
        else:
            self.msgErro(1)

    # Metodo cadastrar usuario (implementar!)
    def cadastrarUsuario(self):
        print('Cadastrando usuario....')
        input('Pressione qualquer tecla para continuar...')

    
    # Metodo para validar e poder acessar as infos do usuario, login (implementar!)
    def fazerLogin(self):
        print('Verificando usuario e recuperando o album do usuario')
        # Leitura do user e senha, validação, armazena o objeto do usuario atual (ou o indice na lista)
        # Se conseguiu acessar, mudar para tela de Gerenciamento do Album
        self.tela = 1
        input('Pressione qualquer tecla para continuar...')

    # Método para carregar o csv de usuarios e criar a lista de objetos usuário da aplicação
    def carregarUsuarios(self,csvUsuarios):
        # Aqui faz a leitura do arquivo de usuários e alimenta a listaUsuarios
        # Abre o arquivo com as infos
        arqUsuarios = open(csvUsuarios)
        # Faz a leitora do csv, agora com o delimitador certo
        leitor = csv.reader(arqUsuarios,delimiter=';')
        # Transforma em lista 
        listaCSVUsuarios = list(leitor) #aqui temos a tabela recuperada para uma lista de listas em python
        # Nunca esqueça de fechar o arquivo!
        arqUsuarios.close()

        # Agora sim, vamos alimentar a lista de objetos usuário
        for i in range(1,len(listaCSVUsuarios)): #percorre linhas, a partir da segunda linha
            # Instancia um objeto da classe Usuario, passando por parâmetro as colunas da tabela 
            usuario = Usuario(int(listaCSVUsuarios[i][0]),listaCSVUsuarios[i][1],listaCSVUsuarios[i][2],listaCSVUsuarios[i][3])                        
            # Adiciona na lista de figurinhas
            self.listaUsuarios.append(usuario)    

        self.imprimirInfoUsuarios() #funcao pra debug

    def imprimirInfoUsuarios(self):
        for usuario in self.listaUsuarios:
            usuario.imprimirInfo()

    def carregarPerfis(self,csvPerfis):
        pass

    def carregarCatalogo(self,csvCatalogo):
        pass

    def carregarEpisodios(self,csvUsuarios):
        pass

