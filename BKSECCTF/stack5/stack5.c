// gcc -m32 -o stack5 stack5.c -fno-stack-protector -no-pie -mpreferred-stack-boundary=2
#include <stdio.h>
#include <stdlib.h> 

void init()
{
        setbuf(stdin, 0);
        setbuf(stdout, 0);
        setbuf(stderr, 0);
}

int main()
{
    char buf[16];  


    init();
    printf("Input :");
    gets(buf); 
    return 0;
}

