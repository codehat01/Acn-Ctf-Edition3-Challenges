#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Thread-local storage for the flag
__thread char tls_flag[] = "QUNOX0NURntDNFRDSC1USEUtTTAwTi01Njc4fQ==";

void math_trick_function(int a, int b) {
    int sum = a + b;
    int product = a * b;
    printf("The sum of %d and %d is %d.\n", a, b, sum);
    printf("The product of %d and %d is %d.\n", a, b, product);
}
void red_herring_function() {
    printf("This is a red herring. Nothing important here.\n");
}
void give_flag() {
    puts("Congratulations! You've found the flag:");
    printf("%s\n", tls_flag);
}
void mislead_function() {
    printf("You're getting warmer, but this isn't the flag.\n");
}
void secret_function() {
    printf("You're really close now...\n");
}
void hidden_function() {
    printf("This is a hidden function. Keep exploring!\n");
}
void check_values(int x) {
    if (x == 42) {
        printf("You've found the magic number! But no flag here.\n");
    } else {
        printf("The number %d is not the magic number. Keep trying.\n", x);
    }
}
void string_manipulation_function(char *input) {
    char result[100];
    strcpy(result, input);
    strcat(result, " - processed");
    printf("The manipulated string is: %s\n", result);
}
void arithmetic_challenge(int num) {
    int doubled = num * 2;
    int squared = num * num;
    printf("The number %d doubled is %d.\n", num, doubled);
    printf("The number %d squared is %d.\n", num, squared);
}

void final_trap_function() {
    printf("Almost there, but this is not the flag!\n");
}

// Padding bytes added around the buffer to add complexity
void vulnerable_function() {
    char padding_before[16]; // Padding before the buffer
    char buffer[64];         // Buffer with potential for overflow
    char padding_after[16];  // Padding after the buffer

    memset(padding_before, 0, sizeof(padding_before));
    memset(padding_after, 0, sizeof(padding_after));

    printf("Enter your input: ");
    gets(buffer);  // Vulnerability: Buffer Overflow
    printf("You entered: %s\n", buffer);
}

void check_palindrome(char *str) {
    int len = strlen(str);
    int is_palindrome = 1;
    for (int i = 0; i < len / 2; i++) {
        if (str[i] != str[len - i - 1]) {
            is_palindrome = 0;
            break;
        }
    }
    if (is_palindrome) {
        printf("The string '%s' is a palindrome.\n", str);
    } else {
        printf("The string '%s' is not a palindrome.\n", str);
    }
}
void array_sum(int arr[], int size) {
    int sum = 0;
    for (int i = 0; i < size; i++) {
        sum += arr[i];
    }
    printf("The sum of the array elements is %d.\n", sum);
}

int main() {
    printf("Welcome to the CTF challenge!\n");
    vulnerable_function();
    printf("Program finished:)\n");
    return 0;
}

