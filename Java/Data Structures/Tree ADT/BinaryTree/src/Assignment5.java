//Blake Richey
//COSC 2336-001
//12-7-2018
//Using a tree make a game that guesses what the player is thinking.
//If it guesses incorrectly it is to make changes to be more accurate.

import java.util.Scanner;

public class Assignment5 {

	public static void main(String[] args) {
		BTNode root = new BTNode("Gandalf");
		Scanner input = new Scanner(System.in);
		BTNode currentNode = root; 
		
		System.out.println("When playing, simply type \"yes\" or \"no\" to the series of questions. "
				+ "I will guess what you're thinking!");
		runGame(currentNode, root);
		
		input.close();


	}
	
	//Makes a new node, replaces currentNode's data with an identifying question
	//newData is the answer to the game the player was thinking of
	//sets new node to the left of the currentNode and sets its data to newData. 
	//moves currentNode value to the right and sets currentNodes value to a new question
	public static void appendTree(BTNode currentNode)
	{
		Scanner input = new Scanner(System.in); //intentionally left open.
		System.out.println("Who were you thinking of?");
		String res = input.nextLine();
		String newData = res; //saves new answer to newData
		System.out.println("Enter a yes/no question distinguishing " + 
				currentNode.getData() + " from " + res);
		res = input.nextLine();
		BTNode tempNodeLeft = new BTNode(newData);
		BTNode tempNodeRight = new BTNode(currentNode.getData());
		currentNode.setRight(tempNodeRight);
		currentNode.setLeft(tempNodeLeft);
		currentNode.setData(res);

	}
	
	//tests if the current node is a leaf
	public static boolean isLeaf(BTNode currentNode)
	{
		return (currentNode.getRight() == null) && (currentNode.getLeft() == null);
	}
	
	//recursively calls self.
	//takes in a node and determines if it is a leaf. if it is it makes a guess
	//otherwise it navigates down the tree to the appropriate answer
	public static void runGame(BTNode currentNode, BTNode root)
	{
		Scanner input = new Scanner(System.in);
		String res = "";
		if (isLeaf(currentNode))	//make a guess
		{
			System.out.println("You were thinking of " + currentNode.getData() + "?");
			res = input.nextLine();
			
			//verify user input is correct
			while(!res.toLowerCase().equals("yes") && !res.toLowerCase().equals("no"))
			{
				System.out.println("Invalid input. Input must be yes or no.");
				res = input.nextLine();
			}
			
			if(res.toLowerCase().equals("no")) //if guess was wrong
			{
				appendTree(currentNode);
				System.out.println("Noted. I added " + currentNode.getLeft().getData() + " to my knowledge pool. "
						+ "Want to play again?");
				res = input.nextLine();
				while(!res.toLowerCase().equals("yes") && !res.toLowerCase().equals("no"))
				{
					System.out.println("Invalid input. Input must be yes or no. Want to play again?");
					res = input.nextLine();
				}
				if (res.toLowerCase().equals("yes"))
				{
					runGame(root, root); //run game again from root
				}
			}
			else if(res.toLowerCase().equals("yes")) //if guess was right
			{
				System.out.println("Well played, but I beat you this time. Want to play again?");
				res = input.nextLine();
				while(!res.toLowerCase().equals("yes") && !res.toLowerCase().equals("no"))
				{
					System.out.println("Invalid input. Input must be yes or no. Want to play again?");
					res = input.nextLine();
				}
				if (res.toLowerCase().equals("yes"))
				{
					runGame(root, root); //run game again from root
				}
			}
		}
		
		

		else 
		{
			System.out.println(currentNode.getData()); //ask question
			res = input.nextLine();
			if (res.toLowerCase().equals("yes"))
			{
				runGame(currentNode.getLeft(), root);
			}
			else if (res.toLowerCase().equals("no"))
			{
				runGame(currentNode.getRight(), root);
			}
			else 
			{
				System.out.println("Invalid input. Answer must be yes or no. Try again.");
				runGame(currentNode, root);
			}
		}
		input.close();
	}
}
