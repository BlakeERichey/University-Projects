import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.PrintWriter;
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
				 procList.addItem(file.nextLine());
			}
			
			procList.runFunction(procList.findMain());
			procList.parseC("3+7/5*2");
			
		} catch (FileNotFoundException e) 
		{
			System.out.println("File does not exist or cannot find file.");
		}
		
		
		

		
	}
}