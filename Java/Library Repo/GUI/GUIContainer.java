import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.FlowLayout;

public class GUIContainer extends JFrame{
  
  private JLabel data;
  
  
  GUIContainer(String title){
    super(title);
    setLayout(new FlowLayout());
    data = new JLabel("Test \tMessage");  //content
    data.setToolTipText("This will show up when you hover over the message");
    add(data);  //adds message to container
  }

}
