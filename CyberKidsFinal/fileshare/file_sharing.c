#include <stdio.h>
#include <fcntl.h>


void banner()
{
    printf("\
  ______ _ _         _____ _                _               __  ___ ___\n\  
 |  ____(_) |       / ____| |              (_)             /_ |\/ _ \\__ \\\n\
 | |__   _| | ___  | (___ | |__   __ _ _ __ _ _ __   __ _   | | | | | ) |\n\
 |  __| | | |\/ _ \\  \\___ \\| '_ \\ \/ _` | '__| | '_ \\ \/ _` |  | | | | |\/ \/\n\
 | |    | | | __\\\/  ____) | | | | (_| | |  | | | | | (_| |  | | |_| \/ \/_ \n\
 |_|    |_|_|\\___| |_____\/|_| |_|\\__,_|_|  |_|_| |_|\\__, |  |_|\\___\/____|\n\
                                                     __\/ |               \n\
                                                    |___\/                \n\
\n");
}

void list_files()
{
    printf("Các tập tin được chia sẻ:\n\
.\n\
├── a.txt\n\
└── b.txt\n\
    \n\
0 directories, 2 files\n\n");
}

int main()
{
    setbuf(stdout, 0);
    char buffer[21];
    char file_name[6];
    char file_name_cache[6];
    int fd;

    memset(buffer,0,21);
    memset(file_name,0,6);
    memset(file_name_cache,0,6);
    banner();
    for(int i =0; i < 3; i++)
    {   
        list_files();
        printf("Nhập tên tập tin bạn muốn đọc: ");
        scanf("%5s",file_name);
        if(strncmp(file_name,file_name_cache,strlen(file_name) > strlen(file_name_cache) ? strlen(file_name):strlen(file_name_cache)))
        {

            memcpy(file_name_cache,file_name,strlen(file_name)+1);

            fd = open(file_name, O_RDONLY);
            if(fd == -1)
            {
                memset(file_name_cache,0,6);
                printf("\n\nTẬP TIN KHÔNG TỒN TẠI!\n\n");
                continue;
            }
        }
        
        read(fd,buffer,20);

        if(!strncmp(file_name,"flag",4))
        {
            printf("\n\nPERMISSION DENIED!\n\n");
            continue;
        }

        
        printf("\n\nNỘI DUNG:\n%s\n\n",buffer);
        memset(buffer,0,20);

    }
    printf("Bye!\n");
    return 0;
}
