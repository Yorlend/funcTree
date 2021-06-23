#include <stdio.h>
#include <inttypes.h>
#include <time.h>

#define N 1000000
#define REPEAT 100
#define CLOCKS_PER_USEC 1000000. / (CLOCKS_PER_SEC * REPEAT)
#define SUCCESS 0
#define ERROR 1

int get_size(int *size);
int input_array(int *pbeg, int *pend);
int max_sum(int *pbeg, int *pend);
int process_1(int *arr, int size);
int process_2(int *arr, int size);

int main(void)
{
    clock_t start_t, end_t;
    double eval_time;
    int exit_code = SUCCESS, size = 0;
    int arr[N] = { 0 };
    int *pbeg = arr, *pend = arr;

    exit_code = get_size(&size);
    if (exit_code != ERROR)
    {
        pend += size;
        exit_code = input_array(pbeg, pend);
    }
    if (exit_code != ERROR)
    {
        eval_time = 0;
        start_t = clock();
        for (int i = 0; i < REPEAT; i++)
            process_1(arr, size);

        end_t = clock();
        eval_time = (double)(end_t - start_t);
        eval_time *= CLOCKS_PER_USEC;
        printf("%lf\n", eval_time);

        eval_time = 0;
        start_t = clock();
        for (int i = 0; i < REPEAT; i++)
            process_1(arr, size);

        end_t = clock();
        eval_time = (double)(end_t - start_t);
        eval_time *= CLOCKS_PER_USEC;
        printf("%lf\n", eval_time);

        eval_time = 0;
        start_t = clock();
        for (int i = 0; i < REPEAT; i++)
            max_sum(pbeg, pend);

        end_t = clock();
        eval_time = (double)(end_t - start_t);
        eval_time *= CLOCKS_PER_USEC;
        printf("%lf\n", eval_time);
    }

    return exit_code;
}

void copy_array(int *given_arr, int *copy, int size)
{
    for (int i = 0; i < size; i++)
        copy[i] = given_arr[i];
    
}

int get_size(int *size)
{
    int exit_code = SUCCESS;
    scanf("%d", size);
    if (*size > N || *size < 1)
        exit_code = ERROR;
    
    return exit_code;
}

int input_array(int *pbeg, int *pend)
{
    int exit_code = SUCCESS;

    for (int *pa = pbeg; pa < pend && exit_code != ERROR; pa++)
        if (scanf("%d", pa) != 1)
            exit_code = ERROR;

    return exit_code;
}

int max_sum(int *pbeg, int *pend)
{
    int tmp = 0, max = *pbeg + *(pend - 1);
    for (int *pb = pbeg + 1, *pe = pend - 2; pb <= pe; pb++, pe--)
    {
        tmp = *pb + *pe;
        if (tmp > max)
            max = tmp; 
    }

    return max;
}

int process_1(int *arr, int size)
{
    int tmp = 0, max = arr[0] + arr[size - 1];
    for (int lo = 1, hi = size - 2; lo <= hi; lo++, hi--)
    {
        tmp = arr[lo] + arr[hi];
        if (tmp > max)
            max = tmp; 
    }

    return max;
}

int process_2(int *arr, int size)
{
    int tmp = 0, max = *arr + *(arr + size - 1);
    for (int lo = 1, hi = size - 2; lo <= hi; lo++, hi--)
    {
        tmp = *(arr + lo) + *(arr + hi);
        if (tmp > max)
            max = tmp; 
    }

    return max;
}
