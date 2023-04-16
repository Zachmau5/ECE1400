
#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

long int factorial(int n) {
    if (n == 0) {
        return 1;
    }
    return n * factorial(n - 1);
}
bool main(int argc, char *argv[]) {
    if (argc != 2) {
        printf("Invalid input\n");
        return false;
    }
    int input = atoi(argv[1]);

    if (input < 0 || input > 50) {
        printf("Invalid input\n");
        return false;
    }

    long int result = factorial(input);
    printf("%ld\n", result);

    return 0;
}

