//Library of custom functions made by Blake Richey
import javax.swing.JOptionPane;

public class common {
  
  common(){
    
  }
  
  //params
  //name:       what to ask the user
  //val:        what to confirm the user meant
  //returns:    true if yes, false if no or cancel
  public static Boolean Confirm(String name, String val) {
    boolean rv = false;
    int res = JOptionPane.showConfirmDialog(null, name + "\n" + val, null, 0);
    if(res == 0) { //answer yes
      rv = true;
    }
    return rv;
  }
  
  //creates new string array of size, size
  public static String[] createStringArray(int size) {
    String[] arr = new String[size];
    return arr;
  }
  
  public static int findMax(int[] arr) {
    int max = arr[0]; //set max to first value
    
    for(int index = 0; index < arr.length;  index++) {
      int currentVal = arr[index];
      if(currentVal > max) { max = currentVal; }
    }
    
    return max;
  }
  
  public static int findMin(int[] arr) {
    int min = arr[0]; //set min to first value
    
    for(int index = 0; index < arr.length;  index++) {
      int currentVal = arr[index];
      if(currentVal < min) { min = currentVal; }
    }
    
    return min;
  }
  
  //returns the index letter of a string as a string
  public static String getLetter(String string, int index) {
    return string.substring(index, index+1);
  }
  
  //initializes arr to be val for each index
  public static Object[][] initArray(Object[][] arr, String val) {
    int rows = arr.length;
    int columns = arr[1].length;
    for(int rowNum = 0; rowNum < rows; rowNum++) {
      for(int colNum = 0; colNum < columns; colNum++) {
        arr[rowNum][colNum] = val;
      }      
    }
    return arr;
  }
  
  //takes name param to display to a GUI input box the value of name
  //returns:    string containing what the user typed
  public static String Input(String name) {
    String input = JOptionPane.showInputDialog(null, name);
    return input;
  }
  
  //quicker way to say System.out.println
  public static void log(int value) {
    System.out.println(value);
  }
  
  //quicker way to say System.out.println
  public static void log(String value) {
    System.out.println(value);
  }
  
  //prints out all elements of an array
  public static void spit(int[] arr) {
    String rv = "";
    int length = arr.length;
    for(int x = 0; x < length; x++) {
      if(rv != "") { rv += ", " + arr[x]; }
      else { rv = "" + arr[x]; }
    }
    System.out.println(rv);
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
  
  //converts value to an int. if it is not an int value return -1,000,000
  public static int stringToInt(String value) {
    try {
      int result = Integer.parseInt(value);
      return result;
    }catch(NumberFormatException err){
      return -1000000;
    }
  } 
}