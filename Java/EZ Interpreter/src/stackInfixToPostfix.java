
public class stackInfixToPostfix {
	
	String output;
	String[] stack;
	String input;
	int top;
	
	public stackInfixToPostfix(String input) 
	{	
		this.input = input;
		stack = new String[input.length()];
		output = "";
		top=0;
	}
	
	public boolean isEmpty() 
	{
		return (top == 0);
	}
	
	public void push(String x)
	{
		stack[top++] = x;
	}
	
	public String pop()
	{
		if (!this.isEmpty())
		{
			return stack[top--];
		}
		else
		{
			return "";
		}
	}
	
	public String peek()
	{
		return stack[top];
	}
	
}
//
//
//
//	public String convertToPostFix() 
//	{
//		for(int index = 0; index < input.length(); index++)
//		{
//			if (!(Character.isDigit(input.charAt(index))))
//			{
//				//System.out.println("1");
//				if (input.charAt(index) == '(')
//				{
//					stack.addItem("(");
//					//System.out.println("im here");
//					stack.addItem(input.substring(index, index+1));
//				}
//				else if (input.charAt(index) == ')')
//				{
//					//System.out.println("2");
//					while(!stack.tail.getData().equals("("))
//					{
//						//System.out.println("im here");
//						output += stack.removeNode(stack.tail);
//					}
//					stack.removeNode(stack.tail); //remove last (
//				}
//				else
//				{
//					//System.out.println("3");
//					if (input.charAt(index) == '*')
//					{
//						if()
//						if(stack.tail.getData().equals("+") ||  stack.tail.getData().equals("-"))
//						output+="*";
//						System.out.println("checking " + stack.tail.getData());
//						while(!stack.isEmpty())
//						{
//							if(!stack.tail.getData().equals("("))
//							{
//								System.out.println("im here");
//								System.out.println(stack.tail.getData());
//								System.out.println("stack is " + stack.getString());
//								output += stack.removeNode(stack.tail);
//							}
//						}
//					}
//				}
//			}
//			else
//			{
//				output += input.substring(index, index+1);
//			}
//		}
//		stack.addItem("1");
//		System.out.println("output is " + output + "\nStack is " + stack.getString());
//		return "";
//	}
//}