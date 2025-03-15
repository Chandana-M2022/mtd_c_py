from prime import check_is_prime
x= int(input('Enter the value for x: '))
y=int(input('Enter the value for y:'))
for number in range(x,y+1):
    if check_is_prime(number):
        print(number)