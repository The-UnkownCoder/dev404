#include <stdio.h>
#include <stdbool.h>
#include "math_utils.h"

void factorial(int n) {
    int fact = 1;
    for (int i = 1; i <= n; i++) fact *= i;
    printf("%d", fact);
}

int recFact(int n) {
    return (n <= 1) ? 1 : n * recFact(n - 1);
}

bool isPrime(int n) {
    if (n <= 1) return false;
    for (int i = 2; i * i <= n; i++)
        if (n % i == 0) return false;
    return true;
}

int nextPrime(int n) {
    n++;
    while (!isPrime(n)) n++;
    return n;
}

void allDivisor(int n) {
    for (int i = 1; i <= n; i++)
        if (n % i == 0) printf("%d ", i);
}
