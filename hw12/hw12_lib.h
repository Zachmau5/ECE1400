#ifndef HW12_LIB_H
#define HW12_LIB_H

#include <stdbool.h>
#include <string.h>
#include <stdio.h>

struct Person {
    char father[50];
    char mother[50];
    char name[20];
    struct Person *next;
    struct Person *prev;

};
struct Person *findHead(struct Person *n);
struct Person *findTail(struct Person *n);
struct Person *FindPerson(struct Person *n, const char *name);
struct Person *addToTail(struct Person *n, const char *name, const char *father, const char *mother);
const char *findFather(struct Person *n, const char *name);
const char *findMother(struct Person *n, const char *name);
void findAncestor(struct Person *n, const char *name, int gen);
void *printList(struct Person *n);
#endif
