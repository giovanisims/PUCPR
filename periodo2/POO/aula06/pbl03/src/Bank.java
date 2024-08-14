import static java.lang.System.out;

class Client {
    private String name;
    private Double balance;

    public Client(String name, double balance) {
        this.name = name;
        this.balance = balance;
    }

    public void depositBalance(double amount) {
        this.balance += amount;
    }

    public void withdrawBalance(double amount) {
        this.balance -= amount;
    }

    public String getData() {
        return ("Nome: " + name + "\nSaldo: " + balance);
    }

}

public class Bank {
    public static void main(String[] args) {
        Client jandiraSilva = new Client("Jandira Silva", 2500.00);
        Client sandraRodrigues = new Client("Sandra Rodrigues", 1800.00);
        Client lucianaTeixeira = new Client("Luciana Teixeira", 5000.00);

        out.println(jandiraSilva.getData());
        out.println(sandraRodrigues.getData());
        out.println(lucianaTeixeira.getData());

        jandiraSilva.withdrawBalance(1000);
        out.println(jandiraSilva.getData());

        sandraRodrigues.withdrawBalance(2000);
        sandraRodrigues.depositBalance(500);
        out.println(sandraRodrigues.getData());
        sandraRodrigues.withdrawBalance(2000);
        out.println(sandraRodrigues.getData());

        lucianaTeixeira.depositBalance(1000);
        out.println(lucianaTeixeira.getData());
    }
}