/**
* Engenharia de Software Moderna - Padrões de Projeto (Cap. 6)
* Prof. Marco Tulio Valente
* 
* Exemplo do padrão de projeto Decorador
*
*/

/* 
* Decoradores implementam sempre a interface Channel
*/
interface Channel {
   void send(String msg); 
   String receive();
}


/**
* TCPChannel é uma canal de comunicação concreto (que usa protocolo TCP)
* E, por isso, é a classe final de uma cadeia de decoradores
*/
class TCPChannel implements Channel {
  
   public void send(String m) {
      System.out.println("Canal concreto (TCP) enviando > " + m);
   }
  
   public String receive() {
     System.out.println("Canal concreto (TCP) recebendo...");
     return "José";
   }

}


/**
* Todos os decoradores são subclasse de ChannelDecorator
*/
class ChannelDecorator implements Channel {
   protected Channel channel;

  public ChannelDecorator(Channel channel) {
     this.channel = channel;
  }
  
  public void send(String m) {
     channel.send(m);
  }
  
  public String receive() {
     return channel.receive();
  }
  
}

/**
* Decorador que:
*  - compacta mensagens antes de enviar (send)
*  - descompacta mensagens depois de receber (receiver)
*/
class ZipChannel extends ChannelDecorator {
  
   public ZipChannel(Channel c) {
      super(c);
   }
   
   public void send(String m)  {
      System.out.println("Decorador compactando > " + m);
      super.channel.send(m);
   }
   
   public String receive()  {
      String m = super.channel.receive();
      System.out.println("Decorador descompactando < " + m);
      return m;
   }
  
}

public class Main {
  
    public static void main(String args[]) {
       Channel c = new ZipChannel(new TCPChannel());
       c.send("Qual seu nome?");
       String r = c.receive();
       System.out.println(r);
    }   

}
