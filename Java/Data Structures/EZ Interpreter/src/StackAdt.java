public class StackAdt {
	
	char[] stack;
	int top;
	
	public StackAdt() 
	{	
		stack = new char[1000];
		top = 0; //where next available spot is
	}
	
	public boolean isEmpty() 
	{
		return (top == 0);
	}
	
	public void push(char x)
	{
		stack[top++] = x;
	}
	
	public char pop()
	{
		if (!this.isEmpty())
		{
			return stack[--top];
		}
		else
		{
			throw new NullPointerException("Null pointer Exception. You tried to remove from an empty list");
		}
	}
	
	public char peek()
	{
		
		if (!this.isEmpty())
		{
			return stack[top-1];
		}
		else
		{
			throw new NullPointerException("Null pointer Exception. You tried to peek at an empty list");
		}
	}
}
