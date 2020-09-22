#include <stdio.h>

void shell(int arg)
{
	if (arg == 0x1337)
		execve("/bin/sh", 0, 0);
	else
		puts("[+] Nice try ahahahhaah !");
}

void overflow()
{
	char name[16];
	printf("[+] Hello, what's your name? : ");
	fgets(name, 64, stdin);
	printf("[+] Welcome, %s\n", name);
}

int main()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	overflow();
	return 0;
}
