#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/time.h>
#include <stdlib.h>
#include <memory.h>
#include <ifaddrs.h>
#include <net/if.h>
#include <stdarg.h>
#include <pthread.h>
#define MAX_CAPACITY 4

// TODO : Add mutex and make it thread safe.

enum request_status
{
	PENDING=0,
	CONNECTED=1,
	COMPLETE=2,
	FAILED=3

};
const char * request_status_to_string(int s)
{
	if (s==PENDING)
		return "PENDING";
	if (s==COMPLETE)
		return "COMPLETE";
	if (s==FAILED)
		return "FAILED";
	if (s==CONNECTED)
		return "CONNECTED";
};
struct cross_thread_request
{
	unsigned char * host;
	unsigned int port;
	unsigned int size;
	unsigned char * buffer;
	enum request_status status;
};

struct cross_thread_request * thread_request[MAX_CAPACITY] ={0};


pthread_t   *  restrict g_worker_thread=NULL;
int find_active_job()
{
	for (int i =0;i<MAX_CAPACITY;++i)
	{
		if (thread_request[i]!=NULL && thread_request[i]->status==PENDING)
		{
			return i;
		}
	}
	return -1;
}
void DumpHex(const void* data, size_t size) {
	char ascii[17];
	size_t i, j;
	ascii[16] = '\0';
	for (i = 0; i < size; ++i) {
		printf("%02X ", ((unsigned char*)data)[i]);
		if (((unsigned char*)data)[i] >= ' ' && ((unsigned char*)data)[i] <= '~') {
			ascii[i % 16] = ((unsigned char*)data)[i];
		} else {
			ascii[i % 16] = '.';
		}
		if ((i+1) % 8 == 0 || i+1 == size) {
			printf(" ");
			if ((i+1) % 16 == 0) {
				printf("|  %s \n", ascii);
			} else if (i+1 == size) {
				ascii[(i+1) % 16] = '\0';
				if ((i+1) % 16 <= 8) {
					printf(" ");
				}
				for (j = (i+1) % 16; j < 16; ++j) {
					printf("   ");
				}
				printf("|  %s \n", ascii);
			}
		}
	}
}
void open_connection(struct cross_thread_request * r)
{
		int sockfd, connfd;
		struct sockaddr_in servaddr, cli;
		char tmp[4096];
  	bzero(tmp,sizeof(tmp));

  	unsigned int currentSize=0;
  	//Make a copy of buffer 
  	unsigned char * buf=(unsigned char * ) malloc(r->size);
  	memcpy(buf,r->buffer,r->size);
  	//Connect
		sockfd = socket(AF_INET, SOCK_STREAM, 0);
  	if (sockfd == -1) {
    		r->status=FAILED;
    		free(buf);
    		return;
  	}
  	bzero(&servaddr, sizeof(servaddr));
  	servaddr.sin_family = AF_INET;
  	servaddr.sin_addr.s_addr = inet_addr(r->host);
  	servaddr.sin_port = htons(r->port);
  	if (connect(sockfd, (struct sockaddr *)&servaddr, sizeof(servaddr)) != 0) 
  	{
    		r->status=FAILED;
    		free(buf);
    		return;
  	}
  	else
  	{
  			r->status=CONNECTED;
  	}

  	//Send data
  	write(sockfd, buf, r->size);

    //Zero memory data
    bzero(buf, r->size);

    
    int nb=read(sockfd,tmp,4096);
    //If read error
    if (nb==-1)
    {
    	r->status=FAILED;
    	return;
    }
    
    //If received bytes > current alloc byte then alloc a new one
    if(nb > r->size)
    {
    	free(buf);
    	buf=malloc(nb);
    	r->size=nb;
    }
    memcpy(buf,tmp,nb);
    //Replace buffer
    free(r->buffer);
    r->buffer=buf;

    r->status=COMPLETE;
    
}
void * __attribute__ ((noinline)) worker(void * arg)
{
	while(1)
	{
		sleep(1);
		int idx=find_active_job();
		
		if (idx!=-1)
		{
			open_connection(thread_request[idx]);
		}
		continue;
		
	}
}
void kill_on_timeout(int sig) {
  if (sig == SIGALRM) {
    _exit(0);
  }
}
size_t __attribute__ ((noinline)) readn(int fd, char *buf, size_t size) {
  size_t pos;
  for (pos = 0; pos < size; pos++) 
  {
    char b;
    if (read(fd, &b, 1) <= 0) 
    {
      _exit(0);
    }

    if (b == '\n') 
    {
      break;
    }
    buf[pos] = b;
  }

  return pos;
}
int __attribute__ ((noinline)) readint(int fd)
{
	char tmp[0x10];
	bzero(tmp,0x10);
	readn(0,tmp,0x10);
	int res = atoi(tmp);
	return res;

}
int __attribute__ ((noinline)) initialize()
{
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stdout, NULL, _IONBF, 0);
	g_worker_thread=(pthread_t* restrict )malloc(sizeof(pthread_t* restrict));
	if (pthread_create(g_worker_thread,NULL,worker,NULL))
	{
		printf("Can't create thread!! Please contact administrator for further information.\n");
		return -1;
	}
	signal(SIGALRM, kill_on_timeout);
	alarm(60);
	memset(thread_request,0,sizeof(struct cross_thread_request*)*MAX_CAPACITY);

};
void __attribute__ ((noinline)) create_request()
{
	printf("Enter request index: ");
	unsigned int idx= readint(0);
	if (idx>=MAX_CAPACITY)
	{
		printf("Overflowed!\n");
		return;
	}
	if (thread_request[idx])
	{
		printf("Choose another one!\n");
		return;
	}
	void * host = malloc(256);
	bzero(host,256);
	printf("Enter hostname: ");
	readn(0,host,256);

	printf("Enter port: ");
	unsigned int port = readint(0);

	printf("Enter input buffer size: ");
	unsigned int size= readint(0);
	if (size>0x1000 || size==0)
	{
		printf("Your size is invalid");
		free(host);
		return;
	}
		
	void * buffer=malloc(size);
	bzero(buffer,size);
	printf("Fill input buffer ");
	readn(0,buffer,size);
	
	struct cross_thread_request * r=(struct cross_thread_request*) malloc(sizeof(struct cross_thread_request));
	r->host=host;
	r->port=port;
	r->buffer=buffer;
	r->status=PENDING;
	r->size=size;
	thread_request[idx]=r;
	printf("Done\n");
}

