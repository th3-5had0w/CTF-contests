#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[])
{
	char a[10] = "rps";
	srand(atoi(argv[1]));
	for (int i = 0; i < 50; ++i)
	{
		printf("%c", a[rand() % 3]);
	}
}
