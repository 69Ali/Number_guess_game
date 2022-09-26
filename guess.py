import random
print("Welcome to a number guess game!")
Hard_level=5
Easy_level=10
def check_answer(guess,answer,turns):
 if guess>answer:
    print("Too high")
    return turns - 1
 elif guess<answer:
    print("too loo")
    return turns - 1
 else:
    print(f"you got the number,answer is {answer}")   
def set_dificulty():
    level=input("Choose a dificulty.Type 'easy' or 'hard' :")     
    if level == "hard":
        print(Hard_level)
    else:
        print(Easy_level)    
def game():

 guess=("Iam thinking of a number 1 to 100")
 answer=random.randint(1,100)
 print(f"The corect answer is {answer}")
 turns=set_dificulty()
 guess=0
 while guess != answer:
  print(f"You have {turns} attempts to guess the number")
 guess=int(input('Make guess'))
 turns=check_answer(guess,answer,turns)
 if turns == 0:
   print("You have run out of guesses,you lose")
 else:
    print("Guess again")    
 