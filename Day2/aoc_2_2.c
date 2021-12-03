#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *file;
    file = fopen("./input", "r");
    int num, x = 0, y = 0, aim = 0;
    char direction[10];
    while (fscanf(file, "%s %d", direction, &num) == 2)
    {
        if (strcmp(direction, "forward") == 0)
        {
            x += num;
            y += aim*num;
        }
        if (strcmp(direction, "up") == 0)
        {
            aim -= num;
        }
        if (strcmp(direction, "down") == 0)
        {
            aim += num;
        }
    }
    printf("%d", x*y);
    fclose(file);
    return 0;
}
