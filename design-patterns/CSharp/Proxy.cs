/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Proxy
*
*/

/**
* Classe auxiliar
*/
public class Book {
  string nome;
  public Book(string nome) {
    this.nome = nome;
  }
}


/**
* Interface implementada pelo objeto base e pelo Proxy
*/
interface BookSearchInterface {
  Book getBook(string ISBN); 
}


/**
* Classe do objeto base
*/
class BookSearch : BookSearchInterface {
  
  public Book getBook(string ISBN) {
    System.Console.WriteLine("Pesquisando no objeto base - ISBN " + ISBN);
    if (ISBN.Equals("2")) {
       return new Book("GoF");
    }  
    return null;
  }
  
}

/** 
* Classe Proxy
*/
class BookSearchProxy : BookSearchInterface {

  private BookSearchInterface bookSearch;

  public BookSearchProxy (BookSearchInterface bookSearch) {
    this.bookSearch = bookSearch;
  }

  public Book getBook(string ISBN) {
    Book book;
    System.Console.WriteLine("Entrando no proxy - ISBN: " + ISBN);
    
    // A ideia aqui é que o Proxy conhece o livro que tem ISBN 1
    // Logo, ele nem precisa fazer a consulta ao objeto base
    if (ISBN.Equals("1")) {
       System.Console.WriteLine("Livro achado no proxy - ISBN: " + ISBN);
       book = new Book("ESM");
    }   
    else {
      System.Console.WriteLine("Livro não achado no proxy; repassando chamada para objeto base - ISBN: " + ISBN);
      book = bookSearch.getBook(ISBN);
    }
    System.Console.WriteLine("Saindo do Proxy");
    return book;
  }
  
}

class Main {
  
  public static void main(string[] args) {   
    BookSearch bs = new BookSearch();
    BookSearchProxy pbs;
    pbs = new BookSearchProxy(bs);
    Book b1 = pbs.getBook("1");
    System.Console.WriteLine("===============");
    Book b2 = pbs.getBook("2");
  }
    
}
