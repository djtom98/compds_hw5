import pandas as pd
from pandas.testing import assert_frame_equal
import unittest
from learnlibs.clean_data import *
from learnlibs.read_data import *
from learnlibs.generate_dummies import *
from learnlibs.split_data import *
from learnlibs.train_and_score import *

# def read_data(path: str):
#     '''
#     Read database.
    
#     Parameters: 
#         path: path to data
        
#     Returns:
#         df (dataframe): database in pandas format
#     '''
#     df = pd.read_csv(path, index_col=0)
#     return df

class Testreaddata(unittest.TestCase):
    pass