void __attribute__ ((noinline)) modify_request()
{
	printf("Enter request index: ");
	unsigned int idx= readint(0);
	if (idx>=MAX_CAPACITY)
	{
		printf("Overflowed!\n");
		return;
	}
	if (thread_request[idx]==NULL)
	{
		printf("Request not found !\n");
		return;
	}
	
	struct cross_thread_request * r =thread_request[idx];
	
	memset(r->host,0,256);
	printf("Enter new hostname: ");
	readn(0,r->host,256);

	printf("Enter new port: ");
	r->port = readint(0);

	printf("Enter new input buffer size: ");
	unsigned int size=readint(0);
	

	if (size>0x1000 || size==0) //If invalid size then keep the old buffer;
	{
		printf("Your size is invalid");
		return;
	}

	if (size>r->size)//If new size > old size then free the old one.
	{
		free(r->buffer);
		r->buffer=malloc(size);
		r->size=size;
	}
	else//else just keep the old buffer;
	{
		r->size=size;
	}
	memset(r->buffer,0,size);
	printf("Fill input buffer:");
	readn(0,r->buffer,size);
	printf("Done!\n");
}
void __attribute__ ((noinline)) delete_request()
{
	printf("Enter request index: ");
	unsigned int idx= readint(0);
	if (idx>=MAX_CAPACITY)
	{
		printf("Overflowed!\n");
		return;
	}
	if (thread_request[idx]==NULL)
	{
		printf("Request not found !\n");
		return;
	}
	if (thread_request[idx]->status==CONNECTED)
	{
		printf("Request is executing, can't delete !\n");
		return;
	}
	struct cross_thread_request * r =thread_request[idx];
	free(r->host);
	free(r->buffer);
	free(r);
	thread_request[idx]=NULL;
	printf("Done!");
}
void __attribute__ ((noinline)) show_result()
{
	for(int i =0;i<MAX_CAPACITY;++i)
	{
		struct cross_thread_request * r =thread_request[i];
		if(r)
		{
			printf("Request index : %d\n",i);
			printf("Host : %s\n",r->host);
			printf("Port : %d\n",r->port);
			printf("Size : %d\n",r->size);
			printf("Buffer :\n");
			DumpHex(r->buffer,r->size);
			printf("\nStatus : %s\n",request_status_to_string(r->status));
		}
	}
}

void __attribute__ ((noinline)) menu()
{
	puts("--------------------------");
	puts("- Hide my 4ss proxy v0.9 -");
	puts("--------------------------");
	puts("- 1. Create request      -");
	puts("- 2. Modify request      -");
	puts("- 3. Delete request      -");
	puts("- 4. Show result         -");
	puts("- 5. Credit              -");
	puts("- 6. Exit proxy          -");
	puts("--------------------------");
}
void __attribute__ ((noinline)) credit()
{
	puts("This unpwnable service made by z3r09!!");
}
void __attribute__ ((noinline)) clean()
{
	for(int i =0;i<MAX_CAPACITY;++i)
	{

		struct cross_thread_request * r =thread_request[i];
		if (r)
		{

			free(r->host);
			free(r->buffer);
			free(r);	
		}
		thread_request[i]=NULL;
	}
	pthread_cancel(*g_worker_thread);
	free(g_worker_thread);
}
int main()
{
	initialize();
	while(1)
	{
		int choice;
		menu();
		printf("Your choice: /> ");
		choice = readint(choice);
		switch(choice)
		{
			case 1 : 
				create_request();
				break;
			case 2 :
				modify_request();
				break;
			case 3 :
				delete_request();
				break;
			case 4 : 
				show_result();
				break;
			case 5 : 
				credit();
				break;
			case 6 : 
				clean();
				puts("BYE");
				exit(0);
				break;
			default :
				puts("Invalid option");
		}
	}
}