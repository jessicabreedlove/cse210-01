# Jessica Reece 
# Tick-Tack-Toe 
# 1/10/2022

def main():
  row1 = ['1', '2', '3']
  row2 = ['4', '5', '6']
  row3 = ['7', '8', '9']

  player = next_player("")
  while not has_winner(row1, row2, row3):
    print_board(row1, row2, row3)
    make_move(player, row1, row2, row3)
    player = next_player(player)
  print_board(row1, row2, row3)
  print('You did it! Great Work!')
 

def print_board(row1, row2, row3):
  print(f"{row1[0]}|{row1[1]}|cl{row1[2]}")
  print('-+-+-')
  print(f"{row2[0]}|{row2[1]}|{row2[2]}")
  print('-+-+-')
  print(f"{row3[0]}|{row3[1]}|{row3[2]}")

def next_player(current):
  if current == '' or current == 'o':
    return 'x'
  elif current == 'x':
    return 'o'

def make_move(player, row1, row2, row3):
  index = int(input(f'{player}\'s turn. On what number would you like to place your {player}? '))
  index -= 1
  if (index >= 0 and index <= 2):
    row1[index] = player
  elif (index >= 3 and index <= 5):
    row2[index - 3] = player
  elif (index >=6 and index <= 8):
    row3[index-6] = player

def has_winner(row1, row2, row3):
  if (row1[0] == row2[0] == row3[0]) or (row1[1] == row2[1] and row3[1]) or (row1[2] == row2[2] and row3[2]) or (row1[0] == row1[1] == row1[2]) or (row2[0] == row2[1] == row2[2]) or (row3[0]  == row3[1] == row3[2]) or (row1[0] == row2[1] == row3[2]) or (row1[2] == row2[2] == row3[0]):
    return True 


if __name__ == "__main__":
    main()



#psuedo code
#step 1 create board
#step 2 accept input from user 
#step 3 insert new value (x or o) in number selected by user
#continue steps 2-3 until 3 in a row
#validate 3 in a row.