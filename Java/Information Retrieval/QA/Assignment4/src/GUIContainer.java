import java.awt.FlowLayout;

import java.io.File;

import javax.swing.*;

public class GUIContainer extends JFrame{
  
  private JLabel data;
  private GUIContainer Container;
  
  
  GUIContainer(String title){
    super(title);
    setLayout(new FlowLayout());
    data = new JLabel("Test \tMessage");  //content
    data.setToolTipText("This will show up when you hover over the message");
    //add(data);  //adds message to container
  }

}
