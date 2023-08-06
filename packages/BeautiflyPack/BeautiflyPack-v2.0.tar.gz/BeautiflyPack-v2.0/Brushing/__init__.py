# -*- coding: utf-8 -*-
"""
Created on Fri Aug  6 22:49:01 2021

@author: Nicolas Ponte
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from datetime import datetime, date
from sklearn import preprocessing
from sklearn.impute import SimpleImputer


class BrushingDataframe(pd.DataFrame):
    """
    The class is used to extend the properties of Dataframes to a prticular
    type of Dataframes in the Risk Indistry. 
    It provides the end user with both general and specific cleaning functions, 
    though they never reference a specific VARIABLE NAME.
    
    It facilitates the End User to perform some Date Feature Engineering,
    Scaling, Encoding, etc. to avoid code repetition.
    
    """

    # a dictionary to save the labels names of encorded columns. contains column name and array of names. 
    column_labels={}

    #Initializing the inherited pd.DataFrame
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
    
    @property
    def _constructor(self):
        def func_(*args,**kwargs):
            df = BrushingDataframe(*args,**kwargs)
            return df
        return func_
    
#-----------------------------------------------------------------------------
                        # DATA HANDLING
#-----------------------------------------------------------------------------

    def SetAttributes(self, kwargs):
        """
        The function will update the type of the variable submitted for change.
        It will veify first that the key is present in the desired dataframe.
        If present, it will try to change the type to the desired format.
        If not possible, it will continue to the next element.         
        Parameters
        ----------
        **kwargs : The key-argument pair of field-type relationship that
        wants to be updated.
        Returns
        -------
        None.
        """
        if self.shape[0] > 0:
            for key,vartype in kwargs.items():
                if key in self.columns:
                    try:
                        self[key] = self[key].astype(vartype)
                    except:
                        print("Undefined type {}".format(str(vartype)))
                else:
                    print("The dataframe does not contain variable {}.".format(str(key)))
        else:
            print("The dataframe has not yet been initialized")

#-----------------------------------------------------------------------------
                        # SUPERVISED - BINARY CLASSIFICATION - DATA CLEANING
#-----------------------------------------------------------------------------    
    def _scan(self, input_var): 
        ''' 
        private scan function to scan the current datafarme features for missing values and returns basic informaiton about the feature in addition to some treatment recommendations. 
        --------------------
        Arguments:
        - input_var (array): list of feature the user would like to scan
        --------------------
        Returns:
        - dictionary of basic information and recommendations

        --------------------
        
        '''
        
        
        dict ={}
        
        for x in input_var: 
            recom = {}
            recom['unique_count']=self[x].nunique()
            recom['Missing_Count']=self[x].isnull().sum()
            recom['Portion_Missing']="{0:.00%}".format(recom['Missing_Count']/self[x].count())
            recom['type']=self[x].dtype
            recom['Recommend_Treatment_for_missing_values'] = "Drop: >%20 are missing" if recom['Missing_Count']/self[x].count()>20 else "impute <%20 are missing"
            recom["Normality Test"]=self._test_for_normality(x)
            recom["Number of outliers"]= len(self.tukeys_method(x)[1])
            
            dict[x]=recom

        #report number of observation with 20% of missing features

        dict['Observations with missing features'] = self._scan_observations()

        # report corrlated features

        dict["Correlated_features"] =self.find_correlated_features()

        
        return dict 

    
    

    
    def scan(self, input_var=[]):
        '''
        scans the current datafarme features for missing values and returns basic informaiton about the feature in addition to some treatment recommendations. 
        --------------------
        Arguments:
        - input_var (array): list of feature the user would like to scan
        --------------------
        Returns:
        - dictionary of basic information and recommendations

        --------------------
        
        '''
        if len(input_var)==0: 
            return self._scan(list(self.columns))
        else: 
            return self._scan(input_var)


    def cleaning_missing(self,target, input_vars=[], threshold=0.2 ):
        """
        data cleaning function that performs teh following steps to clean the dataset: 
            * remove all duplicates from the whole data sets
            * remove observation that has missing features of 20% by default or as set by the user using the threshold parameter. 
            * it analyzes each column to the check the possiblity of dropping this columns if the percentage of missing data is more than
              the threshold. 
            * it perform imputation based on mean or meadian for numeric variable or the mode for categorical variables. 
                
            --------------------
            Arguments:
            - input_var (array): list of feature the user would like to check messings values
            --------------------
            Returns:
            - cleaned dataset

            --------------------

        """
        self.drop_duplicates(inplace=True)
        
        # remove observations excceeding the threshod 
        index = self[self.isna().sum(axis=1)/len(self.columns)*100 > threshold].index
        self.drop(index, inplace=True)

        # iterate over the columns to drop columns exceeding the threshold. 
        vars = input_vars
        
        if len(vars) ==0: 
            vars = self.columns
        
        vars=vars.drop(target)
        for x in vars: 
            missing=self[x].isnull().sum()/self[x].count()*100
            
            if missing>threshold: 
                self.drop(x, inplace=True)

        # After droping columns removing missing observation, now impute null values based on their type: 


        for col in vars:
            if self[col].dtype.name in ['int64', 'float64']:
                
                self.apply_SimpleImputer([col])

            else:
                self.apply_SimpleImputer([col], strategy='constant', fill_value="Unknown")

        
        return self
 
    def recommended_transformation(self,target, input_vars=[],  ):
        """
        data preparation (for each column provide methods to perform
        transformations - for example: time calculation like age, days as customers, 
        days to due date, label encoding, imputation, standard scalling, dummy creation 
        or replacement of category value by its probability of default depending, justify 
        transformation depending of the variable type, or explain why transformation is 
        not necessary);

        Returns
        -------
          Dataframe               
        """
        
        vars= input_vars

        if len(vars)==0:
            vars=self.columns

        vars=vars.drop(target)
        for col in vars:
            if self[col].dtype.name in ['int64', 'float64']:
                self.apply_min_max([col])

            elif self[col].dtype.name in ['datetime64[ns]']:
                self.convert_date_to_days(col)

            else:
                self.lable_Encode_Columns([col])

    
        return self
    
#-----------------------------------------------------------------------------
                        # Additional functions
#-----------------------------------------------------------------------------    
    def convert_column_to_date(self,input_var=[]):
        """
        basic function to confert a column into a date 
                
            --------------------
            Arguments:
            - input_var (array): list of feature the user would like to convert into dates
            --------------------
            Returns:
            a message to indicate the conversion is successful or not

            --------------------

        """
        try: 
            for var in input_var:
                self[var]=np.vectorize(lambda x: datetime.strptime(x, "%Y-%m-%d").date()) (self[var])

            return "successfully converted all variables"
        except Exception as ex:
            return ex


    def lable_Encode_Columns(self, vars): 
        """
            a function to encode the column into numbers using the label enconder
                
            --------------------
            Arguments:
            - input_var (array): list of columns
            --------------------
            Returns:
            - None

            --------------------

        """

        if len(vars) !=0:
            for var in vars: 
                le = preprocessing.LabelEncoder()
                self[var] =le.fit_transform(self[var])
                self.column_labels[var]=le.classes_


    def apply_min_max(self, vars): 
        """
            a function to encode the column into numbers using the min_max scaler
                
            --------------------
            Arguments:
            - input_var (array): list of columns
            --------------------
            Returns:
            - None

            --------------------

        """

        if len(vars) !=0:
            for var in vars: 
                mx = preprocessing.MinMaxScaler()
                self[var] =mx.fit_transform(self[var].to_numpy().reshape(-1, 1))

    def apply_standarScaler(self, vars): 
        """
            a function to encode the column into numbers using the standardScaler
                
            --------------------
            Arguments:
            - input_var (array): list of columns
            --------------------
            Returns:
            - None

            --------------------

        """

        if len(vars) !=0:
            for var in vars: 
                ss = preprocessing.StandardScaler()
                self[var] =ss.fit_transform(self[var].to_numpy().reshape(-1, 1))

    def apply_SimpleImputer(self, vars, missing_values=np.nan, strategy='mean', fill_value="Unknown"): 
        """
            a function to encode the column into numbers using the SimpleImputer
                
            --------------------
            Arguments:
            - input_var (array): list of columns
            --------------------
            Returns:
            - None

            --------------------

        """
        if len(vars) !=0:
            for var in vars: 
                if self[var].dtype.name != 'datetime64[ns]': 
                    si = SimpleImputer(missing_values=missing_values, strategy=strategy, fill_value=fill_value)
                    self[var] =si.fit_transform(self[var].to_numpy().reshape(-1, 1))


    def _scan_observations(self): 
        """
            a function to identify the number of observation with 20% of missing columns
                
            --------------------
            Arguments:
            - None
            --------------------
            Returns:
            - number of observations

            --------------------

        """
        num = ((self.isna().sum(axis=1)/len(self.columns)*100) > 20).sum()

        return num

    
    def _test_for_normality(self, var, alpha=0.05): 
        '''
        a private method to test for normality of numeric variable using Shapior test. 
        Test whether a sample differs from a normal distribution.
        This function tests the null hypothesis that a sample comes from a normal distribution. 
        It is based on D'Agostino and Pearson's test that combines skew and kurtosis to produce an omnibus test of normality.

        --------------------
        Arguments:
        - var (string): the column name
        - var(float): the threshold of the alpha based on the confidency internval. Default value is 0.05
        --------------------
        Returns:
        - string indicating if the variable is normally distributed or not.
        --------------------
        
        '''
        try:
            if self[var].dtype in ['int64', 'float64']:
                    
                _, p = stats.normaltest(self[var])

                if p> alpha: 
                    return "the data is normal, recommended imputation method is: the mean"
                else: 
                    return "the data failed the nomality test, recommended imputation method is: Median, transformation using log, minmax, and power transforamtion."
            else: 
                return "the variable is not numeric, use the mode"
        except: 
            return "the variable is not numeric, use the mode"



    def convert_birthdate_age(self, BD_column):
        """
            a function to convert the birthdate into age in years
                
            --------------------
            Arguments:
            - input_var : column name
            --------------------
            Returns:
            - dataframe

            --------------------

        """
        df = self
        df["AGE"] = df[BD_column].apply(lambda x : (pd.datetime.now().year - x.year)).astype(int)
        df.drop(BD_column, axis=1, inplace=True)
        return df

    def convert_date_to_days(self, BD_column):
        """
            a function to convert the a date column into days

            --------------------
            Arguments:
            - input_var : column name
            --------------------
            Returns:
            - dataframe

            --------------------

        """
        df = self
        df[BD_column] = df[BD_column].apply(lambda x : (pd.datetime.now().day - x.day)).astype(int)
        
        return df    
        
    def find_correlated_features(self, cutoff = 0.8):
        '''
        Finds features that have a pairwise Pearson correlation exceeding a specified threshold. For each pair of features, only one feature is returned.
        --------------------
        Arguments:
        - cutoff (float): correlation threshold
        - method (string): correlation type: 'pearson', 'spearman' or both
        --------------------
        Returns:
        - list of correlated features
        --------------------
        
        '''
        # extract numeric features
        df=self 
        numerics = [col for col in df.columns if df[col].dtype != 'object']
        df = df[numerics]

        # compute correlations
        corr_matrix = df.corr().abs()
        
        # transform to lower triangle
        corr_lower = corr_matrix.where(np.tril(np.ones(corr_matrix.shape), k = -1).astype(np.bool))

        # remove features
        features = [col for col in corr_lower.columns if any(corr_lower[col] > cutoff)]

        # return results
        if len(features) > 0:
            print()
            return 'Found {} correlated features.'.format(len(features)) + str(features)
        else:
            return 'No correlated features found.'


    def tukeys_method(self, var):
        '''
        a function uses tukey's method to detects outliers and return a tuple containing the index and the value of the outliers in the passed column. 
        --------------------
        Arguments:
        - var (string): the name of the column to examine. 
        
        --------------------
        Returns:
        - tuple of the index and value of outliers
        --------------------
        
        '''

        if self[var].dtype not in ['int64', 'float64']:
            return [],[]

        #Takes two parameters: dataframe & variable of interest as string
        df=self
        q1 = df[var].quantile(0.25)
        q3 = df[var].quantile(0.75)
        iqr = q3-q1
        inner_fence = 1.5*iqr
        outer_fence = 3*iqr
        
        #inner fence lower and upper end
        inner_fence_le = q1-inner_fence
        inner_fence_ue = q3+inner_fence
        
        #outer fence lower and upper end
        outer_fence_le = q1-outer_fence
        outer_fence_ue = q3+outer_fence
        
        outliers_prob = []
        outliers_poss = []
        for index, x in enumerate(df[var]):
            if x <= outer_fence_le or x >= outer_fence_ue:
                outliers_prob.append(index)
        for index, x in enumerate(df[var]):
            if x <= inner_fence_le or x >= inner_fence_ue:
                outliers_poss.append(index)
        return outliers_prob, outliers_poss
