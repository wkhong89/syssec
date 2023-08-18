/* cpbuf.c */
#include <stdio.h>
#include <string.h>

void main(void)
{
	char src[40] = "Hello world \0 Extra string";
	char dest[40];

	// copy to dest (destination) from src (source)
	strcpy(dest, src);
}
