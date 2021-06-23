#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define N 10
#define ERROR 1
#define SUCCESS 0

int input_array(int *arr, int *size);
void output_array(int *arr, int size);
int form_array(int *arr, int size, int *modified, int *mod_size);
char first_and_last(int num);

int main(void)
{
    int exit_code = SUCCESS;
    int arr[N] = { 0 }, result_arr[N], size = 0, res_size = 0;
    if (input_array(arr, &size) == ERROR)
        exit_code = ERROR;
    else
        exit_code = form_array(arr, size, result_arr, &res_size);

    if (exit_code == SUCCESS)
        output_array(result_arr, res_size);
    
    return exit_code;
}

int input_array(int *arr, int *size)
{
    int tmp = 0, exit_code = SUCCESS;
    scanf("%d", size);
    if (*size > N)
        exit_code = ERROR;
    for (int i = 0; i < *size && exit_code == SUCCESS; i++)
        if (scanf("%d", &arr[i]) != 1)
            exit_code = ERROR;

    if (scanf("%d", &tmp) != EOF)
        return 1;
    
    return exit_code;
}

void output_array(int *arr, int size)
{
    for (int i = 0; i < size; i++)
        printf("%d\n", arr[i]);   
}

// forming new array
int form_array(int *arr, int size, int *modified, int *mod_size)
{
    int j = 0;

    for (int i = 0; i < size; i++)
        if (first_and_last(arr[i]))
        {
            modified[j] = arr[i];
            j++;
        }
    *mod_size = j;

    return *mod_size == 0 ? ERROR : SUCCESS;
}

char first_and_last(int num)
{
    num = abs(num);
    int digits = (int)log10(num);
    int first, last;

    first = (int)(num / pow(10, digits));
    last = num % 10;

    return last == first;
}
