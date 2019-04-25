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
				  System.out.println("These displayed here for your convenience:\n" + common.listToString(queries, "\n"));
				  common.Output(common.listToString(queries, "\n") + 
						  "\n\n\nPress okay after you have saved the search results in a file.");
				  
				  GUIFileChooser fileChoice = new GUIFileChooser();
				  File input = fileChoice.getFile();
				  
				  try{
					  String contents = common.readFile(input);
					  common.Alert(contents);
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

}
