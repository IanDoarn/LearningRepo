/**
 * FizzBuzz
 * Written by: Ian Doarn
 */
public class FizzBuzz {
    static String fizzbuzz(int n) {
        if(n % 3 == 0 && n % 5 == 0)
            return "FizzBuzz";
        else if(n % 3 == 0)
            return "Fizz";
        else if(n % 5 == 0)
            return "Buzz";
        return Integer.toString(n);
    }
    public static void main(String[] args) {
        for(int i = 0; i < 100; i++)
            System.out.println(fizzbuzz(i + 1));
    }
}
