// erasing from list
#include <iostream>
#include <list>
using namespace std;

int main()
{
	unsigned int i;
	list<unsigned int> mylist;
	list<unsigned int>::iterator it1, it2;

	// set some values

	for (i = 1; i < 10; i++)
	{
		mylist.push_back(i * 10);
		// 10 20 30 40 50 60 70 80 90
	}
	it1 = it2 = mylist.begin();
	advance(it2, 6);
	++it1;
	it1 = mylist.erase(it1); // 10 30 40 50 60 70 80 90
	it2 = mylist.erase(it2); // 10 30 40 50 60 80 90
	++it1;
	++it2;

	mylist.erase(it1, it2); // 10 30 60 80 90

	cout << "mylist contains: ";
	for (it1 = mylist.begin(); it1 != mylist.end(); ++it1)
	{
		cout << "" << *it1;
		cout << endl;
	}

	return 0;
}
