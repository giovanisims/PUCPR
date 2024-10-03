package aula14;

public class Sports {
    public static void main(String[] args){
        RadicalSports rad1 = new RadicalSports();
        RadicalSports rad2 = new RadicalSports();

        Skate skate1 = new Skate();
        Skate skate2 = new Skate();

        Surf surf1 = new Surf();
        Surf surf2 = new Surf();

        Scooter scooter1 = new Scooter();
        Scooter scooter2 = new Scooter();

        rad1.moves();
        rad2.moves();

        skate1.moves();
        skate2.moves();

        surf1.manobras();
        surf2.manobras();

        scooter1.moves();
        scooter2.moves();
    }
}

class RadicalSports {
    public void moves() {
        System.out.println("Adrenalina a mil...\n");
    }
}

class Skate extends RadicalSports {
    public void moves() {
        System.out.printf("Manobra de skate 1%nManobra de skate 2%nManobra de skate 3%n%n");
    }
}

class Surf extends RadicalSports {
    public void manobras() {
        System.out.printf("Manobra de surf 1%nManobra de surf 2%nManobra de surf 3%n%n");
    }
}

class Scooter extends RadicalSports {
    public void moves() {
        System.out.printf("Manobra de patinete 1%nManobra de patinete 2%nManobra de patinete 3%n%n");
    }
}