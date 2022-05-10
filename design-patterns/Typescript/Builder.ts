/**
 * Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
 * Prof. Marco Tulio Valente
 *
 * Exemplo do padrão de projeto Builder
 *
 */

class Livro {
  private nome: string;
  private autores: string;
  private editora: string;
  private ano: string;

  private constructor(
    nome: string,
    autores: string,
    editora: string,
    ano: string
  ) {
    this.nome = nome;
    this.autores = autores;
    this.editora = editora;
    this.ano = ano;
  }

  public toString(): string {
    return `${this.nome}. ${this.autores}, ${this.editora}, ${this.ano}`;
  }

  /**
   * Livro.Builder é uma classe interna, pública e estática de Livro.
   * Por isso, é que podemos chamar "new Livro.Builder()" diretamente,
   * sem precisar de instanciar antes um objeto do tipo Livro.
   *
   */
  public static Builder = class {
    private nome: string;
    private autores: string;
    private editora: string;
    private ano: string;

    public setNome(nome: string) {
      this.nome = nome;
      return this;
    }

    public setAutores(autores: string) {
      this.autores = autores;
      return this;
    }

    public setEditora(editora: string) {
      this.editora = editora;
      return this;
    }

    public setAno(ano: string) {
      this.ano = ano;
      return this;
    }

    public build(): Livro {
      return new Livro(this.nome, this.autores, this.editora, this.ano);
    }
  };
}

function main() {
  const esm: Livro = new Livro.Builder()
    .setNome("Engenharia Soft Moderna")
    .setEditora("UFMG")
    .setAno("2020")
    .build();

  console.log(`Livro 1: ${esm.toString()}`);

  const gof = new Livro.Builder()
    .setNome("Design Patterns")
    .setAutores("Gof")
    .setAno("1995")
    .build();

  console.log(`Livro 2: ${gof.toString()}`);
}

main();
