#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    int token = 5;
    char password[16];

    printf("Welcome Admin.\n");
    printf("The token is currently: %x, change it for the flag.\n", token);
    printf("Enter Your Password: ");

    fflush(stdout);
    gets(password);
    
    printf("Password: %s\n", password);
    printf("Token: %x\n", token);

    if (token != 5) {
        printf("EHS{flag}");
    }

}