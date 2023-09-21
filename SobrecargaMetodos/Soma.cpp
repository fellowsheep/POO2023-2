#include <iostream>
#include <string>

class MinhaClasse {
public:
    int soma(int a, int b) {
        return a + b;
    }

    std::string soma(std::string a, std::string b) {
        return a + b;
    }
};

int main() {
    MinhaClasse minhaInstancia;

    // Soma de inteiros
    int somaInt = minhaInstancia.soma(5, 3);
    std::cout << "Soma de inteiros: " << somaInt << std::endl;

    // Concatenação de strings
    std::string concatStr = minhaInstancia.soma("Hello", " World");
    std::cout << "Concatenação de strings: " << concatStr << std::endl;

    return 0;
}

