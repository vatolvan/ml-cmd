from pprint import pprint
from PyInquirer import prompt
from PyInquirer import Validator, ValidationError

import pandas as pd

def open_file():
  questions = [
      {
          'type': 'input',
          'name': 'file_name',
          'message': 'Path to CSV file',
          'validate': lambda text: len(text) > 0 or 'Must not be empty',
      },
      {
          'type': 'input',
          'name': 'delimiter',
          'message': 'Delimiter?',
          'validate': lambda text: len(text) > 0 or 'Must not be empty',
          'default': ';'
      },
      {
          'type': 'input',
          'name': 'n_headers',
          'message': 'Number of header rows?',
          'validate': lambda text: text.isdigit() or 'Must not be empty and an integer number',
          'default': '1'
      }
  ]

  answers = prompt(questions)
  file_name = answers['file_name']
  delimiter = answers['delimiter']
  n_headers = int(answers['n_headers'])
  print("Trying to open file: " + file_name + ", with delimiter '" + delimiter + "' and " + str(n_headers) + " header rows")

  header = list(range(0, n_headers))

  df = pd.read_csv(file_name, header=header, delimiter=delimiter)

  input("Loaded data successfully, press Enter to continue...")

  return df