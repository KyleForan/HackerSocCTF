#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

int freestuff() {
    asm("pop %rdi; ret;");
}

int vuln(void) {
    char unsafebuffer[16];

    fflush(stdout);
    puts("There is no win function, how will you get the shell now?");
    
    printf("Input: "); 
    fgets(unsafebuffer, 200, stdin);
    
}

int main(void) {
    vuln();
} 