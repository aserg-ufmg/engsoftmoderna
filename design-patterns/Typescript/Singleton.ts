/**
 * Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
 * Prof. Marco Tulio Valente
 *
 * Exemplo do padrão de projeto Singleton
 *
 */

/**
 * A classe Logger é um Singleton.
 * Logo, por construção, poderá existir no máximo uma instância (objeto)
 * dessa classe.
 */
class Logger {
  private constructor() {} // Proíbe clientes de chamar new Logger()

  private static instance: Logger | null = null;

  public static getInstance(): Logger {
    if (this.instance === null)
      // 1ª vez que chama-se getInstance
      this.instance = new Logger();

    return this.instance;
  }

  public log(...args: any): void {
    console.log(...args);
  }
}

function teste() {
  // Logger = new Logger(); => daria um erro de compilação
}

function f(): void {
  const log: Logger = Logger.getInstance();
  log.log(`Executando f ${log}`);
}

function g(): void {
  const log: Logger = Logger.getInstance();
  log.log(`Executando g ${log}`);
}

function h(): void {
  const log: Logger = Logger.getInstance();
  log.log(`Executando h`);
}

function main() {
  f();
  g();
  h();

  console.log(
    `Observe que as 3 chamadas executaram no mesmo objeto, com ID: ${Logger.getInstance()}`
  );
}

main();
