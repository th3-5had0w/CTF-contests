#include <stdio.h>
#include <time.h>
#include <stdlib.h>

int main(){
	int v5[5] = {0};
	unsigned int v0 = time(0);
	srand(v0);
	for (int i = 0; i <= 4; ++i ){
		v5[i] = random() % 1337;
		printf("%d ", v5[i]);
	}
}
