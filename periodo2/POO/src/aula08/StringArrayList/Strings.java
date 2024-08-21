package aula08.StringArrayList;

import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Strings {
    public static void main(String[] args) {
        ArrayList<String> stringlist = new ArrayList<>();
        Scanner input = new Scanner(System.in);
        stringlist.add("String1");
        stringlist.add("String3");
        stringlist.add("String5");
        stringlist.add("String2");
        stringlist.add("String4");

        ArrayList<String> originalList = new ArrayList<>(stringlist);

        while (true) {
            System.out.println("""
                    ********* Menu *********\

                    (1) Ordenado\

                    (2) Não Ordenado\

                    (3) Sair\

                    \s""");
            System.out.print("Opção: ");
            String choice = input.nextLine();

            switch (choice) {
                case "1":
                    Collections.sort(stringlist);
                    for (String element:stringlist){
                        System.out.println(element);
                    }
                    break;
                case "2":
                    for (String element:originalList){
                        System.out.println(element);
                    }
                    break;
                case "3":
                    System.out.println("Saindo...");
                    input.close();
                    return;
                default:
                    System.out.println("Opção Inválida. Tente novamente.");
                    break;
            }
        }
    }
}