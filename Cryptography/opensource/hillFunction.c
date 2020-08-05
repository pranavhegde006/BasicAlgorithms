#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
#define MAX 1000

char plainTextString[3];
char plainText[MAX];
char keyString[MAX];
char cipherTextString[3];
char cipherText[MAX];

char *hillEncrpt(char *plainTextString, char *keyString, char *cipherTextString);
int charToInt(char x);
int modBy26(int x);
int intToChar(int x);

int main(){
    clock_t t; 
    t = clock(); 


    strcat(plainText, "pranavpythoasdfasfjksajflksaoeqioytqopwuialjkhfajkbhakbnqiuweyruighjzvchzmdbfhjsgfewrq");
    printf("The length of plain text is:    %d\n", strlen(plainText));

    if(!(strlen(plainText) %2)){
        strcat(plainText, "z");
    }

    for(int i = 0; i < strlen(plainText) - 1; i += 2){
        plainTextString[0] = plainText[i];
        plainTextString[1] = plainText[i + 1];
        strcat(cipherText, hillEncrpt(plainTextString, keyString, cipherTextString));
    }

    
    
    printf("%s\n", cipherText);


    t = clock() - t; 
    double time_taken = ((double)t)/CLOCKS_PER_SEC; // in seconds 
  
    printf("compilation time: %f\n", time_taken); 
    return 0;
}


char *hillEncrpt(char *plainTextString, char *keyString, char *cipherTextString){

    int plainTextMatrix[2] = {0, 0};
    int cipherTextMatrix[2] = {0, 0};
    int keyMatrix[2][2] = {{0, 0}, {0, 0}};

    for(int i = 0; i < 2; i++){
        plainTextMatrix[i] = charToInt(plainTextString[i]);
    }

    int index = 0;
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            keyMatrix[i][j] = charToInt(keyString[index]);
            index++;
            cipherTextMatrix[i] += keyMatrix[i][j] * plainTextMatrix[j]; 
        }
        cipherTextMatrix[i] = modBy26(cipherTextMatrix[i]);
    }

    for(int i = 0; i < 2; i++){
        cipherTextString[i] = intToChar(cipherTextMatrix[i]);
    }
    return cipherTextString;
}


int charToInt(char x){
    return (int)x - 97;
}

int modBy26(int x){
    int rem = x % 26;
    if (rem < 0){
        return 26 + rem;
    }
    return rem;
}

int intToChar(int x){
    return (char)(x + 97);
}
