#include "brichey.h"

using namespace std;

void restart();
bool runCmd(int *ic, int registers[], int ram[], int *accum);

int main() {
	//initialize variables
	int ram[1000];
	int registers[10];
	int ic = 0;	//next instruction to be run
	int accum = 0; //total num of instruction run
	string	 filename;
	ifstream readFile;
	ofstream writeFile;
	initArray(registers, 10, 0);	//initialize all values in registers to 0


	cout << "File Should Be in Same Directory as .exe\n" << "Enter File Name to Read (e.g. test.txt): ";
	Input(filename);	//Take input from console and save value to filename (pass by reference)

	cout << "Filename is " << filename << "\nOpening..." << endl;
	
	//***open file named filename***
	readFile.open(filename);
	if (!readFile.is_open()) { //file failed to open?
		cout << "Failed to find file... You will be prompted again." << endl;
		system("pause");
		system("CLS");
		main();
		exit(EXIT_FAILURE);
	}

	//***load ram***
	string cmd;	//variable for instruction value
	getline(readFile, cmd);
	int index = 0;	//current ram index
	while (readFile.good() && index < 1000) { //while not EOF
		try
		{
			char e = 'e';
			if (cmd.length() > 3 && isdigit(stoi(cmd))) { throw e; }
		}
		catch (char e) {
			cout << "Invalid Format Type." << endl;
			restart();
		}
		ram[index] = stoi(cmd);
		readFile >> cmd; //save next word into word
		index++;
	}
	readFile.close();

	bool run = true;
	while (run) {
		run = runCmd(&ic, registers, ram, &accum);
	}

	cout << "Registers 0-9:" << endl;
	spit(registers, 10); //display registers
	//cout << "Ram:" << endl;
	//spit(ram, 20);
	cout << "ic: " << ic << " accum " << accum << endl;

	
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

//runs executions loaded in ram
bool runCmd(int *ic, int registers[], int ram[], int *accum) {
	*accum = *accum + 1; //increase number of instructions run
	string instr;
	if (ram[*ic] == 100) { return false; } //cease execution
	else{
		instr = intToString(ram[*ic]);
	}

	char type = instr.at(0);	//type of cmd to execute
	int x	  = to_int(instr.at(1));	//variable changes in purpose
	int y     = to_int(instr.at(2));	//variable changes in purpose

	if (type == '2') {
		registers[x] = y;
	}
	else if (type == '3') {
		registers[x] *= y;
		registers[x] = registers[x] % 1000;
	}
	else if (type == '4') {
		registers[x] += y;
		registers[x] = registers[x] % 1000;
	}
	else if (type == '5') {
		registers[x] = registers[y];
	}
	else if (type == '6') {
		registers[x] *= registers[y];
		registers[x] = registers[x] % 1000;
	}
	else if (type == '7') {
		registers[x] = registers[x] + registers[y];
		registers[x] = registers[x] % 1000;
	}
	else if (type == '0') {
		cout << "Hello" << endl;
	}
	
	*ic = *ic + 1;
	return true; 
}