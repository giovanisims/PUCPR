package aula17;
import java.time.LocalDateTime;
import java.util.ArrayList;

public class PBL08b {
}

class Bank {
    private String name;
    private final ArrayList<CheckingAcount> accounts;

    public Bank(String name) {
        this.name = name;
        this.accounts = new ArrayList<>();
    }

    public void newAccount(int number, String password, double balance) {
        accounts.add(new CheckingAcount(number, password, balance));
    }

    public void withdraw(int number, String password, double value) throws InvalidAccountException, InvalidPasswordException, InvalidTimeException, InvalidBalanceException {
        CheckingAcount account = null;
        for (CheckingAcount acc : accounts) {
            if (acc.getNumber() == number) {
                account = acc;
                break;
            }
        }
        if (account == null) {
            throw new InvalidAccountException();
        }
        if (LocalDateTime.now().getHour() >= 22 || LocalDateTime.now().getHour() <= 8) {
            throw new InvalidTimeException();
        }
        account.withdraw(value, password);
    }
}

class CheckingAcount {
    private final int number;
    private String password;
    private double balance;

    public CheckingAcount(int number, String password, double balance) {
        this.number = number;
        this.password = password;
        this.balance = balance;
    }

    public int getNumber() {
        return number;
    }

    public void withdraw(double value, String password) throws InvalidPasswordException, InvalidBalanceException {
        if (!this.password.equals(password)) {
            throw new InvalidPasswordException();
        }
        if (value > balance) {
            throw new InvalidBalanceException();
        }
        balance -= value;
    }
}