from pprint import pprint

from PyInquirer import prompt
from PyInquirer import Validator, ValidationError, Separator

def preprocess(data):
  questions = [
    {
        'type': 'confirm',
        'message': 'Remove rows with NaN values?',
        'name': 'remove_nan',
        'default': True,
    },
    {
        'type': 'checkbox',
        'name': 'drop_columns',
        'message': 'Which columns do you want to drop from data? (Press Enter to continue)',
        'choices': [{"name": c} for c in list(data.columns)],
    },
  ]

  answers = prompt(questions)

  pprint(answers)

  if answers['remove_nan']:
    data = remove_nan(data)

  if len(answers['drop_columns']) > 0:
    data = drop_columns(data, answers['drop_columns'])


  input("Preprocessed data successfully, press Enter to continue...")

  return data

def remove_nan(data):
  print("Removing rows with NaN values...")
  data = data.dropna() # removes rows with any NaN values
  data = data.reset_index(drop=True) # reset's row indexes in case any rows were dropped
  return data

def drop_columns(data, columns):
  print("Dropping columns: ")
  pprint(columns)
  data = data.drop(columns, axis=1)
  return data