#include <stdio.h>
#include <stdlib.h>
#define window_size 3

int sum_vector (int* vector, int size)
{
    int i, sum = 0;
    for (i = 0; i < size; i++)
    {
        sum += vector[i];
    }
    return sum;
}

void shift (int* vector, int size)
{
    int i;
    for (i = 0; i < size-1; i++)
    {
        vector[i] = vector[i+1];
    }
    return;
}

int main()
{
    FILE *file;
    file = fopen("./input", "r");
    int window[window_size], past_sum, current_sum, count = 0, i;
    for(i = 0; i < window_size; i++)
    {
        fscanf(file, "%d", window+i);
    }
    past_sum = sum_vector (window, window_size);
    while(fscanf(file, "%d", window+(window_size-1)) == 1)
    {
        current_sum = sum_vector (window, window_size);
        if (current_sum>past_sum)
        {
            count++;
        }
        past_sum = current_sum;
        shift(window, window_size);
    }
    printf("%d", count);
    fclose(file);
    return 0;
}
