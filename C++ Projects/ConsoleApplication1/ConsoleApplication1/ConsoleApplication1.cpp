// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
using namespace std;

int total(int maxVal);
void passByValue(int x);
void passByReference(int *x);

int main()
{
	//****enum practice****
	//enum Name_Choice {Mark, Greg, Jen, Chris, Vicky, Billy};
	////const int Mark = 0; => Mark = 0, Greg = 1, Jen = 3...
	//Name_Choice VP = Greg;
	//if (VP == Greg) {
	//	cout << "your vp is Greg" << endl;
	//}

	//cout << "Gregs actual value is " << Greg; //displays 1

	//***Struct practice***
	/*struct newperson {
		char name[20];
		int age;
	};

	newperson bucky = { "Bucky", 21 };

	cout << bucky.name;*/	//displays bucky

	//***pointers practice***
	int fish = 5;
	cout << &fish << endl;	//prints address of fish variable
	int *fishPointer;		//initialize pointer
	fishPointer = &fish;	//sets pointer to memory address of fish
	cout << fishPointer << endl; //should be same as earlier cout

	int betty = 13;
	int sandy = 13;

	passByValue(betty);
	passByReference(&sandy);

	cout << "betty is now" << betty << endl;
	cout << "sandy is now" << sandy << endl;

	//***input output practice***
	/*string mystr;
	cout << "What's your name? ";
	cin >> mystr;
	cout << "Hello " << mystr << ".\n";
	cout << "What is your favorite team? ";
	std::cin.ignore(INT_MAX, '\n');
	getline(cin, mystr);*/
	//system("pause");
	//int sum = total(5);
	//cout << "sum is " << sum;



	//****Array practice****
	//const int capacity = 50000;
	//int test[capacity];
	//int sum = 0;
	//for (int x = 0; x < capacity; x++) {
	//	test[x] = x;
	//	//cout << "adding " << x << " to " << sum << endl;
	//	sum += test[x];
	//}
	//cout << "sum is " << sum << endl;
	system("pause");
	return 0;
}

//****for loop practice****
/*int total(int maxVal) {
	int sum = 0;
	for (int x = 0; x <= maxVal; x++) {
		sum += x;
	}
	return sum;
}*/
// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file

void passByValue(int x) {
	x = 99;
}

void passByReference(int *x) {
	*x = 66;	//changes actual value, not memory address
}