#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int win(void) {
    puts("Congrats!!");
    system("cat ./flag");
}

int vuln(void) {
    char buffer[16];

    printf("The address of win: %p\n", win);

    fflush(stdout);
    printf("How to get to win???: ");
    gets(buffer);
    
    printf("%s\n", buffer);

    return 1;
}

int main(void) {
    vuln();
}