public class LinkedList {

	Node head;
	Node  tail;
	
	public LinkedList() {
		head = null;
		tail = null;
	}
	
	public boolean isEmpty() {
		return (head == null);
	}
	
	public void addItem(String x) {
		if (isEmpty()) 
		{
			head = new Node(x);
			tail = head;
		} 
		else 
		{
			Node tempNode = new Node(x);
			tail.setNext(tempNode);
			tail = tempNode;
		}
	
	}

	public String getString() {
		Node currentNode = head;
		String tempString = "";
		while(currentNode.getNext() != null) {
			tempString += currentNode.getData() + "\n";
			currentNode = currentNode.getNext();
		}
		tempString += currentNode.getData();
		return tempString;
	}
	
	public Node findMain()  //make sure list isnt empty
	{
		Node currentNode = head;
		while(currentNode.getNext() != null) 
		{
			if(currentNode.getData().equals("f main"))
			{
				return currentNode;
			}
			currentNode = currentNode.getNext();
		}
		return null;
	}
	
	public void runMain() 
	{
		Node tempNode = findMain().getNext();
		while(tempNode.getNext() != null) //loop will continue until it reaches q then end
		{
			parseString(tempNode.getData());
			tempNode = tempNode.getNext();
		}
	}
	
	public void parseString(String line)
	{
		if(line.substring(0, 1).equals("f"))
		{
			System.out.println(line + "f");
		}
		if(line.substring(0, 1).equals("p"))
		{
			parseP(line);
		}
		if(line.substring(0, 1).equals("c"))
		{
			System.out.println(line + "c");
		}
		if(line.substring(0, 1).equals("x"))
		{
			System.out.println(line + "x");
		}
	}
	
	public void parseP(String line)
	{
		System.out.println(line.substring(2, line.length()));
	}
	
	public void parseC(String line)
	{
		
	}
}