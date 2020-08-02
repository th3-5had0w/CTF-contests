#include <unistd.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <stdio.h>

int main(){
	char buf[50];
	memset(buf, 0, 50);
	int f = open("./flag.txt",O_RDONLY);
	read(f, buf, 50);
	write(0, buf, 50);
}
