//Blake Richey
//4315 Assignment 5
//The goal of this program is to simulate basic natrual language interpretation
//by rewriting a `where...` question query and displaying alternative queries.
//it then loads input from a file of the user selection that contains
//a google page corresponding to a search of that query
//and attempts to determine the answer to the question using kterm indexes

import java.io.File;
import java.io.FileNotFoundException;

public class Assignment5 {

  public static void main(String[] args){
	  boolean run = true;
	  while (run) {
		  run = false;
		  LinkedList list = new LinkedList();
		  String question = ""; 
		  question = common.Input("Ask your question");
		  if(question == null ) { break; } //cancels program
		  question = question.toLowerCase(); //avoid null error
		  if(question != "" && question.length() >= 5 
			  && (question.startsWith("Where") || question.startsWith("where"))) {
			  String[] stoplist = {"do", "is", "can", "does", "was", "i", "the", "a", "are"};
			  String words[] = question.substring(5, question.length()).trim().split(" "); //remove `where`

			  //remove stop words
			  for(int index = 0; index < words.length; index++) { 
				  if(!common.contains(stoplist, words[index])) {
					  list.addNode(words[index]);
				  }
			  }
			  
			  if(list.getLength() >= 1) {
				  words = list.getList();
				  String[] queries = new String[3];
				  queries[0] = common.contains(words, "go")?
						  common.listToString(words, " ") + " destination"
						  :common.listToString(words, " ") + " location";
				  queries[1] = common.listToString(words, " ") + " where";
				  queries[2] = question.contains("do")?
						  common.listToString(words, " ")
						  :question;
						  
			      //display queries
				  common.Output(common.listToString(queries, "\n") + 
						  "\n\n\nPress okay after you have saved the search results in a file.\n(Proceed to Question 2)");
				  
				  //get file to read
				  GUIFileChooser fileChoice = new GUIFileChooser();
				  File input = fileChoice.getFile();
				  
				  try{
					  String 	 contents 	   = common.readFile(input, true);
					  String[]   lines     	   = contents.split("\n");
					  LinkedList oneGramList   = new LinkedList();
					  LinkedList twoGramList   = new LinkedList();
					  LinkedList threeGramList = new LinkedList();
					  LinkedList allGramList   = new LinkedList();	//all in one
					  
					  //generate kgram lists
					  for(int i = 0; i<lines.length; i++) {
					    String[] tempWords = lines[i].trim().split(" "); //words per line
					    for(int index = 0; index < tempWords.length; index++) { //if word is uppercase add to kgram list
					      //one gram
					      if(Character.isUpperCase(tempWords[index].charAt(0))) {
					        oneGramList.addNode(tempWords[index]);
					        allGramList.addNode(tempWords[index]);
					      }
					      
					      //two gram
					      if(index + 1 < tempWords.length 
					          && Character.isUpperCase(tempWords[index].charAt(0))
					          && Character.isUpperCase(tempWords[index+1].charAt(0))) {
					        twoGramList.addNode(tempWords[index] + " " + tempWords[index+1]);
					        allGramList.addNode(tempWords[index] + " " + tempWords[index+1]);
					      }
					      
					      //three gram
					      if(index + 2 < tempWords.length 
                              && Character.isUpperCase(tempWords[index].charAt(0))
                              && Character.isUpperCase(tempWords[index+1].charAt(0))
                              && Character.isUpperCase(tempWords[index+2].charAt(0))) {
                            threeGramList.addNode(tempWords[index] + " " + tempWords[index+1] + " " + tempWords[index+2]);
                            allGramList.addNode  (tempWords[index] + " " + tempWords[index+1] + " " + tempWords[index+2]);
                          }
					    }
					  }
					  
					  String[] oneGramArr   = oneGramList  .getList();
					  String[] twoGramArr   = twoGramList  .getList();
					  String[] threeGramArr = threeGramList.getList();
					  String[] allGramArr   = allGramList  .getList();
					  
					  //find valid answers in each list prioritizing three-gram indexes, then 2, then 1
					  LinkedList answers = new LinkedList();
					  int threshold = 3;       //threshold to be considered a good answer
					  
					  for(int i = 0; i < threeGramArr.length; i++) {
					    if(common.count(threeGramArr, threeGramArr[i]) > threshold
					        && !answers.isInList(threeGramArr[i])) {
					      answers.addNode(threeGramArr[i]);
					    }
					  }
					  
					  if(answers.getLength() < 3) {
						  for(int i = 0; i < twoGramArr.length; i++) {
	                        if(common.count(twoGramArr, twoGramArr[i]) > threshold
	                            && !answers.isInList(twoGramArr[i])) {
	                          answers.addNode(twoGramArr[i]);
	                        }
	                      }
					  }
					  
					  if(answers.getLength() < 3) {
						  for(int i = 0; i < oneGramArr.length; i++) {
	                        if(common.count(oneGramArr, oneGramArr[i]) > threshold
	                            && !answers.isInList(oneGramArr[i])) {
	                          answers.addNode(oneGramArr[i]);
	                        }
	                      }
					  }
					  
					  String[] answersArr = answers.getList();
					  String[] text = new String[3];
					  String currentFrequentWord = findMostFrequent(allGramArr, question, answersArr);
					  text[0] = currentFrequentWord + " " + common.count(allGramArr, currentFrequentWord);
					  currentFrequentWord = findSecondMostFreuqent(allGramArr, question, answersArr);
					  text[1] = currentFrequentWord + " " + common.count(allGramArr, currentFrequentWord);
					  currentFrequentWord = findThirdMostFreuqent(allGramArr, question, answersArr);
					  text[2] = currentFrequentWord + " " + common.count(allGramArr, currentFrequentWord);

					  common.Alert(common.listToString(text, "\n"));
				  }catch(Exception e) {
					  if(input != null) {
						  common.Alert("Error reading file. File not found\n\nFile attempted to read: " + input);
					  }else {
						  if(common.Confirm("No File Selected. Rerun?", "")) {
							  run = true;
						  }
					  }
				  }
			  }else {
				  common.Alert("Question not specific enough. I dont understand.");
				  run = true;
			  }
			  
		  }else {
			  common.Alert("Invalid question structure. Question must begin with `Where`. Try again.");
			  run = true;	//re-run 
		  }
	  }
  }
  
