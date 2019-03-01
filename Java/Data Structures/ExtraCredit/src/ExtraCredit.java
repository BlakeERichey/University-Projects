//Blake Richey
//COSC 2336-001
//ExtraCredit
//create several recursive functions specified in the extracredit assignment

public class ExtraCredit {
	
	public static void main(String[] args)
	{
		ExtraCredit d = new ExtraCredit();
		System.out.println(d.rec1("15", "37"));
		System.out.println(d.rec2("This is an example"));
		
		Node testing = new Node("test");
		Node tempNode = new Node("one");
		testing.setNext(tempNode);
		System.out.println(d.rec3("one", testing));
		
	}
	
	//calculate the sum of all numbers between num1 and num2
	public int rec1(String num1, String num2)
	{
		int tempNum1 = Integer.parseInt(num1);
		int tempNum2 = Integer.parseInt(num2);
		int sum = 0;
		
		if (tempNum1 == tempNum2)
		{
			return tempNum1;
		}
		else if (tempNum2 > tempNum1)
		{
			sum+=tempNum2--;
			return sum + rec1(num1, tempNum2+"");
		}
		else //num1 is larger than num2
		{
			return sum;
		}
	}
	
	//recursively iterate through string str and count number of vowels found
	public int rec2(String str)
	{
		int index = str.length()-1;
		int sum = 0;
		char[] list = new char[] {'a', 'e', 'i', 'o', 'u'};
		
		if (index == 0) 
		{
			//is character a vowel?
			for(int x=0; x<list.length; x++) 
			{
				if (str.charAt(index) == list[x])
				{
					return ++sum;
				}
			}
		}
		else if (index >= 0)
		{
			//is character a vowel?
			for(int x=0; x<list.length; x++) 
			{
				if (str.charAt(index) == list[x])
				{
					++sum;
				}
			}
			return sum + rec2(str.substring(0, index));
		}
		return sum;
	}

	//iterates through linked list "list" and determines if the String "key" is in it.
	public boolean rec3(String key, Node list)
	{
		if (list.getData().equals(key)) //value matches a node's data
		{
			return true;
		}
		else
		{
			if (list.getNext() != null)
			{
				return (false || rec3(key, list.getNext()));
			}
			else
			{
				return false;	//end of linked list reached
			}
		}
	}
	
//	public Node rec4(Node list1, Node list2)
//	{
//		
//	}
	
}
