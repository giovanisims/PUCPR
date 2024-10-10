package aula16;

public class PBL07 {
    public static void main(String[] args) {
        Batman batman = new Batman(true, 0, 0, 0, 0);
        JamesBond jamesBond = new JamesBond(true, 0, 0, 0, 0);
        Joker joker = new Joker(true, 0, 0, 0, 0);
        Penguin penguin = new Penguin(true, 0, 0, 0, 0);
        Goldfinger goldfinger = new Goldfinger(true, 0, 0, 0, 0);
        DrNo drNo = new DrNo(true, 0, 0, 0, 0);

        batman.run(10.5f, 20.3f);
        batman.leap(5.0f);
        batman.shoot();

        jamesBond.run(15.0f, 25.0f);
        jamesBond.leap(7.0f);
        jamesBond.shoot();

        joker.run(5.0f, 10.0f);
        joker.leap(3.0f);
        joker.shoot();

        penguin.run(8.0f, 12.0f);
        penguin.leap(4.0f);
        penguin.shoot();

        goldfinger.run(20.0f, 30.0f);
        goldfinger.leap(10.0f);
        goldfinger.shoot();

        drNo.run(18.0f, 28.0f);
        drNo.leap(9.0f);
        drNo.shoot();

        batman.die();
        jamesBond.die();
        joker.die();
        penguin.die();
        goldfinger.die();
        drNo.die();
    }
}

abstract class Character {
    protected boolean alive;
    protected float position_x;
    protected float position_y;
    protected float position_z;
    protected int color;

    Character(boolean alive, float position_x, float position_y, float position_z, int color){
        this.alive = alive;
        this.position_x = position_x;
        this.position_y = position_y;
        this.position_z = position_z;
        this.color = color;
    }

    public void run(float x, float y) {}
    public void leap(float z) {}
    public void shoot() {}
    public void die() {
        this.alive = false;
        System.out.println("Morreu");
    }
}

abstract class Hero extends Character {

    Hero(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void run(float x, float y) {
        System.out.printf("%s correndo%n", this.getClass().getSimpleName());
    }

    @Override
    public void leap(float z) {
        System.out.printf("%s pulando%n", this.getClass().getSimpleName());
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

}

abstract class Villain extends Character {

    Villain(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void run(float x, float y) {
        System.out.printf("%s correndo%n", this.getClass().getSimpleName());
    }

    @Override
    public void leap(float z) {
        System.out.printf("%s pulando%n", this.getClass().getSimpleName());
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }
}

class Batman extends Hero implements Camouflage {
    Batman(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

    public void camouflage(int color) {
        this.color = color;
        System.out.printf("%s camuflando%n", this.getClass().getSimpleName());
    }
}

class JamesBond extends Hero {
    JamesBond(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

    public void leap() {}
}

abstract class Robber extends Villain {

    Robber(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

    public void leap() {}
}

abstract class Terrorist extends Villain {

    Terrorist(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }
}

class Joker extends Robber {

    Joker (boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }
}

class Penguin extends Robber {

    Penguin (boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

    @Override
    public void run(float x, float y) {
        System.out.printf("%s correndo%n", this.getClass().getSimpleName());
    }
}

class Goldfinger extends Terrorist implements Personify {
    private Hero hero;
    Goldfinger (boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

    public void leap() {}
    public void camouflage(int color) {}
    public void personify(Hero h) {
        this.hero = h;
        System.out.println("Personificando");
    }
}

class DrNo extends Terrorist {

    DrNo(boolean alive, float position_x, float position_y, float position_z, int color){
        super(alive, position_x, position_y, position_z, color);
    }

    @Override
    public void shoot() {
        System.out.printf("%s atirando%n", this.getClass().getSimpleName());
    }

    public void leap() {}
    public void run(float x, float y) {
        System.out.printf("%s correndo%n", this.getClass().getSimpleName());
    }
}

interface Camouflage {
    void camouflage(int color);
}

interface Personify extends Camouflage {
    void personify(Hero h);
}