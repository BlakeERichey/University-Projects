import java.net.*;
import java.io.*;
import java.util.concurrent.TimeUnit;
import java.text.DecimalFormat;

public class TCPClient 
{

	public static void main(String[] args) 
	{
		String serverName = "localhost";
//		String serverName = "129.114.230.129";
		int port = 8000;
		int packet_size = 1000;
		DecimalFormat formatter1 = new DecimalFormat("#.#");
		DecimalFormat formatter2 = new DecimalFormat("#.##");
		
		try 
		{
			System.out.println("Connecting to " + serverName + " on port " + port);
			
			Socket clientSocket = new Socket(serverName, port);  //create socket for connecting to server
			clientSocket.setSoTimeout(1000);
			
			System.out.println("Just connected to " + clientSocket.getRemoteSocketAddress());
			
			OutputStream outToServer = clientSocket.getOutputStream();  //stream of bytes
			
			DataOutputStream out = new DataOutputStream(outToServer);
			
			byte[] bytes = new byte[packet_size];
			byte val = 1;
			for(int i=0; i<packet_size; i++) {
			  bytes[i] = val;
			  if(val == 1) {
			    val = 0;
			  }else {
			    val = 1;
			  }
			}			
			
			double startTime = System.nanoTime();
			double alpha = startTime;
			int index = 0;
			double[] rtts = new double[10];
			for(int packets_sent=0; packets_sent<10; packets_sent++) {
			  try {
			    out.write(bytes);			    
			    InputStream inFromServer = clientSocket.getInputStream();  //stream of bytes
			    
			    DataInputStream in = new DataInputStream(inFromServer);
			    
			    byte[] packet = new byte[packet_size];
			    
			    boolean valid = true; //validate packet has correct contents 
			    try {
			      in.readFully(packet); //read contents of packet sent from client
			      for(int i = 0; i<packet_size; i++) {
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
			      
			      rtts[index++] = rtt;
			      System.out.println("TCP Server sent a valid response after: " + formatter2.format(rtt/1000000) + "ms");
			    }
			  } catch (SocketTimeoutException timeout) {
			    System.out.println("No response...");
			  }
			  
			}
			
			clientSocket.close();
			
			int sum = 0;
			for(int i=0; i<10; i++) {
			  sum += rtts[i];
			}
			double avg_rtt = sum/10.0/1000000;
			System.out.println("Average RTT: " + formatter2.format(avg_rtt) + "ms");
			System.out.println("Average Data Rate: " + (avg_rtt > 0?formatter1.format(80000000/avg_rtt):"0"));
			
		} 
		catch (IOException e)
		{
			e.printStackTrace();
		}
	}

}
