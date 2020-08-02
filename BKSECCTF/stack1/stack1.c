// gcc -m32 -o stack1 stack1.c -fno-stack-protector 
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
    int cookie = 0xdeadbeef;
    char buf[16]; 
    printf("Input : "); 
    gets(buf); 
    if (cookie == 0x41424344) 
    {
        system("/bin/sh\x00");
    }
    else 
    {
        printf("Your cookie : 0x%x\n", cookie);
    }
    return 0;
}