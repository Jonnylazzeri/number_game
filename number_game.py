import random

rand_num = random.randint(1,100)

game_running = True

def easy_or_hard():
  difficulty = input("I'm thinking of a number between 1 and 100\nChoose a difficulty. Type 'easy' or 'hard'... ")
  if difficulty == 'hard':
    return 5
  else:
    return 10
  
tries = easy_or_hard()

while game_running:  
  
  guess = int(input(f"What number am I thinking of? You have {tries} tries: "))
  if guess > rand_num:
    print('Too high!')
    tries -= 1
  elif guess < rand_num:
    print('Too low!')
    tries -= 1
  else:
    print(f'Congratulations! The number was {guess}!! You win!')
    game_running = False
    break
  
  if tries == 0:
    print(f'Sorry, you lose! The answer was {rand_num}')
    game_running = False
    break