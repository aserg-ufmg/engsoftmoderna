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
public abstract class Funcionario {

   protected double salario;

   public Funcionario(double salario) {
     this.salario = salario;
   }
  
   public abstract double calcDescontosPrevidencia();
   public abstract double calcDescontosPlanoSaude();
   public abstract double calcOutrosDescontos();

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
public class FuncionarioCLT : Funcionario {
  
  public FuncionarioCLT(double salario) : base(salario) { }
  
  // implementa método abstrato
  public override double calcDescontosPrevidencia() { 
     return salario * 0.1;   // somente um exemplo
  }
  
  // implementa método abstrato
  public override double calcDescontosPlanoSaude() {
     return 100.0;
  }
  
  // implementa método abstrato 
  public override double calcOutrosDescontos() {
    return 20.0;
  }
  
}

class Main {
  
  public static void main(string[] args) {   
    FuncionarioCLT func = new FuncionarioCLT(1000);
    double salario = func.calcSalarioLiquido();
    System.Console.WriteLine("Salário Líquido: " + salario);  
  }
  
}
