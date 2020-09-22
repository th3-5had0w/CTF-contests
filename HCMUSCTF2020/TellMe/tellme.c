#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(){
	int userid;
	char passwd[32];


	fflush(stdin);
	fflush(stdout);
	printf("Hi there, please login!");
	printf("\nYour UserID: ");
	
	fflush(stdout);
 	fflush(stdin);
	scanf("%d", &userid);
	printf("\nPassword: ");
	
	fflush(stdout);
 	fflush(stdin);
	
	getchar();
	fgets(passwd, 32, stdin);
	fflush(stdout);
 	fflush(stdin);

	if(userid == 0x3211 && !strcmp("sUpErPassHCMUS\n", passwd)){
		printf("Wellcome back! Aministrator ^_^\n");
		fflush(stdout);
		fflush(stdin);
		system("/bin/cat flag");
		exit(0);
		
	}

	printf("Hey!! Who are you???\n");
	
	fflush(stdout);
 	fflush(stdin);
	return 0;

}
