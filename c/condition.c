#include <stdio.h>

int main()
{
	int nmbr;
	float gpa;

	printf("Input your number : ");
	scanf("%d", &nmbr);

	if ((nmbr < 0) || (nmbr >100))
	{
		printf("Number is Invalid. Valid number range Number = [0,100]\n");
		return 1;
	}

	if (nmbr >= 80)
	{
		gpa = 5.0;
		printf("Congratulation.\n");
	}
	else if (nmbr >= 70)
	{
		gpa = 4.0;
	}
	else if (nmbr >= 60)
	{
		gpa = 3.5;
	} 
	else if (nmbr >= 50)
	{
		gpa = 3.0;
	}
	else if (nmbr >= 40)
	{
		gpa = 2.0;
	}
	else if (nmbr >= 33)
	{
		gpa = 1.0; 
	}
	else
	{
		gpa = 0;
		printf("Study hard. Better luck next time.\n");
	}
	
	printf("Your number is %d. Your GPA is %2.1f\n", nmbr, gpa);
	return 0;
}