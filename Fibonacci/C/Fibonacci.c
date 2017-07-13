// Fibonacci.c 
// Calculate fibonacci numbers up to 20
// Written by: Ian Doarn

#include <stdio.h>

void calculate(int n) {
	int a = 0, b = 1, c = 0, i = 0;

	for (i = 1; i < n + 1; i++) {
		c = a + b;
		a = b;
		b = c;

		printf("%d: %d\n", i, a);
	}
}

int main() {
	calculate(20);
	return 0;
}
