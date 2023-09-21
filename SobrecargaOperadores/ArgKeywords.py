class MinhaClasse:
    def exemplo(self, arg1, arg2=None):
        if arg2 is None:
            return arg1
        else:
            return arg1 + arg2

objeto = MinhaClasse()

print(objeto.exemplo(arg1=5)) # Chamada do Caso 1
print(objeto.exemplo(arg1=5, arg2=3))  # Chamada do Caso 2