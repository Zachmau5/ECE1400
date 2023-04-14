#include "hw12_lib.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
void *printList(struct Person *n) {
    n=findHead(n);
    while(n->next!= NULL) {
        n=n->next;
        printf("%s %s %s\n", n->name, n->father, n->mother);
    }
}
struct Person *findHead(struct Person *n) {
    while(n->prev!=NULL) {
        n=n->prev;
        }
        return n;
}
struct Person *findTail(struct Person *n) {
    while(n->next!=NULL) {
        n=n->next;
        }
        return n;
}

struct Person *FindPerson(struct Person *n, const char *name) {
     n=findHead(n);
     while(strcmp(n->name, name)!=0) {
     n=n->next;
     if(n==NULL) {
        return NULL;
        }
     }
     return n;
}

struct Person *addToTail(struct Person *n, const char *name, const char *father, const char *mother) {
    n=findTail(n);
    struct Person *NewPerson=malloc(sizeof(struct Person));
    strncpy(NewPerson->name, name,sizeof(NewPerson->name));
    strncpy(NewPerson->father,father,sizeof(NewPerson->father));
    strncpy(NewPerson->mother,mother,sizeof(NewPerson->mother));
    NewPerson->prev=n;
    NewPerson->next=NULL;
    n->next=NewPerson;
    return NewPerson;
}

const char *findFather(struct Person *n, const char *name) {
    n=FindPerson(n,name);
    if(n==NULL) {
        printf("%s is batman \n", name);
        return 0;
        }
        return n->father;
 }                                                                                                                                                                     1,1           Top
const char *findMother(struct Person *n, const char *name) {
    n=FindPerson(n,name);
    if(n==NULL) {
        printf("%s is batman \n", name);
        return 0;
        }
        return n->mother;

}
void findAncestor(struct Person *n, const char *name, int gen) {
    n=FindPerson(n,name);
    char dad[10]="NULL";
    if(strcmp(n->father,dad)==0){
    //printf("if state");
        return;
        }
    else {
    if(gen>1){
        printf("great");
        }
    if(gen>=1){
        printf("grand");
        }
    printf("father ");
    printf("%s \n", n->father);
    findAncestor(n,n->father,gen+1);
    if(gen>1){
        printf("great");
        }
    if(gen>=1){
        printf("grand");
        }
    printf("mother ");
    printf("%s \n", n->mother);
    findAncestor(n,n->mother,gen+1);
}
    return;

}
/*
struct sNode *findKid(struct sNode *n, const char *name) {
    n=findHead(n);
    while(strcmp(n->name, name)!=0) {
        n=n->next;
        if(n==NULL) {
            return NULL;

        }
    }
    return n;
    */
}

