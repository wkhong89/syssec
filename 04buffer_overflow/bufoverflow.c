/* bufoverflow.c */
#include <string.h>

void foo(char *str)
{
	char buffer[12];
	/* The following statement will result in a buffer overflow */
	strcpy(buffer, str);
}

int main(void)
{
	char *str = "This is defnitely longer than 12";
	foo(str);

	return 1;
}
