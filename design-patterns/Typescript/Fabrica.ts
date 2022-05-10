/**
 * Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
 * Prof. Marco Tulio Valente
 *
 * Exemplo do padrão de projeto Fábrica
 */

/**
 * Interface e classe dos objetos que serão fabricados.
 */
interface Channel {}

class TCPChannel implements Channel {}
class UDPChannel implements Channel {}

class ChannelFactory {
  public static create(): Channel {
    console.log("Neste momento, estamos trabalhando com TCPChannel");
    return new TCPChannel();
  }
}

function f(): void {
  const c: Channel = ChannelFactory.create();
}

function g(): void {
  const c: Channel = ChannelFactory.create();
}

function h(): void {
  const c: Channel = ChannelFactory.create();
}

function main(): void {
  f();
  g();
  h();
}

main();
