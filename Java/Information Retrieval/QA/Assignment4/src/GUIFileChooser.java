import java.io.File;

import javax.swing.*;

public class GUIFileChooser {

  public static void main(String[] args) {
	GUIContainer basic = new GUIContainer("Title");     
    basic.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //close when you hit x button
    basic.setSize(1000, 600);
    
    JFileChooser chooser = new JFileChooser();
    int choice = chooser.showOpenDialog(basic);
    if(choice != JFileChooser.APPROVE_OPTION) {}
    File chosenFile = chooser.getSelectedFile();
  }
}
