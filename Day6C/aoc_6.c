#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define DAYS 256
#define TIMER 9
#define INPUT_LEN 601

int main()
{
    FILE *f;
    f = fopen("input.txt", "r");
    char input[INPUT_LEN], *val;
    int num, i, j;
    long fish[TIMER] = {0}, zeros, sum = 0;
    fscanf(f, "%s", input);
    val = strtok(input, ",");
    while(val!=NULL)
    {
        num = atoi(val);
        fish[num]++;
        val = strtok(NULL, ",");
    }
    for(i=0; i<DAYS; i++)
    {
        zeros = fish[0];
        for(j=1; j<TIMER; j++)
        {
            fish[j-1] = fish[j];
        }
        fish[6] += zeros;
        fish[8] = zeros;
    }
    for(i=0; i<TIMER; i++)
    {
        sum += fish[i];
    }
    printf("%ld", sum);
    fclose(f);
    return 0;
}