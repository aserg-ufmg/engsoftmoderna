/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Observador
*
*/

import java.util.List;
import java.util.ArrayList;
import java.util.Iterator;

/**
* Classe Subject (que faz parte da implementação interna do padrão)
* Todo sujeito deve herdar dessa classe
* Ela inclui métodos para adicionar, remover e notificar os
* observadores desse sujeito
*
*/
class Subject {
  
  private List<Observer> observers = new ArrayList<Observer>();
  
  public void addObserver(Observer observer) {
    observers.add(observer);
  }
  
  public void removeObserver(Observer observer) {
    observers.remove(observer);
  }
  
  public void notifyObservers() {
    Iterator<Observer> it = observers.iterator();
    while (it.hasNext()) {
      Observer obs= it.next();
      obs.update(this); 
    }
  }
  
}

/**
* Interface Observer (também faz parte da implementação interna do padrão)
* Todo observador deve implementar essa interface
*/
interface Observer {
  public void update(Subject s);
}


/**
* Temperatura são sujeitos (isto é, objetos que podem ser observados)
*/
class Temperatura extends Subject  {
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
class TermometroCelsius implements Observer  {
  
  public void update(Subject s) { // método chamado quando o valores de uma temperatura mudam
    double temp = ((Temperatura) s).getTemp();
    System.out.println("Temperatura Celsius: " + temp);
  }

}

public class Main {
  
  public static void  main(String [] args) {
    Temperatura t = new Temperatura();
    t.addObserver(new TermometroCelsius ());
    t.setTemp(100.0); // muda temperatura; logo, observadores são notificados
  }

}
