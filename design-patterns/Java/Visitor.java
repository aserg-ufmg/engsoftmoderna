/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Visitor
*
*/

import java.util.ArrayList;
import java.util.List;

/**
* Veiculo é a raiz de uma hierarquia de classes
* Todas as classes dessa hierarquia aceitam (método accept) visitas de objetos "Visitor"
* Ou seja, Veiculos e suas subclasses estão abertas para tais visitas
* Mas elas não sabem exatamente o que o Visitor vai fazer com o seus dados
*
*/

abstract class Veiculo {
   private String placa;    

  public Veiculo(String placa) {
     this.placa = placa;
  }
  
  public String getPlaca() {
     return placa;  
  }
   
  abstract public void accept(Visitor v);

}


class Carro extends Veiculo {
   
  public Carro (String placa) {
     super(placa);  
  }
  
  
  public void accept(Visitor v) {
     v.visit(this);  // compilador já conhece o tipo de this (= Carro)
  }  // porém, a chamada é dinâmica, pois diversas classes podem implementar a interface Visitor

}

class Onibus extends Veiculo {

  public Onibus (String placa) {
     super(placa);  
  }    
  
  public void accept(Visitor v) {
    v.visit(this);
  }

}

/**
* A interface Visitor deve ser implementada por classes visitantes
*
*/
interface Visitor {
  void visit(Carro c);
  void visit(Onibus o);
}  

/**
* PrintVisitor é uma classe visitante
* Ela imprime a placa de Veiculos concretos (isto é, Carro e Onibus) na tela
*
*/
class PrintVisitor implements Visitor {
  
   public void visit(Carro c) { 
     System.out.println("Visitando um Carro: " + c.getPlaca()); 
       
   } 
  
   public void visit(Onibus o)  { 
     System.out.println("Visitando um Onibus: " + o.getPlaca()); 
   } 

}


public class Main {
  
   public static void main(String[] args) {
      List<Veiculo> list = new ArrayList<Veiculo>();
      list.add(new Carro("C1"));
      list.add(new Onibus("O1"));
      list.add(new Carro("C2"));
      list.add(new Onibus("O2"));
     
      // Vamos "visitar", com um PrintVisitor, cada Veiculo da lista
      PrintVisitor visitor = new PrintVisitor();
      for (Veiculo veiculo: list) {
        veiculo.accept(visitor);
      }
     
      // Benefício do padrão Visitor:
      // Podemos implementar uma outra classe Visitor sem ter que mexer na implementação
      // da classe Veiculo e de suas subclasses. Em seguinda, podemos usar esse Visitor 
      // para visitar todos os veículos da nossa lista.
   }    

}