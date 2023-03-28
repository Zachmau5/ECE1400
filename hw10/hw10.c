#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]) {
    if (argc != 4) {
        printf("Usage: program_name input_filename output_filename buffer_size\n");
        exit(1);
    }

    char *input_filename = argv[1];
    char *output_filename = argv[2];
    int buffer_size = atoi(argv[3]);

    // Allocate a buffer of floats of the given size
    float *buffer = malloc(buffer_size * sizeof(float));
    printf("size of buffer: %i\n",buffer_size);
    if (buffer == NULL) {
        printf("Error: Failed to allocate memory for buffer\n");
        exit(1);
    }

    // Open the input file
    FILE *input_file = fopen(input_filename, "r");
    if (input_file == NULL) {
        printf("Error: Failed to open input file '%s'\n", input_filename);
        exit(1);
    }

    // Open the output file
    FILE *output_file = fopen(output_filename, "w");
    if (output_file == NULL) {
        printf("Error: Failed to open output file '%s'\n", output_filename);
        exit(1);
    }

    // Fill the circular buffer from the input file
    int i = 0;
    while (i < buffer_size && fscanf(input_file, "%f", &buffer[i]) == 1) {
        i++;
    }
    int buffer_head = 0;
    int buffer_tail = i % buffer_size;
    int buffer_count = i;

    // Calculate the average of the values in the buffer
    float sum = 0;
    for (int j = 0; j < buffer_count; j++) {
        sum += buffer[j];
    }
    float average = sum / buffer_size;

    // Read the remaining values from the input file and update the circular buffer
    float value;
    while (fscanf(input_file, "%f", &value) == 1) {
        // Rotate the circular buffer
        buffer_head = (buffer_head + 1) % buffer_size;
        buffer_tail = (buffer_tail + 1) % buffer_size;

        // Replace the oldest value in the buffer with the new value
        buffer[buffer_head] = value;

        // Calculate the average of the values in the buffer
        sum = 0.00000;
        for (int j = buffer_head, count = 0; count < buffer_size; j = (j + 1) % buffer_size, count++) {
            sum += buffer[j];
        }
        float average = (sum / buffer_size);
        fprintf(output_file, "%.6f\n",average);
    }

    // Close the input and output files, and free the buffer memory
    fclose(input_file);
    fclose(output_file);
    free(buffer);

    return 0;
}

