package aula14;

public class Comida {
    public static void main(String[] args){
        Pizza pizza1 = new Pizza("Portuguesa");
        Pizza pizza2 = new Pizza("Baiana");

        Steak steak1 = new Steak("Picanha");
        Steak steak2 = new Steak("Maminha");

        Bread bread1 = new Bread("Pão De Queijo");
        Bread bread2 = new Bread("Francês");

        cook(pizza1);
        cook(pizza2);
        cook(steak1);
        cook(steak2);
        cook(bread1);
        cook(bread2);
    }

    public static void cook(Pizza pi) {
        System.out.println("Assando a pizza");
        pi.showMessage();
    }

    public static void cook(Steak s) {
        System.out.println("Assando o bife");
        s.showMessage();
    }

    public static void cook(Bread br) {
        System.out.println("Assando o pão");
        br.showMessage();
    }
}

class Pizza {
    private final String flavor;

    Pizza(String flavor) {
        this.flavor = flavor;
    }

    public void showMessage() {
        System.out.printf("Pizza sabor %s%n%n", flavor);
    }
}

class Steak {
    private final String cut;

    Steak(String cut) {
        this.cut = cut;
    }

    public void showMessage() {
        System.out.printf("Bife com o corte%n%n", cut);
    }
}

class Bread {
    private final String type;

    Bread(String type) {
        this.type = type;
    }

    public void showMessage() {
        System.out.printf("Pão do tipo%n%n", type);
    }
}