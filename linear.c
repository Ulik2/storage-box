#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int x[7] = {1, 23, 13, 98, 70, 66, 50};
    for (int i = 0 ; i < 7 ; i++)
    {
        if ( x[i] == 50 )
        {
            printf("True\n");
        }
        else
        {
            printf("False: %i\n", x[i]);
        }
    }
}