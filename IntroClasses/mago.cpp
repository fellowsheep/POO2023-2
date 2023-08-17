#include <iostream>
using namespace std;

class Mago {
public:
    // Atributos de classe
    static bool possuiMagia;

    // Método construtor
    Mago(string nome, int idade, string escola) {
        // Atributos de instância
        this->nome = nome;
        this->idade = idade;
        this->escola = escola;
        cout << "Mago " << this->nome << " foi criado!" << endl;
    }

    // Outros métodos
    void andar() {
        cout << "Estou andando" << endl;
    }

    void falar() {
        cout << "Ola amigue! Meu nome é " << this->nome << endl;
    }

    void invocarMagia() {
        cout << "Invocando magia!" << endl;
    }

    // Destrutor
    ~Mago() {
        cout << "Deixou de existir!" << endl;
    }

private:
    string nome;
    int idade;
    string escola;
};

bool Mago::possuiMagia = true;

int main() {
    Mago mago1("Gandalf", 150, "Aprendizes de Merlin");
    mago1.andar();
    mago1.falar();
    mago1.invocarMagia();

    return 0;
}
