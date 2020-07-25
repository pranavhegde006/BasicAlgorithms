#include<stdio.h>
#include<time.h>
#include<stdlib.h>
#include<string.h>

int charToInt(char x);
int modBy26(int x);
int intToChar(int x);


int main(){
    time_t rawtime;
    struct tm * currentTime;            
    time( &rawtime );
    currentTime = localtime( &rawtime );

    //time concept based keys commented at the end of the file
    char plainTextString[2];
    int plainTextMatrix[2] = {0, 0};
    int cipherTextMatrix[2] = {0, 0};
    char cipherTextString[3];
    cipherTextString[2] = '\0';
    int keyMatrix[2][2] = {{0, 0}, {0, 0}};
    char keyString[4];

    printf("Enter your key: ");
    gets(keyString);
    
    printf("Enter your two character plain text:    ");
    gets(plainTextString);

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

    printf("The cipher text is:     %s", cipherTextString);
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

// int keyMatrix[2][2] = {{currentTime->tm_mday, currentTime->tm_sec}, {currentTime->tm_min, currentTime->tm_hour}};
