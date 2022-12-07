class CardSet:
  # A card set is a deck of study cards that will contain multiple cards. It can be reviewed and studied
  def __init__(self):
    # Create empty dictionary, this will be used to keep track of added cards
    cardSet = {}
    self.printInstructions()

  def printInstructions(self):
    print('''
    Welcome to Flash It! 
    To add: use "add"
    To delete: use "delete"
    To update use "update"
    ''')

biology = CardSet()
