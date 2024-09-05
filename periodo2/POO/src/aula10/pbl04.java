package aula10;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class pbl04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Book book1 = new Book(1, "title1", 2000, "publisher1", "author1", 100, true);
        Book book2 = new Book(2, "title2", 2000, "publisher2", "author1", 100, false);
        Book book3 = new Book(3, "title3", 2000, "publisher3", "author3", 100, false);

        Book book4 = new Book(4, "title1", 2000, "publisher1", "author1", 100, true);
        Book book5 = new Book(5, "title2", 2000, "publisher2", "author1", 100, true);
        Book book6 = new Book(6, "title3", 2000, "publisher3", "author3", 100, false);

        Book book7 = new Book(7, "title1", 2000, "publisher1", "author1", 100, false);
        Book book8 = new Book(8, "title2", 2000, "publisher2", "author1", 100, false);
        Book book9 = new Book(9, "title3", 2000, "publisher3", "author3", 100, false);

        Book book10 = new Book(10, "title1", 2000, "publisher1", "author1", 100, true);
        Book book11 = new Book(11, "title2", 2000, "publisher2", "author1", 100, true);
        Book book12 = new Book(12, "title3", 2000, "publisher3", "author3", 100, true);

        Shelf shelf1 = new Shelf(new ArrayList<>(), "shelf1");
        shelf1.addBook(book1);
        shelf1.addBook(book2);
        shelf1.addBook(book3);

        Shelf shelf2 = new Shelf(new ArrayList<>(), "shelf2");
        shelf2.addBook(book4);
        shelf2.addBook(book5);
        shelf2.addBook(book6);

        Shelf shelf3 = new Shelf(new ArrayList<>(), "shelf3");
        shelf3.addBook(book7);
        shelf3.addBook(book8);
        shelf3.addBook(book9);

        Shelf shelf4 = new Shelf(new ArrayList<>(), "shelf4");
        shelf4.addBook(book10);
        shelf4.addBook(book11);
        shelf4.addBook(book12);

        Library library1 = new Library(new ArrayList<>(), "library1");
        library1.addShelf(shelf1);
        library1.addShelf(shelf2);

        Library library2 = new Library(new ArrayList<>(), "library2");
        library2.addShelf(shelf3);
        library2.addShelf(shelf4);

        ArrayList<Library> libraries = new ArrayList<>();
        libraries.add(library1);
        libraries.add(library2);

        HashMap<Integer, Book> bookMap = new HashMap<>();
        for (Library library : libraries) {
            for (Shelf shelf : library.library) {
                for (Book book : shelf.shelf) {
                    bookMap.put(book.bookID, book);
                }
            }
        }

        for (Library library : libraries) {
            System.out.printf("%s: %n", library.libraryName);
            for (Shelf shelf : library.library) {
                System.out.printf("    %s: %n", shelf.shelfName);
                for (Book book : shelf.shelf) {
                    System.out.printf("        ID: %d | Título: %s | Ano de lançamento: %d | Editora: %s | Autor: %s | Número de páginas: %d | Emprestado: %s%n",
                            book.bookID, book.title, book.year, book.publisher, book.author, book.pages, book.leased ? "Sim" : "Não");
                }
            }
        }

        while (true) {
            System.out.println("""
                    ********* Menu *********
                    (1) Alugar um livro  
                    (2) Devolver um livro  
                    (3) Sair  
                    """);
            System.out.print("Opção: ");
            int option = sc.nextInt();

            switch (option) {
                case 1:
                    System.out.println("Digite o ID do livro que deseja alugar: ");
                    int choice = sc.nextInt();
                    Book chosenBook = bookMap.get(choice);
                    if (chosenBook != null && !chosenBook.leased) {
                        System.out.printf("Título do livro escolhido: %s%n", chosenBook.title);
                        chosenBook.leased = true;
                    } else {
                        System.out.println("ID inválido, ou o livro está alugado");
                    }
                    break;
                case 2:
                    System.out.println("Digite o ID do livro que deseja devolver: ");
                    int returnChoice = sc.nextInt();
                    Book returnBook = bookMap.get(returnChoice);
                    if (returnBook != null && returnBook.leased) {
                        System.out.printf("Título do livro devolvido: %s%n", returnBook.title);
                        returnBook.leased = false;
                    } else {
                        System.out.println("ID inválido, ou o livro não está alugado");
                    }
                    break;
                case 3:
                    System.out.println("Saindo...");
                    sc.close();
                    return;
                default:
                    System.out.println("Opção Inválida. Tente novamente.");
                    break;
            }
        }
    }
}

class Book {
    public int bookID;
    public String title;
    public int year;
    public String publisher;
    public String author;
    public int pages;
    public Boolean leased;

    public Book(int bookID, String title, int year, String publisher, String author, int pages, Boolean leased) {
        this.bookID = bookID;
        this.title = title;
        this.year = year;
        this.publisher = publisher;
        this.author = author;
        this.pages = pages;
        this.leased = leased;
    }
}

class Shelf {
    public final ArrayList<Book> shelf;
    public final String shelfName;

    public Shelf(ArrayList<Book> shelf, String shelfName) {
        this.shelf = shelf;
        this.shelfName = shelfName;
    }

    public void addBook(Book book) {
        shelf.add(book);
    }
}

class Library {
    public final ArrayList<Shelf> library;
    public final String libraryName;

    public Library(ArrayList<Shelf> library, String libraryName) {
        this.library = library;
        this.libraryName = libraryName;
    }

    public void addShelf(Shelf shelf) {
        library.add(shelf);
    }
}