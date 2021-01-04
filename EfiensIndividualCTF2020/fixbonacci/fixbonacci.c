#include <stdio.h>
#include <stdlib.h>

const int N = 10;

void getFlag()
{
    system("cat flag.txt");
    exit(0);
}

int check(int A[])
{
    if (A[0] != 1 || A[1] != 1)
        return 0;

    int a = 1, b = 1, c;
    for (int i = 2; i < N; ++i)
    {
        c = a + b;
        a = b, b = c;
        if (A[i] != c) return 0;
    }

    return 1;
}

int main()
{
    setvbuf(stdin, NULL, _IOLBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);

    int A[] = {1, 1, 2, 3, 5, 8, 13, 21, 34, 65};
    int idx = 0;

    printf("The first %d numbers of Fibonacci sequence are:", N);
    for (int i = 0; i < N; ++i)
        printf(" %d", A[i]);

    printf("\nHmm, something is wrong. Can you fix it?\n");
    printf("Index: ");
    scanf("%d", &idx);
    printf("Value: ");
    scanf("%d", &A[idx]);

    if (check(A))
        printf("Oh, my bad. Thank you very much!\n");
    else
        printf("You need to learn math first!\n");

    return 0;
}
