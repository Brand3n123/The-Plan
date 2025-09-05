name = input("Tell the Magic 8-Ball your name: ")
question = input("Tel the Magic 8-Ball your question: ")
answer = ""


from colorama import init, Fore, Style
import random
init()


random_number = random.randint(1, 9)



if (random_number == 1):
  answer = "Yes - definitely"
elif(random_number == 2):
  answer = "It is decidedly so"
elif(random_number == 3):
  answer = "Without a doubt"
elif(random_number == 4):
 answer = "Reply hazy, try again"
elif(random_number == 5):
  answer = "Ask again later"
elif(random_number == 6):
  answer = "Better not tell you now"
elif(random_number == 7):
  answer = "My sources say no"
elif(random_number == 8):
  answer = "Outlook not so good"
elif(random_number == 9):
  answer = "Very doubtful"
else: 
  print("Error")

if (question == ""):
  print ("You must not be inquizitive of the Magic 8-Ball's wonderful powers......please ask a question so that you may live")
elif (name == ""):
  print ("Question:", question)
  print(Fore.PURPLE + Style.BRIGHT + "Magic 8-Ball's answer: " + answer + Style.RESET_ALL)
else:
  print(name, "asks:", question)
  print(Fore.PURPLE + Style.BRIGHT + "Magic 8-Ball's answer: " + answer + Style.RESET_ALL)