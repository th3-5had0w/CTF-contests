#include <stdio.h>
#include <stdlib.h>
int main()
{
	setbuf(stdin, 0);
	setbuf(stdout, 0);
	setbuf(stderr, 0);
	char flag[64];
	char name[256];
	FILE* f = fopen("flag.txt", "r");
	if (f == NULL)
	{
		puts("[+] Error, please contact admin");
		exit(1);
	}
	fgets(flag, sizeof(flag), f);
	fclose(f);
	printf("[+] What's your name: ");
	fgets(name, sizeof(name), stdin);
	printf("[+] Hello: ");
	printf(name);
	return 0;
}
