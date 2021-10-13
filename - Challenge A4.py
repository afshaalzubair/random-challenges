original_length = input("What is the original length: ")
# Asks for the input of the original length.
b = 0
# Setting the value of b for the following equation. B is the percentage of light speed.
new_length = int(original_length) * ((1-b ** 2) ** .5)
# This is the equation of the new length, which is calculated by the original length times the square root of
# 1 minus b, b being the percentage of light speed, .5 being the square root operation.
lightspeed = b * 300000000
# Calculating the lightspeed based on the percentage of it, used below.

print("Percent of Light        Speed (m/s)        Length")   # Table formatting.
print("----------------        -----------        ------")   # Table formatting.
b = 0                                                        # Establishing the first value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the first value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("0                      ", lightspeed,"                ", new_length) # Printing the calculated data.
b = 0.25                                                     # Establishing the second value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the second value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("25                     ", lightspeed,"       ", new_length) # Printing the calculated data.
b = 0.50                                                     # Establishing the third value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the third value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("50                     ", lightspeed,"      ", new_length) # Printing the calculated data.
b = 0.75                                                     # Establishing the fourth value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the fourth value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("75                     ", lightspeed,"      ", new_length) # Printing the calculated data.
b = 0.90                                                     # Establishing the fifth value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the fifth value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("90                     ", lightspeed,"      ", new_length) # Printing the calculated data.
b = 0.95                                                     # Establishing the sixth value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the sixth value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("95                     ", lightspeed,"      ", new_length) # Printing the calculated data.
b = 0.99                                                     # Establishing the seventh value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of sixth value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("99                     ", lightspeed,"      ", new_length) # Printing the calculated data.
b = 0.999                                                    # Establishing the eighth value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the eighth value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("99.9                   ", lightspeed,"      ", new_length) # Printing the calculated data.
b = 0.9999                                                   # Establishing the ninth value of b.
new_length = int(original_length) * ((1-b ** 2) ** .5)       # Calculating the new length of the ninth value of b.
lightspeed = b * 300000000                                   # Calculating the light speed for the value of b.
print("99.99                  ", lightspeed,"      ", new_length) # Printing the calculated data.