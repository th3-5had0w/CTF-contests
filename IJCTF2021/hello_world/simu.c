#include <stdio.h>

int main(){
	char v1, v2, v3, v4, v5, v6, v7, v8;
	int result;
	char lel[100] = "dau_b";
	for (int i =0;;i+=2){
		result = (unsigned int)i;
		if (i>=100){
			break;
		}
		v7 = ((unsigned int)lel[i] >> 4) + 16 * lel[i+1];
		v6 = ((unsigned int)lel[i+1] >> 4) + 16 * lel[i];
		if (v7 >= 0){
			v1 = 2 * v7;
		}
		else{
			v1 = (2 * v7) | 1;
		}

		if (v1 >= 0){
			v2 = 2 * v1;
		}
		else{
			v2 = (2 * v1) | 1;
		}

		if (v2 >= 0){
			v3 = 2 * v2;
		}
		else{
			v3 = (2 * v2) | 1;
		}

		v8 = v3;

		if (v6 >= 0){
			v4 = 2 * v6;
		}
		else{
			v4 = (2 * v6) | 1;
		}

		if (v4 >= 0){
			v5 = 2 * v4;
		}
		else{
			v5 = (2 * v4) | 1;
		}
		lel[i] = v8 ^ 0x13;
		lel[i+1] = v5 ^ 0x37;
	}
	printf("%s\n", lel);
	return result;
}
