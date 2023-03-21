#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Prompt the user to enter the filename
    char filename[100];
    printf("Please enter a filename: ");
    scanf("%s", filename);

    // Prompt the user to enter a word to search for
    char search_word[100];
    printf("Please enter a word to search for: ");
    scanf("%s", search_word);

    // Prompt the user to enter a word to replace with
    char replace_word[100];
    printf("Please enter a word to replace it with: ");
    scanf("%s", replace_word);

    // Read the file and count how many times the word is in the file
    int count = 0;
    FILE *file = fopen(filename, "r");
    if (file == NULL) {
        printf("Error opening file.\n");
        return 1;
    }
    char line[100];
    while (fgets(line, sizeof(line), file)) {
        char *ptr = strstr(line, search_word);
        while (ptr != NULL) {
            count++;
            ptr = strstr(ptr + 1, search_word);
        }
    }
    fclose(file);

    // Print the count of the search word
    printf("The word %s was found %d times.\n", search_word, count);

    // Create an output filename by replacing the extension with ".out"
    char *output_filename = malloc(strlen(filename) + 5);
    strcpy(output_filename, filename);
    char *extension = strrchr(output_filename, '.');
    if (extension == NULL) {
        strcat(output_filename, ".out");
    } else {
        strcpy(extension, ".out");
    }

    // Write a new file with the output filename which replaces the search word with the replacement word
    file = fopen(output_filename, "w");
    if (file == NULL) {
        printf("Error creating output file.\n");
        return 1; 
    }

FILE *input_file = fopen(filename, "r");
FILE *output_file = fopen("raven.out", "w");

if (input_file == NULL || output_file == NULL) {
    printf("Error opening file\n");
    return 1;
}

while (fgets(line, sizeof(line), input_file)) {
    char *ptr = strstr(line, search_word);
    while (ptr != NULL) {
        int offset = ptr - line;
        fprintf(output_file, "%.*s%s%s", offset, line, replace_word, ptr + strlen(search_word));
        ptr = strstr(ptr + 1, search_word);
    }
    fputs(line, output_file);
}

fclose(input_file);
fclose(output_file);


    // Print a message to confirm that the new file has been written
    printf("The new file %s has been created.\n", output_filename);

    return 0;
}

