#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<time.h>
#define MAX 100

char keyString[5];


char *run(char *keyString);
int modBy26(int x);
int charToInt(char x);
int intToChar(int x);


int main(){
    
    printf("%s", run(keyString));

    return 0;
}


char *run(char *keyString){

    time_t rawtime;
    struct tm * currentTime;            
    time(&rawtime);
    currentTime = localtime(&rawtime);

    int modularInverse = 3;
    int first, second, third, fourth;
    first = currentTime->tm_min % 26;
    second = 1;
    third = 1;
    fourth = currentTime->tm_sec % 26;

    char keyMatrixInString[MAX];

    for(int i = 1; i < 26; i++){
        for(int j = 1; j < 26; j++){
            if((first * fourth - j * i) != 0){
                if((modBy26((first * fourth - j * i) * modularInverse)) == 1){
                    second = i;
                    third = j;
                    break;
                }
            }
        }
    }

    keyString[0] = intToChar(first);
    keyString[1] = intToChar(second);
    keyString[2] = intToChar(third);
    keyString[3] = intToChar(fourth);

    return keyString;
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
