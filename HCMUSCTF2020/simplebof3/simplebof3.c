#include <stdio.h>

int lock1 = 0;
int lock2 = 0;
int lock3 = 0;
int lock4 = 0;

void shell()
{
	if (lock1 && lock2 && lock3 && lock4)
		execve("/bin/sh", 0, 0);
	else
		puts("[+] Nice try!");
}

void cat()
{
	lock1 = 1;
}

void dog()
{
	if (lock1)
		lock2 = 1;
}

void pig()
{
	if (lock1)
		lock3 = 1;
	else
		lock2 = 1;
}

void elephant()
{
	if (lock1 && lock3)
		lock4 = 1;
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


