/* shellcode.c */
#include <unistd.h>
#include <stddef.h>
void main()
{
	char *name[2];
	name[0] = "/bin/sh";
	name[1] = NULL;
	execve(name[0], name, NULL);
}
