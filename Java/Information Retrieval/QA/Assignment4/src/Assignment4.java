import java.io.File;
import java.io.FileNotFoundException;

public class Assignment4 {

  public static void main(String[] args){
	  boolean run = true;
	  while (run) {
		  run = false;
		  LinkedList list = new LinkedList();
		  String question = ""; 
		  question = common.Input("Ask your question");
		  if(question == null ) { break; } //cancels program
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
				  System.out.println("These displayed here for your convenience:\n" + common.listToString(queries, "\n"));
				  common.Output(common.listToString(queries, "\n") + 
						  "\n\n\nPress okay after you have saved the search results in a file.\n(Proceed to Question 2)");
				  
				  //get file to read
				  GUIFileChooser fileChoice = new GUIFileChooser();
				  File input = fileChoice.getFile();
				  
				  try{
					  String contents = common.readFile(input, true);
					  String[] lines = contents.split("\n");
					  LinkedList oneGramList = new LinkedList();
					  LinkedList twoGramList = new LinkedList();
					  LinkedList threeGramList = new LinkedList();
					  
					  //generate kgram lists
					  for(int i = 0; i<lines.length; i++) {
					    String[] tempWords = lines[i].split(" "); //words per line
					    for(int index = 0; index < tempWords.length; index++) { //if word is uppercase add to kgram list
					      //one gram
					      if(Character.isUpperCase(tempWords[index].charAt(0))) {
					        oneGramList.addNode(tempWords[index]);
					      }
					      
					      //two gram
					      if(index + 1 < tempWords.length 
					          && Character.isUpperCase(tempWords[index].charAt(0))
					          && Character.isUpperCase(tempWords[index+1].charAt(0))) {
					        twoGramList.addNode(tempWords[index] + " " + tempWords[index+1]);
					      }
					      
					      //three gram
					      if(index + 2 < tempWords.length 
                                                  && Character.isUpperCase(tempWords[index].charAt(0))
                                                  && Character.isUpperCase(tempWords[index+1].charAt(0))
                                                  && Character.isUpperCase(tempWords[index+2].charAt(0))) {
                                                threeGramList.addNode(tempWords[index] + " " + tempWords[index+1] + " " + tempWords[index+2]);
                                              }
					    }
					  }
					  
					  String[] oneGramArr = oneGramList.getList();
					  String[] twoGramArr = twoGramList.getList();
					  String[] threeGramArr = threeGramList.getList();
					  
					  //find top 3 in each list prioritizing three-gram indexes, then 2, then 1
					  LinkedList answers = new LinkedList();
					  int threshold = 3;       //threshold to be considered a good answer
					  
					  for(int i = 0; i < threeGramArr.length; i++) {
					    if(common.count(threeGramArr, threeGramArr[i]) > threshold
					        && !answers.isInList(threeGramArr[i])) {
					      answers.addNode(threeGramArr[i]);
					    }
					  }
					  
					  for(int i = 0; i < twoGramArr.length; i++) {
                                            if(common.count(twoGramArr, twoGramArr[i]) > threshold
                                                && !answers.isInList(twoGramArr[i])) {
                                              answers.addNode(twoGramArr[i]);
                                            }
                                          }
					  
					  for(int i = 0; i < oneGramArr.length; i++) {
                                            if(common.count(oneGramArr, oneGramArr[i]) > threshold
                                                && !answers.isInList(oneGramArr[i])) {
                                              answers.addNode(oneGramArr[i]);
                                            }
                                          }
					  
					  String[] answersArr = answers.getList();
					  String[] text = new String[3];
					  for(int i = 0; i < 3; i++) {
					    text[i] = answersArr[i];
					  }

					  common.Alert(common.listToString(text, "\n"));
				  }catch(Exception e) {
					  if(input != null) {
						  common.Alert("Error reading file. File not found\n\nFile attempted to read: " + input);
					  }else {
						  if(common.Confirm("No File Selected. Rerun?", "")) {
							  run = true;
						  }
					  }
					  e.printStackTrace();
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
  public static String findMostFrequent(String[] list) {
    int count = 0;
    String word = "";
    for(int i = 0; i<list.length; i++) {
      String currentWord = list[i];
      int occurences = common.count(list, word);  
      if(occurences > count) {
        count = occurences;
        word = currentWord;
      }
    }
    return word;
  }
  
  public static String findSecondMostFreuqent(String[] list) {
    int count = 0;
    String word = "";
    String mostCommon = findMostFrequent(list);
    for(int i = 0; i<list.length; i++) {
      String currentWord = list[i];
      int occurences = common.count(list, word);  
      if(!currentWord.equals(mostCommon) && occurences > count) {
        count = occurences;
        word = currentWord;
      }
    }
    return word;
  }
  
  public static String findThirdMostFreuqent(String[] list) {
    int count = 0;
    String word = "";
    String mostCommon = findMostFrequent(list);
    String secondMostCommon = findSecondMostFreuqent(list);
    for(int i = 0; i<list.length; i++) {
      String currentWord = list[i];
      int occurences = common.count(list, word);  
      if(!currentWord.equals(mostCommon) 
          && !currentWord.equals(secondMostCommon) 
          && occurences > count) {
        count = occurences;
        word = currentWord;
      }
    }
    return word;
  }

}
