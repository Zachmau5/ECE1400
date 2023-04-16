#include <stdbool.h>
#include "hw12_lib.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int main(int argc, char *argv[]){
    if (argc != 3) {
        printf("Incorrect Usage");
        return 1;
    }
    const char *filein=argv[1];
    const char *name=argv[2];
    struct Person head;
    head.prev=NULL;
    head.next=NULL;
    
    FILE *in_file=fopen(filein,"r");
    	if(in_file==NULL){
    	printf("no input found ya dumb dumb");
    		return 1;
    		}
    	char child[20];
    	char father[50];
    	char mother[50];
    	int gen=0;
    	while(fscanf(in_file,"%s%s%s",child,father,mother) ==3) {
		addToTail(&head,child,father,mother);
		}
//Finds and prints ancestors
    printf("ancestors of %s:\n",name);
    findAncestor(&head,name,gen);
//Finds and Prints decendants
    printf("descendants of %s:\n",name);
    findDecendant(&head,name,gen);
//XTRA, finds siblings. Removed for test
    //printf("siblings of %s:\n",name);
    //printSiblings(&head, name);
}
