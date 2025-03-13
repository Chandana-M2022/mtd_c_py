//accept the number from the user and check if it even
#include<stdio.h>
int main(){
    int inputNum = 0;
    puts("Enter a number to check if it is Even");
    scanf("%d",&inputNum);
    if(inputNum % 2 == 0)
        printf("%d is Even", inputNum);
    else
        printf("%d is not  an Even number",inputNum);
}