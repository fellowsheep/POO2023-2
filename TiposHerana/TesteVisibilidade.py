class Coisa:
    def __init__(self):
        self.publico = None
        self._protegido = None
        self.__privado = None
        print('Coisa foi criada')
    
class CoisaDerivada:
    def __init__(self):
        super().__init__()
        ('Coisa derivada foi criada')

coisa = Coisa()
coisaDerivada = CoisaDerivada()

#-------------------------------
coisa.publico = 'A'
coisa._protegido = 'E'
coisa.__privado = 'B'
print(coisa._protegido)
print(coisa.__privado)
#-------------------------------
coisaDerivada.publico = 'C'
coisaDerivada.__privado = 'D'
coisaDerivada._protegido = 'F'
print(coisaDerivada.__privado)
print(coisaDerivada._protegido)
