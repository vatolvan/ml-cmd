from pprint import pprint
from PyInquirer import prompt

from sklearn.linear_model import LogisticRegression, LinearRegression

def train_model(data):
  questions = [
    {
      'type': 'list',
      'name': 'model_type',
      'message': 'Regression or Classification?',
      'choices': [
          'Regression',
          'Classification',
          'Exit'
      ]
    },
    {
      'type': 'list',
      'name': 'response_variable',
      'message': 'Select response variables. The rest are used as predictors',
      'choices': [c for c in list(data.columns)],
      'when': lambda answers: answers['model_type'] is not 'Exit'
    },
  ]

  answers = prompt(questions)

  if answers['model_type'] == 'Exit':
    return None

  resp = answers['response_variable']
  y = data[resp]
  X = data.drop(resp, axis=1)

  if answers['model_type'] == 'Regression':
    create_model = create_regression_model
  elif answers['model_type'] == 'Classification':
    create_model = create_binary_classifier

  model = create_model(X.values, y.values)

  print('Created model with coefficients: ')
  pprint(model.coef_)

  input('Press Enter to continue...')

  return model

def create_regression_model(X, y):
  model = LinearRegression()
  model.fit(X, y)
  return model

def create_binary_classifier(X, y):
  model = LogisticRegression(solver='lbfgs', multi_class='auto')
  model.fit(X, y)
  return model