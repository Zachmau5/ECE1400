#include <stdio.h>
#include <string.h>
#define MAX_LEN 100 //max len for strings
int main(){
  const char str1[] = "The quick brown fox jumps over the lazy dog!";
  const char str2[] = "Mary had a little lamb.";
  char str3[MAX_LEN]="";
  //find length of string
  printf("%s\n", str1);
  int len = strlen(str1);
  printf("The string is %d characters long\n",len);

  // find index of z
  //initializes index to not found/before the string starts
  int index = -1; 
  
  for (int i = 0; i < len; i++) {
    if (str1[i] == 'z') {
      index = i;

      // Exit the loop once the first occurrence is found
      break;
    }
  }
  // printing index
  if (index != -1) {
    printf("The letter z is at index %d\n", index);
  } else {
    printf("The letter z is not found in the string.\n");
  }
    

   //Find and print 3rd words
   //establish word with max length
   char word[MAX_LEN];
   // looks for string_string_string with max len established before
   int num_words = sscanf(str1, "%s %s %s", word, word, word);

   //loop to just find 3rd word, can be used for more, change x val
   if(num_words >=3){
   printf("The third word is %s\n", word);
   }
   
   //find jumps using pointers
   //strstr fuction used to located first occurance of jumps
   char* ptr=strstr(str1, "jumps");

    if (ptr != NULL) {
   //finds word after the word jump
   int num_words = sscanf(ptr + strlen("jumps"), "%s", word); 
    if (num_words >= 1) {
   printf("The word after jumps is %s\n", word);
}
}

    //concatenate the strings together
    strcat(str3, str1);
    //adds empty space to fill later with str2
    strcat(str3, " ");
   //combines the two
    strcat(str3, str2);
    //print new string
    printf("%s\n",str3);

    return 0;
}

