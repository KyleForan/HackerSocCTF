#include <stdio.h>
#include <string.h>

char* flag1 = "G}\n";
char* flag2 = "EHS{FAK";
char* flag3 = "E_FLA";
char total[32];

int main(void) {
    char input[32];
    
    printf("Enter a password: ");
    fgets(input, 32, stdin);

    strcpy(total, flag2);
    strcat(total, flag3);
    strcat(total, flag1);
    
    if (strcmp(total, input) == 0) {
        puts("Correct Password!");
    } else {
        puts("Incorrect :(");
    }
    
}