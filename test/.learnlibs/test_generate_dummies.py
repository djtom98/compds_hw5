import pandas as pd

import unittest
from pandas.testing import assert_frame_equal

from learnlibs.clean_data import *
from learnlibs.read_data import *
from learnlibs.generate_dummies import *
from learnlibs.split_data import *
from learnlibs.train_and_score import *
# def gen_ohe(df: pd.DataFrame, cols: list):
#     '''
#     Generate dummies using one hot encoding.
    
#     Parameters: 
#         df (dataframe): dataframe to generate one hot encoding dummies for
#         cols (list): list of columns to generate dummies
        
#     Returns:
#         dummies_df: dataframe with dummy column added
#     '''
#     dummies_df = pd.get_dummies(df, columns=cols)
#     return dummies_df

class TestCleanData(unittest.TestCase):
    def test_gen_ohe_cols(self):
        data=pd.DataFrame({'col1':[1,2,3,4,5]})
        expected_output=['col1_1','col1_2','col1_3','col1_4','col1_5']
        output=gen_ohe(data,['col1']).columns.tolist()
        self.assertEqual(expected_output,output)

    def test_gen_ohe_cols(self):
        data=pd.DataFrame({'col1':[1,2,3,4,5]})
        expected_output=pd.DataFrame({'col1':[1,2,3,4,5],'col2_2':[1,0,0,0,0],'col1_3':[0,1,0,0,0]})
        ['col1_1','col1_2','col1_3','col1_4','col1_5']

        output=gen_ohe(data,['col1']).columns.tolist()
        self.assertEqual(expected_output,output)



# a=TestCleanData()
# a.test_gen_ohe_cols()

        



# def gen_binary(df: pd.DataFrame, cols: list):
#     '''
#     Generate binary dummies.
    
#     Parameters: 
#         df (dataframe): dataframe to generate binary dummies for
#         cols (list): list of columns to generate dummies
        
#     Returns:
#         dummies_df: dataframe with dummy column added
#     '''
#     dummies_df = pd.get_dummies(df, columns=cols)
#     return dummies_df
    