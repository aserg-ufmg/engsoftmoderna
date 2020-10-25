/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Visitor
*
*/

using System.Collections.Generic;

/**
* Veiculo é a raiz de uma hierarquia de classes
* Todas as classes dessa hierarquia aceitam (método accept) visitas de objetos "Visitor"
* Ou seja, Veiculos e suas subclasses estão abertas para tais visitas
* Mas elas não sabem exatamente o que o Visitor vai fazer com o seus dados
*
*/

abstract class Veiculo {
   private string placa;    

  public Veiculo(string placa) {
     this.placa = placa;
  }
  
  public string getPlaca() {
     return placa;  
  }
   
  public abstract void accept(Visitor v);

}


class Carro : Veiculo {
   
  public Carro (string placa) : base(placa) { }
  
  
  public override void accept(Visitor v) {
     v.visit(this);  // compilador já conhece o tipo de this (= Carro)
  }  // porém, a chamada é dinâmica, pois diversas classes podem implementar a interface Visitor

}

class Onibus : Veiculo {

  public Onibus (string placa) : base(placa) { }    
  
  public override void accept(Visitor v) {
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
class PrintVisitor : Visitor {
  
   public void visit(Carro c) { 
     System.Console.WriteLine("Visitando um Carro: " + c.getPlaca()); 
       
   } 
  
   public void visit(Onibus o)  { 
     System.Console.WriteLine("Visitando um Onibus: " + o.getPlaca()); 
   } 

}


public class Main {
  
   public static void main(string[] args) {
      List<Veiculo> list = new List<Veiculo>();
      list.Add(new Carro("C1"));
      list.Add(new Onibus("O1"));
      list.Add(new Carro("C2"));
      list.Add(new Onibus("O2"));
     
      // Vamos "visitar", com um PrintVisitor, cada Veiculo da lista
      PrintVisitor visitor = new PrintVisitor();
      foreach (Veiculo veiculo in list) {
        veiculo.accept(visitor);
      }
     
      // Benefício do padrão Visitor:
      // Podemos implementar uma outra classe Visitor sem ter que mexer na implementação
      // da classe Veiculo e de suas subclasses. Em seguinda, podemos usar esse Visitor 
      // para visitar todos os veículos da nossa lista.
   }    

}