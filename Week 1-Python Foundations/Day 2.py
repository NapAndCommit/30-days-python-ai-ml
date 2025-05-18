import random

target = random.randint(1, 10)
attempts = 5

while attempts > 0:
    guess = int(input("Guess the number (1-10): "))
    
    if guess == target:
        print("🎉 Correct! You win.")
        break
    elif guess < target:
        print("Too low.")
    else:
        print("Too high.")
    
    attempts -= 1

if attempts == 0:
    print(f"Game Over! The number was {target}")