//gcc heap.c -o note_heap -z noexecstack -fstack-protector-all -fPIE -pie -z now
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>

#include "seccomp.h"

int *int_ptr=0;
short int *short_ptr=0;
int _bool=0;
int show_time=2;


// void sandbox()
// {
// 	prctl(PR_SET_NO_NEW_PRIVS,1,0,0,0);
// 	struct sock_filter sfi[] = {
// 		{0x20,0x00,0x00,0x00000004},
// 		{0x15,0x00,0x05,0xc000003e},
// 		{0x20,0x00,0x00,0x00000000},
// 		{0x35,0x00,0x01,0x40000000},
// 		{0x15,0x00,0x02,0xffffffff},
// 		{0x15,0x01,0x00,0x0000003b},
// 		{0x06,0x00,0x00,0x7fff0000},
// 		{0x06,0x00,0x00,0x00000000},
// 	};
// 	struct sock_fprog sfp = {8,sfi};
// 	prctl(PR_SET_SECCOMP,2,&sfp);
// }
void init(){
	int fd = open("./flag.txt",O_RDONLY);
	if(fd==-1)
	{
		printf("No flag.txt file found\n");
		exit(-1);
	}
	dup2(fd,666);
	close(fd);
	setvbuf(stdout,0LL,2,0LL);
	setvbuf(stdin,0LL,1,0LL);
	setvbuf(stderr, 0LL, 2, 0LL);
	sandbox();
}

void menu(){
	puts("========================");
	puts("+   EzPez(?) Heap      +");
	puts("========================");
	puts("1: Create ");
	puts("2: Remove ");
	puts("3: Show ");
	puts("4: Leave message and quit. ");
	puts("------------------------");
	printf("choice>> ");
}

void bye(){
	char buf[100];
	puts("What message you want to leave? ");
	scanf("%99s",buf);
	printf("Your message :%s\n",buf);
	puts("See you again!");
	exit(0);
}

int get_atoi(){
	char buf[16];
	read(0,buf,16);	
	return atoi(buf);
}

void show(){
	if(show_time && show_time--){
		printf("TYPE:\n1: int\n2: short int\n> ");
		int choice=get_atoi();
		if (choice==1 && int_ptr)
			printf("Your int type note number :%d\n",*int_ptr);
		if (choice==2 && short_ptr)
			printf("Your short type note number :%d\n",*short_ptr);
	}
}

void create(){
	printf("TYPE:\n1: int\n2: short int\n> ");
	int choice=get_atoi();
	if (choice==1){
		int_ptr =(int *)malloc(0x20);
		if (!int_ptr)
			exit(-1);
		_bool=1;
		printf("Your note number: ");
		*int_ptr=get_atoi();
		*(int *)((char *)int_ptr+8)=*int_ptr;
		puts("Successfully added!");
	}
	else if (choice==2){
		short_ptr =(short *)malloc(0x10);
		if (!short_ptr)
			exit(-1);
		_bool=1;
		printf("Your note number: ");
		*short_ptr=get_atoi();
		*(short int *)((char *)short_ptr+8)=*short_ptr;
		puts("Successfully added!");
	}
}

void delete(){
	if(_bool){
		printf("TYPE:\n1: int\n2: short int\n> ");
		int choice=get_atoi();
		if (choice==1 && int_ptr){
			free(int_ptr);
			_bool=0;
			puts("Successfully Removed!");
		}
		else if (choice==2 && short_ptr){
			free(short_ptr);
			_bool=0;
			puts("Successfully Removed!");
		}
	}
	else
		puts("Invalid!");
}

int main(void){
	init();
	while(1){
		int choice;
		menu();
		choice=get_atoi();
		switch(choice){
			case 1:
				create();
				break;
			case 2:
				delete();
				break;
			case 3:
				show();
				break;
			case 4:
				bye();
		}
	}
	return 0;
}
