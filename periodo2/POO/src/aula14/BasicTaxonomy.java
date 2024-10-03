package aula14;

public class BasicTaxonomy {
    public static void main(String[] args) {
        Dog dog = new Dog(10.5f, 5, 4, "Marrom");
        Kangaroo kangaroo = new Kangaroo(55.0f, 3, 2, "Cinza");
        Snake snake = new Snake(2.3f, 2, 0, "Verde");
        Turtle turtle = new Turtle(1.5f, 10, 4, "Marrom");
        ClownFish clownFish = new ClownFish(0.2f, 1, 0, "Laranja");
        Kynguo kynguo = new Kynguo(0.1f, 1, 0, "Dourado");
        Chicken chicken = new Chicken(2.0f, 2, 2, "Branco");
        Macaw macaw = new Macaw(1.0f, 4, 2, "Azul");

        dog.buryBone();
        dog.wagTail();
        kangaroo.usePouch();
        kangaroo.move();
        snake.move();
        turtle.move();
        clownFish.releaseBubbles();
        kynguo.releaseBubbles();
        chicken.buildNest();
        macaw.buildNest();
    }
}

abstract class Animal {
    protected float weight;
    protected int age;
    protected int limbs;

    public Animal(float weight, int age, int limbs) {
        this.weight = weight;
        this.age = age;
        this.limbs = limbs;
    }

    abstract void move();
    abstract void feed(String food);
    abstract void makeSound();
}

class Reptile extends Animal {
    private String scaleColor;

    public Reptile(float weight, int age, int limbs, String scaleColor) {
        super(weight, age, limbs);
        this.scaleColor = scaleColor;
    }

    @Override
    void move() {}

    @Override
    void feed(String food) {}

    @Override
    void makeSound() {}
}

class Mammal extends Animal {
    protected String furColor;

    public Mammal(float weight, int age, int limbs, String furColor) {
        super(weight, age, limbs);
        this.furColor = furColor;
    }

    @Override
    void move() {}

    @Override
    void feed(String food) {}

    @Override
    void makeSound() {}
}

class Fish extends Animal {
    protected String scaleColor;

    public Fish(float weight, int age, int limbs, String scaleColor) {
        super(weight, age, limbs);
        this.scaleColor = scaleColor;
    }

    public void releaseBubbles() {
        System.out.println("Soltando bolhas");
    }

    void move() {}

    void feed(String food) {}

    void makeSound() {}
}

class Bird extends Animal {
    protected String featherColor;
    public Bird(float weight, int age, int limbs, String featherColor) {
        super(weight, age, limbs);
        this.featherColor = featherColor;
    }

    public void buildNest() {
        System.out.println("Construindo o ninho");
    }

    void move() {}

    void feed(String food) {}

    void makeSound() {}
}


class Dog extends Mammal {

    public Dog(float weight, int age, int limbs, String furColor) {
        super(weight, age, limbs, furColor);
    }
    public void buryBone() {
        System.out.println("O osso foi enterrado");
    }
    public void wagTail() {
        System.out.println("Abanando o rabo");
    }
}

class Kangaroo extends Mammal {
    public Kangaroo(float weight, int age, int limbs, String furColor) {
        super(weight, age, limbs, furColor);
    }
    public void usePouch() {
        System.out.println("Usando a bolsa");
    }

    void move() {
        System.out.println("O canguru está pulando");
    }
}


class Snake extends Reptile {
    public Snake(float weight, int age, int limbs, String scaleColor) {
        super(weight, age, limbs, scaleColor);
    }
}

class Turtle extends Reptile {
    public Turtle(float weight, int age, int limbs, String scaleColor) {
        super(weight, age, limbs, scaleColor);
    }
}


class ClownFish extends Fish {
    public ClownFish(float weight, int age, int limbs, String scaleColor) {
        super(weight, age, limbs, scaleColor);
    }
}

class Kynguo extends Fish {
    public Kynguo(float weight, int age, int limbs, String scaleColor) {
        super(weight, age, limbs, scaleColor);
    }
}


class Chicken extends Bird {
    public Chicken(float weight, int age, int limbs, String featherColor) {
        super(weight, age, limbs, featherColor);
    }
}

class Macaw extends Bird {
    public Macaw(float weight, int age, int limbs, String featherColor) {
        super(weight, age, limbs, featherColor);
    }
}