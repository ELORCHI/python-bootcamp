#include <stdio.h>
#include <unistd.h>
int main()
{
    int i;
    char *str = "hello";

    while (str[i] != '\0')
    {
	write(1, str + i, 1);
	i++;
    }
    return (0);
}
