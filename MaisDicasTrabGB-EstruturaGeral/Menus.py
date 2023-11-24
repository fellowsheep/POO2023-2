import os # Biblioteca de sistema operacional do Python

class GerenciadorMenus:
   
    def __init__(self):
        pass
    
    def menuInicial(self):
        # Limpa a tela - Win/Linux/MacOS 
        os.system('cls') 
        print('----------------UNIFLIX - TELA INICIAL----------------')
        print('1 - Acessar')
        print('2 - Criar conta')
        print('0 - Sair da Aplicacao\n')
        item = input('Escolha uma opcao: ')
        return item

    def menuUsuario(self):
        # Limpa a tela - Win/Linux/MacOS 
        os.system('cls') 
        print('----------------MENU DO USUÁRIO----------------')
        print('1 - Alterar a assinatura')
        print('2 - Acessar perfil')
        print('3 - Editar perfil')
        print('4 - Remover perfil')
        print('0 - Voltar para o menu anterior\n')
        item = input('Escolha uma opcao: ')
        return item

    def menuPerfil(self):
        # Limpa a tela - Win/Linux/MacOS 
        os.system('cls') 
        print('----------------MENU DO PERFIL----------------')
        print('1 - Buscar por nome')
        print('2 - Últimos assistidos')
        print('3 - Favoritos')
        print('4 - Filmes')
        print('5 - Séries')
        print('6 - Documentários')
        print('7 - Animacoes')
        print('8 - Programas de TV')
        print('0 - Voltar para o menu anterior\n')
        item = input('Escolha uma opcao: ')
        return item