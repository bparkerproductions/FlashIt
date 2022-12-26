import uuid
import random

exec(open('./app/cardSet.py').read())

exec(open('./app/quizzer.py').read())

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
