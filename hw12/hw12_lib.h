#ifndef HW12_LIB_H
#define HW12_LIB_H

#include <stdbool.h>
#include <string.h>
#include <stdio.h>
struct Person {
    char name[30];
    char father[30];
    char mother[30];
    struct Person *curr;
    struct Person *curr2;
    struct Person *prev;
    struct Person *next;
};


void *printList(struct Person *head);
struct Person *findHead(struct Person *n);
struct Person *findTail(struct Person *n);
struct Person *FindPerson(struct Person *head, const char *name);
struct Person *addToTail(struct Person *head, const char *name, const char *father, const char *mother);

struct Person* findFather(struct Person *head, const char* name);
const char *findMother(struct Person *head, const char *name);


void findAncestor(struct Person *head, const char *name, int gen);
void findDecendant(struct Person *head, const char *name, int gen);
void printSiblings(struct Person* head, const char* name);
