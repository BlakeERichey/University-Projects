#pragma once
#include <string>
using namespace std;

class Node{
	public:
		Node();
		~Node();

	private:
		string	data;
		struct Node	*nextNode;
	};

	Node::Node()
	{

	}

	Node::~Node()
	{

	}