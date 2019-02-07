#pragma once
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>

int total(int x, int y) {
	return x + y;
}

//takes val address and changes its value to whatever is input to the console
std::string & Input(std::string &val) {
	val.clear();		//reinitialize val
	getline(std::cin, val);
	return val;
}