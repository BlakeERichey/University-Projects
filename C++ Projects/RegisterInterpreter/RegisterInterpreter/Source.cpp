#include "brichey.h"

using namespace std;

//string & Input(string &val);
void restart();

int main() {
	//initialize variables
	int ram[1000];
	int registers[10];
	string	 filename;
	ifstream readFile;
	ofstream writeFile;

	cout << "File Should Be in Same Directory as .exe\n" << "Enter File Name to Read (e.g. test.txt): ";
	Input(filename);	//Take input from console and save value to filename (pass by reference)

	cout << "Filename is " << filename << "\nOpening..." << endl;
	
	//open file named filename
	readFile.open(filename);
	if (!readFile.is_open()) { //file failed to open?
		cout << "Failed to find file... You will be prompted again." << endl;
		system("pause");
		system("CLS");
		main();
		exit(EXIT_FAILURE);
	}

	string cmd;	//variable for instruction value
	getline(readFile, cmd);
	while (readFile.good()) { //while not EOF
		try
		{
			char e = 'e';
			if (cmd.length() > 3) { throw e; }
		}
		catch (char e) {
			cout << "Invalid Format Type." << endl;
			restart();
		}
		cout << cmd << endl;
		readFile >> cmd; //save next word into word
	}
	readFile.close();

	cout << endl << "Pausing before exiting..." << endl;
	system("pause");
	return 0;
}

void restart() {
	cout << "Restarting Program..." << endl;
	system("pause");
	system("CLS");
	main();
	exit(EXIT_FAILURE);
}