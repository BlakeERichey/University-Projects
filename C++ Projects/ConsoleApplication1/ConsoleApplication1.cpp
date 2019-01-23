// ConsoleApplication1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include "pch.h"
#include <iostream>
#include <string>
using namespace std;

int total(int maxVal);

int main()
{
	/*string mystr;
	cout << "What's your name? ";
	cin >> mystr;
	cout << "Hello " << mystr << ".\n";
	cout << "What is your favorite team? ";
	std::cin.ignore(INT_MAX, '\n');
	getline(cin, mystr);*/
	system("pause");
	int sum = total(5);
	cout << "sum is " << sum;



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

int total(int maxVal) {
	int sum = 0;
	for (int x = 0; x <= maxVal; x++) {
		sum += x;
	}
	return sum;
}
// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
