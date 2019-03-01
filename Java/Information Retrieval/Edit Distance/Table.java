import java.awt.*;
import javax.swing.*;

//Example use:
//String[] columnNames = {"Name", "Eye-Color", "Gender"};
//
//Object[][] data = {
//    {"Bill", "Hazel", "Male"},
//    {"Mary", "Black", "Female"},
//    {"Rick", "Red", "Male"},
//    {"Janice", "Yellow", "Female"}
//};
//
//Table newTable = new Table(3, data);
//newTable.renderTable("Basic Table");

//Another:
//String[] columnNames = createStringArray(word.length());
//for(int x = 0; x<word.length(); x++) {
//  columnNames[x] = getLetter(word, x);
//}
//
////X - newWord
////Y - word
//Object[][] data = new String[word.length()+1][newWord.length()+1];
//
//Table newTable = new Table(newWord.length()+1, data);
//newTable.renderTable(newTable, "Basic Table");
//}
public class Table extends JFrame{
  JTable table;
  
  public Table() {
    setLayout(new FlowLayout());
    System.out.println("I am in this constructor");
    String[] columnNames = {"Name", "Eye-Color", "Gender"};
    
    Object[][] data = {
        {"Bill", "Hazel", "Male"},
        {"Mary", "Black", "Female"},
        {"Rick", "Red", "Male"},
        {"Janice", "Yellow", "Female"}
    };
    
    table = new JTable(data, columnNames);      //rows then columns
    table.setPreferredScrollableViewportSize(new Dimension(500, 500));  //wide, tall for cells
    table.setFillsViewportHeight(true);
    
    JScrollPane scrollPane = new JScrollPane(table);
    add(scrollPane);
  }
  
  public Table(int numCols, Object[][] data) {
    
    String[] columnNames = new String[numCols];
    for(int x = 0; x<numCols; x++) {
      columnNames[x] = String.valueOf(x);
    }
    
    table = new JTable(data, columnNames);      //rows then columns
    table.setPreferredScrollableViewportSize(new Dimension(500, 500));  //wide, tall for cells
    table.setFillsViewportHeight(true);
    
    JScrollPane scrollPane = new JScrollPane(table);
    add(scrollPane);
  }
  
  public void renderTable(String title) {
    Table gui = new Table();
    gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    gui.setSize(600, 600);
    gui.setVisible(true);
    gui.setTitle(title);
  }
  
  public void renderTable(Table gui, String title) {
    gui.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    gui.setSize(600, 600);
    gui.setVisible(true);
    gui.setTitle(title);
  }
}
