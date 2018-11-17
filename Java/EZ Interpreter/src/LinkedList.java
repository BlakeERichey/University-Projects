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
	
	public void addItem(String x) 
	{
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
	
	public String removeNode(Node item)
	{
		String tempString = item.getData();
		if(head == tail)
		{
			head=null;
			tail=null;
		}
		else if (item == tail)
		{
			//find node prior to tail
			Node currentNode = head;
			while(currentNode.getNext() != tail) 
			{
				currentNode = currentNode.getNext();
			}
			tail = currentNode;
			tail.setNext(null);
		}
		else
		{
			System.out.println("Tempstring is" + tempString);
			//find node prior to item
			Node currentNode = head;
			while(currentNode.getNext() != item) 
			{
				currentNode = currentNode.getNext();
			}
			currentNode.setNext(item.getNext());
		}

		return tempString;
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
	
	public void runFunction(Node functionNode) 
	{
		Node tempNode = functionNode.getNext();
		while(tempNode.getNext() != null) //loop will continue until it reaches q then end
		{
			if(tempNode.getData().substring(0, 1).equals("q"))
			{
				//System.out.println("Q encountered. exiting function call.");
				break;
			}
			//System.out.println("just testing" + tempNode.getData().substring(0, 1));
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
			parseX(line);
		}
	}
	
	public void parseP(String line)
	{
		System.out.println(line.substring(2, line.length()));
	}
	
	public String parseC(String line)
	{
		System.out.println("line is " + line);
		stackInfixToPostfix tempStack = new stackInfixToPostfix(line);
		return convertToPostFix(tempStack);
	}
	
	public static String convertToPostFix(stackInfixToPostfix line)
	{
		for(int index = 0; index < line.input.length(); index++)
		{
			if (!(Character.isDigit(line.input.charAt(index))))
			{
				if (line.input.charAt(index) == '(')
				{
					line.push("(");
					System.out.println(line.stack[0]);

				}
				else if (line.input.charAt(index) == ')')
				{
					while (!line.isEmpty() && !line.stack[line.top].equals("("))
					{
						for(int x =0; x<line.stack.length; x++)
						{
							System.out.println("stack element is" );
						}
						System.out.println(line.stack[line.top].equals("("));
						line.output+=line.pop();
					}
				}
			}
			else
			{
				line.output+=line.input.substring(index, index+1);
			}
		}
		System.out.println(line.stack[0]);
		return line.output;
	}
	
	
//	public String stackInfixToPostfix(String line) 
//	{
//		String tempString = "";
//		String[] tempStack = new String[line.length()];
//		int stackTail = 0;
//		for(int index = 0; index < line.length(); index++)
//		{
//			if (!(Character.isDigit(line.charAt(index))))
//			{
//				tempStack[stackTail++] = line.substring(index, index+1);
//			}
//			else
//			{
//				tempString += line.substring(index, index+1);
//			}
//		}
//		System.out.println("tempString is " + tempString);
//		return "";
//	}
	
	public void parseX(String line)
	{
		String functionName = line.substring(2, line.length());
		Node currentNode = head;
		//System.out.println("Function name in parseX is " + functionName);
		while(currentNode.getNext() != null) { //getting hung up on q after f alpha
			if (currentNode.getData().substring(0, 1).equals("f")) //look for node that has function named the same as we are looking for
			{
				if (currentNode.getData().substring(2, currentNode.getData().length()).equals(functionName))
				{
					runFunction(currentNode);
					break;
				}
			}
			currentNode = currentNode.getNext();
			//System.out.println(currentNode.getData());
		}

	}
}