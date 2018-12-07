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
	
	//finds f main in file being interpreted
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
	
	//runs a function, f,. main automatically calls the "f main" of the interpreted language
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
	
	//determines which call is being made
	public void parseString(String line)
	{
		if(line.substring(0, 1).equals("p"))
		{
			parseP(line);
		}
		if(line.substring(0, 1).equals("c"))
		{
			System.out.println(parseC(line.substring(2, line.length())));
		}
		if(line.substring(0, 1).equals("x"))
		{
			parseX(line);
		}
	}
	
	//processes p calls
	public void parseP(String line)
	{
		System.out.println(line.substring(2, line.length()));
	}
	
	//processes c calls
	public double parseC(String line)
	{
		return evaluatePostfix(infixToPostfix(line));
	}
	
	//processes X calls
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
	
    //prioritized operators
    static int Priority(char ch) 
    { 
        switch (ch) 
        { 
        case '+': 
        case '-': 
            return 1; 
       
        case '/': 
        case '*': 
            return 2; 
       
        case '^': 
            return 3; 
        } 
        return -1; 
    } 
    
    //conversion method similar to example found online, though using my methods rather than an ArrayList.
    //https://www.geeksforgeeks.org/stack-set-2-infix-to-postfix/
    //converts infix expression to postfix expression
    public static String infixToPostfix(String line) 
    { 
        String result = new String(""); 
          
        // initialize empty stack 
        StackAdt stack = new StackAdt(); 
          
        for (int i = 0; i<line.length(); ++i) 
        { 
            char c = line.charAt(i); 
              
             // If character is an operand, add it to output. 
            if (Character.isLetterOrDigit(c)) 
                result += c; 
               
            //If character is '(', push it to the stack. 
            else if (c == '(') 
                stack.push(c); 
              
             
            else if (c == ')') 
            { 
            	//pop off stack until ( is encountered
                while (!stack.isEmpty() && stack.peek() != '(') 
                    result += stack.pop(); 
                  
                if (!stack.isEmpty() && stack.peek() != '(') 
                    return "Invalid Expression"; // invalid expression                 
                else
                    stack.pop(); 
            } 
            else // an operator is encountered 
            { 
                while (!stack.isEmpty() && Priority(c) <= Priority(stack.peek())) 
                    result += stack.pop(); 
                stack.push(c); 
            } 
       
        } 
       
        // pop all the operators from the stack 
        while (!stack.isEmpty()) 
            result += stack.pop(); 
       
        return result; 
    } 

    //evaluates the total of a postfix expression
    public double evaluatePostfix(String exp)
    {
    	StringStack tempStack = new StringStack();
    	for(int i =0; i<exp.length(); i++)
    	{
    		//System.out.println("hello" + exp.charAt(i));
    		
    		if ((Character.isDigit(exp.charAt(i))))
    		{
    			tempStack.push(exp.substring(i, i+1));
    		}
    		else
    		{
    			double val1 = Double.parseDouble(tempStack.pop());
    			double val2 =  Double.parseDouble(tempStack.pop());
    			if (exp.charAt(i) == '*')
    			{
    				tempStack.push(val2*val1 + "");
    			} else if ((exp.charAt(i) == '/'))
    			{
    				tempStack.push(val2/val1+"");
    			} else if ((exp.charAt(i) == '+'))
    			{
    				//System.out.println(val1 + " " + val2 + " " + tempStack.peek());
    				tempStack.push(val2+val1 + "");
    			} else if ((exp.charAt(i) == '-'))
    			{
    				tempStack.push(val2-val1+"");
    			}
    		}
    	}
    	return Double.parseDouble(tempStack.pop());
    }

}