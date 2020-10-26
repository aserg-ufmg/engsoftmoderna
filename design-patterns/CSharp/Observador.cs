/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Observador
*
*/

using System.Collections.Generic;

/**
* Classe Subject (que faz parte da implementação interna do padrão)
* Todo sujeito deve herdar dessa classe
* Ela inclui métodos para adicionar, remover e notificar os
* observadores desse sujeito
*
*/
class Subject {
  
  private List<Observer> observers = new List<Observer>();
  
  public void addObserver(Observer observer) {
    observers.Add(observer);
  }
  
  public void removeObserver(Observer observer) {
    observers.Remove(observer);
  }
  
  public void notifyObservers() {
    foreach(var observer in observers){
      observer.update(this);
    }
  }
  
}

/**
* Interface Observer (também faz parte da implementação interna do padrão)
* Todo observador deve implementar essa interface
*/
interface Observer {
  void update(Subject s);
}


/**
* Temperatura são sujeitos (isto é, objetos que podem ser observados)
*/
class Temperatura : Subject  {
   private double temp;
   
   public double getTemp() {
     return temp;
   }
  
   public void setTemp(double temp) {
     this.temp = temp;
     notifyObservers(); // notifica os meus observadores
   }
  
}


/**
* TermometroCelsius são observadores (de Temperatura)
*/
class TermometroCelsius : Observer  {
  
  public void update(Subject s) { // método chamado quando o valores de uma temperatura mudam
    double temp = ((Temperatura) s).getTemp();
    System.Console.WriteLine("Temperatura Celsius: " + temp);
  }

}

public class Main {
  
  public static void  main(string[] args) {
    Temperatura t = new Temperatura();
    t.addObserver(new TermometroCelsius ());
    t.setTemp(100.0); // muda temperatura; logo, observadores são notificados
  }

}
