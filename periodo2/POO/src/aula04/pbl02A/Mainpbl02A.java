import java.util.Scanner;
import java.lang.Math;

public class Mainpbl02A {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Type a: ");
        double a = sc.nextDouble();
        System.out.print("Type b: ");
        double b = sc.nextDouble();
        if (a <= b) {
            System.out.print("Type n: ");
            int n = sc.nextInt();
            if (n > 0) {
                double total_area = 0;
                double x = a;
                double h = (b - a) / n;
                double y1 = f(x);
                int i = 0;
                while (i < n) {
                    x = x + h;
                    double y2 = f(x);
                    double trapezium_area = ((y1 + y2) / 2) * h;
                    total_area = total_area + trapezium_area;
                    y1 = y2;
                    i = i + 1;
                }
                System.out.println("The total area is: " + total_area);
            }
            else {
                System.out.println("n must be greater than 0");
            }
        }
        else {
            System.out.println("a must be less than or equal to b");
        }
    }
    static double f(double x) {
        return 2 * Math.sin(x) + Math.cos(x)/3;
    }
}