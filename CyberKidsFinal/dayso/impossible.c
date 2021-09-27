#include <stdlib.h> // for atoi
#include <unistd.h>
#include <sys/stat.h> // for stat
#include <string.h>   // for strlen
#include <fcntl.h>    // for open

#define WIN 1
#define LOSE 0

char secret[512] = {0};
int secret_length = 0;
int res = LOSE;
char flag[64] = {0};
char flag_length = 0;

void print_error_and_exit(const char *msg)
{
    // Write a message and then exit program
    write(STDOUT_FILENO, msg, strlen(msg));
    write(STDOUT_FILENO, "\n", 1);
    exit(1);
}

void read_flag()
{
    // Read flag.txt into "flag" variable.
    struct stat st;
    int fd;
    int nread;
    // Get file size first
    if (stat("flag.txt", &st) != 0)
        print_error_and_exit("[+] Loi~ \"stat\", xin vui long lien he tac gia");
    flag_length = st.st_size;

    // We have size of the file, now read it.
    fd = open("flag.txt", O_RDONLY);
    if (fd == -1)
        print_error_and_exit("[+] Loi~ \"open\", xin vui long lien he tac gia");
    nread = read(fd, flag, flag_length);
    if (nread == -1 || nread != flag_length)
        print_error_and_exit("[+] Loi~ \"read\", xin vui long lien he tac gia");

    // Close the file.
    close(fd);
}

void read_line(char *buf, unsigned int max_size)
{
    // Read a line from keyboard
    char tmp;
    unsigned int i = 0;
    for (;i < max_size; ++i)
    {
        if (-1 == read(STDIN_FILENO, &tmp, 1)) // Read one character
            print_error_and_exit("[+] Loi~ \"read_line\", xin vui long lien he tac gia");
        if (tmp == '\n') // Make sure to null-terminate the string
        {
            buf[i] = 0;
            break;
        }
        else 
        {
            buf[i] = tmp;
        }
    }
    if (i == max_size)
        buf[i - 1] = 0;
}

int read_int()
{
    // Read an integer from keyboard
    char tmp[32];
    read_line(tmp, sizeof(tmp));
    return atoi(tmp);
}

void read_secret()
{
    write(STDOUT_FILENO, "[+] Hay nhap do dai chuoi bi mat: ", 34);
    secret_length = read_int();
    if (secret_length > 511)
        print_error_and_exit("[+] Do dai chuoi bi mat phai nho hon 512");
    else if (secret_length == 0)
        print_error_and_exit("[+] Do dai chuoi bi mat phai khac 0");
    write(STDOUT_FILENO, "[+] Hay nhap chuoi bi mat: ", 27);
    read_line(secret, secret_length);
    if (strncmp(secret, "CyberK1d", 8) != 0) // Must start with "CyberK1d"
        print_error_and_exit("[+] Chuoi bi mat phai bat dau bang \"CyberK1d\"");
}

void setup()
{
    read_flag();
    read_secret();
}

void play()
{
    int sum = 0;
    for (unsigned int i = 0; i < strlen(secret); ++i)
    {
        unsigned char tmp = (unsigned char)secret[i]; // Convert to unsigned first.
        sum = sum + tmp;
    }
    int total_loop = 500;
    while (total_loop != 0 && sum != 0 && sum != 1)
    {
        if (sum % 2 == 0)
            sum = sum / 2;
        else
            sum = sum * 3 + 1;
        total_loop--;
    }

    if (sum == 0)
        res = WIN;
}

int main(int argc, char *argv[])
{
    if (argc >=2) chdir(argv[1]);
    setup();
    play();
    if (res == WIN)
    {
        write(STDOUT_FILENO, "[+] Chuc mung ban. Phan thuong cua ban la: ", 43);
        write(STDOUT_FILENO, flag, flag_length);
        write(STDOUT_FILENO, "\n", 1);
    }
    else
    {
        write(STDOUT_FILENO, "[+] Rat tiec, dap an cua ban la chua chinh xac\n", 47);
    }
    return 0;
}
