#include<stdio.h>
int main()
{
    int number = 0;
    int remainderDigit = 0;
    int sumOfDigits = 0;
    puts(" Enter a number to know your lucky number");
    scanf("%d",&number);
    while(number>0)
    {
       
        remainderDigit = number%10;
        sumOfDigits = sumOfDigits + remainderDigit;
        number = number/10;
    }
    if(number == 0 && sumOfDigits > 9 )
        {
            number = sumOfDigits;
            sumOfDigits = 0;
            remainderDigit = number%10;
            sumOfDigits = sumOfDigits + remainderDigit;
            number = number/10;
           
        }
        printf(" Your lucky number is %d",sumOfDigits);
}