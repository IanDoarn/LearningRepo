// Fizzbuzz.cpp
// Written by: Ian Doarn

#include "stdafx.h"

int main()
{
	for (int i = 1; i < 101; i++) 
	{
		if (i % 3 == 0 && i % 5 == 0)
			printf("FizzBuzz\n");
		else if (i % 3 == 0)
			printf("Fizz\n");
		if (i % 5 == 0)
			printf("Buzz\n");
		else
			printf("%d\n", i);
	}
    return 0;
}

