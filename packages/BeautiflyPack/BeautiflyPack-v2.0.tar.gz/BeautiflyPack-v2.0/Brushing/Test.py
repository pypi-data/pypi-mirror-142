import pandas as pd
import numpy as np
from datetime import datetime, date
from sklearn import preprocessing

from Github.Beautifly.Brushing as bd 

""" from Github.Beautifly.Brushing.BrushingDataframe import _scan
from Github.Beautifly.Brushing.BrushingDataframe import cleaning_missing
from Github.Beautifly.Brushing.BrushingDataframe import recommended_transformation
from Github.Beautifly.Brushing.BrushingDataframe import convert_column_to_date
from Github.Beautifly.Brushing.BrushingDataframe import lable_Encode_Columns
from Github.Beautifly.Brushing.BrushingDataframe import apply_min_max
from Github.Beautifly.Brushing.BrushingDataframe import apply_standarScaler
from Github.Beautifly.Brushing.BrushingDataframe import apply_SimpleImputer
from Github.Beautifly.Brushing.BrushingDataframe import _scan_observations
from Github.Beautifly.Brushing.BrushingDataframe import _test_for_normality
from Github.Beautifly.Brushing.BrushingDataframe import convert_birthdate_age
from Github.Beautifly.Brushing.BrushingDataframe import get_missing_values_table
from Github.Beautifly.Brushing.BrushingDataframe import find_correlated_features
from Github.Beautifly.Brushing.BrushingDataframe import tukeys_method
from Github.Beautifly.Brushing.BrushingDataframe import get_missing_values_table
from Github.Beautifly.Brushing.BrushingDataframe import get_missing_values_table """


def SetAttributes():
    data = {'ACCOUNT_NUMBER': [1, np.nan, 7, 66, np.nan], 
        'LOAN_OPEN_DATE': ['2016-01-28', '2012-04-08', '2014-11-28', '2017-05-21', '2019-02-18'], 
        'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'HOUSEWIFE', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = bd.SetAttributes(df, drop = True)
    assert df.shape[1] == 5
    
"""     
def _scan():
    data = {'ACCOUNT_NUMBER': [1, np.nan, 7, 66, np.nan], 
        'LOAN_OPEN_DATE': ['2016-01-28', '2012-04-08', '2014-11-28', '2017-05-21', '2019-02-18'], 
        'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'HOUSEWIFE', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df =  _scan(df, drop = True)
    assert df.shape[1] 

def cleaning_missing():
    data = {'ACCOUNT_NUMBER': [1, np.nan, 7, 66, np.nan], 
        'LOAN_OPEN_DATE': ['2016-01-28', '2012-04-08', '2014-11-28', '2017-05-21', '2019-02-18'], 
        'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'HOUSEWIFE', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = cleaning_missing(df, drop = True)
    assert df.shape[1]
    
    
def SetAttributes_4():
    data = {'ACCOUNT_NUMBER': [1, np.nan, 7, 66, np.nan], 
        'LOAN_OPEN_DATE': ['2016-01-28', '2012-04-08', '2014-11-28', '2017-05-21', '2019-02-18'], 
        'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'HOUSEWIFE', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = recommended_transformation(df, drop = True)
    assert df.shape[1] 
    
   
def lable_Encode_Columns():
    data = { 'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'Manager', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = lable_Encode_Columns(df, drop = True)
    assert df.shape[1] 
        
        
def lable_Encode_Columns():
    data = { 'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'Manager', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = lable_Encode_Columns(df, drop = True)
    assert df.shape[1] 
        
        
def lable_Encode_Columns():
    data = { 'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'Manager', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = lable_Encode_Columns(df, drop = True)
    assert df.shape[1]         
              
def lable_Encode_Columns():
    data = { 'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'Manager', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = lable_Encode_Columns(df, drop = True)
    assert df.shape[1]        
        
        
def lable_Encode_Columns():
    data = { 'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'Manager', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = lable_Encode_Columns(df, drop = True)
    assert df.shape[1]       
              
def lable_Encode_Columns():
    data = { 'PROFESSION': ['Shop Owner', 'Manager', 'Company Owner', 'Manager', 'EMPLOYEE']}
    df = pd.DataFrame(data)
    df = lable_Encode_Columns(df, drop = True)
    assert df.shape[1]      """