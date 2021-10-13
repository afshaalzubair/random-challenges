# gets the six digit code from the user. 
six_dig_num = input('input 6 digit student number: ') 
# converts the input to a list so it can have computation done to the individual numbers. 
digits = list(six_dig_num) 
# defines variables, multiplier is the number by which each number is multiplied and seventh_digit is the seventh digit. 
multiplier = 1 
seventh_digit = 0 
# most of the math happens within the for loop. 
for number in digits: 
    # changes seventh digit variable to a total given by the equation. 
    seventh_digit = seventh_digit + multiplier * int(number) 
# takes the total outputted by the computation, divides by 10 and sets seventh digit variable to the remainder. 
seventh_digit = seventh_digit % 10 
# prints the full seven digit number with the seventh digit at the end. 
print(str(six_dig_num) + str(seventh_digit)) 