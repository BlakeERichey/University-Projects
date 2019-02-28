#include "brichey.h"

using namespace std;

int main() {
	//initialize values
	const int sides = 20; //sides to dice
	int possibilities[sides];
	int rolls[sides];
	for (int x = 0; x < sides; x++) {
		possibilities[x] = x + 1; //possibilities[2] = 3
	}
	initArray(rolls, sides, 0);

	bool run		= true;
	int iteration	= 0;
	int accum		= 0;
	int testQty		= 50;	//number of iterations to test
	//roll
	while (iteration < testQty) {
		while (run) {
			int roll = rand() % sides + 1;
			rolls[roll - 1] += 1;
			accum++;
			run = false;
			for (int index = 0; index < sides; index++) {
				if (rolls[index] == 0) {
					run = true;
				}
			}
		}
		run = true;
		initArray(rolls, sides, 0);
		iteration++;
	}
	cout << "It took " << accum / (double) testQty << " number of rolls on average to get all 20 possibilities given " << testQty << " number of iterations.";
	cout << endl << "Pausing before exiting..." << endl;
	system("pause");
	return 0;
}