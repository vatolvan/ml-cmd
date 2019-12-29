from pprint import pprint
from PyInquirer import prompt

from sklearn import linear_model

def train_model(data):
  questions = [
    {
      'type': 'list',
      'name': 'model_type',
      'message': 'Regression or Classification?',
      'choices': [
          'Regression',
          {
            'name': 'Classification (Binary)',
            'disabled': 'Not implemented'
          },
          {
            'name': 'Classification (Multiclass)',
            'disabled': 'Not implemented'
          },
          'Exit'
      ]
    },
    {
      'type': 'list',
      'name': 'response_variable',
      'message': 'Select response variables. The rest are used as predictors',
      'choices': [c for c in list(data.columns)],
    },
  ]

  answers = prompt(questions)

  if answers['model_type'] == 'Exit':
    return None

  resp = answers['response_variable']
  y = data[resp]
  X = data.drop(resp, axis=1)

  model = create_regression_model(X, y)

  print('Created model with coefficients: ')
  pprint(model.coef_)

  input('Press Enter to continue...')

  return model

def create_regression_model(X, y):

  reg = linear_model.LinearRegression()
  reg.fit(X, y)

  return reg
