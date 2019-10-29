import java.net.*;
import java.io.*;
import javax.swing.JOptionPane;
import java.text.DecimalFormat;

public class UDPClient 
{

        public static void main(String[] args) 
        {
                String serverName = "localhost";
                //String serverName = "192.168.1.152";
                int port = 10999;
                int packet_size = 1000;
                DecimalFormat formatter1 = new DecimalFormat("#.#");
                DecimalFormat formatter2 = new DecimalFormat("#.##");
                
                try 
                {
                        DatagramSocket clientSocket = new DatagramSocket();
                        clientSocket.setSoTimeout(1000);
                        
                        InetAddress IPAddress = InetAddress.getByName(serverName);
                        
                      //construct packet
                        byte[] packet = new byte[packet_size];
                        byte val = 1;
                        for(int i=0; i<packet_size; i++) {
                          packet[i] = val;
                          if(val == 1) {
                            val = 0;
                          }else {
                            val = 1;
                          }
                        }
                        
                        //send + receive echo
                        double startTime = System.nanoTime();
                        double alpha = startTime; //time to subtract from after each packet sent
                        int packet_number = 0;
                        double[] rtts = new double[10];
                        
                        System.out.println("Pinging " + serverName);
                        for(int packets_sent=0; packets_sent<10; packets_sent++) {
                          try {
                        
                            DatagramPacket sendPacket = new DatagramPacket(packet, packet.length, IPAddress, port);
                            
                            clientSocket.send(sendPacket);
                            
                            byte[] receiveData = new byte[1024];
                            
                            DatagramPacket receivePacket = new DatagramPacket(receiveData, receiveData.length);
                            
                            clientSocket.receive(receivePacket);
                            
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
                            
                            if(!valid) {
                              System.out.println("Invalid packet structure.");                                
                            }else {
                              //calculate RTT
                              double endTime = System.nanoTime();
                              double rtt = endTime - alpha;
                              alpha = endTime;
                              
                              rtts[packet_number++] = rtt;
                              System.out.println("TCP Server sent a valid response after: " + formatter2.format(rtt/1000000) + "ms");
                            }
                            
                       } catch (SocketTimeoutException timeout) {
                         System.out.println("No response...");
                       }
                        
                    }
                    clientSocket.close();
                    
                    //Log Average RTT results
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
