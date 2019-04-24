public class Assignment4 {

  public static void main(String[] args){
	  LinkedList list = new LinkedList();
	  boolean run = true;
	  while (run) {
		  run = false;
		  String question = common.Input("Ask your question");
		  if(question != "" && question.length() >= 5 
			  && (question.startsWith("Where") || question.startsWith("where"))) {
			  String[] stoplist = {"i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"};
			  String words[] = question.substring(5, question.length()).trim().split(" ");
			  common.Alert(common.listToString(words, "\n"));
			  
		  }else {
			  common.Alert("Invalid question structure. Question must begin with `Where`. Try again.");
			  run = true;	//re-run 
		  }
	  }
  }

}
