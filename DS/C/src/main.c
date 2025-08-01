#include <stdio.h>
#include "patterns.h"
#include "math_utils.h"
#include "ds.h"
#include "dsq.h"

void printMenu() {
    printf("\nChoose pattern:\n");
    printf("1. Horizontal *\n");
    printf("2. Vertical *\n");
    printf("3. 0 1 2 3\n");
    printf("4. 1 2 3 4\n");
    printf("5. * * * (Grid)\n");
    printf("6. * * * (Triangle)\n");
    printf("7. * * * (Inverted) triangle\n");
    printf("8. Factorial\n");
    printf("9. Recursive factorial\n");
    printf("10. Check num is prime or not\n");
    printf("11. Print the next prime number\n");
    printf("12. Print all divisors of a number\n");
}

int main() {
    int n = 0, choice = 0;
    printf("Enter n: ");
    scanf("%d", &n);

    printMenu();
    scanf("%d", &choice);
    
    switch (choice) {
        case 1: pattern1(n); break;
        case 2: pattern2(n); break;
        case 3: pattern3(n); break;
        case 4: pattern4(n); break;
        case 5: pattern5(n); break;
        case 6: pattern6(n); break;
        case 7: pattern7(n); break;
        case 8: factorial(n); break;
        case 9: printf("%d\n", recFact(n)); break;
        case 10: printf(isPrime(n) ? "%d is prime\n" : "%d isn't prime\n", n); break;
        case 11: printf("The next prime number after %d is %d\n", n, nextPrime(n)); break;
        case 12: allDivisor(n); break;
        default: printf("Invalid choice!\n");
        
    }
    return 0;
}
