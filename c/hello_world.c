#include <stdio.h>

int main() {
  int I = -1230; // 32 bit = 4 byte
  float f = 3.14159e5; // 32 bit = 4 byte
  double d = 3.14159876543e19; // 64 bit = 8 byte
  char c = 7; // 8 bit = 1 byte

  printf("int I = %u\n", I);
  printf("float f = %e\n", f);
  printf("double d = %le\n", d);
  printf("char c = %c\n", c);
  return 0;
}
