import java.net.*;
import java.io.*;
import java.util.concurrent.TimeUnit;

public class TCPClient 
{

	public static void main(String[] args) 
	{
		String serverName = "localhost";
		//String serverName = "192.168.1.135";
		int port = 8000;
		
		try 
		{
			System.out.println("Connecting to " + serverName + " on port " + port);
			
			Socket clientSocket = new Socket(serverName, port);  //create socket for connecting to server
			
			System.out.println("Just connected to " + clientSocket.getRemoteSocketAddress());
			
			OutputStream outToServer = clientSocket.getOutputStream();  //stream of bytes
			
			DataOutputStream out = new DataOutputStream(outToServer);
			
			byte[] bytes = new byte[1000];
			byte val = 1;
			for(int i=0; i<1000; i++) {
			  bytes[i] = val;
			  if(val == 1) {
			    val = 0;
			  }else {
			    val = 1;
			  }
			}			
			
			double startTime = System.nanoTime();
			double alpha = startTime;
			for(int packets_sent=0; packets_sent<10; packets_sent++) {
			  out.write(bytes);
			  out.write(bytes);
			  
			  InputStream inFromServer = clientSocket.getInputStream();  //stream of bytes
			  
			  DataInputStream in = new DataInputStream(inFromServer);
			 
			  byte[] packet = new byte[1000];
			  
			  boolean valid = true; //validate packet has correct contents 
			  try {
			    in.readFully(packet); //read contents of packet sent from client
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
			  } catch (IndexOutOfBoundsException ie) {
			    ie.printStackTrace();
			    valid = false;
			  }
			  
			  if(!valid) {
			    System.out.println("Invalid packet structure.");                                
			  }else {
			    double endTime = System.nanoTime();
			    double rtt = endTime - alpha;
			    alpha = endTime;
			    
			    System.out.println("TCP Server sent a valid response after: " + rtt/1000000 + "ms");
			  }
			}
			
			clientSocket.close();
			
		} 
		catch (IOException e)
		{
			e.printStackTrace();
		}
	}

}
