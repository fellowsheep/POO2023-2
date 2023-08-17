using System;

class Mago {
    // Atributos de classe
    public static bool possuiMagia = true;

    // Atributos de instância
    private string nome;
    private int idade;
    private string escola;

    // Método construtor
    public Mago(string nome, int idade, string escola) {
        this.nome = nome;
        this.idade = idade;
        this.escola = escola;
        Console.WriteLine("Mago " + this.nome + " foi criado!");
    }

    // Outros métodos
    public void Andar() {
        Console.WriteLine("Estou andando");
    }

    public void Falar() {
        Console.WriteLine("Ola amigue! Meu nome é " + this.nome);
    }

    public void InvocarMagia() {
        Console.WriteLine("Invocando magia!");
    }

    // Destrutor
    ~Mago() {
        Console.WriteLine("Deixou de existir!");
    }
}

class Program {
    static void Main(string[] args) {
        Mago mago1 = new Mago("Dumbledore", 180, "Escola de Magia de Hogwarts");
        mago1.Andar();
        mago1.Falar();
        mago1.InvocarMagia();
    }
}
