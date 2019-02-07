#include "brichey.h"

using namespace std;

string & Input(string &val);

int main() {
	string	 filename;
	ifstream readFile;
	ofstream writeFile;

	cout << "File Should Be in Same Directory as .exe\n" << "Enter File Name to Read: ";
	Input(filename);	//Take input from console and save value to filename

	cout << "Filename is " << filename;

	cout << endl;
	system("pause");
	return 0;
}