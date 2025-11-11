#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int win(int arg1, int arg2){
	printf("Arg1: %p/0xdeadbeef, Arg2: %p/0xcafebabe\n", arg1, arg2);
    if (arg1 == 0xdeadbeef && arg2 == 0xcafebabe) {
        puts("Congrats!!");
        system("cat ./flag");
    }
    exit(0);
}

int vuln(void) {
    char buffer[16];

    fflush(stdout);
    puts("Now can you return to win... with arguments?");
    puts("Call win with the arguments 0xdeadbeef and 0xcafebabe");
    printf("Input: ");
    fgets(buffer, 200, stdin);
    
    printf("%s\n", buffer);
}

int main(void) {
    vuln();
} 
