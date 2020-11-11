from random import randint

def validate_input(inp,colors):
  if len(inp)!= 4:
    return False
  for i in range(0,4):
    if inp[i] not in colors:
      return False
  return True

colors = ['R', 'O', 'Y', 'G', 'B', 'P']
solution = f'{colors[randint(0,5)]}{colors[randint(0,5)]}{colors[randint(0,5)]}{colors[randint(0,5)]}'
print("solution=", solution)

turn_count = 0

def eval_win(guess, solution):
  score = {'Black': 0, 'White':0}
  i=0
  sol_len=len(solution)
  while i<sol_len:
    if guess[i] == solution[i]:
      score['Black'] +=1
      solution = solution[:i]+solution[i+1:]
      sol_len-=1
      guess = guess[:i]+guess[i+1:]
    else:
      i+=1
  for element in set(guess):
    if element in set(solution):
      score['White'] +=1
  return score

while turn_count < 10:
  guess = input(f'{10-turn_count} guesses left.\nMake a guess: ')
  if not validate_input(guess,colors):
    continue
  turn_count +=1
  score = eval_win(guess, solution)
  print(" Black:",score['Black'],'\n',"White:",score['White'])
  if score['Black'] == 4:
    print("You won!!")
    break