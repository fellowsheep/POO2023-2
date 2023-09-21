class MinhaClasse:
    def exemplo(self, arg1, arg2=None):
        if arg2 is None:
            return arg1
        else:
            return arg1 + arg2
    
    def exemplo2(self, arg1=None, arg2=None):
        if arg1 != None:
            print('Arg1 = ', arg1)
        if arg2 != None:
            print('Arg2 = ', arg2)
        
objeto = MinhaClasse()

print(objeto.exemplo(arg1=5)) # Chamada do Caso 1
print(objeto.exemplo(arg1=5, arg2=3))  # Chamada do Caso 2

print(objeto.exemplo2(arg2=3))
print(objeto.exemplo2(arg2=3,arg1=2))