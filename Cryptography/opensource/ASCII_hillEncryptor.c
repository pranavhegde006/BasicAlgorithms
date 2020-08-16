#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int ASCIImodulo(int x);

int main(){

    char plainText[100];
    int matrix[100];
    int key[2][2] = {{7, 8}, {11, 11}};
    int cipherMatrix[100];

    printf("Enter your two digit plain text:  ");
    scanf("%s", plainText);

    for(int i = 0; i < 2; i++){
        matrix[i] = (int)plainText[i];
        for(int j = 0; j < 2; j++){
            cipherMatrix[i] += key[i][j] * matrix[j];
        }
        cipherMatrix[i] = ASCIImodulo(cipherMatrix[i]);
    }

    printf("Your cipher text is:    %c%c", cipherMatrix[0], cipherMatrix[1]);
    return 0;
}



int ASCIImodulo(int x){
    int rem = x % 128;
    if(rem < 0){
        rem += 128;
    }
    return rem;
}