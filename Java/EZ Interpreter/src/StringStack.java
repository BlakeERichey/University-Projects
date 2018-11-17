public class StringStack {
	
	String[] stack;
	int top;
	
	public StringStack() 
	{	
		stack = new String[1000];
		top = 0; //where next available spot is
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
			return stack[--top];
		}
		else
		{
			throw new NullPointerException("Null pointer Exception. You tried to remove from an empty list");
		}
	}
	
	public String peek()
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
