#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <string.h>
#include <time.h>
typedef struct User
{
    char username[8];
    char password[8];
} User;

User users[8];
int total = 0;

void getStr(char *buf, size_t n)
{
    int r;
    r = read(STDIN_FILENO, buf, n);
    if (r <= 0)
    {
        puts("[+] Loi~  roi`");
        exit(1);
    }
    if (buf[r - 1] == '\n')
        buf[r - 1] = '\x00';
}

int getInt()
{
    char buf[64];
    getStr(buf, sizeof(buf));
    return atoi(buf);
}

void printFlag()
{
    system("cat flag.txt");
}

void getRandom(char *buf, size_t n)
{
    srand(time(0));
    int fd;
    fd = open("/dev/urandom", O_RDONLY);
    if (fd == -1)
    {
        puts("[+] Loi~ roi` 2");
        exit(1);
    }
    int r;
    r = read(fd, buf, n);
    if (r <= 0)
    {
        puts("[+] Loi~ roi` 3");
        exit(1);
    }
    close(fd);
}

int login()
{
    char username[8];
    char password[8];
    int isAdmin;
    int ret;
    printf("[+] Ten dang nhap: ");
    getStr(username, sizeof(username));
    printf("[+] Mat khau: ");
    getStr(password, sizeof(password));
    ret = 0;
    for (int i = 0; i < total; ++i)
    {
        if (strcmp(username, users[i].username) == 0 && strcmp(password, users[i].password) == 0)
        {
            ret = 1;
            if (strcmp(username, "admin") == 0)
            {
                isAdmin = 1;
            }
            break;
        }
    }
    if (isAdmin == 1)
    {
        printFlag();
    }
    return ret;
}

void addUser(char *username, char *password)
{
    if (total >= sizeof(users) / sizeof(users[0]))
    {
        printf("[+] Khong the them user moi\n");
        return;
    }
    User *pUser = &users[total];
    memcpy(pUser->username, username, sizeof(pUser->username));
    memcpy(pUser->password, password, sizeof(pUser->password));
    total++;
}

void menu()
{
    puts(">>> He thong tu thien version 13.67(B) aka \"HL BANK\" <<<");
    puts("1. Them user vao he thong");
    puts("2. Dang nhap");
    puts("3. Thoat");
    printf("> ");
}

int checkExistingUsername(char* username)
{
    for (int i = 0; i < total; ++i)
    {
        if (strcmp(username, users[i].username) == 0)
            return 1;
    }
    return 0;
}

int main(int argc, char *argv[])
{
    setbuf(stdout, 0);
    setbuf(stdin, 0);
    setbuf(stderr, 0);
    char userAdmin[8];
    char passAdmin[8];
    strcpy(userAdmin, "admin");
    getRandom(passAdmin, sizeof(passAdmin));
    addUser(userAdmin, passAdmin);
    do
    {
        menu();
        switch (getInt())
        {
        case 1:
        {
            char username[8] = {0};
            char password[8] = {0};
            printf("[+] Username moi: "); getStr(username, sizeof(username));
            if (checkExistingUsername(username) == 1)
            {
                puts("[+] Username da ton tai");
                break;
            }
            printf("[+] Password moi: "); getStr(password, sizeof(password));
            addUser(username, password);
            puts("[+] Da~ them user!");
            break;
        }
        case 2:
        {
            if (login()) 
            {
                puts("[+] Dang nhap thanh cong");
            }
            else
            {
                puts("[+] Dang nhap that bai");
            }
            break;
        }
        case 3:
        {
            return 0;
        }
        }
    } while (1);
    return 0;
}