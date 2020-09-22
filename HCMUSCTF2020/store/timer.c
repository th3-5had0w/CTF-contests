#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(){
	srand(time(0)+2);
	sleep(1);
	rand();
	rand();
	rand();
	sleep(1);
	printf("%d\n", rand() % 123456);
}
