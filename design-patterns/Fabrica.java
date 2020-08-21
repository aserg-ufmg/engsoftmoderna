/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Fábrica
*
*/

/**
* Interface e classe dos objetos que serão fabricados.
*/

interface Channel {}

class TCPChannel implements Channel {}

class UDPChannel implements Channel {}


/**
* A classe ChannelFactory implementa um método fábrica estático.
* Isto é, um método que centraliza a criação de objetos que
* implementam a interface Channel
*
* Se amanhã quisermos que o sistema use UDPChannel, basta
* mudar a implementação de create()
*/

class ChannelFactory {
  
  public static Channel create() { // método fábrica estático
    System.out.println("Neste momento, estamos trabalhando com TCPChannel");
    return new TCPChannel();
  }

}

public class Main { 

  void f() {
    Channel c = ChannelFactory.create();  
  }

  void g() {
    Channel c = ChannelFactory.create();
  }
  
  void h() {
    Channel c = ChannelFactory.create();
  }
  
  public static void main(String [] args) {
     Main m = new Main();
     m.f();
     m.g();
     m.h(); 
  }

}