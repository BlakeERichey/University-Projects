
public class VeryLargeInteger implements VeryLargeIntegerInterface
{
	private int[] digits;
	private int indexOfLast;
	private int MAX_CAPACITY = 10000;

	public VeryLargeInteger(int x)
    	{
		
			//convert passed int to a string then reverse it
			StringBuffer s = new StringBuffer(x + "");
			s.reverse();
			
			//initializes an array of size 10000 and a value corresponding to its current length, indexOfLast
			digits = new int[MAX_CAPACITY];
			indexOfLast = s.length() - 1;
			
			//assigns each integer value into an array cell starting from the last digit
			for (int i = indexOfLast; i>=0;i--)
			{
				digits[i] = Character.getNumericValue(s.charAt(i));
			}
    	}

	//returns the number of digits in the current value of the ADT
    public String getString()
	{
    	//Concatenates each integer in the array to a tempString in reverse order
    	String tempString = "";
    	for(int i=indexOfLast;i>=0;i--)
    	{
    		tempString += digits[i];
    	}
		return  tempString;
	}
	
    //returns the number of digits in the current value of the ADT
	public int length()
	{
		return indexOfLast + 1;
	}

	//Returns the number of zero digits at the right end of the current value of the
	//ADT. For example, 479001600 has two rightmost zeros
	public int numTrailZero()
	{
		int count = 0;
		
		//verify the array is not empty
		if(indexOfLast == 0)
			return -1;
		else
		{
			for (int i = 0; i<=indexOfLast; i++)
			{
				if (digits[i] == 0)
				{
					//increase the counter for the number of 0's by 1 for each iteration of the for loop
					count++;
				}
				else
					//exit for loop on first instance of non zero number
					break;
			}
		}
		return count;
	}
	
	//Returns the value of the rightmost, nonzero digit. For example, 479001600
	//has a 6 as the rightmost, nonzero digit
	public int lastNonZero()
	{
		return digits[numTrailZero()];
	}
	
	//An operation that increases the current value of the ADT by multiplying it by an
	//argument int value
	public void multiply(int x)
	{
		int carry = 0;
		int[] tempArray = new int[MAX_CAPACITY];
		int tempLastIndex = indexOfLast;
		
		for (int i = 0; i<=indexOfLast; i++)
		{
			//make copy of digits
			tempArray[i] = digits[i];
		}
		
		for(int iterations = 0; iterations<=x; iterations++)
		{
			//add tempArray to digits and store in digits. adds digits to itself, but keeps tempArray to be able to do it multiple times
			for (int i = 0; i<=tempLastIndex; i++)
			{
				int currentDigit = tempArray[i];
				digits[i] = (tempArray[i] + digits[i] + carry) % 10;
				if ((currentDigit+currentDigit+carry)>=10)
				{
					carry = 1;
				}
				else
				{
					carry = 0;
				}
			}
			
			//if last number addition was greater than 10 then carry over 1 to a new index
			if (carry == 1)
			{
				indexOfLast++;
				digits[indexOfLast]++;
			}
		}
	}

}
