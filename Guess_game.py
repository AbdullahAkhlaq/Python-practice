import random
winning_number=random.randint(1,100)
guess = 1
user_num=int(input("Enter a number between 1 and 100: "))
game_over = False

while True:
    if user_num==winning_number:
        print(f"You win , and you guessed in {guess} times")
        break
    else: 
        if winning_number < user_num:
            print(" too high")
           
        else:
            print("too low")
            
        guess +=1
        user_num = int(input("guess again :"))