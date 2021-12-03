#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
    FILE *file;
    file = fopen("./input", "r");
    int num, x = 0, y = 0;
    char direction[10];
    while (fscanf(file, "%s %d", direction, &num) == 2)
    {
        if (strcmp(direction, "forward") == 0)
        {
            x += num;
        }
        if (strcmp(direction, "up") == 0)
        {
            y -= num;
        }
        if (strcmp(direction, "down") == 0)
        {
            y += num;
        }
    }
    printf("%d", x*y);
    fclose(file);
    return 0;
}
