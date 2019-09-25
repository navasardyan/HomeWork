from random import randint
WORDS = {1 : 'MANUK', 2: 'FELIQS', 3 : 'TARON', 4 : 'RUBEN', 5 : 'MARIAM', 6 : 'ASHXEN'}
Key = randint(1,6)
WORD = WORDS[Key]
X = ['_'] * len(WORD)
Live = 10


def logika(letter):
  global Live
  if letter in WORD:
    i = -1
    if letter in X:
      Live -= 1
    for I in WORD:
      i += 1
      if I == letter:
        X[i] = I
   
    print(X)
    
    print('Попыток =', Live)
  else:
    Live -= 1
    print('Не угадали попробуйте еще раз!: ')
    print('Попыток =',Live)

def is_game_finished(X):
  if Live == 0:
    print('------------Вы проиграли!------------')
    return False
     
  if '_' in X:
    return True 
  else:
      print('------------Поздравляю Вы нашли нужную имею!------------')
      return False

  
  
def main():
  print(WORD)
  print(X)
  print('Попыток =',Live)
  while  is_game_finished(X):
    letter = (str(input('Выводите любую латинскую букву: '))).upper()
    logika(letter)

main()