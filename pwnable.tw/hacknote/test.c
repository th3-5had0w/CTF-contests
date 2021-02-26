#include <stdio.h>
#include <stdlib.h>

int main(){
	int *a=malloc(10);
	int *b=malloc(10);
	free(a);
	free(b);
	free(a);
	*a=0x4141414141414141;
	malloc(10);
	malloc(10);
}
