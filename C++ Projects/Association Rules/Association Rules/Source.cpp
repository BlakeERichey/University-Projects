#include "brichey.h"

using namespace std;

int main() {
	string implier;
	string implied;
	int supportImplier = 0;
	int supportBoth = 0;

	cout << "Implier statement: ";
	Input(implier);
	cout << "Implied statement: ";
	Input(implied);

	supportImplier = getInt("Support for " + implier + ": ");
	supportBoth    = getInt("Support for " + implier + " and " + implied + ": ");

	cout << "Confidence for \"" << implier << " implies " << implied << "\": " << supportBoth / float(supportImplier) << endl;
	system("pause");
	return 1;
}