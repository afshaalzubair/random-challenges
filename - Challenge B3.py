number = int(input("Input a number: "))      # The user inputs a number.
binaryNumber = bin(number)                   # The number is converted into binary.
stringNumber = str(binaryNumber)             # The binary number is converted into a string.
finalNumber = stringNumber.count("1")        # The code counts the number of 1s in the string.
if (finalNumber % 2 == 0):                   # If the number has an even number of 1s.
    print(number, "is an evil number.")      # Then it is an evil number.
else:                                        # If the number has an odd number of 1s.
    print(number, "is an odious number.")    # Then it is an odious number.