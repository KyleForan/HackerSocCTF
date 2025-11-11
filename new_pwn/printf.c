#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int token;

int vuln(void){
    char buffer[200];
    token = 0xdeadbeef;

    printf("Changing the token without overflow??\n");
    printf("Changing token at %p to a new value 0xfeedf00d\n", &token);
    printf("Input: ");

    fflush(stdout);
    fgets(buffer, 200, stdin);
    printf(buffer);

    if (token == 0xfeedf00d) {
        puts("Congrats");
        system("cat ./flag");
    } else {
        printf("Token: %x\n", token);
    }

}

int main(void) {
    vuln();
}