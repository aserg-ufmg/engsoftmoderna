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
class Book {
  String nome;
  public Book(String nome) {
    this.nome = nome;
  }
}


/**
* Interface implementada pelo objeto base e pelo Proxy
*/
interface BookSearchInterface {
  Book getBook(String ISBN); 
}


/**
* Classe do objeto base
*/
class BookSearch implements BookSearchInterface {
  
  public Book getBook(String ISBN) {
    System.out.println("Pesquisando no objeto base - ISBN " + ISBN);
    if (ISBN.equals("2")) {
       return new Book("GoF");
    }  
    return null;
  }
  
}

/** 
* Classe Proxy
*/
class BookSearchProxy implements BookSearchInterface {

  private BookSearchInterface base;

  BookSearchProxy (BookSearchInterface base) {
    this.base = base;
  }

  public Book getBook(String ISBN) {
    Book book;
    System.out.println("Entrando no proxy - ISBN: " + ISBN);
    
    // A ideia aqui é que o Proxy conhece o livro que tem ISBN 1
    // Logo, ele nem precisa fazer a consulta ao objeto base
    if (ISBN.equals("1")) {
       System.out.println("Livro achado no proxy - ISBN: " + ISBN);
       book = new Book("ESM");
    }   
    else {
      System.out.println("Livro não achado no proxy; repassando chamada para objeto base - ISBN: " + ISBN);
      book = base.getBook(ISBN);
    }
    System.out.println("Saindo do Proxy");
    return book;
  }
  
}

class Main {
  
  public static void main(String[] args) {   
    BookSearch bs = new BookSearch();
    BookSearchProxy pbs;
    pbs = new BookSearchProxy(bs);
    Book b1 = pbs.getBook("1");
    System.out.println("===============");
    Book b2 = pbs.getBook("2");
  }
    
}
