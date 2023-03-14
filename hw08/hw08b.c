#include <stdio.h>

int main() {
   int i;

   // using a for loop
   // i++ is an increment operator, it is the same as saying i=i+1
   for (i = 1; i <= 5; i++) {
      printf("%d\n", i);
   }
   // using a while loop
   i = 1;
   while (i <= 5) {
      printf("%d\n", i);
      i++;
   }
   // using a do while loop
   i = 1;
   do {
      printf("%d\n", i);
      i++;
   } while (i <= 5);
   return 0;
}

