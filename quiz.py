print("Welcome to my computer quiz")
playing = input("Do you want to play?-Give answer in Yes or No ")

if playing.lower() != "yes":
    quit()
score = 0
print("okay !! Let's play")
answer = input("What is the full form of AWS? ")

if answer.lower() == "amazon web services":
    print("Correct Answer!!!!")
    score += 1
else:
    print("Oops!!Wrong Answer")
answer = input("What is another name for Network Interface Cables ? ")

if answer.lower() == "ethernet":
    print("Correct Answer!!!!")
    score += 1
else:
    print("Oops!!Wrong Answer")
answer = input("What is the full form of RAM ? ")

if answer.lower() == "random access memory":
    print("Correct Answer!!!!")
    score += 1
else:
    print("Oops!!Wrong Answer")
answer = input("What is the full form of GPU ? ")

if answer.lower() == "graphics processing unit":
    print("Correct Answer!!!!")
    score += 1
else:
    print("Oops!!Wrong Answer")
answer = input("Keyword used in Java for inheriting a class ? ")
if answer.lower() == "extends":
    print("Correct Answer!!!!")
    score += 1
else:
    print("Oops!!Wrong Answer")
if score == 5:
    print("Hurray!! you have scored 5 out of 5")
else:
    print("Your score is " + str(score) + " out of 5")



