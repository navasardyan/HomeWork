from random import randint

X = "X"
O = "O"
EMPTY = " "

def add_board():
    """
    Создание игральной доски
    :return: доска для игры
    """
    board = []
    for i in range(COUNT):
        board.append(EMPTY)
    return board

def write_board(board):
    
   print("\n\t", "|",board[6], "|", board[7], "|", board[8],"|")
   print("\t", "|""-----------""|",)
   print("\t", "|", board[3], "|", board[4], "|", board[5], "|")
   print("\t", "|""-----------""|",)
   print("\t", "|", board[0], "|", board[1], "|", board[2], "|""\n")

def pieces():

   y = int((input('Если хотите начать первым нажмите 1/0! ')))
   if y:
     human = X
     comp = O
   else:
     comp = O
     human = X
   return human, comp


def human_step(board, human):
   human_step = int(input('Ваш ход от 1 до 9! = '))
   if board[human_step - 1] == EMPTY:
     board[human_step - 1] = human
   else:
     print('-----------это поле занята---------- \n Будьте внимательны, попробуйте еще раз! ' )

   print (board)

def computer_step(board, comp, human):
   comp_step = 4
   
   while board[comp_step] != EMPTY:
     comp_step = randint(0,8)
   
   
   board[comp_step] = comp 
   
   print(board)



def winner(board):
   WAYS_WIN = (
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6)
    )
   
   for  i in WAYS_WIN:
     if board[i[0]] == board[i[1]] == board[i[2]]:
       winner = board[i[1]]
       return winner
   else:
     print('Вы не смогли победить: НИЧЬЯ')

def main():
  
    print("""Игра крестики-нолики, противостояние с компьютером\n
    Чтобы сделать ход, необходимо ввести число от 0 до 8. Число однозначно соответствует
    полям доски, как показано на рисунке ниже:
   | 7 | 8 | 9 |
   |-----------|
   | 4 | 5 | 6 |
   |-----------|
   | 1 | 2 | 3 |
    """)
   board = add_board()
   write_board(board)
   human, computer = pieces()
   if human == X:
     human_step()
   else:
     computer_step()





main()