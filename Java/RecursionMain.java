/*Blake Richey
 * COSC 2336-001
 * FALL 2018
 * 11/3/18
 * The Goal of the Project is to recursively process a made up Markup language that is read from a file and printed out to a new file.
 *Recursion() is a helper function that recursively processes a string of text using conditions defined by a fictional markup language. 
 * the main() function prompts the user for locations to be saved and where to read from and handles error checking to make sure the file it is reading from exist.
*/

import java.util.Scanner;
import java.io.File;
import java.io.FileOutputStream;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class RecursionMain {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);
		System.out.println("Please list the path to the file (for example: \"C:\\Users\\Blake\\eclipse-workspace\\Assignment3\\src\\mytext.txt\"):");
		String fileName = input.nextLine(); //file to read from
		try 
		{
			Scanner file = new Scanner(new File(fileName));
			System.out.println("Please list the path where you would like the interpretted contents to be saved"
					+ "(for example: C:\\Users\\Blake\\eclipse-workspace\\Assignment3\\src\\newfile.txt)");
			String fileOut = input.nextLine(); //file to write to, creates if it does not exist, replaces if file exists.
			
			//write to file, fileOut
			FileOutputStream fos = new FileOutputStream(fileOut, false /*replace instead of append*/);
			PrintWriter text = new PrintWriter(fos); 
			
			while(file.hasNextLine())
			{
				text.println(Recursion(file.nextLine()));				
			}
			//close file leaks
			text.close();
			file.close();
			input.close();
			
			System.out.println("Successful! Please look at " + fileOut + " to see the contents.");
		} catch (FileNotFoundException e) 
		{
			System.out.println("Unable to find " + fileName);
		} catch (Exception arbitraryException) {
			System.out.println("Exception found upon execution. Please contact Blake Richey for assistance.");
		}
		
		
	}

	//Recursion() is a helper function that recursively processes a string of text using conditions defined by a fictional markup language. 
	//When certain substrings are encountered perform a specific task.
	//#REV means to reverse the following text until #END is encountered
	//#QUO, Like REV however puts the string in quotes rather than reversing the string
	//#NXT changes each character to 1 later character in the alphabet, looping z to a and keeping the same case
	//#DBL removes double letters
	private static String Recursion(String text) {
		String output = ""; //return variable
		if (!text.contains("#"))
		{
			output = text;
		}
		else {
			output = text.substring(0, text.indexOf('#')); 			
			String cmd = text.substring(text.indexOf('#'), text.indexOf('#')+4); //CMD
			String cmdtext = text.substring(text.indexOf('#')+4, text.indexOf("#END") + 4); //BETWEEN CMD AND #END INCLUDING #END
			String remainingText = text.substring(text.indexOf("#END") + 4, text.length()); //REMAINING SUBSTRING AFTER FIRST #END
			if (cmd.equals("#REV")) 
			{
				StringBuffer reverse = new StringBuffer(Recursion(cmdtext).trim());
				output += reverse.reverse();
			}
			if (cmd.equals("#QUO"))
			{
				output += "\"" + Recursion(cmdtext).trim() + "\"";
			}
			if (cmd.equals("#NXT")) 
			{
				String recursionFinal = Recursion(cmdtext).trim(); //stored variable so Recursion only needs to be calculated once
				String modifiedString = ""; //String after char changes have been finished
				for (int i=0; i<recursionFinal.length(); i++) 
				{
					char tempChar = recursionFinal.charAt(i); //filler default character
					int tempASCII = (int)recursionFinal.charAt(i) + 1; //ascii value of shifted char
					if (tempASCII >= 66 &&  tempASCII <= 91) 
					{
						tempChar = (char)((tempASCII % 65)% 26 + 65); //changes shifted character from Z to A
					}
					if (tempASCII >= 98 &&  tempASCII <= 123) 
					{
						tempChar = (char)((tempASCII % 97)% 26 + 97); //changes shifted character from Z to A
					}
					modifiedString += tempChar;
				}
				output += modifiedString;
			}
			if (cmd.equals("#DBL"))
			{
				String recursionFinal = Recursion(cmdtext).trim(); //stored variable so Recursion only needs to be calculated once
				String modifiedString = ""; //String after doubles have been removed
				for (int i=0; i<recursionFinal.length(); i++) {
					
					modifiedString += recursionFinal.charAt(i);
					
					//print last character, then dont make comparison to character after it, shortcircuit. Special consideration in event 
					//last 2 characters arent doubles				
					if (i != recursionFinal.length() - 1 && recursionFinal.charAt(i) == recursionFinal.charAt(i+1))
					{
						i++; //if double encountered, skip a character
					}
				}
				output += modifiedString;
			}
			output += Recursion(remainingText);
		}
		
		return output;
		
	}

}
