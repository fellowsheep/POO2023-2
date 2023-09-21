class MinhaClasse:
    def soma(self, *args):
        if len(args) == 2 and isinstance(args[0], int) and isinstance(args[1], int):
            # Soma de inteiros
            return args[0] + args[1]
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], str):
            # Concatenação de strings
            return args[0] + args[1]
        else:
            raise TypeError("Argumentos inválidos")

# Criando uma instância da classe
minha_instancia = MinhaClasse()

# Soma de inteiros
soma_int = minha_instancia.soma(5, 3)
print("Soma de inteiros:", soma_int)

# Concatenação de strings
concat_str = minha_instancia.soma("Hello", " World")
print("Concatenação de strings:", concat_str)