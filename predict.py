from pprint import pprint
from PyInquirer import prompt
from sklearn.metrics import mean_squared_error, r2_score

from open_file import open_file

def predict(model):
  print('Load test data')
  test_data = open_file()

  questions = [
    {
      'type': 'list',
      'name': 'response_variable',
      'message': 'Select response variables. The rest are used to do the predictions.',
      'choices': [c for c in list(test_data.columns)],
    },
  ]

  answers = prompt(questions)

  resp = answers['response_variable']
  if (resp is not None):
    y_test = test_data[resp]

  X_test = test_data.drop(resp, axis=1)
  y_pred = model.predict(X_test)

  print('Mean squared error: %.2f' % mean_squared_error(y_test, y_pred))
  print('Coefficient of determination: %.2f' % r2_score(y_test, y_pred))

  questions = [
    {
      'type': 'confirm',
      'name': 'save_data',
      'message': 'Save predictions?',
    },
    {
      'type': 'input',
      'name': 'output_file',
      'message': 'File to save',
      'when': lambda answers: answers['save_data']
    },
  ]

  answers = prompt(questions)

  if (answers['save_data']):
    X_test[resp] = y_pred
    X_test.to_csv(answers['output_file'], index=False)
    print('Saved predictions to %s' % answers['output_file'])

  input('\nPress Enter to continue...')