package aula08.Albums2;

import java.util.ArrayList;
import java.util.Scanner;

public class AlbumsMain2 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        ArrayList<Music> songs = new ArrayList<>();

        Album album = new Album("Hip-Hop", 2017, "Big Fish Theory", "Vince Staples");

        for (int i = 0; i < 5; i++) {
            System.out.print("Digite o nome da musica a sua duração, separados por uma vírgula: ");
            String[] parts = input.nextLine().split(",");
            String title = parts[0].trim();
            double length = Double.parseDouble(parts[1].trim());

            Music song = new Music(title, length);
            songs.add(song);
        }


        System.out.printf("Genêro: %s | Ano: %x | Nome: %s | Artista(s): %s %n%n",
                            album.genre(), album.year(), album.name(), album.artist());

        for (Music song : songs) {
            System.out.printf("Título: %s | Duração: %1.2f %n",song.title(), song.length());
        }

    }
}

record Album(String genre, int year, String name, String artist) {

}

record Music(String title, double length) {
}