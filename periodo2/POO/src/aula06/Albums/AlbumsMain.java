public class AlbumsMain {
    public static void main(String[] args) {
        Album album = new Album("Hip-Hop", 2024, "Favorites", "Me");

        album.songs[0] = new Music("The Heart Part 5", 5.32);
        album.songs[1] = new Music("HUMBLE.", 2.57);
        album.songs[2] = new Music("Alright", 3.39);
        album.songs[3] = new Music("Backseat Freestyle", 3.33);
        album.songs[4] = new Music("Money Trees", 6.27);

        System.out.printf("Genêro: %s | Ano: %s | Nome: %s | Artista(s): %s %n%n",
                            album.genre, album.year, album.name, album.artist);

        for (Music song : album.songs) {
            System.out.println(song.playMusic());
        }

    }
}

class Album {
    String genre;
    int year;
    String name;
    String artist;
    public Music[] songs = new Music[5];

    Album(String genre, int year, String name, String artist) {
        this.genre = genre;
        this.year = year;
        this.name = name;
        this.artist = artist;
    }
}

class Music {
    String title;
    double length;

    Music(String title, double length) {
        this.title = title;
        this.length = length;
    }

    String playMusic() {
        return String.format("Título: %s | Duração: %s",
                                    title, length);
    }
}