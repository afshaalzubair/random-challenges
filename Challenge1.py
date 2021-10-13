import random
balloptions = ["It is decidedly so.", "It is certain.", "Don't count on it.", "Concentrate and ask again.", "Cannot predict now.", "Better not tell you now.", "Ask again later.", "As I see it, yes." ]
input("Ask the ball something. ")
print(balloptions[random.randint(0,7)])