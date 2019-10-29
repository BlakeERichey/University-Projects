import java.net.*;
import java.io.*;
import java.util.Arrays;

public class UDPServer 
{

        public static void main(String[] args) 
        {
                
                try 
                {
                        DatagramSocket serverSocket = new DatagramSocket(10999); //creates a datagram socket and binds it to port 10999
                        byte[] receiveData = new byte[1024];
                        int packet_size = 1000;
                        
                        while (true) 
                        {
                        
                                System.out.println("UDP Server waiting for client on port " + serverSocket.getLocalPort() + "...");
                                
                                DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                                        
                                serverSocket.receive(receivePacket);
                                int num_bytes = receivePacket.getLength();
                                
                                //validate packet has correct contents 
                                boolean valid = true;
                                try {
                                       if(num_bytes != packet_size) {
                                               valid = false;
                                       }
                                       
                                       if(valid) {
                                               //validate packet information
                                               for(int i = 0; i<1000; i++) {
                                                       if(i%2 == 0) {
                                                               if(receiveData[i] == 0) {
                                                                       valid = false;                                        
                                                               }
                                                       }else if((i+1)%2 == 0){
                                                               if(receiveData[i] == 1) {
                                                                       valid = false;                                  
                                                               }
                                                       }
                                               }
                                       }                        
                                } catch (IndexOutOfBoundsException ie) {
                                  ie.printStackTrace();
                                  valid = false;
                                }
                                
                                InetAddress IPAddress = receivePacket.getAddress();
                                
                                int port = receivePacket.getPort();
                                
                                //construct response
                                if(valid) {
                                  byte[] packet = new byte[num_bytes];
                                  byte val = 1;
                                  for(int i=0; i<num_bytes; i++) {
                                    packet[i] = val;
                                    if(val == 1) {
                                      val = 0;
                                    }else {
                                      val = 1;
                                    }
                                  }       
                                
                                DatagramPacket sendPacket = new DatagramPacket(packet, packet.length, IPAddress, port);
                                
                                serverSocket.send(sendPacket);
                                }else {
                                  System.out.println("Error. Invalid packet structure");
                                }
                                
                                System.out.println();
                        }
                }
                catch (IOException e)
                {
                        e.printStackTrace();
                }

        }

}
