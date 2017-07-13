// Fibonacci.cs
// Written By: Ian Doarn
using System;

namespace Program
{
    /// <summary>
    /// Simple Fibonacci sequence up to 20 numbers
    /// </summary>
    class Fibonacci
    {
    
        /// <summary>
        /// fibonacci sequence method
        /// </summary>
        /// <param name="n"> Number by which to calculate to </param>
        /// <returns></returns>
        private static int fibonacci(int n)
        {
            int a = 0;
            int b = 1;
            int c;

            for(int i = 1; i < n + 1; i++)
            {
                c = a + b;
                a = b;
                b = c;

                Console.WriteLine(i.ToString() + ": " + a.ToString());
            }

            return a;
        }

        static void Main(string[] args)
        {
            // Call function, we are only going up to 20 fibonacvci numbers
            fibonacci(20);

            // Wait for user to press a key to close
            Console.ReadKey();
        }
    }
}
