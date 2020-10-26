/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Adaptador
*
*/


/**
* Classe concreta, representando um projetor da Samsung
*/
class ProjetorSamsung {
  
  public void turnOn() { 
    System.out.println("Ligando projetor da Samsung");
  }

}


/**
* Classe concreta, representando um projetor da LG
*/
class ProjetorLG {

  public void enable(int timer) {
    System.out.println("Ligando projetor da LG em " + timer + " minutos");
  }

}

/**
* Interface para "abstrair" o tipo de projetor (Samsung ou LG)
*/
interface Projetor {
  void liga();
}

/**
* Adaptador de ProjetorSamsung para Projetor
* Um objeto da classe a seguir é um Projetor (pois implementa essa interface), 
* mas internamente repassa toda chamada de método para o objeto adaptado 
* (no caso, um ProjetorSamssung)
*/
class AdaptadorProjetorSamsung implements Projetor {

   private ProjetorSamsung projetor;

   AdaptadorProjetorSamsung (ProjetorSamsung projetor) {
     this.projetor = projetor;
   }

   public void liga() {
     projetor.turnOn(); // chama método do objeto adaptado (ProjetorSamsung)
   }
  
}


/**
* Idem classe anterior, mas agora adaptando ProjetoLG para Projetor 
*/
class AdaptadorProjetorLG implements Projetor {

   private ProjetorLG projetor;

   AdaptadorProjetorLG (ProjetorLG projetor) {
     this.projetor = projetor;
   }

   public void liga() {
     projetor.enable(0); // chama método de objeto adaptado (ProjetorLG)
   }
  
}


class SistemaControleProjetores { // não tem conhecimento de "projetores concretos"
  
  void init(Projetor projetor) {
    projetor.liga();  // liga qualquer projetor, sem precisar saber se é Samsung ou LG
  }

}

class Main {
  
  public static void main(String[] args) {
     AdaptadorProjetorSamsung samsung = new AdaptadorProjetorSamsung(new ProjetorSamsung());
     AdaptadorProjetorLG lg = new AdaptadorProjetorLG(new ProjetorLG());
     SistemaControleProjetores scp = new SistemaControleProjetores();
     scp.init(samsung); // recebem como parâmetros objetos adaptadores, 
     scp.init(lg);      // que possuem internamente objetos (isto é, projetores) concretos
  }

}
