#include <stdio.h>


int condition()
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


int condition_up()
{
	int nmbr;
	float gpa;

	printf("Input your number : ");
	scanf("%d", &nmbr);



	if ((nmbr >= 80) && (nmbr <=100))
	{
		gpa = 5.0;
		printf("Congratulation.\n");
	}
	else if ((nmbr >= 70) && (nmbr < 79))
	{
		gpa = 4.0;
	}
	else if ((nmbr >= 60) && (nmbr <69))
	{
		gpa = 3.5;
	} 
	else if ((nmbr >= 50) && (nmbr <=59))
	{
		gpa = 3.0;
	}
	else if ((nmbr >= 40) && (nmbr <=49))
	{
		gpa = 2.0;
	}
	else if ((nmbr >= 33) && (nmbr <=39))
	{
		gpa = 1.0; 
	}
	else if (!((nmbr < 0) || (nmbr > 32)))
	{
		gpa = 0.0;
		printf("Study hard. Better luck next time.\n");
	}
	else
	{
		printf("Number is Invalid. Valid number range Number = [0,100]\n");
		return 1;
	}
	printf("Your number is %d. Your GPA is %2.1f\n", nmbr, gpa);
	
	return 0;
}


int testing()
{
	int nmbr1 = ((2*2) == 4); // answes = 1
	int nmbr0 = ((2/2) == 2); // answes = 2


	printf("%d\n", !(nmbr1 || nmbr0));
	printf("%d\n", (!nmbr1 && !nmbr0));
	printf("%d\n", !(nmbr1 && nmbr0));
	printf("%d\n", (!nmbr1 || !nmbr0));
}

int main()
{
	return testing();
}