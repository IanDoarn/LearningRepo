// Fibonacci.cpp 
// Calculate fibonacci numbers up to 20

#include "stdafx.h"
#include <iostream>
#include "Fibonacci.h"
using namespace std;

void Fibonacci::calculate(int n) {
	static int a = 0, b = 1, c;

	for (int i = 1; i < n + 1; i++) {
		c = a + b;
		a = b;
		b = c;

		cout << i << ": " << a << endl;
	}

}


int main() {
	Fibonacci fib;
	fib.calculate(20);

    return 0;
}

