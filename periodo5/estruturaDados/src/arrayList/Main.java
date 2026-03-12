package arrayList;

import java.util.Arrays;

public class Main {
    public static void main(String[] args) {
        // Test 1: String list
        ArrayList<String> nomes = new ArrayList<>();
        nomes.data = new String[]{"Ana", "Bruno", "Carla"};
        nomes.capacity = nomes.data.length;

        System.out.println("=== TESTE COM STRINGS ===");
        System.out.println("Array inicial: " + Arrays.toString(nomes.toArray()));

        System.out.println("get(0): " + nomes.get(0)); // Ana
        System.out.println("get(2): " + nomes.get(2)); // Carla

        nomes.set(1, "Beatriz");
        System.out.println("Após set(1, \"Beatriz\"): " + Arrays.toString(nomes.toArray()));

        System.out.println("contains(\"Ana\"): " + nomes.contains("Ana"));       // true
        System.out.println("contains(\"Bruno\"): " + nomes.contains("Bruno"));   // false
        System.out.println("contains(\"Carla\"): " + nomes.contains("Carla"));   // true

        System.out.println("indexOf(\"Ana\"): " + nomes.indexOf("Ana"));         // 0
        System.out.println("indexOf(\"Beatriz\"): " + nomes.indexOf("Beatriz")); // 1
        System.out.println("indexOf(\"Xuxa\"): " + nomes.indexOf("Xuxa"));       // -1

        System.out.println("toArray(): " + Arrays.toString(nomes.toArray()));
        System.out.println();

        // Test 2: Integer list
        ArrayList<Integer> numeros = new ArrayList<>();
        numeros.data = new Integer[]{10, 20, 30, 40};
        numeros.capacity = numeros.data.length;

        System.out.println("=== TESTE COM INTEGERS ===");
        System.out.println("Array inicial: " + Arrays.toString(numeros.toArray()));

        System.out.println("get(1): " + numeros.get(1)); // 20
        System.out.println("get(3): " + numeros.get(3)); // 40

        numeros.set(2, 99);
        System.out.println("Após set(2, 99): " + Arrays.toString(numeros.toArray()));

        System.out.println("contains(10): " + numeros.contains(10)); // true
        System.out.println("contains(30): " + numeros.contains(30)); // false
        System.out.println("contains(99): " + numeros.contains(99)); // true

        System.out.println("indexOf(10): " + numeros.indexOf(10));   // 0
        System.out.println("indexOf(99): " + numeros.indexOf(99));   // 2
        System.out.println("indexOf(123): " + numeros.indexOf(123)); // -1

        System.out.println("toArray(): " + Arrays.toString(numeros.toArray()));
        System.out.println();

        // Test 3: Single-element list
        ArrayList<String> unica = new ArrayList<>();
        unica.data = new String[]{"Teste"};
        unica.capacity = unica.data.length;

        System.out.println("=== TESTE COM 1 ELEMENTO ===");
        System.out.println("Array inicial: " + Arrays.toString(unica.toArray()));
        System.out.println("get(0): " + unica.get(0));
        System.out.println("contains(\"Teste\"): " + unica.contains("Teste"));
        System.out.println("indexOf(\"Teste\"): " + unica.indexOf("Teste"));
    }
}
