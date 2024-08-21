package aula08.ObjectsArrayList;
import java.util.ArrayList;
import java.util.Scanner;

public class Objects {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Movie> movies = new ArrayList<>();
        for (int i = 0; i < 5; i++) {
            System.out.print("Digite o título do filme a sua data de lançamento, separados por uma vírgula: ");
            String[] parts = input.nextLine().split(",");
            String title = parts[0].trim();
            int launchDate = Integer.parseInt(parts[1].trim());

            Movie movie = new Movie(title, launchDate);
            movies.add(movie);
        }
        for (Movie element: movies){
            System.out.printf("Título: %s | Data de lançamento: %x %n", element.title(), element.launchDate());
        }
    }
}

record Movie(String title, int launchDate) {
}