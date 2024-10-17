package aula17;

public class PBL08Teste {
    public static void main(String[] args) {
        Bank bank = new Bank("MyBank");

        bank.newAccount(1, "password1", 1000.0);
        bank.newAccount(2, "password2", 2000.0);
        bank.newAccount(3, "password3", 3000.0);
        bank.newAccount(4, "password4", 4000.0);
        bank.newAccount(5, "password5", 5000.0);

        performWithdrawal(bank, 1, "password1", 500.0);
        performWithdrawal(bank, 1, "wrongpassword", 500.0);
        performWithdrawal(bank, 1, "password1", 2000.0);
        performWithdrawal(bank, 6, "password1", 500.0);
        performWithdrawal(bank, 2, "password2", 1000.0);
        performWithdrawal(bank, 3, "password3", 2500.0);
        performWithdrawal(bank, 4, "password4", 4000.0);
        performWithdrawal(bank, 5, "password5", 5000.0);
        performWithdrawal(bank, 2, "password2", 1000.0);
        performWithdrawal(bank, 3, "password3", 500.0);
    }

    private static void performWithdrawal(Bank bank, int accountNumber, String password, double amount) {
        try {
            bank.withdraw(accountNumber, password, amount);
            System.out.printf("Saque de %.2f pela conta %d feito com sucesso%n", amount, accountNumber);
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}