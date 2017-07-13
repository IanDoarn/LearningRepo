/**
 * Fibonacci
 * Prints first 20 fibonacci numbers starting at 1
 * Written by: Ian Doarn
 */
public class Fibonacci {
    static void fibonacci(int n) {
        int a = 0,b = 1, c;

        for(int i = 1; i < n + 1; i++) {
            c = a + b;
            a = b;
            b = c;
            System.out.printf("%d: %d\n", i, a);
        }
    }

    public static void main(String[] args) {
        fibonacci(20);
    }
}
