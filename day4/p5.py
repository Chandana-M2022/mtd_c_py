input_str = input('Enter a string:')
digits =[]
for char in input_str:
    if char.isdigit():
        digits.append(char)

digits = list(set(digits))

digits.sort(reverse = True)

digits_str =''.join(digits)
biggest_number = int(digits_str)
print(f'The resultant number is {biggest_number}')

 
