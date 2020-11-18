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
  
  turnOn(): void { 
    console.log("Ligando projetor da Samsung");
  }

}


/**
* Classe concreta, representando um projetor da LG
*/
class ProjetorLG {

  enable(timer: number): void {
    console.log("Ligando projetor da LG em " + timer + " minutos");
  }

}

/**
* Interface para "abstrair" o tipo de projetor (Samsung ou LG)
*/
interface Projetor {
  liga(): void;
}

/**
* Adaptador de ProjetorSamsung para Projetor
* Um objeto da classe a seguir é um Projetor (pois implementa essa interface), 
* mas internamente repassa toda chamada de método para o objeto adaptado 
* (no caso, um ProjetorSamssung)
*/
class AdaptadorProjetorSamsung implements Projetor {

   private projetor: ProjetorSamsung;

   constructor(projetor: ProjetorSamsung ) {
     this.projetor = projetor;
   }

   liga(): void {
     this.projetor.turnOn(); // chama método do objeto adaptado (ProjetorSamsung)
   }
  
}

/**
* Idem classe anterior, mas agora adaptando ProjetoLG para Projetor 
*/
class AdaptadorProjetorLG implements Projetor {

   private projetor: ProjetorLG;

   constructor (projetor: ProjetorLG) {
     this.projetor = projetor;
   }

   public liga():void {
     this.projetor.enable(0); // chama método de objeto adaptado (ProjetorLG)
   }
  
}


class SistemaControleProjetores { // não tem conhecimento de "projetores concretos"
  
  init(projetor: Projetor): void {
    projetor.liga();  // liga qualquer projetor, sem precisar saber se é Samsung ou LG
  }

}

let samsung: AdaptadorProjetorSamsung = new AdaptadorProjetorSamsung(new ProjetorSamsung());
let lg: AdaptadorProjetorLG  = new AdaptadorProjetorLG(new ProjetorLG());
let scp: SistemaControleProjetores = new SistemaControleProjetores();
scp.init(samsung); // recebem como parâmetros objetos adaptadores, 
scp.init(lg);      // que possuem internamente objetos (isto é, projetores) concretos
