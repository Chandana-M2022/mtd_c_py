from prime import check_is_prime
x= int(input('Enter the start value: '))
y=int(input('Enter the end value:'))
print('The prime numbers between start value and end value are')
for number in range(x,y+1):
    if check_is_prime(number):
        print(number,end=" ")