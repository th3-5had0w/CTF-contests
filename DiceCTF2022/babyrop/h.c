#include <stdio.h>
#include <fcntl.h>

int main(){
	int fd = open("flag.txt", 0, 0);
	printf("%d\n", fd);
}
