/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Builder
*
*/

class Livro {
   private string nome;
   private string autores;
   private string editora;
   private string ano;
  
   private Livro (string nome, string autores, string editora, string ano) {
     this.nome = nome;
     this.autores = autores;
     this.editora = editora;
     this.ano = ano;
   }
  
   public string toString() {
     return nome + ". " + autores + "," + editora + "," + ano;      
   }
    
   /**
   * Livro.Builder é uma classe interna, pública e estática de Livro. 
   * Por isso, é que podemos chamar "new Livro.Builder()" diretamente, 
   * sem precisar de instanciar antes um objeto do tipo Livro.
   *
   */
   public class Builder {
     private string nome;
     private string autores;
     private string editora;
     private string ano; 
     
     public Builder setNome(string nome) {
        this.nome = nome;
        return this;
     }

     public Builder setAutores(string autores) {
        this.autores = autores;
        return this;
     }
     
     public Builder setEditora(string editora) {
        this.editora = editora;
        return this;
     }
     
     public Builder setAno(string ano) {
        this.ano = ano;
        return this;
     }
     
     public Livro build() {
        return new Livro(nome, autores, editora, ano); 
     }
  }
  
}


class Program {
  public static void main(string[] args) {
     Livro esm = new Livro.Builder()
                          .setNome("Engenharia Soft Moderna")
                          .setEditora("UFMG")
                          .setAno("2020")
                          .build();
     System.Console.WriteLine("Livro 1: " + esm.toString());
     
     Livro gof = new Livro.Builder()
                          .setNome("Design Patterns")
                          .setAutores("GoF")
                          .setAno("1995")
                          .build();
     System.Console.WriteLine("Livro 2: " + gof.toString());                        
  }
}