  //finds most frequent word in a list of words
  public static String findMostFrequent(String[] list, String query, String[] answersArr) {
    int count = 0;
    String word = "";
    for(int i = 0; i<list.length; i++) {
      String currentWord = list[i];
      int occurences = common.count(list, currentWord);
      if(occurences > count
    		  && common.contains(answersArr, currentWord)
    		  && !query.toLowerCase().contains(currentWord.toLowerCase())) {
        count = occurences;
        word = currentWord;
      }
    }
    return word;
  }
  
  public static String findSecondMostFreuqent(String[] list, String query, String[] answersArr) {
    int count = 0;
    String word = "";
    String mostCommon = findMostFrequent(list, query, answersArr);
    for(int i = 0; i<list.length; i++) {
      String currentWord = list[i];
      int occurences = common.count(list, currentWord);  
      if(!currentWord.equals(mostCommon) 
    		  && occurences > count
    		  && common.contains(answersArr, currentWord)
    		  && !query.toLowerCase().contains(currentWord.toLowerCase())) {
        count = occurences;
        word = currentWord;
      }
    }
    return word;
  }
  
  public static String findThirdMostFreuqent(String[] list, String query, String[] answersArr) {
    int count = 0;
    String word = "";
    String mostCommon = findMostFrequent(list, query, answersArr);
    String secondMostCommon = findSecondMostFreuqent(list, query, answersArr);
    for(int i = 0; i<list.length; i++) {
      String currentWord = list[i];
      int occurences = common.count(list, currentWord);  
      if(!currentWord.equals(mostCommon) 
          && !currentWord.equals(secondMostCommon)
          && common.contains(answersArr, currentWord)
          && !query.toLowerCase().contains(currentWord.toLowerCase())
          && occurences > count) {
        count = occurences;
        word = currentWord;
      }
    }
    return word;
  }

}
