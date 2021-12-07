#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
//#define FUNCTION fuel += abs(crabs[j]-i); //part 1
#define FUNCTION fuel += abs(crabs[j]-i)*(abs(crabs[j]-i)+1)/2; //part 2

int main() {
    FILE *f;
    f = fopen("input.txt", "r");
    int crabs[4000], crabs_size = 0, min_fuel = INFINITY, min_crab = INFINITY, max_crab = -INFINITY, i, j, fuel;
    while(fscanf(f, "%d,", crabs+crabs_size)==1)
    {
        crabs_size++;
    }
    for(i=0; i<crabs_size; i++)
    {
        min_crab = MIN(crabs[i], min_crab);
        max_crab = MAX(crabs[i], max_crab);
    }
    for(i=min_crab; i<=max_crab; i++)
    {
        fuel = 0;
        for(j=0; j<crabs_size; j++)
        {
            FUNCTION
        }
        min_fuel = MIN(min_fuel, fuel);
    }
    printf("%d", min_fuel);
    fclose(f);
    return 0;
}
