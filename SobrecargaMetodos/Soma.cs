using System;

public class MinhaClasse
{
    public int Soma(int a, int b)
    {
        return a + b;
    }

    public string Soma(string a, string b)
    {
        return a + b;
    }

    public static void Main(string[] args)
    {
        MinhaClasse minhaInstancia = new MinhaClasse();

        // Soma de inteiros
        int somaInt = minhaInstancia.Soma(5, 3);
        Console.WriteLine("Soma de inteiros: " + somaInt);

        // Concatenação de strings
        string concatStr = minhaInstancia.Soma("Hello", " World");
        Console.WriteLine("Concatenação de strings: " + concatStr);
    }
}