package biblioteca;

public abstract class ItemBibliotecaDigital {
    protected String titulo;
    protected String autor;

    ItemBibliotecaDigital(String titulo, String autor) {
        this.titulo = titulo;
        this.autor = autor;
    }

    protected abstract String descricao();

}