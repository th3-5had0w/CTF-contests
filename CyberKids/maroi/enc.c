#include <stdio.h>
#include <string.h>

int checkPassword(char * input) {
    int input_len = strlen(input);
    if ((input_len ^ 0x000000000000000F)) return 0;;
    if ((strncmp(input, "\x43"
            "T\106{", 4) ^ 0x0000000000000000)) return 0;;
    if (input[14] != '}') return 0;;
    const char * flag = input + 4;
    if ((flag[0] > '0') & !!(flag[0] > '0') || (flag[0] < '0') & !!(flag[0] < '0')) return 0;;
    if (((int) flag[1] + 6969 ^ 7067)) return 0;; // flag[1] = 'b'
    if (((int) flag[2] + (int) flag[3] ^ 0x00000000000000DB)) return 0;; // flag[2] = f
    if (((int) flag[3] - (int) flag[2] ^ 0x000000000000000F)) return 0;; // flag[3] = u
    if (flag[4] - flag[3] != (char)(-18)) return 0;; // flag[4] = c
    if (((flag[5] ^ '0') ^ 0x0000000000000004)) return 0;; //flag[5] = 4
    char o_f5c873c850d6c0a448164d6be733d86f = (char) flag[6] * (char) flag[5]; 
    if ((char)(flag[6] * flag[5]) != -112) return 0;;
    if ((10 * (int) flag[7] - 12 * (int) flag[8] + 19 * (int) flag[9] ^ 0x00000000000007D4)) return 0;;
    if ((28 * (int) flag[7] - (int) flag[8] + 69 * (int) flag[9] ^ 0x00000000000022D2)) return 0;;
    if ((113 * (int) flag[7] - 126 * (int) flag[8] + 999 * (int) flag[9] ^ 0x000000000001AB43)) return 0;;
    return 1;
};

int main()
{
	char password[128];
	printf("[+] Hay~ nhap password: ");
	gets(password);
	if (0 != checkPassword(password))
		printf("[+] Password dung, flag la %s\n", password);
	else
		printf("[+] Ban da nhap sai password\n");
	return 0;
}
