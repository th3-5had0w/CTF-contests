// gcc -m32 -mpreferred-stack-boundary=2 stack3.c -o stack3 -fno-stack-protector -no-pie
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
    int cookie = 0xdeadbeef;
    

    init();
    printf("Input : "); 
    gets(buf); 
    if (cookie == 0x000D0A00) 
    {
        system("/bin/sh");
    }
    else 
    {
        printf("Your cookie : 0x%x\n", cookie);
    }
    return 0;
}
