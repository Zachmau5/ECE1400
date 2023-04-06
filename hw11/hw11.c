#include <stdio.h>
#include <string.h>
#include "hw11_lib.h"

int main() {
    char command[10];
    char name[69];
    char filename[69];
    float grade;

    printf("> ");
    while (scanf("%s", command) != 0) {
        if (strcmp(command, "g") == 0) {
            scanf("%s", name);
            if (strlen(name) > 0) {
                grade = studentGetAverage(name);
                if (grade != 0) {
                    printf("%.2f\n", grade);
                }
            } else {
                grade = studentGetGrade(name);
                if (grade == 0) {
                    printf("%.2f\n", grade);
                }
            }
        } else if (strcmp(command, "r") == 0) {
            scanf("%s", name);
            studentRemove(name);
        } else if (strcmp(command, "p") == 0) {
            studentPrintList();
        } else if (strcmp(command, "c") == 0) {
            printf("%d\n", studentCount());
        } else if (strcmp(command, "d") == 0) {
            studentDeleteList();
        } else if (strcmp(command, "l") == 0) {
            scanf("%s", filename);
            studentLoad(filename);
        } else if (strcmp(command, "q") == 0) {
            break;
        }
        printf("> ");
    }

    return 0;
}
