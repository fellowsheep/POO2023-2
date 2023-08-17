public class Mago {
    // Atributos de classe
    static boolean possuiMagia = true;

    // Atributos de instância
    private String nome;
    private int idade;
    private String escola;

    // Método construtor
    public Mago(String nome, int idade, String escola) {
        this.nome = nome;
        this.idade = idade;
        this.escola = escola;
        System.out.println("Mago " + this.nome + " foi criado!");
    }

    // Outros métodos
    public void andar() {
        System.out.println("Estou andando");
    }

    public void falar() {
        System.out.println("Ola amigue! Meu nome é " + this.nome);
    }

    public void invocarMagia() {
        System.out.println("Invocando magia!");
    }

    // Destrutor
    @Override
    protected void finalize() {
        System.out.println("Deixou de existir!");
    }

    public static void main(String[] args) {
        Mago mago1 = new Mago("Merlin", 200, "Escola de Feitiçaria");
        mago1.andar();
        mago1.falar();
        mago1.invocarMagia();
    }
}
