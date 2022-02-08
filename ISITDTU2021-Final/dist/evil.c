#include <stdio.h>

int main() {
    char c;
    fread(&c, 1, 0x1000, stdin);
    puts("Status: 200 OK\n\nGood luck");
}
