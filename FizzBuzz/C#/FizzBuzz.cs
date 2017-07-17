// Fizzbuzz.cs
// Written By: Ian Doarn
using System;
using System.Text;


namespace Program
{
    class FizzBuzz
    {
        private static string fizzbuzz(int n)
        {
            if(n % 3 == 0 && n % 5 == 0)
            {
                return "FizzBuzz";
            }
            else if(n % 3 == 0)
            {
                return "Fizz";
            }
            else if (n % 5 == 0)
            {
                return "Buzz";
            }

            return n.ToString();

        }

        public static void Main(string[] args)
        {
            for(int i = 0; i < 101; i++)
            {
                Console.WriteLine(fizzbuzz(i));
            }
            Console.ReadLine();
        }
    }
}
