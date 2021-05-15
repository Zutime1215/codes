#include <stdio.h>

int main()
{	
	const double PI = 3.141592654;
	
	double radius;
	printf("Type the radius of the circle: ");
	scanf("%lf", &radius);
	
	double circumference = 2.0 * PI * radius;
	printf("\nCircumference of the circle = %lf\n\n", circumference);
	
	double area = PI * radius * radius;
	printf("Area of the circle = %lf\n\n", area);

	double volume = (4.0 / 3.0) * PI * radius * radius * radius;
	printf("volume of the sphere = %lf\n\n", volume);
	
	return 0;
}