#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    system("echo QUNOX0NURntDNFRDSC1USEUtTTAwTi01Njc4fQ== | base64 --decode");
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

void vulnerable_function() {
    char buffer[64];
    printf("Enter your input (no spaces or tabs allowed): ");
    
    int i = 0;
    char ch;
    while ((ch = getchar()) != '\n' && i < sizeof(buffer) - 1) {
        if (ch == ' ') {
            printf("Spaces are not allowed!\n");
            return;
        }
        if (ch == '\t') {
            printf("Tabs are not allowed!\n");
            return;
        }
        buffer[i++] = ch;
    }
    buffer[i] = '\0';

    // Replace special sequences `/s` with space and `/t` with tab
    for (int j = 0; j < i; j++) {
        if (buffer[j] == '/' && buffer[j+1] == 's') {
            buffer[j] = ' ';
            memmove(&buffer[j+1], &buffer[j+2], i - j - 1);
            i--;
        } else if (buffer[j] == '/' && buffer[j+1] == 't') {
            buffer[j] = '\t';
            memmove(&buffer[j+1], &buffer[j+2], i - j - 1);
            i--;
        }
    }

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
    printf("Program finished :)\n");
    return 0;
}

