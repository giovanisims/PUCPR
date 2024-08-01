import java.util.Scanner;
import java.util.List;
import java.util.Random;
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("How many numbers should there be? ");
        int length = sc.nextInt();
        List <Integer> list = ArrayList(length);
        CheckArrayList(list);
    }
    public static List<Integer> ArrayList(int length) {
        List<Integer> list = new ArrayList<>();
        Random random = new Random();
        for (int i = 0; i < length; i++) {
            list.add(random.nextInt(100));
        }
        return list;
    }
    public static void CheckArrayList(List<Integer> list) {
        String kind;
        String div3;
        for (int i:list){
            if (i % 2 == 0){
                kind = " Is even";
            }
            else{
                kind = " Is odd";
            }
            if (i % 3 == 0){
                div3 = " is divisible by 3";
            }
            else{
                div3 = " is not divisible by 3";
            }
            System.out.println(i + kind + div3);
        }
    }
}