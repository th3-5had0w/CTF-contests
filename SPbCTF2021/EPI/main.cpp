#pragma GCC optimize ("O3")

#include <stdio.h>
#include <stdlib.h>

int main(){
	FILE *file_stream = fopen("flag.png.encrypted", "rb");
	fseek(file_stream, 0LL, 2);
	long length = ftell(file_stream);
	fseek(file_stream, 0LL, 0);
	u_int8_t *buf = (u_int8_t*)malloc(length);
	fread(buf, 1, length, file_stream);
	fclose(file_stream);
	FILE *fo = fopen("flag.png", "wb");

	u_int64_t lengtha;
	lengtha	= length;
	if ( (length & 1) != 0 )
		lengtha = length + 1;
	/*
	for (u_int64_t i = 0; i < lengtha >> 1; ++i ){
		u_int16_t state = *(u_int16_t*)&buf[2 * i];
		printf("%x\n", state);
		for (u_int64_t round = 0; round < 0x20F76D2; ++round )
			state = ((((((((state / 21727 + 11258) / 18199) ^ 0x448C) / 25561) - 14122) / 31663) + 16196) / (-1635)) ^ 0x6bb1;
		*(u_int16_t*)&buf[2 * i] = state;
		printf("%x\n", (u_int16_t)state);
		//printf("%ld/%ld\n", i, (lengtha >> 1) - 1);
		fwrite(&buf[2 * i], 2, 1, fo);
	}
	*/

	for (u_int64_t i = 0; i < lengtha >> 1; ++i ){
                u_int16_t state = *(u_int16_t*)&buf[2 * i];
		for (u_int64_t round = 0; round < 0x20F76D2; ++round ){
			u_int16_t j = 0;
			while (j <= 65535){
				if (state == (u_int16_t)(21727 * (18199 * ((25561 * (31663 * ((-1635) * (j ^ 0x6BB1) - 0x3F44) + 14122)) ^ 0x448C) - 11258))){
					printf("Round: %lx | Current %x | %x\n", round, state, (u_int16_t)(21727 * (18199 * ((25561 * (31663 * ((-1635) * (j ^ 0x6BB1) - 0x3F44) + 14122)) ^ 0x448C) - 11258)));
					state = j;
					break;
				}
				//printf("Testing j: %u\n", j);
				++j;
			}
		}
		printf("Origin value: %x\n", state);
		*(u_int16_t*)&buf[2 * i] = (u_int16_t)state;
		fwrite(&buf[2 * i], 2, 1, fo);
	}
	fclose(fo);

}
