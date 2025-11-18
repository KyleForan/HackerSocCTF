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

int win(void) {
    puts("Congrats!!!");
    system("cat ./flag");
}

int get_rand_seed(void) {
    for (int i = 0; i < rand() % 1000; i++) {
        rand() % 100 + 1;
    }
    
    return rand() % 127158;
}

int main(void) {
    int guess;

    srand(get_rand_seed());

    puts("Guess the correct number 10 times to get the flag");
    for (int i = 0; i < 10; i++) {
        printf("Guess a number between 1 and 1000000: ");
        scanf("%d", &guess);

        if (rand() % 1000000 + 1 != guess) {
            puts("Incorrect!");
            exit(0);
        }
    }

    win();
} 