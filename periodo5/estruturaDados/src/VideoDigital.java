public class VideoDigital extends ItemBibliotecaDigital implements Baixavel, Visualizavel{

    VideoDigital(String titulo, String autor) {
        super(titulo, autor);
    }

    @Override
    public String Baixar() {
        return "Baixando: " + titulo;
    }

    @Override
    public String Visualizar() {
        return "Visualizando: " + titulo;
    }

    @Override
    protected String descricao() {
        return "Descrição do livro: " + titulo;
    }
}
