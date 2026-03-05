public class Ebook extends ItemBibliotecaDigital implements Baixavel{
    Ebook(String titulo, String autor) {
        super(titulo, autor);
    }

    @Override
    public String Baixar() {
        return "Baixando: " + titulo;
    }

    @Override
    protected String descricao() {
        return "Descrição do livro: " + titulo;
    }
}
