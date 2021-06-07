#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#define MAX_BOOK_PAGES (16)
#define MAX_BOOK (8)

typedef struct _Book {
    char *page[MAX_BOOK_PAGES];
    int page_size[MAX_BOOK_PAGES];
    int totalPage;
} Book, *PBook;

Book book_arr[MAX_BOOK];

void hacker()
{
    puts("Hacker!!!!!!!!!");
    exit(1);
}

int read_until(int n)
{
    int z;
    while ((z = getchar()) != n)
        ; // do nothing
}
int get_int()
{
    int d;
    scanf("%d", &d);
    read_until('\n');
    return d;
}

int get_int_prompt(char* content)
{
    printf("%s", content);
    return get_int();
}


Book* get_book(int idx)
{
    if (idx < 0 || idx >= MAX_BOOK)
        hacker();
    return &book_arr[idx];
}

char* get_page(PBook pBook, int idx)
{
    if (idx < 0 || idx >= pBook->totalPage)
        hacker();
    return pBook->page[idx];
}

char* create_new_page(int* page_size)
{
    int idx;
    int tpage_size;
    puts("[+] Do you want to create a new page or copy from another page?");
    puts("1: Create new page");
    puts("2: Copy from another page");
    idx = get_int_prompt("> ");
    if (idx != 1 && idx != 2)
        hacker();
    if (idx == 1)
    {
        tpage_size = get_int_prompt("[+] New page size: ");
        if (tpage_size < 0 || tpage_size > 2048)
            hacker();
        char* new_page = (char*)malloc(tpage_size);
        printf("[+] Enter new content: ");
        ssize_t n = read(STDIN_FILENO, (void*)new_page, tpage_size - 1);
        new_page[n] = '\0';
        *page_size = tpage_size;
        return new_page;
    }
    else // idx == 2
    {
        idx = get_int_prompt("[+] Which book you want to copy from?: ");
        PBook pBook = get_book(idx);
        idx = get_int_prompt("[+] Which page you want to copy from?: ");
        char* page = get_page(pBook, idx);
        char* new_page = strdup(page);
        *page_size = pBook->page_size[idx];
        return new_page;
    }
}

void print_page()
{
    int idx;
    idx = get_int_prompt("[+] Which book you want to print?: ");
    PBook pBook = get_book(idx);
    idx = get_int_prompt("[+] Which page you want to print?: ");
    if (idx < 0 || idx >= MAX_BOOK_PAGES)
        hacker();
    printf("[+] Content: %s\n", pBook->page[idx]);
}

void add_page()
{
    int idx;
    idx = get_int_prompt("[+] Which book you want to add a new page?: ");
    PBook pBook = get_book(idx);
    if (pBook->totalPage >= MAX_BOOK_PAGES)
    {
        puts("[+] You can't add to this book anymore");
        return;
    }
    idx = pBook->totalPage;
    pBook->page[idx] = create_new_page(&pBook->page_size[idx]);
    pBook->totalPage++;
}

void delete_page()
{
    int idx;
    idx = get_int_prompt("[+] Which book you want to delete page?: ");
    PBook pBook = get_book(idx);
    if (pBook->totalPage == 0)
    {
        puts("[+] This book is empty");
        return;
    }
    idx = pBook->totalPage - 1;
    free(pBook->page[idx]);
    pBook->totalPage--;
    puts("[+] Deleted");
}

void edit_page()
{
    int idx;
    idx = get_int_prompt("[+] Which book you want to edit?: ");
    PBook pBook = get_book(idx);
    idx = get_int_prompt("[+] Which page you want to edit?: ");
    char* page = get_page(pBook, idx);
    printf("[+] Enter new content: ");
    ssize_t n = read(STDIN_FILENO, page, pBook->page_size[idx] - 1);
    page[n] = '\0';
}

int menu()
{
    puts("-------> Book manager version 4.01.90.4 <-------");
    puts("1. Add a new page");
    puts("2. Print a page");
    puts("3. Edit a page");
    puts("4. Delete a page");
    puts("5. Secret");
    puts("6. Exit");
    return get_int_prompt("> Your choice: ");
}

void setup() 
{
    setbuf(stdin, 0);
    setbuf(stdout, 0);
    setbuf(stderr, 0);
    alarm(120);
}

int main(int argc, char* argv[])
{
    setup();
    int choice;
    do 
    {
        choice = menu();
        switch (choice)
        {
            case 1:
            {
                add_page();
                break;
            }
            case 2:
            {
                print_page();
                break;
            }
            case 3:
            {
                edit_page();
                break;
            }
            case 4:
            {
                delete_page();
                break;
            }
            case 5:
            {
                puts("[+] Not implemented yet!!!");
                break;
            }
            case 6:
            {
                // do nothing
                break;
            }
            default:
            {
                puts("[+] Wrong choice");
                break;
            }
        }
    } while (choice != 6);
    return 0;
}