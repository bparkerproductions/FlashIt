class CardSet:
  # A card set is a deck of study cards that will contain multiple cards. It can be reviewed and studied
  def __init__(self):
    # Create empty dictionary, this will be used to keep track of added cards
    cardSet = {}

    self.userChoice()

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
    Welcome to Flash It! 
    To add: use "add"
    To delete: use "delete"
    To update use "update"
    To exit, use "exit"
    ''')

  def deleteCard(self):
    print('Choose a card to delete')

  def updateCard(self):
    print('Choose a card to update')

  def addCard(self):
    print('Choose a card to add')

biology = CardSet()
