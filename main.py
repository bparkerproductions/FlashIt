class CardSet:
  # A card set is a deck of study cards that will contain multiple cards. It can be reviewed and studied
  def __init__(self):
    # Create empty dictionary, this will be used to keep track of added cards
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

      elif userChoice == 'add':
        self.addCard()
        
      elif userChoice == 'delete':
        if len(cardSet) == 0:
          print('There are no cards to delete')
        else:
          self.deleteCard()

      elif userChoice == 'update':
        if len(cardSet) == 0:
          print('There are no cards to update')
        else:
          self.updateCard()
          
      else:
        print('This command is not recognized, please try again')

  def printInstructions(self):
    print('''
    To add: use "add"
    To delete: use "delete"
    To update use "update"
    To exit, use "exit"
    ''')

  # User can delete a card based on the dictionaries index
  def deleteCard(self):
    print('Choose a card to delete')

  # User can update a card based on dictionary index if it exists
  def updateCard(self):
    print('Choose a card to update')

  # User can add a card or cancel the creation to go back to main prompt
  def addCard(self):
    print('To cancel a card, type :cancel for the question or answer')

    while True:
      # get card question
      cardQuestion = input('Choose the question for your card')

      if cardQuestion == ':cancel':
        break

      # get card answer
      cardAnswer = input('Choose the answer for your card')
      
      if cardAnswer == ':cancel':
        break

      # Check if the conditions pass, if so then add the card. Else, the user needs to try again
      if len(cardAnswer) > 0 and len(cardQuestion) > 0:
        self.addCardToDictionary(cardQuestion, cardAnswer)
        break
      else:
        print('Your question or answer cannot be empty')

  # Add the card to the dictionary and give it a inique referable ID
  def addCardToDictionary(self, question, answer):
    cardId = 'card' + str(len(self.cardSet)+1)
    self.cardSet[cardId] = {
      'question': question,
      'answer': answer
    }

    print('Card added!')

biology = CardSet()
