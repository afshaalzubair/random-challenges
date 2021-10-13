

chickenLeg = input("How many chickens? ")
total = int(chickenLeg) * 2
print("You have " + str(total) + " legs.")

cowLeg = input("How many cows? ")
total2 = int(cowLeg) * 4
print("You have " + str(total2) + " legs.")

pigLeg = input("How many pigs? ")
total3 = int(pigLeg) * 4
print("You have " + str(total3) + " legs.")

total4 = int(total) + int(total2) + int(total3)

print("You have a combined total of " + str(total4) + " legs.")