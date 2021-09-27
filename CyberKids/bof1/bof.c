#include <stdio.h>
#include <fcntl.h>


char admin_password[40];

void print_flag()
{
	char flag[20];


	int fd = open("flag.txt", O_RDONLY);
	
	if(fd == -1){
		printf("flag.txt không tồn tại\n");
		exit(1);
	}


	if((read(fd,flag,20)) == -1)
	{
		printf("read() không thành công\n");
		exit(1);
	}

	printf("Chúc mừng em đã khai thác lỗ hổng Buffer Overflow thành công!\nĐây là phần thưởng của em %s\n",flag);

}

void banner()
{
    printf(
    "         -------------------------\n\
        |                         |\n\
        |  ĐĂNG NHẬP              |\n\
        |                         |\n\
        |   -------------------   |\n\
        |  |Admin              |  |\n\
        |   -------------------   |\n\
        |                         |\n\
        |   Guest Session         |\n\
         -------------------------\n\n");
}

void admin_account()
{
    int fd, len;
	
	if((fd = open("password.txt", O_RDONLY)) == -1){
		printf("password.txt không tồn tại\n");
		exit(1);
	}

	if((len = read(fd,admin_password,40)) == -1)
	{
		printf("read() không thành công\n");
		exit(1);
	}
    printf(
    "         -------------------------\n\
        |                         |\n\
        |   Admin                 |\n\
        |                         |\n\
        |   -------------------   |\n\
        |  | *****             |  |\n\
        |   -------------------   |\n\
        |                         |\n\
        |                         |\n\
         -------------------------\n\n");
}

void guest_account()
{
    printf(
    "         -------------------------\n\
        |                         |\n\
        |   Guest Session         |\n\
        |                         |\n\
        |                         |\n\
        |  ĐĂNG NHẬP THÀNH CÔNG!  |\n\
        |                         |\n\
        |                         |\n\
        |                         |\n\
         -------------------------\n\n");
}


void wrong_password()
{
    printf(
    "         -------------------------\n\
        |                         |\n\
        |   Admin                 |\n\
        |                         |\n\
        |                         |\n\
        |  MẬT KHẨU KHÔNG ĐÚNG!   |\n\
        |                         |\n\
        |                         |\n\
        |                         |\n\
         -------------------------\n\n");
}

int main()
{
    setbuf(stdout, 0);
    char password[20];
    char isAdmin = '0';
    int loginAsUser;
    
    banner();
    printf("Đăng nhập với user:\n1. Nhập 1 là Admin\n2. Nhập 2 là Guest\n");
    scanf("%d%*c",&loginAsUser);
    if(loginAsUser == 2)
        guest_account();
    else if(loginAsUser == 1)
    {
        admin_account();
        printf("Nhập password:\n");
        gets(password);
        if(!strncmp(password,admin_password,20))
            isAdmin = '1';
        else
            wrong_password();
    }

    if(isAdmin == '1')
        print_flag();
    
    return 0;
}
