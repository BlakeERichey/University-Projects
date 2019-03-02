import javax.swing.JFrame;
import javax.swing.JFileChooser;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class main {

  public static void main(String[] args){
    GUIContainer basic = new GUIContainer("Title");     
    basic.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //close when you hit x button
    basic.setSize(1000, 600);
    
    JFileChooser chooser = new JFileChooser();
    int choice = chooser.showOpenDialog(basic);
    if(choice != JFileChooser.APPROVE_OPTION) {}
    File chosenFile = chooser.getSelectedFile();
    try {
      Scanner file = new Scanner(chosenFile);
      String fileContents = "";       //file contents are stored in this variable
      while(file.hasNextLine()) {
        fileContents += file.nextLine() + "\n";
      }
      System.out.println(fileContents);
    } catch (FileNotFoundException e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
    
    basic.setVisible(true);
    
  }

}
