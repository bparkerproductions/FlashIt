import uuid

class CardSet:
  # A card set is a deck of study cards that will contain multiple cards. It can be reviewed and studied
  def __init__(self, cardObj=False):
    
    # Create empty dictionary or passed in dictionary. This will be used to keep track of added cards
    if cardObj:
      self.cardSet = cardObj
    else:
      self.cardSet = {}
    
    print(self.styledMessage('Welcome to Flash It!', '#', 2))

    self.userChoice()

  # This is where the user can choose what action to do. Exit, quiz, add, delete, view, or update
  def userChoice(self):
    while True:
      self.printInstructions()
      userChoice = input('What would you like to do?\n')

      if userChoice == 'exit':
        print(self.styledMessage('Good bye'))
        break

      elif userChoice == 'quiz':

        if len(self.cardSet) >= 2:
          # Create quiz instance and start the interactive quizzer
          Quizzer(self.cardSet)
        else:
          print(self.styledMessage('You need at least 2 cards to be able to quiz yourself', '!'))

      elif userChoice == 'view':
        self.viewCards()

      elif userChoice == 'add':
        self.addCard()
        
      elif userChoice == 'delete':
        if len(self.cardSet) == 0:
          print(self.styledMessage('There are no cards to delete', '!'))
        else:
          self.deleteCard()

      elif userChoice == 'update':
        if len(self.cardSet) == 0:
          print(self.styledMessage('There are no cards to update', '!'))
        else:
          self.updateCard()
          
      else:
        print(self.styledMessage('This command is not recognized, please try again', '!'))

  def printInstructions(self):
    print('''
----------------------------------
|  To add: use "add"             |
|  To view all cards: use "view" |
|  To delete: use "delete"       |
|  To update use "update"        |
|  To quiz yourself type "quiz"  |
|  To exit, use "exit"           |
----------------------------------
    ''')

  # User can delete a card based on the dictionaries index
  def deleteCard(self):
    self.viewCards()
    
    while True:
      cardToDelete = input(self.styledMessage('Enter the card ID to delete it. Type :cancel to cancel', '-') + '\n')

      if cardToDelete == ':cancel':
        break

      elif(self.checkForCard(cardToDelete)):
        del self.cardSet[cardToDelete]
        print('\n' + self.styledMessage('Card Deleted!', '=') + '\n')
        break
    
      else:
        print('\n' + self.styledMessage('Card with this ID does not exist', '!') + '\n')

  # User can update a card based on dictionary index if it exists
  def updateCard(self):
    self.viewCards()

    while True:
      cardToUpdate = input(self.styledMessage('Enter the card ID to update it. Type :cancel to cancel') + '\n')

      if cardToUpdate == ':cancel':
        break
  
      elif(self.checkForCard(cardToUpdate)):

        # Prompt question
        print('\nCurrent Question: ' + self.cardSet[cardToUpdate]['question'])
        newQuestion = input(self.styledMessage('What is your new question? Enter nothing to leave it as is.', '-') + '\n')

        if(len(newQuestion) == 0):
          newQuestion = self.cardSet[cardToUpdate]['question']

        # Prompt Answer
        print('\nCurrent Answer: ' + self.cardSet[cardToUpdate]['answer'])
        newAnswer = input(self.styledMessage('What is your new answer? Enter nothing to leave it as is.', '-') + '\n')

        if(len(newAnswer) == 0):
          newAnswer = self.cardSet[cardToUpdate]['answer']

        # Update the dictionary with the new values
        self.cardSet[cardToUpdate]['question'] = newQuestion
        self.cardSet[cardToUpdate]['answer'] = newAnswer
        print('\n' + self.styledMessage('Card Updated!', '='))
        break
        
      else:
        print('\n' + self.styledMessage('Card with this ID does not exist', '!') + '\n')

  # User can add a card or cancel the creation to go back to main prompt
  def addCard(self):

    print(self.styledMessage('To cancel a card, type :cancel for the question or answer'))

    while True:
      # get card question
      cardQuestion = input('\n' + self.styledMessage('Choose the question for your card:', '-') + '\n')

      if cardQuestion == ':cancel':
        break

      # get card answer
      cardAnswer = input(self.styledMessage('Choose the answer for your card:', '-') + '\n')
      
      if cardAnswer == ':cancel':
        break

      # Check if the conditions pass, if so then add the card. Else, the user needs to try again
      if len(cardAnswer) > 0 and len(cardQuestion) > 0:
        self.addCardToDictionary(cardQuestion, cardAnswer)
        break
      else:
        print('\n' + self.styledMessage('Your question or answer cannot be empty', '!', 1))

  # Add the card to the dictionary and give it a inique referable ID
  def addCardToDictionary(self, question, answer):
    cardId = 'card-' + uuid.uuid4().hex[:4]
    self.cardSet[cardId] = {
      'question': question,
      'answer': answer
    }

    print(self.styledMessage('Card added!', '='))

  # Check if a card with a given ID exists in the dictionary
  def checkForCard(self, cardId):
    for key in self.cardSet:
      if key == cardId:
        return True

    return False

  # Loop through all cards and display their attributes
  def viewCards(self):
    printFormat = '''
-----------------------------------\n
CardId: {}
Question: {}
Answer: {} \n 
-----------------------------------
    '''

    if len(self.cardSet) > 0:
      print(self.styledMessage('Your Cards:', '-'))

      # Loop through each card
      for key, value in self.cardSet.items():
        print(printFormat.format(key, value['question'], value['answer']))
    else:
      print('\n' + self.styledMessage('There are no cards to view', '!'))

  # Take a boring instructional prompt and give it a specified border and spacing
  def styledMessage(self, message, style='*', spaces=1):
    finalMessage = ''
    finalMessage += style * (len(message) + 8)
    if spaces:
      finalMessage += ('\n|   ' + len(message) * ' ' + '   |') * spaces

    finalMessage += '\n|   ' + message + '   |\n'

    if spaces:
      finalMessage += ('|   ' + len(message) * ' ' + '   |\n') * spaces

    finalMessage += style * (len(message) + 8)
    return finalMessage