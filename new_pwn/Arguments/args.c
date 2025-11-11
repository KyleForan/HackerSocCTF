#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int win(int arg1, int arg2){
    if (arg1 == 0xdeadbeef && arg2 == 0xcafebabe) {
        puts("Congrats!!");
        system("cat ./flag");
    }
    return 1;
}

int vuln(void) {
    char buffer[16];

    fflush(stdout);
    printf("Now can you return to win... with arguments?: ");
    printf("Call win with the arguments 0xdeadbeef and 0xcafebabe");
    fgets(buffer, 200, stdin);
    
    printf("%s\n", buffer);}

int main(void) {
    vuln();
} 