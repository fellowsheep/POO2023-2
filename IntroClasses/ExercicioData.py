class Data:
    #Atributo da classe
    nomesMeses = ['Janeiro', 'Fevereiro', 'Marco', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    
    #Método construtor
    def __init__(self,dia,mes,ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def imprimirData(self):
        print(self.dia,'/',self.mes,'/',self.ano)

    def imprimirDataPorExtenso(self,cidade):

        strmes = self.nomesMeses[int(self.mes)-1]

        if self.mes == 1:
            strmes = 'Janeiro'
        elif self.mes == 2:
            strmes = 'Fevereiro'
        elif self.mes == 3:
            strmes = 'Marco'
        elif self.mes == 4:
            strmes = 'Abril'
        elif self.mes == 5:
            strmes = 'Maio'
        elif self.mes == 6:
            strmes = 'Junho'
        elif self.mes == 7:
            strmes = 'Julho'
        elif self.mes == 8:
            strmes = 'Agosto'
        elif self.mes == 9:
            strmes = 'Setembro'
        elif self.mes == 10:
            strmes = 'Outubro'
        elif self.mes == 11:
            strmes = 'Novembro'
        elif self.mes == 12:
            strmes = 'Dezembro'
        print(cidade,' , ',self.dia, ' de ', strmes, ' de ', self.ano)    

data = Data(24,8,2023)

data.imprimirData()
data.imprimirDataPorExtenso('Porto Alegre')