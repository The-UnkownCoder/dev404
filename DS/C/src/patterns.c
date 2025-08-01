#include <stdio.h>
#include "patterns.h"

void pattern1(int n) {
    for (int i = 0; i < n; i++) printf("* ");
    printf("\n");
}

void pattern2(int n) {
    for (int i = 0; i < n; i++) printf("*\n");
}

void pattern3(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < 5; j++) printf("%d ", j);
        printf("\n");
    }
}

void pattern4(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 1; j < 5; j++) printf("%d ", j);
        printf("\n");
    }
}

void pattern5(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < n; j++) printf("* ");
        printf("\n");
    }
}

void pattern6(int n) {
    for (int i = 0; i < n; i++) {
        for (int j = 0; j <= i; j++) printf("* ");
        printf("\n");
    }
}

void pattern7(int n) {
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n - i; j++) printf("  ");
        for (int j = 1; j <= i; j++) printf("* ");
        printf("\n");
    }
}
