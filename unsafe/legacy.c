// legacy.c

#include <stdio.h>
#include<stdlib.h>
#include<string.h>



typedef struct
{
    int id;
    float salary;
} Employee;


void increment(int *ptr)
{
    (* ptr)++;
}

void process(int *input, int *output, int size)
{
    for (int i = 0; i < size; i++)
    {
        output[i] = input[i] * 2;
    }
}

void increase_salary(Employee *employee)
{
    employee->salary += 5000;
}

void uppercase(char *text)
{
    for (int i = 0; text[i] != '\0'; i++)
    {
        if (text[i] >= 'a' && text[i] <= 'z')
        {
            text[i] = text[i] - 32;
        }
    }
}
void create_number(int **value)
{
    *value = (int*)malloc(sizeof(int));

    **value = 100;
}

char* get_name()
{
    char *name = malloc(100);

    strcpy(name, "Ravi");

    return name;
}
