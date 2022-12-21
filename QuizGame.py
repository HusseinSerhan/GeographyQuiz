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
answer = input("What does RAM stand for? ").lower()

if answer == "random access memory":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

##q4 
answer = input("What does PSU stand for? ").lower()

if answer == "power supply":
    print("Correct!")
    score += 1 
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score/4) * 100) + "%")
