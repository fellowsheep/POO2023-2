public class MinhaClasse {
    public int soma(int a, int b) {
        return a + b;
    }

    public String soma(String a, String b) {
        return a + b;
    }

    public static void main(String[] args) {
        MinhaClasse minhaInstancia = new MinhaClasse();

        // Soma de inteiros
        int somaInt = minhaInstancia.soma(5, 3);
        System.out.println("Soma de inteiros: " + somaInt);

        // Concatenação de strings
        String concatStr = minhaInstancia.soma("Hello", " World");
        System.out.println("Concatenação de strings: " + concatStr);
    }
}