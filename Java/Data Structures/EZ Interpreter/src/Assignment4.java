//Blake Richey
//Data Scructures 2336-001
//The goal of this assignment is to interpret a fictional language with given syntax requirements using a stack.
//StackAdt is used to perform comparisons against individual characters in a string. 
//StringStack is used to convert strings to doubles and vice versa to calculate the sum of a expression using a stack
//LinkedList.java has several functions, of which include a linked list and several functions 
//	referencing the attributes of the class to perform calculations and find locations in the file.
//VLINode is a basic Node class that defines Nodes to be used in the LinkedList.java

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class Assignment4 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in); //no need?
		String fileName = "test.txt";
		LinkedList procList = new LinkedList();
		try {
			Scanner file = new Scanner(new File(fileName)); //set up scanner, file, to read from fileName, args[0]
			while(file.hasNextLine()) 
			{
				//generate linked list with contents of file
				procList.addItem(file.nextLine());
			}
			
			//run f main of file
			procList.runFunction(procList.findMain());
			
			file.close();
			input.close();
			
		} catch (FileNotFoundException e) 
		{
			System.out.println("File does not exist or cannot find file.");
		}
		
		
	}


}

