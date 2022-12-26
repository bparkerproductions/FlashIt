# The Quizzer class is for quizzing the user for existing flash cards
class Quizzer(CardSet):
  def __init__(self, cardSet):
    print('Welcome to quizzer! Here you can test our knowledge and go through the flashcards you made. You can exit anytime by typing :cancel')
    self.cardSet = cardSet
    self.chooseQuizMode()
  
  def chooseQuizMode(self):
    
    while True:
      userChoice = input('Would you like to shuffle cards or do them in order? (type shuffle or order)\n')

      if userChoice == ':cancel':
        break
      elif userChoice == 'shuffle':
        self.shuffleQuiz()
        break
      elif userChoice == 'order':
        self.orderQuiz()
        break
      else:
        print('That option was not recognized, please try again')

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
    print('To cancel the quizzing, just type :cancel')
    
    for card in cardList:
      print('\nQuestion:' + self.cardSet[card]['question'])
      answer = input('What is your answer?\n')

      if answer == ':cancel':
        break
      elif answer.lower() == self.cardSet[card]['answer'].lower():
        print('Good job! Your answer is correct.')
      else:
        print('Not quite, the answer is ' + self.cardSet[card]['answer'])