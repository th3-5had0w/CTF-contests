// gcc -m32 -o stack2 stack2.c -fno-stack-protector
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
    int cookie;
    char buf[16];  

    init();
    printf("Input : "); 
    gets(buf); 
    if (cookie == 0x01020305) 
    {
        system("/bin/sh");
    }
    else 
    {
        printf("Your cookie : 0x%x\n", cookie);
    }
    return 0;
}