minutesAmount = input("How many minutes? ")
framesAmount = input("How many frames per second? ")

def frames(minutes, fps):
    return int(minutes) * 60 * int(fps)
print("That is", int(frames(minutesAmount, framesAmount)), "frames in total. ")
