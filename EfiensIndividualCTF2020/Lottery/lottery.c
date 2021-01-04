#include <stdio.h>
#include <stdlib.h>
#include <time.h>

//gcc -m32 -o lottery lottery.c
int main(void)
{
    srand(time(0));
    char name[10];
    int number, s1, s2;
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);
    printf("Give me your name:");
    fgets(name, 10, stdin);

    s1 = rand() % 1000000;
    s2 = rand() % 1000000;
    printf("Hello ");
    printf(name);
    puts("\nPick a number: ");
    scanf("%d", &number);
    if (number != s1 + s2)
    {
        printf("The lucky number is %d\n", s1 + s2);
        puts("Good luck next time");
    }
    else
    {
        system("/bin/cat flag.txt");
    }
    return 0;
}
