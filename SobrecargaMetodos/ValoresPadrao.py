class MinhaClasse:
    def exemplo(self, arg1, arg2=None):
        if arg2 is None:
            # Caso 1: Comportamento quando arg2 não é fornecido
            return arg1
        else:
            # Caso 2: Comportamento quando arg2 é fornecido
            return arg1 + arg2
        
    def exemplo2(self, arg1, arg2=0):
        return arg1 + arg2
    
    

objeto = MinhaClasse()
print(objeto.exemplo(5))
print(objeto.exemplo(2,2))

print(objeto.exemplo2(5))
print(objeto.exemplo2(2,2))