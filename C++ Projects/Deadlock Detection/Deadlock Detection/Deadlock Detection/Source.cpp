#include "brichey.h";

using namespace std;

void displayResourceLine(int resources);
bool isValidRequest(int request[], int work[], int qty);

int main() {
	const int MAX_CAPACITY = 100;	//maximum number of resources and processes
	const int processes = getInt("Enter number of processes (max 100): ");
	const int resources = getInt("Enter number of resources (max 100): ");

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
	cout << "Allocation Matrix: " << processes << " Processes, " << resources << " Resources." << endl;
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
	cout << "Request Matrix: " << processes << " Processes, " << resources << " Resources." << endl;
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
	cout << "Available Resources Vector: " << resources << " Resources." << endl;
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

	//---------------Step 2 to Algorithm---------------
	bool run = true;
	while (run) {
		run = false;
		int process = 0;
		for (process; process < processes; process++) {
			if (finish[process] == false
				&& isValidRequest(request_matrix[process], work, resources)) {
				break;
			}
		}
		if (process < processes) { //---------------Step 3 to Algorithm---------------
			cout << "Process " << process << " can be allocated space... Running again..." << endl;
			addArr(allocation_table[process], work, resources);
			finish[process] = true;
			run = true;	//resources have changed, rerun
		}
	}

	
	//---------------Display Results---------------
	clearConsole();
	//Display Allocation Matrix
	cout << "Allocated" << endl;
	displayResourceLine(resources);
	for (int process = 0; process < processes; process++) {
		printArr(allocation_table[process], resources);
	}

	//Display Available Resources Vector
	cout << endl << endl << "Available" << endl;
	displayResourceLine(resources);
	printArr(available_matrix, resources);

	//Display Requested Matrix
	cout << endl << endl << "Requested" << endl;
	displayResourceLine(resources);
	for (int process = 0; process < processes; process++) {
		printArr(request_matrix[process], resources);
	}

	//---------------Step 4 to Algorithm---------------
	bool deadlocked = false;
	for (int process = 0; process < processes; process++) {
		if (finish[process] == 0) { //unfinished processes?
			deadlocked = true; 
			break; 
		}
	}

	//Display Deadlock Status
	cout << endl << endl;
	if (deadlocked) {
		cout << "System is deadlocked, the deadlocked processes are:" << endl;
		for (int process = 0; process < processes; process++) {
			if (finish[process] == 0) { cout << "Process " << process << endl; }
		}
	}
	else {
		cout << "System is not deadlocked, all processes can complete." << endl;
	}

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