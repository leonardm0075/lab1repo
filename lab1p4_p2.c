#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>



void stringremove(char *str){
/*Removes all non-alpha and also makes everything lowercase */
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
    int numofrepeat = 0;
    int i = 0; 
    int j = 0;
    printf("Enter the name of the file you want to read in\n");
    char file_name[20];
        scanf("%[^\n]s", file_name);
        
    
    fp = fopen(file_name, "r");

    while (fgets(buffer, 300, fp) != NULL) {
    }
    stringremove(buffer);  /* Removes all non alpha */
    fclose(fp);
    printf("\n");
    
    int counter = 0; /*Variable that counts total number of words in the read in string*/
    int n;
    for (n=0; buffer[n] != '\0'; n++) {     /*Counts the number of words in buffer */
        if(buffer[n] == ' ' && buffer[n+1] != ' '){
            counter++;
        }
     }
    
    counter = counter + 1; /* Number of words in the the file we read in*/
    int l = 0; /*All these variables are counters for the upcoming loops */
    int m = 0;
    int q = 0;
    int v = 0;
    char *token = strtok(buffer, " "); /*Tokenizing the read in string and storing them in arrays to easily access*/
    char *array1[counter]; /*These arrays are identical and used to compare each other at different indices*/
    char *array2[counter];
    char *array3[counter];
    while (token!=NULL) { /*Stores the tokens into arrays*/
        array1[l++] = token;
        array2[m++] = token;
        token = strtok(NULL, " ");
    }
    
    for(i=0; i < counter; i++) { /*This huge for loop takes a word in the array and compares it to check for certain conditions and is the main counter*/
       char *compword = array1[i];
       
       for(int d = 0; d < 30; d++) { /*This for loop checks to see if compword has been seen before by corroborating it with another array that stores words that have already been seen and checks 30 times*/
           for(v=0; v<q; v++){
                if(strcmp(compword, array3[v]) == 0){
                    i++;
                    compword = array1[i];
                    break;
                }
           }
       }
       for(j=i; j<counter; j++) { /*This for loop does the comparing to see if the original main word at the top is repeated anywhere in the array and if it is, we save that word for the checking we did above so not to double count it*/
           if (i==j){       
           }
           else{
               /*We need to see if this word has been seen already so we can skip its index else if it hasnt been seen we need to save it for the check */   
               if (strcmp(compword, array2[j]) == 0) { 
                    numofrepeat = numofrepeat+1;
                    array3[q] = array2[j];
                    q++;
              }
           }
        }
       }
    
    int finalnum = counter - numofrepeat;
    printf("The number of distinct words is: %d\n", finalnum);
    return 0;
}


