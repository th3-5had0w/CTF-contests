#include <stdio.h>
#include <stdlib.h>

int main(){
	int *ptr[10];
	for (int i=0; i<10; ++i){
		ptr[i] = malloc(0x10);
	}
	
	for (int i=0;i<7;++i){
		free(ptr[i]);
	}
	free(ptr[7]);
	free(ptr[8]);
	free(ptr[9]);
	return 0;
}
