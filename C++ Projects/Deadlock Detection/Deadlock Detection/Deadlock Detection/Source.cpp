#include "brichey.h";

using namespace std;

void displayResourceLine(int resources);
bool isValidRequest(int request[], int work[], int qty);
bool terminate(int request[][100], int work[], int processQty, int finish[], int resourceQty);

int main() {
	const int MAX_CAPACITY = 100;	//maximum number of resources and processes
	const int processes = getInt("Enter number of processes: ");
	const int resources = getInt("Enter number of resources: ");

	int work[MAX_CAPACITY];		//which resources are available while a request is taking place
	int finish[MAX_CAPACITY];	//which processes are complete
	int available_matrix[MAX_CAPACITY];				  //resources available at start of request
	int request_matrix[MAX_CAPACITY][MAX_CAPACITY];	  //request  values
	int allocation_table[MAX_CAPACITY][MAX_CAPACITY]; //currently allocated values


	//initialize 1 dimensional arrays
	initArray(work,             resources, 0);
	initArray(finish,           processes, 0);
	initArray(available_matrix, resources, 0);	
	
	//input values for allocation matrix
	clearConsole();
	cout << "Initializing Allocation Matrix... Sample Input for a 5 Resource Process Allocation: 12300" << endl;
	for (int process = 0; process < processes; process++) {
		cout << "Enter Allocation Array for Process " << process << ": ";
		initArray(allocation_table[process], resources, 0); //initialize process allocation

		//take input
		string num = "";
		Input(num);
		
		for (int index = 0; index < num.length(); index++) {
			allocation_table[process][index] = to_int(num[index]);
		}
	}

	//Input values for request matrix
	clearConsole();
	cout << "Initializing Request Matrix... Sample Input for a 5 Resource Process Allocation: 12300" << endl;
	for (int process = 0; process < processes; process++) {
		cout << "Enter Request for Process " << process << ": ";
		initArray(request_matrix[process], resources, 0); //initialize process request

		//take input
		string num = "";
		Input(num);

		for (int index = 0; index < num.length(); index++) {
			request_matrix[process][index] = to_int(num[index]);
		}
	}

	//input values for available resources vector
	clearConsole();
	cout << "Enter Values for Available Vector... Sample input for a 5 Resource System: 13521" << endl;
	//take input
	string num = "";
	Input(num);

	for (int index = 0; index < num.length(); index++) {
		available_matrix[index] = to_int(num[index]);
	}

	//---------------Step 1 to Algorithm---------------
	copyArr(available_matrix, work, MAX_CAPACITY);	//set work matrix = available matrix
	for (int process = 0; process < processes; process++) {	//find processes with no allocations
		if (isEmpty(allocation_table[process], resources)) {
			finish[process] = 1;
		}
	}

	cout << "Finish Array: " << endl;
	printArr(finish, processes);

	//---------------Step 2 to Algorithm---------------
	bool resume = !terminate(request_matrix, work, processes, finish, resources); //continue?
	while (resume) {
		for (int process = 0; process < processes; process++) {
			cout << "continue";
		}
	}

	/*
	clearConsole();
	//---------------Display Results---------------
	//Display Allocation Matrix
	cout << endl << endl << "Allocated" << endl;
	displayResourceLine(resources);
	for (int process = 0; process < processes; process++) {
		printArr(allocation_table[process], resources);
	}

	//Display Available Resources Vector
	cout << "Available" << endl;
	displayResourceLine(resources);
	printArr(available_matrix, resources);

	//Display Requested Matrix
	cout << endl << endl << "Requested" << endl;
	displayResourceLine(resources);
	for (int process = 0; process < processes; process++) {
		printArr(request_matrix[process], resources);
	}

	*/

	cout << endl << "Pausing before exiting..." << endl;
	system("pause");
	return 0;
}

void displayResourceLine(int resources) {
	for (int resource = 0; resource < resources; resource++) {
		cout << "R" << resource << " ";
	}
	cout << endl;
}

//compares each index of a process's request and work array
//request: single process request for available resources
//qty:	   resource array size
bool isValidRequest(int request[], int work[], int qty) {
	for (int index = 0; index < qty; index++) {
		if (request[index] > work[index]) { return false; }
	}
	return true;
}

//returns true if all conditions are present to terminate the program
//request: request matrix
//work:	   work matrix
bool terminate(int request[][100], int work[], int processQty, int finish[], int resourceQty) {

	bool allValid = true;
	for (int process = 0; process < processQty; process++) {
		if (!(finish[process] == 0
			&& isValidRequest(request[process], work, resourceQty)))
		{
			allValid = false;
		}
	}
	return allValid;
}