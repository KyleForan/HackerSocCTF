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
    asm("pop %rsi; ret;");
}

int win(int arg1, int arg2){
	printf("Arg1: %p/0xdeadbeef, Arg2: %p/0xfeedf00d\n", arg1, arg2);

    if (arg1 == 0xdeadbeef && arg2 == 0xfeedf00d) {
        puts("Congrats!!");
        system("cat ./flag");
    }

    exit(0);
    
}

int vuln(void) {
    char buffer[16];

    fflush(stdout);
    puts("Now can you return to win... with arguments 64x?");
    printf("Input: ");
    fgets(buffer, 200, stdin);
    
    printf("%s\n", buffer);}

int main(void) {
    vuln();
} 