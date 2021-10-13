yenMoney = input("How much Yen do you have?: ")

def yen_to_usd(yen):
    return int(yen) / 107.5
print("That is ", str(yen_to_usd(yenMoney)), "US dollars.")

