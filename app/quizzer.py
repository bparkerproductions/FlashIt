import random

# The Quizzer class is for quizzing the user for existing flash cards
class Quizzer(CardSet):
  def __init__(self, cardSet):
    print(self.styledMessage('Welcome to quizzer! Here you can test our knowledge and go through the flashcards you made.', '-') + '\n')
    print(self.styledMessage('You can exit anytime by typing :cancel'))
    self.cardSet = cardSet
    self.chooseQuizMode()
  
  def chooseQuizMode(self):
    
    while True:
      userChoice = input(self.styledMessage('Would you like to shuffle cards or do them in order? (type shuffle or order)', '-') + '\n')

      if userChoice == ':cancel':
        break
      elif userChoice == 'shuffle':
        self.shuffleQuiz()
        break
      elif userChoice == 'order':
        self.orderQuiz()
        break
      else:
        print(self.styledMessage('That option was not recognized, please try again', '!') + '\n')

  # A quiz method that tests the user in random order
  def shuffleQuiz(self):
    randomCardSet=list(self.cardSet.keys())
    random.shuffle(randomCardSet)
    self.cardQuiz(randomCardSet)

  # A quiz method that tests the user in sequential order
  def orderQuiz(self):
    self.cardQuiz(self.cardSet)

  # The actual quizzing logic/prompts. The order quiz and shuffle quiz utilize this logic
  def cardQuiz(self, cardList): 
    print(self.styledMessage('To cancel the quizzing, just type :cancel'))
    
    for card in cardList:
      print('\nQuestion: ' + self.cardSet[card]['question'])
      answer = input(self.styledMessage('What is your answer?', '-') + '\n')

      if answer == ':cancel':
        break
      elif answer.lower() == self.cardSet[card]['answer'].lower():
        print('\n' + self.styledMessage('Good job! Your answer is correct.', '='))
      else:
        print('\nNot quite, the answer is ' + self.cardSet[card]['answer'])