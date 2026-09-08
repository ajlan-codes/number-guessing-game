import random

print("Hi everyone who got time to look at my first little game")
print("We are in a number guessing game")


name = input("What is your name? ")
greeting = input("How should I greet you? ")
print(greeting, name + "!")

college = input("Which college do you study at? ")
branch = input("Which branch are you studying? ")

print("I see you are from", college)
print("And you're studying", branch)

ready = input("Are you ready to play? yes/no: ")

if ready == "yes":
    print("Awesome! Let's begin")

    difficulty = input("Choose difficulty: hard, easy, or medium: ")

    if difficulty == "easy":
      secret = random.randint(1, 200)
    
    elif difficulty == "medium":
      secret = random.randint(1, 100)
    
    elif difficulty == "hard":
      secret = random.randint(1, 50)


    
    if difficulty == "easy":
       attempts = 15
       score = 150
       multiplier = 1
    elif difficulty == "medium":
       attempts = 10
       score = 250
       multiplier = 2
    elif difficulty == "hard":
       print("nice challenge!")
       attempts = 5
       score = 400
       multiplier = 3
    else:
       print("Invalid difficulty")    
       attempts = 0
    
    used_attempts=0     
    won = False

    for i in range(attempts):
        guess = int(input("Guess the number? "))
        used_attempts = used_attempts + 1

        if guess == secret:
            print("You have won!")
            print("You used", used_attempts, "attempts.")
            print("your scoreis",score)
            
            final_score = score * multiplier
            print("Your final score is", final_score)
         
            won = True
            break

        elif guess < secret:
            print("This is low, try again you lost 25 points")
            score = score - 25

        elif guess > secret:
            print("This is high, try again.you lost 25 points")
            score = score - 25
    if won == False and attempts > 0:
     print("You lost!")
     print("You used all", used_attempts, "attempts.")
     print("Your final score is", score)
     print("Better luck next time!")
   
    else:
      if score >= 300:
         print("Excellent! 🏆")
      elif score >= 200:
         print("Good job! 👍")
      else:
         print("Keep practicing! 💪")       
    if won == True and score >= 300:
         print("Amazing! 🏆")   
    if won or score >= 300:
       print("Great performer!") 
 
elif ready == "no":
    print("No problem! Take your time.")

else:
    print("I don't understand, but let's try anyway!")
