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
        print('Good bye')
        break

      elif userChoice == 'quiz':

        if len(self.cardSet) >= 2:
          # Create quiz instance and start the interactive quizzer
          Quizzer(self.cardSet)
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
    cancelMessage = self.styledMessage('''
**************************************
|   To cancel a card, type :cancel   |
|   for the question or answer       |
**************************************
''')

    questionPromptText = self.styledMessage('''
*****************************************
|   Choose the question for your card:  |
*****************************************
  ''')

    answerPromptText = self.styledMessage('''
***************************************
|   Choose the answer for your card   |
***************************************
  ''')

    print(cancelMessage)

    while True:
      # get card question
      cardQuestion = input(questionPromptText)

      if cardQuestion == ':cancel':
        break

      # get card answer
      cardAnswer = input(answerPromptText)
      
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

  # Take a boring instructional prompt and give it a specified border and spacing
  def styledMessage(self, message, style='*', spaces=0):
    finalMessage = ''
    finalMessage += style * (len(message) + 8)
    if spaces:
      finalMessage += ('\n|   ' + len(message) * ' ' + '   |') * spaces

    finalMessage += '\n|   ' + message + '   |\n'

    if spaces:
      finalMessage += ('|   ' + len(message) * ' ' + '   |\n') * spaces

    finalMessage += style * (len(message) + 8)
    return finalMessage