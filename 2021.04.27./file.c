#include <cs50.h>
#include <stdio.h>
#include <string.h>

int main(void)
{
    char name[10];
    char number[10];

    FILE *file = fopen("phonebook.csv","a");
    printf("Name: ");
    scanf("%s", name);
    printf("Number: ");
    scanf("%s", number);
    fprintf(file, "%s, %s\n", name, number);
    fclose(file);
}