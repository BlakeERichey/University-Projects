//Blake Richey
//COSC 4315-001
//Prof: Dr. Leonard Brown
//Date: Feb 1, 2019
//Prompt user for a file to read. Generates an list of tokens found in the file
//Uses PorterStemmer Algorithm to Stem words
//Stemming ignores special characters and End of Sentence marking Punctuation is
//always treated as end of sentence (! . ?)
//Just Initiate Program and Follow Graphical User Interface for Instructions!

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import javax.swing.JOptionPane;

public class assignment1 {

  public static void main(String[] args) {	
    Stemmer stemmer = new Stemmer();
    
    String input = Input("Enter the direct path of the file to be tokenized: " + 
        "(e.g. C:/Users/Blake/Desktop/example.txt)");   
    boolean res = false;
    if(input != null) {
      res = Confirm("Is the following correct?", input);
    }
    if(res) {   //correct input; start tokenization
      try {
        LinkedList tokensList = new LinkedList();       //linked list containing all tokens
        Scanner file = new Scanner(new File(input));
        
        //read entire file
        String fileContents = "";       //file contents are stored in this variable
        while(file.hasNextLine()) {
          fileContents += file.nextLine() + "\n";
        }
        System.out.println(fileContents);
        
        //stem words and generate list
        for(int index = 0; index < fileContents.length(); index++) {
          char currentChar = fileContents.charAt(index);
          //build word, one character at a time
          if((currentChar >= 'a' && currentChar <= 'z') || (currentChar >= 'A' && currentChar <= 'Z')) {
            stemmer.add(currentChar);  
          }else if(currentChar == ' ' 
              || currentChar == '?'
              || currentChar == '!'
              || currentChar == '.'
              || currentChar == '\n') { //if space/end of sentence punctuation is encountered, generate stem of word and add to index LL
            stemmer.stem();
            String stem = stemmer.toString();
            
            //add word to tokens list, dont add repeats
            if(!stem.isEmpty() && stem != null && !tokensList.isInList(stem)) {
              tokensList.addNode(stem);              
              System.out.println("word added to index: " + stemmer.toString());
            }
            stemmer = new Stemmer();    //reset stemmer to empty array of chars
          }          
        }
        
        System.out.println("Total unique tokens: " + tokensList.getLength());
      
      } catch (FileNotFoundException err) {
        Output("Sorry. The file: \'" + input + "\' was not found.");
        Output("Give this to you system admin: \n" +  err.toString());
      }
    }else { /* What to do if user cancels, if anything*/ }
  }
  
  
  //takes name param to display to a GUI input box the value of name
  //returns:    string containing what the user typed
  public static String Input(String name) {
    String input = JOptionPane.showInputDialog(null, name);
    return input;
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
  
  //val:        string being displayed to user
  public static void Output(String val) {
    JOptionPane.showMessageDialog(null, val);
  }
}