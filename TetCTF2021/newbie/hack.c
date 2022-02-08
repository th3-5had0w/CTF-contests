#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char *table = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";

int main(int argc, char *argv[]){
	char s[56] = {0};
	for (int i = 0; i <= 0xffff; ++i){
		srand(i);
		memset(s, 0, 48);
		for (int j = 0; j <= 31; ++j ){
			s[j] = table[rand() % 62];
		}
		printf("%d:%s ", i, s);
	}
	return 0;
}