#include <stdio.h>

void flag()
{
    char flag[64];
    FILE* f = fopen("flag.txt", "r");
    fgets(flag, sizeof(flag), f);
    fclose(f);
    printf("[+] Flag: %s", flag);
}

int main()
{
    char name[256];
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
    printf("[+] What's your name: ");
    fgets(name, sizeof(name), stdin);
    printf("[+] Hello ");
    printf(name);
    return 0;
}

