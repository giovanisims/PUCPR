package biblioteca;

public class Main {
    public static void main(String[] args) {
        var ebook = new Ebook("O Senhor dos Anéis", "J.R.R. Tolkien");
        var video = new VideoDigital("A Viagem de Chihiro", "Hayao Miyazaki");

        System.out.println(ebook.descricao());
        System.out.println(ebook.Baixar());

        System.out.println(video.descricao());
        System.out.println(video.Visualizar());
        System.out.println(video.Baixar());
    }
}