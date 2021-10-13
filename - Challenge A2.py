# defines what a longhorn should look like in the code 
longhorn = '''|**********************| 
|#######........#######| 
|....####......####....| 
|.......########.......| 
|......##########......| 
|........######........| 
|..........##..........| 
|..........##..........| 
|..........##..........| 
************************''' 
# variable that keeps track of how many longhorns there are 
longhornNumber = 1 
# loop that runs until there are 15 longhorns 
while longhornNumber < 16: 
    # prints longhorn picture 
    print(longhorn) 
    # prints longhorn number 
    print(str(longhornNumber)) 
    # increases total longhorn count by 1 
    longhornNumber += 1 