#include<stdio.h>
#include<string.h>
#define MAX 100

int main(){
    char plainText[MAX];
    int cipherArray[MAX];
    int key;
    printf("Enter the plaintext:    ");
    gets(plainText);
    printf("Enter your key:    ");
    scanf("%d", &key);
    char *cipherText = plainText;
    
    for(int i = 0; i < strlen(plainText); i++){
        cipherArray[i] = (((((int)plainText[i] - 97) + key) % 26) + 97);
        cipherText[i] = (char)cipherArray[i];
    }
    printf("-----------------------------\n");
    printf("Your cipher text is:    %s", cipherText);
    return 0; 
}