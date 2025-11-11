#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int freestuff() {
    asm("pop %rdi; ret;");
}

int vuln(void) {
    char unsafebuffer[16];

    fflush(stdout);
    puts("Now can you return to win... with arguments 64x?");
    
    printf("Input: "); 
    fgets(unsafebuffer, 200, stdin);
    
}

int main(void) {
    vuln();
} 