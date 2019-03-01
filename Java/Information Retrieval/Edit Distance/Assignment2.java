//Blake Richey
//COSC 4315 - Information Retreival
//Dr. Leonard Brown
//This program is designed to find the edit distance from one word to another
//and generate the edit distance table according to Levenshtein Distance algorithm

import javax.swing.JOptionPane;

public class Assignment2 {

  public static void main(String[] args) {
    String word    = Input("What word do you want to find the Edit Distance from?");
    String newWord = Input("What word do you want to find the Edit Distance to?");
    String msg     = "Finding distance between " + word + " and " + newWord + ".";
    msg           += "\nLook at Table Title for Information on Words."; 
    boolean res    = Confirm(msg, "");
    
    common blake = new common();        //initialize library, would be better as a jar. Will be implemented later
    
    if(res) { //if ok is clicked
      String[] columnNames = createStringArray(word.length());
      for(int x = 0; x<word.length(); x++) {
        columnNames[x] = getLetter(word, x);
      }
 
      //X - newWord
      //Y - word
      Object[][] data = new String[word.length()+2][newWord.length()+2];
      common.initArray(data, "0"); //initialize array to all 0s
      
      //initalize first row
      for(int num = 2; num<data[0].length; num++) {
        data[0][num] = getLetter(newWord, num-2);
      }
      
      //initalize second row
      for(int num = 0; num<data[1].length; num++) {
        data[1][num] = "" + (num-1);
      }
      
      //initalize first column
      for(int num = 2; num<data.length; num++) {
        data[num][0] = getLetter(word, num-2);
      }
      
    //initalize second column
      for(int num = 0; num<data.length; num++) {
        data[num][1] = "" + (num-1);
      }
      
      //reinitialize corner to empty strings
      data[0][0] = "";
      data[0][1] = "";
      data[1][0] = "";
      
      //fill in data regarding edit distance
      for(int row = 2; row<data.length; row++) {
        for(int col = 2; col<data[row].length; col++) {
          //possibile edit distances, Levenshtein Distance algorithm
          int val1 = common.stringToInt(data[row-1][col-1].toString());
          int val2 = common.stringToInt(data[row-1][col].toString());
          int val3 = common.stringToInt(data[row][col-1].toString());
          
          //if letters are the same
          if(!data[row][0].toString().equals(data[0][col].toString())) {
            val1++;
          }
          
          int[] vals = {val1, val2+1, val3+1};
          int min = common.findMin(vals);       //minimum distance to arrive and new string, per cell
          data[row][col] = "" + min;
        }
      }
      
      //generate table, then render with title
      Table newTable = new Table(newWord.length()+2, data);
      String title = "X - " + newWord + ", Y - " + word;
      newTable.renderTable(newTable, title);
    }
  }
  
  public static String Input(String name) {
    String input = JOptionPane.showInputDialog(null, name);
    return input;
  }
  
  public static Boolean Confirm(String name, String val) {
    boolean rv = false;
    int res = JOptionPane.showConfirmDialog(null, name + "\n" + val, null, 2);
    if(res == 0) { //answer yes
      rv = true;
    }
    return rv;
  }
  
  public static String[] createStringArray(int size) {
    String[] arr = new String[size];
    return arr;
  }
  
  //prints out all elements of an array
  public static void spit(String[] arr) {
    String rv = "";
    int length = arr.length;
    for(int x = 0; x < length; x++) {
      if(rv != "") { rv += ", " + arr[x]; }
      else { rv = arr[x]; }
    }
    System.out.println(rv);
  }
  
  //returns the index letter of a string as a string
  public static String getLetter(String string, int index) {
    return string.substring(index, index+1);
  }
}