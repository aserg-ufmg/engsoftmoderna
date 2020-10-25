/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Template Method
*
*/

/**
* Classe que implementa um Template Method (calcSalarioLiquido)
* Veja que essa classe é abstrata
*/
abstract class Funcionario {

   protected double salario;

   public Funcionario(double salario) {
     this.salario = salario;
   }
  
   abstract double calcDescontosPrevidencia();
   abstract double calcDescontosPlanoSaude();
   abstract double calcOutrosDescontos();

   /**
   * Template Method: define o esqueleto de um algoritmo
   * Ele ainda é um "template" porque os métodos chamados são abstratos
   */
   public double calcSalarioLiquido() { 
     double prev = calcDescontosPrevidencia();
     double saude = calcDescontosPlanoSaude();
     double outros = calcOutrosDescontos();
     return salario - prev - saude - outros;
   }
}

/** 
* Subclasse que implementa os métodos abstratos chamados pelo Template Method
* Ela vai herdar o template method (calcSalarioLiquido)
* Mas vai ter que implementar os métodos abstrados chamados por ele
*/
class FuncionarioCLT extends Funcionario {
  
  public FuncionarioCLT(double salario) {
     super(salario);
  }
  
  // implementa método abstrato
  double calcDescontosPrevidencia() { 
     return salario * 0.1;   // somente um exemplo
  }
  
  // implementa método abstrato
  double calcDescontosPlanoSaude() {
     return 100.0;
  }
  
  // implementa método abstrato 
  double calcOutrosDescontos() {
    return 20.0;
  }
  
}

class Main {
  
  public static void main(String[] args) {   
    FuncionarioCLT func = new FuncionarioCLT(1000);
    double salario = func.calcSalarioLiquido();
    System.out.println("Salário Líquido: " + salario);  
  }
  
}
