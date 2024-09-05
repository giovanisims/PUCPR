package aula11;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;

public class Bank01 {
    public static void main(String[] args) {
        Bank bank = new Bank("Banco1");

        Account account1 = new SavingsAccount("contapoupanaça1", 1);
        Account account2 = new SavingsAccount("contapoupanaça2", 2);
        Account account3 = new CheckingAccount("contacorrente1", 3);
        Account account4 = new CheckingAccount("contacorrente2", 4);

        bank.addAccount(account1);
        bank.addAccount(account2);
        bank.addAccount(account3);
        bank.addAccount(account4);

        System.out.println(bank);

        account1.deposit(100);
        account2.deposit(200);
        account3.deposit(400);
        account4.deposit(800);

        System.out.println(account1);
        System.out.println(account4);

        account1.withdraw(50);
        account2.withdraw(100);
        account3.withdraw(200);
        account4.withdraw(400);

        System.out.println(account1);
        System.out.println(account4);

        account1.withdraw(1000);
        account2.withdraw(1000);
    }
}

class Bank {
    private final String name;
    private final List<Account> accounts;


    Bank(String name) {
        this.name = name;
        this.accounts = new ArrayList<>();
    }

    public String getName() {
        return this.name;
    }

    public List<Account> getAccounts() {
        return this.accounts;
    }

    public void addAccount(Account account) {
        this.accounts.add(account);
    }

    @Override
    public String toString() {
        return String.format("Nome do banco: %s | Contas afiliadas: %n %s %n", getName(), getAccounts());
    }
}

class Account {
    private final String accountHolder;
    private final int accountID;
    private double balance;
    private final LocalDate creationDate;

    Account(String accountHolder, int accountNumber) {
        this.accountHolder = accountHolder;
        this.accountID = accountNumber;
        this.creationDate = LocalDate.now();
    }

    public String getAccountHolder() {
        return accountHolder;
    }

    public int getAccountID() {
        return accountID;
    }

    public LocalDate getCreationDate() {
        return creationDate;
    }

    public double getBalance() {
        return balance;
    }

    public void withdraw(double value) {
        if (value > 0 && value <= this.balance) {
            this.balance -= value;
        } else {
            System.out.println("Você não pode retirar mais do que a conta contem");
        }
    }

    public void deposit(double value) {
        this.balance += value;
    }
}

class SavingsAccount extends Account{
    private double interestRate;

    SavingsAccount(String accountHolder, int accountID) {
        super(accountHolder, accountID);
    }

    public boolean depositInterest(double value) {
        return true;
    }

    @Override
    public String toString() {
        return String.format("Nome: %s | ID: %d | Data de criação: %s | Saldo: %.2f %n",
                getAccountHolder(), getAccountID(), getCreationDate(), getBalance());
    }
}

class CheckingAccount extends Account{
    private double MaintenanceRate;

    CheckingAccount(String accountHolder, int accountID) {
        super(accountHolder, accountID);
    }

    public boolean debitMaintenance(double value) {
        return true;
    }
    @Override
    public String toString() {
        return String.format("Nome: %s | ID: %d | Data de criação: %s | Saldo: %.2f %n",
                getAccountHolder(), getAccountID(), getCreationDate(), getBalance());
    }
}
