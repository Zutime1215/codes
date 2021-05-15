#include <stdio.h>

int main()
{
	int nmbr;
	printf("Type a number : ");
	scanf("%d", &nmbr);

	if ((nmbr%2) != 0)
	{
		printf("The number is odd.\n");
	}
	else
	{
		printf("The number is even.\n");
	}	
	return 0;
}