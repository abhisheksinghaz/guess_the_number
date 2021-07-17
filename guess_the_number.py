import random

class GuessingGame:

  def __init__(self):
    try:
      self.ini = int(input("Range begins at: "))
      self.fin = int(input("Range ends at: "))
      self.ran = random.randint(self.ini, self.fin)
    except:
      print ("Please enter valid entries.")
    #print(self.ran)

  def input_guess(self):
    self.guess = int(input("Guess the number: "))

  def check_guess(self):
    if self.guess == self.ran:
      print("Congratulations! You got it right.")
      return True
    elif self.guess < self.ran:
      print("You guessed too low. Try again!")
      return False
    else: 
      print("You guessed too high. Try again!")
      return False

if __name__ == "__main__":
  obj = GuessingGame()
  while True:
    obj.input_guess()
    if obj.check_guess():
      break
