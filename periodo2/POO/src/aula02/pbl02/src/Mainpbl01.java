import java.util.Scanner;
import java.util.Random;

// Code that I made on my own

/*
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("How many numbers should there be? ");
        int length = sc.nextInt();
        List <Integer> list = GetArrayList(length);
        CheckArrayList(list);
    }
    public static List<Integer> GetArrayList(int length) {
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

 */

// Code that I made with the help of the teacher

public class Mainpbl01 {
    public static void main(String[] args){
        int n = GetUserNumber();
        int[] vector = MakeRandomVector(n);

        for(int i : vector){
            if (i % 2 == 0){
                System.out.println(i + " is even");
            }
            else{
                System.out.println(i + " is odd");
            }
            if (i % 3 == 0){
                System.out.println(i + " is divisible by 3");
            }
        }

    }
    public static int GetUserNumber(){
        Scanner sc = new Scanner(System.in);
        System.out.println("How many numbers should there be? ");
        return sc.nextInt();
    }

    public static int[] MakeRandomVector(int n){
        int[] vector = new int[n];
        Random r = new Random();

        // for i in range(n)
        for (int i = 0; i < n; i++){
            vector[i] = r.nextInt(0,100);
        }
        return vector;
    }

}