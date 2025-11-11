#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int freestuff() {
    asm("pop %rdi; ret;");
    asm("pop %rsi; ret;");
}

int win(int arg1, int arg2){
    printf("First arg: %p\nSecond arg: %p\n", arg1, arg2);

    if (arg1 == 0xdeadbeef && arg2 == 0xfeedf00d) {
        puts("Congrats!!");
        system("cat ./flag");
    }
    return 1;
}

int vuln(void) {
    char buffer[16];

    fflush(stdout);
    printf("Now can you return to win... with arguments 64x?: ");
    fgets(buffer, 200, stdin);
    
    printf("%s\n", buffer);}

int main(void) {
    vuln();
} 