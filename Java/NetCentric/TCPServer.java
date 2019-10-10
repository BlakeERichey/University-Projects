import java.net.*;
import java.io.*;

public class TCPServer 
{
	
	public static void main(String[] args) 
	{
				
		ServerSocket serverSocket;
		
		try 
		{
		
			   serverSocket = new ServerSocket(8000); //creates a socket and binds it to port 9999
			   //serverSocket = new ServerSocket(0); //creates a socket and binds it to next available port 
			   
			   System.out.println("TCP Server waiting for client on port " + serverSocket.getLocalPort() + "...");
			   
			   Socket connectionSocket = serverSocket.accept();  //listens for connection and 
			   // creates a connection socket for communication
			   System.out.println("Just connected server port # " + connectionSocket.getLocalSocketAddress() + " to client port # " + connectionSocket.getRemoteSocketAddress());
			   double timeout = System.currentTimeMillis();
			   while (true)
			   {
			     try {
//			           System.out.println("Elapsed Time:" + (System.currentTimeMillis() - timeout));
				   if(System.currentTimeMillis() - timeout > 10000) {
				     timeout = System.currentTimeMillis();
				     throw new SocketException();
				   }
				   DataInputStream in = new DataInputStream(connectionSocket.getInputStream()); //get incoming data in bytes from connection socket
				   
				   byte[] packet = new byte[1000];
				   in.readFully(packet); //read contents of packet sent from client
				   boolean valid = true; //received packet has correct contents 
				   for(int i = 0; i<1000; i++) {
				     if(i%2 == 0) {
				       if(packet[i] == 0) {
				         valid = false;				         
				       }
				     }else if((i+1)%2 == 0){
				       if(packet[i] == 1) {
                                         valid = false;                                  
                                       }
				     }
				   }
				   
				   System.out.println("Valid: " + valid);
				   for(int i=0; i<1000; i++) {
				     System.out.print(packet[i]);
				   }
				   System.out.println();
				   
				   System.out.println("RECEIVED: from IPAddress " + 
							connectionSocket.getInetAddress() + " and from port " + connectionSocket.getPort());
				   DataOutputStream out = new DataOutputStream(connectionSocket.getOutputStream()); //setup a stream for outgoing bytes of data
				   if(!valid) {
				     System.out.println("Invalid packet structure.");
				   }else {
				     
				     out.write(packet); //echo packet				     
				   }
				   
//				   connectionSocket.close();  //close connection socket after this exchange
				   
				   System.out.println();
			     } catch (SocketException se) {
			       connectionSocket.close();
	                       System.out.println("TCP Server waiting for client on port " + serverSocket.getLocalPort() + "...");
	                           
	                       connectionSocket = serverSocket.accept();  //listens for connection and 
	                       // creates a connection socket for communication
	                       System.out.println("Just connected server port # " + connectionSocket.getLocalSocketAddress() + " to client port # " + connectionSocket.getRemoteSocketAddress());
	                       timeout = System.currentTimeMillis();
			     } catch (EOFException streamend) {
			       connectionSocket.close();
			       //stream fully processed
			     }
			   }
	
		} 
		catch (IOException e)
		{
				e.printStackTrace();
		}
	}

}
