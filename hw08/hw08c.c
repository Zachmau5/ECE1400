#include <stdio.h>
#include <stdbool.h>

bool isEven(int x){
    return( x % 2)==0;
}

bool isPrime(int x){
    if (x<=1){
        return false;
    }
   for (int i = 2; i <= x/2; i++) {
      if (x % i == 0) {
         return false;
      }
}
}
int main() {
   for (int i = 1; i <= 20; i++) {
      printf("%d\t%s\t%s\n", i, isEven(i) ? "even" : "odd", isPrime(i) ? "prime" : "composite");
   }

   return 0;
}



