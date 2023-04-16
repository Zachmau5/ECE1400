#include "hw12_lib.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
const char* NULL_STRING = "NULL";
void *printList(struct Person *n) {
	n=findHead(n);
	while(n->next!= NULL) {
		n=n->next;
		printf("%s %s %s\n", n->name, n->father, n->mother);
	}
	return NULL;
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

struct Person* findFather(struct Person* head, const char* name) {
    struct Person* person = FindPerson(head, name);
    if (person == NULL) {
        printf("%s is not found.\n", name);
        return NULL;
    }
    struct Person* father = FindPerson(head, person->father);
    if (father == NULL) {
        printf("%s's father is not found.\n", name);
        return NULL;
    }
    return father;
}




const char *findMother(struct Person *n, const char *name) {
    n=FindPerson(n,name);
    if(n==NULL) {
    	printf("%s is batman \n", name);
    	return 0;
    	}
    	return n->mother;

}
void findAncestor(struct Person *n, const char *name, int gen) {
    if (n==NULL) {
        return;
    }
    n=FindPerson(n, name);
    if(n==NULL) {
        return;
    }
    if (strcmp(n->father, NULL_STRING) != 0) {
        if (gen > 2) {
            printf("great ");
        }    
        if (gen > 1) {
            printf("great ");
        }
        if (gen >= 1) {
            printf("grand");
        }
        printf("father ");
        printf("%s \n", n->father);
        findAncestor(n, n->father, gen+1);
    }
    if (strcmp(n->mother, NULL_STRING) != 0) {
        if (gen > 2) {
            printf("great ");
        }    
        if (gen > 1) {
            printf("great ");
        }
        if (gen >= 1) {
            printf("grand");
        }
        printf("mother ");
        printf("%s \n", n->mother);
        findAncestor(n, n->mother, gen+1);
    }
}
void findDecendant(struct Person *n, const char *name, int gen) {
    n=findHead(n);
    while(n->next != NULL) {
        n=n->next;
        if(strcmp(n->father, name)==0) {
            if (gen>2) {
                printf("great ");
            }
            if (gen>1) {
                    printf("great ");
             }
             if (gen>=1) {
                printf("grand");
             }
            printf("child ");
            printf("%s\n",n->name);
            findDecendant(n,n->name, gen+1);
        }
        if(strcmp(n->mother, name)==0) {
            if (gen>2) {
                printf("great ");
            }
            if (gen>1) {
                printf("great ");
            }
             if (gen>=1) {
                printf("grand");
             }
            printf("child ");
            printf("%s\n",n->name);
            findDecendant(n,n->name, gen+1);
        }

    }
    return;
}
void printSiblings(struct Person* head, const char* name) {
    struct Person* curr = FindPerson(head, name);
    if (curr == NULL) {
        printf("%s not found.\n", name);
        return;
    }
    if (curr->father == NULL) {
        printf("%s has no father.\n", name);
        return;
    }
    struct Person* father = FindPerson(head, curr->father);
    if (father == NULL) {
        printf("%s's father not found.\n", name);
        return;
    }
    int count = 0;
    for (struct Person* curr2 = head; curr2 != NULL; curr2 = curr2->next) {
        if (strcmp(curr2->father, father->name) == 0 && strcmp(curr2->name, name) != 0 && strcmp(curr2->mother, curr->mother) == 0) {
            printf("%s ", curr2->name);
            count++;
        }
    }
    if (count == 0) {
        printf("%s has no siblings.\n", name);
    } else {
        printf("\n");
    }
}
