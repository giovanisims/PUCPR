package aula11;

public class Animal01 {
    public static void main(String[] args) {
        Dog d1 = new Dog("dog1");
        Cat c1 = new Cat("cat1");
        Cat c2 = new Cat();

        d1.bark();
        c1.meow();
        c2.meow();

        d1.walk();
        c1.walk();
        c2.walk();
    }
}

class Animal {
    private final String name;
    private final String breed;

    public Animal() {
        this.name = "Nome Genérico";
        this.breed = "Raça Genérica";
    }
    public Animal(String nome) {
        this.name = nome;
        this.breed = "Raça Genérica";
    }

    public String getName() {
        return this.name;
    }

    public void walk() {
        System.out.printf("Você levou %s para caminhar. %n", this.name);
    }
}

class Dog extends Animal {
    public Dog(String name) {
        super(name);
    }
    public Dog() {
        super();
    }

    public void bark() {
        System.out.printf("%s latiu! %n", this.getName());
    }
}

class Cat extends Animal {
    public Cat(String name) {
        super(name);
    }

    public Cat() {
        super();
    }

    public void meow() {
        System.out.printf("%s miou! %n", this.getName());
    }
}