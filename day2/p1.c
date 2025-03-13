#include<stdio.h>
int main()
{
    int inputNum = 0;
    puts(" Enter a number to print a  math table");
    scanf("%d",&inputNum);
    for(int i = 1; i <= 20; i++)
    {
        printf("%d * %02d =  %03d\n",inputNum,i,inputNum*i);
    }


}
