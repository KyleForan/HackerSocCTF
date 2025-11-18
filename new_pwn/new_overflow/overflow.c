#include <stdio.h>
#include <stdlib.h>
#include <string.h>

__attribute__((constructor)) void setup() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}


int main(void) {
    int x, y, z, tot;

    puts("Enter 3 positive numbers where");
    puts("num 1 + num 2 is less than both");
    puts("num 2 + num 3 is less than both");
    puts("num 1 + num 2 + num 3 == 1016");
    printf("Input > ");

    scanf("%d %d %d", &x, &y, &z);

    if (x < 0 || y < 0 || z < 0) {exit(0);}
    
    tot = x + y;
    if (tot > x || tot > y) {
        printf("Incorrect %d is greater than %d and %d\n", tot, x, y);
        exit(0);
    }

    tot = z + y;
    if (tot > z || tot > y) {
        printf("Incorrect %d is greater than %d and %d\n", tot, y, z);
        exit(0);
    }

    tot = x + y + z;
    if (tot == 1016) {
        puts("Congrats!!!");
        system("cat ./flag");
    } else {
        printf("Incorrect the total is %d not 1016\n", tot);
    }

} 