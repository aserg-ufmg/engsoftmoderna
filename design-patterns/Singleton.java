/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Singleton
*
*/

/**
* A classe Logger é um Singleton.
* Logo, por construção, poderá existir no máximo uma instância (objeto)
* dessa classe.
*/
class Logger {

  private Logger() {} // proíbe clientes de chamar new Logger()

  private static Logger instance; // instância única

  public static Logger getInstance() {
    if (instance == null) // 1a vez que chama-se getInstance
      instance = new Logger();
    return instance;
  }

  public void println(String msg) {
    // registra msg na console, mas poderia ser em um arquivo
    System.out.println(msg);      
  }
  
}


class Main {
  
  void teste () {
    // Logger = new Logger(); => daria um erro de compilação
  }
  
  void f() {
    Logger log = Logger.getInstance();  
    log.println("Executando f " + log);
  }

  void g() {
    Logger log = Logger.getInstance();  
    log.println("Executando g " + log);
  }

  void h() {
    Logger log = Logger.getInstance();  
    log.println("Executando h " + log);
  }
  
  public static void main(String[] args) {
    Main m = new Main();
     m.f();
     m.g();
     m.h(); 
     System.out.println("Observe que as 3 chamadas executaram no mesmo objeto, com ID: " + Logger.getInstance());
  }
  
}
