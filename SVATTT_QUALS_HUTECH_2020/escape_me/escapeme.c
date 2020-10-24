#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <sys/mman.h>
#include <seccomp.h>
#include <linux/seccomp.h>
#include <sys/wait.h>
#include <sys/user.h>

void init_seccomp()
{
	scmp_filter_ctx ctx;
	ctx = seccomp_init(SCMP_ACT_KILL);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(read), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(write), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(fstat), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(exit_group), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(mmap), 0);
	seccomp_rule_add(ctx, SCMP_ACT_ALLOW, SCMP_SYS(munmap), 0);
	seccomp_load(ctx);
}

void read_buf(char *buf, uint32_t size)
{
	unsigned char c;
	uint32_t i = 0;

	while(i < size){
		read(0, &c, 1);
		if(c == '\n'){
			break;
		}
		buf[i++] = c;
	}
}

uint32_t read_uint32()
{
	char buf[32] = {0};
	read_buf(buf, 31);

	return (uint32_t)strtoul(buf, NULL, 0);
}

void sandbox_process(int read_fd, int write_fd)
{
	char *shellcode = NULL;
	uint32_t sc_size = 0;
	void (*exec)(char *);
	char *output;
	uint32_t out_size = 0;

	// disable stdin/stdout
	close(0);
	close(1);

	init_seccomp();

	shellcode = mmap(NULL, 0x2000, PROT_EXEC | PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0);
	exec = (void(*) (char *))shellcode;
	output = mmap(NULL, 0x1000, PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0);

	while(1){
		read(read_fd, (char *)&sc_size, sizeof(uint32_t));
		if(sc_size == 0) continue;

		// printf("[DEBUG] got %d bytes from broker process\n", sc_size);
		read(read_fd, shellcode, sc_size);
		memset(output, 0, 0x1000);

		exec(output);

		out_size = *((uint32_t *)output);
		// printf("[DEBUG] send %d bytes to broker process\n", out_size);

		write(write_fd, output, sizeof(uint32_t));
		if(out_size > 0)
			write(write_fd, output + 4, out_size);
	}

	munmap(shellcode, 0x2000);
	munmap(output, 0x1000);
}

void broker_process()
{
	char output[256] = {0};
	char *sc = NULL;
	uint32_t sz;
	uint32_t out_sz;
	uint32_t opt;

	pid_t pid = 0;
	int fd1[2];
	int fd2[2];
	pid_t res = 1;
	int status;

	int ret;
	fd_set set;
	struct timeval timeout;

	/* Initialize the timeout data structure. */
	timeout.tv_sec = 5;
	timeout.tv_usec = 0;

	pipe(fd1);
	pipe(fd2);

	/* Initialize the file descriptor set. */
	FD_ZERO(&set);
	FD_SET(fd2[0], &set);

	while(1){
		printf("\t\tMenu\n");
		printf("1. Run your shellcode.\n");
		printf("2. Exit.\n");

		do{
			printf(">");
			opt = read_uint32();
		} while(opt != 1 && opt != 2);

		if(opt != 1){
			kill(pid, SIGKILL);
			break;
		}

		if(pid != 0){
			res = waitpid(pid, &status, WNOHANG);
		}

		if(res != 0){
			pid = fork();
			if(pid == 0){
				sandbox_process(fd1[0], fd2[1]);
			
			} else if (pid < 0) {
				printf("fork() error\n");
				exit(1);
			}
		}

		printf("Give me shellcode:\n");
		printf("Shellcode size:");
		sz = read_uint32();

		if(sz > 0x2000) sz = 0x2000;
		sc = (char *)malloc(sz);
		read(1, sc, sz);

		write(fd1[1], (char *)&sz, sizeof(uint32_t));
		write(fd1[1], sc, sz);
		free(sc);

		printf("Waiting your shellcode execute....\n");
		sleep(2);

		// check child process is alive or not
		res = waitpid(pid, &status, WNOHANG);
		if (res != 0){
			printf("Your shellcode crashed or exited. %d\n", res);
			continue;
		}

		ret = select(FD_SETSIZE, &set, NULL, NULL, &timeout);
		if(ret == 0){
			printf("Your shellcode timeout\n");
			kill(pid, SIGKILL);
			continue;
		} else if(ret < 0){
			//printf("Error\n");
			break;
		}

		read(fd2[0], &out_sz, sizeof(uint32_t));
		printf("Done, got %d bytes returned\n", out_sz);
		if(out_sz > 0){
			read(fd2[0], output, out_sz);
			printf("Your shellcode output:\n");
			puts(output);
		}
	}
}

int main()
{

	setvbuf(stdin, NULL , _IONBF , 0);
	setvbuf(stdout, NULL , _IONBF , 0);

	broker_process();

	return 0;
}