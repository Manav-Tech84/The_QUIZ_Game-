
print("Welcome to the quiz game.")
Player_name = input("Enter Your name: ")

player = input(Player_name + " Do you want to play ? ")

if player.lower() != "yes":
    quit()
print("Okay Let's Start :)")
score = 0

#1
answer = input("CPU stands for ? ")
if answer.lower() == "central processing unit":
    print("Correct")
    score +=1
else:
    print("Incorrect")

#2
answer = input("In Ms Word the mailing list is known as the____? ")
if answer.lower() == "data source":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#3
answer = input("Window key + D ? ")
if answer.lower() == "show desktop":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#4
answer = input("Ctrl + N Shortcut key is used in Ms Word to__ ? ")
if answer.lower() == "new document":
    print("Correct")
    score += 1
else:
    print("Incorrect")

#5
answer = input("Bit is also called __ ? ")
if answer.lower() == "binary digit":
    print("Correct")
    score += 1
else:
    print("Incorrect")
#6
answer = input("RAM stands for ? ")
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print(Player_name +" You Get "+str(score)+" Question are Correct ")
print(Player_name + " You Get "+str((score / 6)*100)+ "% Score.")