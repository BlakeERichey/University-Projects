#pragma once
#include <iostream>
#include <string>
#include <fstream>
#include <cstdlib>
#include <sstream>

int total(int x, int y) {
	return x + y;
}

//takes val address and changes its value to whatever is input to the console
std::string & Input(std::string &val) {
	val.clear();		//reinitialize val
	getline(std::cin, val);
	return val;
}

//initializes values of an array
//size: array length
void initArray(int arr[], int size, int val) {
	for (int x = 0; x < size; x++) {
		arr[x] = val;
	}
}

//displays qty number of elements from an array
void spit(int array[],int qty) {
	for (int index = 0; index < qty; index++) {
		std::cout << array[index] << std::endl;
	}
}

std::string intToString(int val) {
	std::stringstream ss;
	ss << val << std::endl;
	std::string valAsString = ss.str();
	return valAsString;
}

//returns char c as an integer between 0-9
int to_int(char c) {
	return c%48;
}