class MinhaClasse:
    def exemplo(self, *args, **kwargs):
        if 'arg2' in kwargs:
            return args[0] + kwargs['arg2']
        else:
            return args[0]
        
objeto = MinhaClasse()

print(objeto.exemplo(5))  # Chamada do Caso 1
print(objeto.exemplo(5, arg2=3))  # Chamada do Caso 2