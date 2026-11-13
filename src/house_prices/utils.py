'''
Utility functions to be used to help the prediction task
'''

# Import libraries
import numpy as np
import pandas as pd
from pathlib import Path

PATH = Path('/Users/alp/Projects/House Prices/data')

def load_datasets(train_path = PATH / 'train.csv', test_path = PATH / 'test.csv') -> tuple[pd.DataFrame, pd.DataFrame]:
    train = pd.read_csv(train_path)
    test = pd.read_csv(test_path)
    return train, test