#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

int charToInt(char x);
int modBy26(int x);
int intToChar(int x);

int main(){
    char keyString[4];
    int keyMatrix[2][2] = {{7, 8}, {11, 11}};
    int cipherTextMatrix[2] = {0, 0};
    char cipherTextString[2];
    char plainTextString[3];
    int plainTextMatrix[2] = {0, 0};
    int modularDeterminant = 0;
    int inverseFactorOfTheDeterminant;
    plainTextString[2] = '\0';

    printf("Enter your key:     ");
    gets(keyString);

    int index = 0; 
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            keyMatrix[i][j] = charToInt(keyString[index]);
            index++;
        }
    }

    printf("Enter the two character cipher text:    ");
    gets(cipherTextString);

    for(int i = 0; i < 2; i++){
        cipherTextMatrix[i] = charToInt(cipherTextString[i]);
    }
    
    modularDeterminant = modBy26(keyMatrix[0][0] * keyMatrix[1][1] - keyMatrix[1][0] * keyMatrix[0][1]);
    for(int i = 1; i < 26; i++){
        if(i * modularDeterminant % 26 == 1){
            inverseFactorOfTheDeterminant = i;
        }
    }

    keyMatrix[0][0] = keyMatrix[0][0] + keyMatrix[1][1];    
    keyMatrix[1][1] = keyMatrix[0][0] - keyMatrix[1][1];  
    keyMatrix[0][0] = keyMatrix[0][0] - keyMatrix[1][1];
    keyMatrix[0][1] = -keyMatrix[0][1];
    keyMatrix[1][0] = -keyMatrix[1][0];
   
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            keyMatrix[i][j] = modBy26(keyMatrix[i][j]);
            keyMatrix[i][j] *= inverseFactorOfTheDeterminant;
            keyMatrix[i][j] = modBy26(keyMatrix[i][j]);
        }
    }
    
    
    for(int i = 0; i < 2; i++){
        for(int j = 0; j < 2; j++){
            plainTextMatrix[i] += keyMatrix[i][j] * cipherTextMatrix[j]; 
        }
        plainTextMatrix[i] = modBy26(plainTextMatrix[i]);
        plainTextString[i] = intToChar(plainTextMatrix[i]);
    }

    printf("The plain text is:     %s", plainTextString);

    return 0;
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
