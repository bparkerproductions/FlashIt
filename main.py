import uuid
import random

class CardSet:
  # A card set is a deck of study cards that will contain multiple cards. It can be reviewed and studied
  def __init__(self, cardObj=False):
    # Create empty dictionary, this will be used to keep track of added cards

    if cardObj:
      self.cardSet = cardObj
    else:
      self.cardSet = {}
    
    print('Welcome to Flash It!')

    self.userChoice()

  # This is where the user can choose what action to do. Exit, add, delete, or update
  def userChoice(self):
    while True:
      self.printInstructions()
      userChoice = input('What would you like to do?\n')

      if userChoice == 'exit':
        print('Good bye')
        break

      elif userChoice == 'quiz':

        if len(self.cardSet) >= 2:
          # Create quiz instance and start the interactive quizzer
          quiz = Quizzer(self.cardSet)
        else:
          print('You need at least 2 cards to be able to quiz yourself')

      elif userChoice == 'view':
        self.viewCards()

      elif userChoice == 'add':
        self.addCard()
        
      elif userChoice == 'delete':
        if len(self.cardSet) == 0:
          print('There are no cards to delete')
        else:
          self.deleteCard()

      elif userChoice == 'update':
        if len(self.cardSet) == 0:
          print('There are no cards to update')
        else:
          self.updateCard()
          
      else:
        print('This command is not recognized, please try again')

  def printInstructions(self):
    print('''
  To add: use "add"
  To view all cards: use "view"
  To delete: use "delete"
  To update use "update"
  To quiz yourself type "quiz"
  To exit, use "exit"
    ''')

  # User can delete a card based on the dictionaries index
  def deleteCard(self):
    while True:
      self.viewCards()
      cardToDelete = input('Enter the card ID to delete it. Type :cancel to cancel\n')

      if cardToDelete == ':cancel':
        break

      elif(self.checkForCard(cardToDelete)):
        del self.cardSet[cardToDelete]
        print('\nCard Deleted!\n')
        break
    
      else:
        print('\nCard with this ID does not exist\n')

  # User can update a card based on dictionary index if it exists
  def updateCard(self):

    while True:
      self.viewCards()
      cardToUpdate = input('Enter the card ID to update it. Type :cancel to cancel\n')

      if cardToUpdate == ':cancel':
        break
  
      elif(self.checkForCard(cardToUpdate)):

        # Prompt question
        print('\nCurrent Question: ' + self.cardSet[cardToUpdate]['question'])
        newQuestion = input('What is your new question? Enter nothing to leave it as is.\n')

        if(len(newQuestion) == 0):
          newQuestion = self.cardSet[cardToUpdate]['question']

        # Prompt Answer
        print('\nCurrent Answer: ' + self.cardSet[cardToUpdate]['answer'])
        newAnswer = input('What is your new answer? Enter nothing to leave it as is.\n')

        if(len(newAnswer) == 0):
          newAnswer = self.cardSet[cardToUpdate]['answer']

        # Update the dictionary with the new values
        self.cardSet[cardToUpdate]['question'] = newQuestion
        self.cardSet[cardToUpdate]['answer'] = newAnswer
        print('\nCard Updated!')
        break
        
      else:
        print('\nCard with this ID does not exist\n')

  # User can add a card or cancel the creation to go back to main prompt
  def addCard(self):
    print('To cancel a card, type :cancel for the question or answer')

    while True:
      # get card question
      cardQuestion = input('\nChoose the question for your card\n')

      if cardQuestion == ':cancel':
        break

      # get card answer
      cardAnswer = input('Choose the answer for your card\n')
      
      if cardAnswer == ':cancel':
        break

      # Check if the conditions pass, if so then add the card. Else, the user needs to try again
      if len(cardAnswer) > 0 and len(cardQuestion) > 0:
        self.addCardToDictionary(cardQuestion, cardAnswer)
        break
      else:
        print('\nYour question or answer cannot be empty')

  # Add the card to the dictionary and give it a inique referable ID
  def addCardToDictionary(self, question, answer):
    cardId = 'card-' + uuid.uuid4().hex[:4]
    self.cardSet[cardId] = {
      'question': question,
      'answer': answer
    }

    print('Card added!')

  # Check if a card with a given ID exists in the dictionary
  def checkForCard(self, cardId):
    for key in self.cardSet:
      if key == cardId:
        return True

    return False

  # Loop through all cards and display their attributes
  def viewCards(self):
    if len(self.cardSet) > 0:
      print('''\nYour Cards:\n---------------''')

      # Loop through each card
      for key, value in self.cardSet.items():
        print('''CardId: {}\nQuestion: {}\nAnswer: {} \n'''.format(key, value['question'], value['answer']))
    else:
      print('\nThere are no cards to view')

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

# Pass in initial data for testing, but also just to have default options for the user
biologyData = {
  'card1': {
    'question': 'What is the powerhouse of the cell?',
    'answer': 'Mitochondria'
  },
  'card2': {
    'question': 'What is the nucleus?',
    'answer': 'A nucleus, as related to genomics, is the membrane-enclosed organelle within a cell that contains the chromosomes. An array of holes, or pores, in the nuclear membrane allows for the selective passage of certain molecules (such as proteins and nucleic acids) into and out of the nucleus.'
  },
  'card3': {
    'question': 'A term used to describe a large, diverse group of eukaryotic, photosynthetic organisms.',
    'answer': 'Algae'
  },
  'card4': {
    'question': 'Collectively refers to all the processes of chemical reactions that build larger molecules out of smaller molecules or atoms;',
    'answer': 'Anabolism'
  }
}

# Initialize first CardSet and pass in test data
biology = CardSet(biologyData)
