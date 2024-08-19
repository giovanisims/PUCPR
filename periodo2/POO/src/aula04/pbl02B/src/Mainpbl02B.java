import java.util.Scanner;

public class Mainpbl02B {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("What is the first term of the AP: ");
        double e_1 = sc.nextDouble();
        System.out.print("What is the common difference of the AP: ");
        double cd = sc.nextDouble();
        System.out.print("What is the number of terms in the AP: ");
        int n = sc.nextInt();
        double e_n = e_1 + (n - 1) * cd;
        System.out.println("The nth term of the AP is: " + e_n);
        double S_n = (e_1 + e_n) * n / 2;
        System.out.print("The sum of all the terms of the AP is: " + S_n);
    }
}