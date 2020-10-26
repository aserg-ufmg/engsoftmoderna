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
public interface Channel {
   void send(string msg); 
   string receive();
}


/**
* TCPChannel é uma canal de comunicação concreto (que usa protocolo TCP)
* E, por isso, é a classe final de uma cadeia de decoradores
*/
class TCPChannel : Channel {
  
   public void send(string m) {
      System.Console.WriteLine("Canal concreto (TCP) enviando > " + m);
   }
  
   public string receive() {
     System.Console.WriteLine("Canal concreto (TCP) recebendo...");
     return "José";
   }

}


/**
* Todos os decoradores são subclasse de ChannelDecorator
*/
class ChannelDecorator : Channel {
   protected Channel channel;

  public ChannelDecorator(Channel channel) {
     this.channel = channel;
  }
  
  public virtual void send(string m) {
     channel.send(m);
  }
  
  public virtual string receive() {
     return channel.receive();
  }
  
}

/**
* Decorador que:
*  - compacta mensagens antes de enviar (send)
*  - descompacta mensagens depois de receber (receiver)
*/
class ZipChannel : ChannelDecorator {
  
   public ZipChannel(Channel c) : base(c) { }
   
   public override void send(string m)  {
      System.Console.WriteLine("Decorador compactando > " + m);
      base.channel.send(m);
   }
   
   public override string receive()  {
      string m = base.channel.receive();
      System.Console.WriteLine("Decorador descompactando < " + m);
      return m;
   }
  
}

public class Program {
  
    public static void main(string[] args) {
       Channel c = new ZipChannel(new TCPChannel());
       c.send("Qual seu nome?");
       string r = c.receive();
       System.Console.WriteLine(r);
    }   

}
