#include <stdio.h>


int main(){
	int ptr;
	FILE *stream = fopen("flag.txt", "rb");
	fread(&ptr, 1uLL, 4uLL, stream);
	printf("%d", ptr);
}
