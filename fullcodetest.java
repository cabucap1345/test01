//OK
// ===== JAVA SECTION =====
public class HelloWorld {
    public static void main(String[] args) {
        for (int i = 0; i < 3; i++) {
            System.out.println("Java says hello number " + i);
        }
        String message = getMessage("Cyberhaven");
        System.out.println(message);
    }

    public static String getMessage(String name) {
        return "Hello " + name + " from Java method!";
    }
}

// ===== JAVASCRIPT SECTION =====
/*
   Some utility functions written in JS
*/
function multiply(a, b) {
    return a * b;
}

function square(n) {
    return multiply(n, n);
}

console.log("JS square of 5:", square(5));
console.log("JS multiply 3*7:", multiply(3,7));

// ===== BATCH SCRIPT SECTION =====
:: Simple Windows batch script
@echo off
setlocal enabledelayedexpansion
for /L %%i in (1,1,3) do (
    echo Batch iteration %%i
)
set GREETING=HelloFromBatch
echo %GREETING%
pause

// ===== PYTHON SECTION =====
# Python utility functions
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def main():
    nums = [3, 5, 7]
    for n in nums:
        print(f"Python factorial of {n} = {factorial(n)}")

if __name__ == "__main__":
    main()

// ===== GOLANG SECTION =====
package main

import "fmt"

func fibonacci(n int) int {
    if n <= 1 {
        return n
    }
    return fibonacci(n-1) + fibonacci(n-2)
}

func main() {
    for i := 0; i < 6; i++ {
        fmt.Println("Go Fibonacci:", fibonacci(i))
    }
}
