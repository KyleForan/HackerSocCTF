#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int win(void){
    puts("Congrats!!");
    system("cat ./flag");

    return 1;
}

int vuln(void) {
    char buffer[120];

    fflush(stdout);
    printf("Now can you find and return to win?\n");
    printf("Safe Input: ");
    fgets(buffer, sizeof(buffer), stdin);
    
    printf(buffer);

    printf("Overflow Input: ");
    gets(buffer);

}

int main(void) {
    vuln();
} 