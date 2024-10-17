package aula17;
import java.util.Scanner;

public class Exception02 {
    public static void main(String[] args) {
        GetString dataString = new GetString();
        GetInt dataInt = new GetInt();
        GetFloat dataFloat = new GetFloat();
        GetChar dataChar = new GetChar();

        try {
            dataString.getString();
        } catch (Exception e) {
            System.out.println("Isso não é uma String");
        }

        try {
            dataInt.getInt();
        } catch (Exception e) {
            System.out.println("Isso não é um Int");
        }

        try {
            dataFloat.getFloat();
        } catch (Exception e) {
            System.out.println("Isso não é um Float");
        }

        try {
            dataChar.getChar();
        } catch (Exception e) {
            System.out.println("Isso não é um Char");
        }
    }
}

class GetString {
    private final Scanner sc = new Scanner(System.in);

    public String getString() throws Exception {
        System.out.println("Digite uma String:");
        return sc.nextLine();
    }
}

class GetInt {
    private final Scanner sc = new Scanner(System.in);

    public int getInt() throws Exception {
        System.out.println("Digite um Int:");
        return sc.nextInt();
    }
}

class GetFloat {
    private final Scanner sc = new Scanner(System.in);

    public float getFloat() throws Exception {
        System.out.println("Digite um Float:");
        return sc.nextFloat();
    }
}

class GetChar {
    private final Scanner sc = new Scanner(System.in);

    public char getChar() throws Exception {
        System.out.println("Digite um Char:");
        String input = sc.next();
        if (input.length() != 1) {
            throw new Exception("Input is not a single character");
        }
        return input.charAt(0);
    }
}