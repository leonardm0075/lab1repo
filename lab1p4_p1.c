
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

void stringremove(char *str){
/*Function that removes all non-alpha and forces everything to lowercase */
    unsigned long i=0;
    unsigned long j=0;
    char c;

    while((c = str[i]) != '\0'){

        if (isalnum(c) || (str[i] == ' ')){
            str[j++] = tolower(c);
            
        }
        i++;
    }
    str[j] = '\0';
}

int main()
{

    FILE *fp;
    char buffer[300];
    int distinctwordcount = 0 ;
    printf("Enter the name of the file you want to read in\n"); 
    char file_name[20];
        scanf("%[^\n]s", file_name); /*Reads in file based off your input */
        
    fp = fopen(file_name, "r");
    while (fgets(buffer, 300, fp) != NULL) {
    }
    fclose(fp);
    printf("\n");
    
    /* Buffer is a array of chars that represents a string in C */
    stringremove(buffer);    
    char *token = strtok(buffer, " "); /*Tokenizes every word in the read in string and counts how many times it tokenizes to give distinct number of words */
    while(token!=NULL) {
        token = strtok(NULL, " "); 
        ++distinctwordcount;  

    }
    
    printf("The distinct word count is: %d\n", distinctwordcount);





return 0;
}
