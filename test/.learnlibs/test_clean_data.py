import pandas as pd
import numpy as np
import unittest
from pandas.testing import assert_frame_equal

from learnlibs.clean_data import *
from learnlibs.read_data import *
from learnlibs.generate_dummies import *
from learnlibs.split_data import *
from learnlibs.train_and_score import *
# def drop_nan(df: pd.DataFrame, cols: list):
#     '''
#     Remove those rows that contain NaN values in the given columns.
    
#     Parameters: 
#         df (dataframe): dataframe to remove rows for
#         cols (list): target columns to remove rows for
        
#     Returns:
#          cleaned_df: dataframe with removed rows in target columns
#     '''
#     cleaned_df = df.dropna(axis=0, subset=cols, how='any')
#     return cleaned_df

class TestCleanData(unittest.TestCase):
    def test_drop_nan(self):
        data=pd.DataFrame({'col1':[1,2,3,4,5,np.nan]})
        # print(data)
        expected_output=pd.DataFrame({'col1':[1,2,3,4,5]})
        output=drop_nan(data,['col1'])
        assert_frame_equal(output,expected_output,check_dtype=False)

    def test_fill_nan(self):
        data=pd.DataFrame({'col1':[1,2,3,4,5,np.nan]})
        expected_output=pd.DataFrame({'col1':[1,2,3,4,5,3]})
        output=fill_nan(data,['col1'])
        assert_frame_equal(output,expected_output,check_dtype=False)


a=TestCleanData()
a.test_drop_nan()




# def fill_nan(df: pd.DataFrame, cols: list):
#     '''
#     Fill NaN with the mean value of the column in the given columns.
    
#     Parameters: 
#         df (dataframe): dataframe to fill NaNs for
#         cols (list): target columns to fill NaNs for
        
#     Returns:
#         df: dataframe with filled NaN in target columns
#     '''
#     df[cols] = df[cols].fillna(df.mean().iloc[0])
#     return df 
    