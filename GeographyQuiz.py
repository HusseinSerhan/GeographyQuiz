print("Welcome to my geography quiz!")

playing = input("Do you want to play? ").lower()

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :D")
score = 0 

##q1 
answer = input("Where is Italy? ").lower()


if answer == "europe":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!") 
    print("The answer was Europe!") 

##q2 
answer = input("Where is the Big Ben? ").lower()

if answer == "London":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    print("The answer was London!") 

##q3 
answer = input("What country has the best football fans? ").lower()

if answer == "Argentina":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    print("The correct answer was Argentina")

##q4 
answer = input("Where is Madrid ").lower()

if answer == "Spain":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")
    print("The answer was Spain")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
