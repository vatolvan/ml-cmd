# -*- coding: utf-8 -*-

from __future__ import print_function, unicode_literals
import regex

from pprint import pprint
from PyInquirer import prompt

from open_file import open_file
from describe_data import display_data
from preprocess import preprocess
from train_model import train_model
from predict import predict
import actions

def run():
  data = None
  model = None

  while True:
    questions = [
      {
        'type': 'list',
        'name': 'action',
        'message': 'What do you want to do?',
        'choices': [
            actions.LOAD_DATA,
            {
              'name': actions.DISPLAY_DATA,
              'disabled': 'Load data first' if data is None else False
            },
            {
              'name': actions.PREPROCESS_DATA,
              'disabled': 'Load data first' if data is None else False
            },
            {
              'name': actions.TRAIN_MODEL,
              'disabled': 'Load data first' if data is None else False
            },
            {
                'name': actions.PREDICT,
                'disabled': 'Create model first' if model is None else False
            },
            actions.EXIT
        ]
      },
    ]

    answers = prompt(questions)

    if answers['action'] == actions.LOAD_DATA:
      data = open_file()
    elif answers['action'] == actions.DISPLAY_DATA:
      display_data(data)
    elif answers['action'] == actions.PREPROCESS_DATA:
      data = preprocess(data)
    elif answers['action'] == actions.TRAIN_MODEL:
      model = train_model(data)
    elif answers['action'] == actions.PREDICT:
      predict(model)
    elif answers['action'] == actions.EXIT:
      return
