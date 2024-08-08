import java.util.Scanner;
import java.lang.Math;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double a = getRealVariable(sc, "a");
        double b = getRealVariable(sc, "b");
        int n = getNaturalVariable(sc, "n");
        double h = getRealVariableNoNegative(sc, "h");
        double x = getRealVariable(sc, "x");
        double y1 = getRealVariableNoNegative(sc, "y1");
        double y2 = getRealVariableNoNegative(sc, "y2");
        double trapezium_area = getRealVariableNoNegative(sc, "trapezium_area");
        double total_area = getRealVariableNoNegative(sc, "total_area");
        int i = getNaturalWithNegatives(sc, "i");
    }

    static double checkFunction
    static int getNaturalWithNegatives(Scanner sc, String variableName) {
        while (true) {
            System.out.println("Enter " + variableName + ": ");
            if (!sc.hasNextInt()) {
                System.out.println("Error: " + variableName + " must be an integer number");
                sc.next();
            } else {
                return sc.nextInt();
            }
        }
    }

    static double getRealVariable(Scanner sc, String variableName) {
        System.out.println("Enter " + variableName + ": ");
        return sc.nextDouble();
    }

    static int getNaturalVariable(Scanner sc, String variableName) {
        while (true) {
            System.out.println("Enter " + variableName + ": ");
            if (!sc.hasNextInt()) {
                System.out.println("Error: " + variableName + " must be a natural number");
                sc.next();
            } else {
                int n = sc.nextInt();
                if (n <= 0) {
                    System.out.println("Error: " + variableName + " must be a natural number");
                } else {
                    return n;
                }
            }
        }
    }

    static double getRealVariableNoNegative(Scanner sc, String variableName) {
        double value;
        while (true) {
            System.out.println("Enter " + variableName + ": ");
            if (sc.hasNextDouble()) {
                value = sc.nextDouble();
                if (value >= 0) {
                    return value;
                } else {
                    System.out.println("Error: " + variableName + " must not be negative.");
                }
            } else {
                System.out.println("Error: Invalid input. Please enter a number.");
                sc.next();
            }
        }
    }
}