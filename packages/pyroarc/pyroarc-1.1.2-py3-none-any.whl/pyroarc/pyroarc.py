from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
import category_encoders as ce
import sklearn
import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns

from statsmodels import robust
from scipy import stats

from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2


import re
from datetime import datetime as dt
import datetime
import time #needed for unix timestamp conversion 
import copy



class Manipulator:
       
   def __init__(self,df,metadata):
       #print('General')
       # initialization of class variables
       self.df=df 
       self.metadata=metadata
       self.allowed_scaling = ['RobustScaler','StandardScaler','MaxAbsoluteScaler','MinMaxScaler','None']
       self.allowed_encoding = ['OHE','FREQ','WOE']
       self.allowed_imputation = ['ConstantImputer','MostFrequentImputer','MeanImputer','MedianImputer','None']
       self.allowed_transformations = ['reciprocal','log X','squared','None']
       self.parameters_list = ['scaling', 'encoding','impute','transformation','None']
           
           
   #class methods:
   def metadata_verifier(self,df,metadata):   
       '''
       This function verifies the format of the metadata. It fills the missing information in the metadata with Nones

       Parameters
       ----------
       df : DataFrame
           The dataframe that the metadata is about.
       metadata : dict
           The metadata that is used for fit and transform functions.

       Returns
       -------
       dict
           returns the fixed metadata.

       '''
       self.metadata_temp = {}
       self.columns_list = df.columns
       self.parameters_list = ['scaling', 'encoding','impute','transformation']
       self.param_val = ''
       self.current_col = {}
       
       for col in self.columns_list: 
           self.current_col = {}
           for param in self.parameters_list:
               self.param_key = param
               try:
                   self.param_val = metadata[col][param]
               except:
                   self.param_val = 'None'
   
               self.current_col[self.param_key] = self.param_val
               
           self.metadata_temp[col] = self.current_col
           
       return self.metadata_temp
    
   
   def get_recommendad_feature_engineering(self,metadata=None):
       '''
       This function is intended to print the metadata in dataframe format to make it easier for user to see the feature engineering that will 
       be done to the data.
       
       Parameters
       ----------
       metadata : dict, optional
           DESCRIPTION. This is the metadata that has the recommended feature engineering changes. The default is None which will revert ot the initialized one.

       Returns
       -------
       df: metadata in DataFrame format

       '''
       try:
           if(metadata == None):
               df = pd.DataFrame(self.metadata).transpose()
    
           else:
               df = pd.DataFrame(metadata).transpose()
           return df
       except:
           print("The metadata is either not avialble or not in the right format or not initalized.")





   def verify_modification(self,transfomration_type,transformation):
       '''
       This function checks if the proposed transformation type is allowed in this package. It checks again the lest of prepared encodings, 
       imputations, scalings, and transfomrations. 

       Parameters
       ----------
       transfomration_type : str 
           This is the type of transformation requested e.g (encoding, scaling, imputation, or transfomration).
           here are the allowed types: ['scaling', 'encoding','impute','bin','transformation']
           
       transformation : str
           This is the specific transformation requested. Here are the allowed trnasformation per type
           Scaling: ['RobustScaler','StandardScaler','MaxAbsoluteScaler','MinMaxScaler']
           Encoding: ['OHE','FREQ','WOE']
           Imputation: ['ConstantImputer','MostFrequentImputer','MeanImputer','MedianImputer']
           Transformation: ['reciprocal','log X','squared']
           
           for imputers you can pass the constant after '_'. example: ConstantImputer_100

       Returns
       -------
       bool
           returns bool indicating if transformation is allowed in this package. 

       '''
       
       try:
            if(transfomration_type.lower().strip() == 'scaling'):
                if(transformation.strip() in self.allowed_scaling):
                    return True
                else:
                    return False
            elif(transfomration_type.lower().strip() == 'encoding'):
                if(transformation.strip() in self.allowed_encoding):
                    return True
                else:
                    return False
            elif(transfomration_type.lower().strip() == 'impute'):
                if(transformation.strip().split('_')[0] in self.allowed_imputation):
                    return True
                else:
                    return False
            elif(transfomration_type.lower().strip() == 'transformation'):
                if(transformation.strip() in self.allowed_transformations):
                    return True
                else:
                    return False
       except:
            print("Your metadata changes should follow the metadata format specified in the package")
            
            
            
            
   def modify_recommended_feature_engineering(self,modified_metadata,metadata=None):
       '''
       This function is used to allow the user to modify the recommended feature engineerings that were given by the scan funciton. 
       Using this function the user can pass a dictionary that will modify only the parts specified in the modified dictionary and use the modified types if allowed 
       in the following fit and transform calls. 
       
       This funciton will not overwrite the metadata but return an updated metadata that needs to be assigned to the object.metadata

       Parameters
       ----------
       modified_metadata : dict
           this is the dictionary containing the metadata that the user would like to change in the metadata.
           
           The expected format is as follows:
               {ColumnName:{TransformationType:Tranformation}}
        e.g.
               {'Gender':{'scaling':'RobustScaler'}} 
       metadata: dict Optional
           This is the metadata that would be changed. The deafult is to modify the metadata stored already in the object. 


       Returns
       -------
       final_metadata : dict
           The function reuturns the update metadata and the user can choose to store it or not.

       '''
       try:
           if(metadata == None):
               final_metadata = copy.deepcopy(self.metadata)
           else:
               final_metadata = metadata
       except:
           print("Your metadata changes should follow the metadata format specified in the package")
           
       try:
             for k in modified_metadata.keys():
                 requested_modifications = dict(modified_metadata[k])
                 for k2 in requested_modifications.keys():
                     if(self.verify_modification(k2,requested_modifications[k2])):
                         final_metadata[k][k2] = requested_modifications[k2].strip()
                     else:
                         print(requested_modifications[k2] + ' is not an allowed '+ k2 + " type. This change is skipped.")
             return final_metadata
       except:
             print("Your modified metadata doesn't match the expected format.")
    




    
   def remove_no_actions(self,metadata):
       '''
       This function removes from the metadata all the types of transformation that were assigned 'none'
       it returns a new metadata that needs to be assigned if needed

       Parameters
       ----------
       metadata : dict
           The metadata that needs to be modified. 

       Returns
       -------
       metadata : dict
           The updated metadata.

       '''
       try:
            for k in metadata.keys():
                transfomrations = dict(metadata[k])
                for k2 in list(transfomrations.keys()):
                    if(type(transfomrations[k2]) == str):
                        if(transfomrations[k2].lower().strip() == 'none'):
                            del transfomrations[k2]
                metadata[k] = transfomrations
            return metadata
       except:
            print("Your metadata doesn't match the expected format")
    

    


   def remove_no_actions_per_type(self,metadata,transformation_type):
       '''
       This function removes the entier key (equivelatn to column in this context) that the recommended transformation_type for it is none from the dataframe.

       Parameters
       ----------
       metadata : dict
           Metadata that needs to be checked.
       transformation_type : str
           the transformation type that we would like to check. example 'scaling'.

       Returns
       -------
       metadata : dict
           The updated metadata after removing the keys that have none for this transformation type.

       '''
       try:
            for k in list(metadata.keys()):
                transfomrations = dict(metadata[k])
                if(type(transfomrations[transformation_type]) == str):
                    if(transfomrations[transformation_type].lower().strip() == 'none'):
                        del metadata[k]
            return metadata
       except:
            print("Your metadata doesn't match the expected format")



    
   
   def is_float(self,val):
        '''
           this function compares if val array is numerical or categorical, it will return true or false per item
    
           Parameters
           ----------
           val : numerical
               value to check.
    
           Returns
           -------
           bool
               val is numerical or not.

        '''
       # this function compares if val array is numerical or categorical, it will return true or false per item
        try:
            float(val)
        except ValueError:
            # print("The value expected is float")
            return False
        else:
            return True
        
        
   
   def check_columns(self,df_columns,proposed_columns):
       '''
       This function wether two list contain similar items for columns amd transformations

       Parameters
       ----------
       df_columns : list
           list of columns in the dataframe.
       proposed_columns : str
           the column that need to be checked.

       Returns
       -------
       bool
           boolean value indicating if the column exists or not.

       '''
       try:
           if len(proposed_columns)==0  :
               print('No column was proposed')
               return False
           else: 
               for i in proposed_columns:
                   
                   if i not in df_columns:
                       print(i,' column is not exist in the current dataframe ')
                       return False
               return True
       except:
            print("The proposed columns or df_columns are not formatted as expected")
       
        
 
    
   def check_transformation(self,current_transformation,proposed_transformation,operation):
       '''
       This function checks if the prposed transformation type in the metadata is a valid transformation in the package

       Parameters
       ----------
       current_transformation : list
           The current transfomration that is in the dataframe.
       proposed_transformation : list
           The newly proposed transformation.
       operation : str
           The type of operation e.g (encoding, scaling, imputation, or transfomration).

       Returns
       -------
       bool
           bool value if the transfomration is allowed or not.

       '''
       try:
           if len(proposed_transformation)==0  : 
               print('no',operation, 'was proposed')
               return False
           else: 
               
               for i in proposed_transformation:
                   t=False
                   for o in current_transformation:
                       ab= '^'+o
                       regexp = re.compile(ab)
                       if regexp.search(i):
                           t=True
                   if t == False:
                       print(i, operation ,'is not exist in the current package ')
                       return False
               return True
       except:
           print("Check Transformation ran into an error while checking the proposed transfomration")
       
        

    
   def check_type(self,df,data_type):
       '''
       This function checks data type if metadata is modified by the user 

       Parameters
       ----------
       df : DataFrame
           The dataframe to use.
       data_type : str
           The data type to check for.

       Returns
       -------
       bool
           The result indicating if the type is as expected.

       '''
       try:
           a= np.vectorize(self.is_float)(df)
           if data_type=='Numerical':
              # use the product of numpy array , if equal 1 means all numerical
              if np.prod(a) != 1:
                  df_t = pd.DataFrame(np.prod(a,axis=0).reshape(1,len(df.columns)), columns = df.columns)
                  print('Ensure all columns are Numerical , please refer to the below dataframe for more info')
                  print(df_t)
                  return False
              else:
                  return True
           # string operations can be apply later 
           elif data_type=='Categorical':
              # use the sum of numpy array , if less than 1 means all numerical 
              if np.sum(a) >= 1 :
                  df_t = pd.DataFrame(np.prod(a,axis=0).reshape(1,len(df.columns)), columns = df.columns)
                  print('Ensure all columns are Categorical, please refer to the below dataframe for more info')
                  print(df_t)
                  return False
              else:
                  return True
           else: 
               print(data_type,'is unknown please select Numerical or Categorical')
       except:
           print("We ran into an issue checking the type in function check_type")




#Start of Date function:--------------------------------------------------------------------------------------
   def date_formatting(self,d, century = '20'):
       '''
           This function checks and correct the date format to be appicable for date operations
               The function accepts the follwing formats
               yyyy/mm/dd
               yyyymmdd
               yymmdd
               yyyy/m/d
               31 Jan 2022
               Note: the simbol "/" could be any kind of character separator. 
           
           Parameters
           ----------
            d : str
                string variable indicating the date 
                
            century : str Default:'20'
                the cnetury we are using
           
           Returns
           -------
           bool
               boolean value indicating if the column exists or not.
       '''
   
       def date_alpha_cleaning(d):
           month_text = ''
           month_num = 0
           months_l = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                         'november', 'december']
           months_s = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec']
           result_date = ''
   
           if len(d) == 9:
               month_text = d[2:5]
           else:
               month_text = d[2:len(d)-4]
   
           if month_text in months_l:
               month_num = int(months_l.index(month_text) + 1)
           elif month_text in months_s:
               month_num = int(months_s.index(month_text) + 1)
           else:
               return -1
   
           if month_num < 10:
               month_num = str('0' + str(month_num))
           else:
               month_num = str(month_num)
   
           result_date = d[-4:] + month_num + d[:2]
           return int(result_date)
   
    
   
    
   
    
   
       def remove_date_separators(d):
           #Check the position of the separator:
           date_structure = []
           date = ''
           sp = 0
           fount_first_sp = False
           fount_second_sp = False
           month_deg = 0
           day_deg = 0
   
           try:
               for i in range(len(d)):
                   try:
                       int(d[i])
                       date_structure.append('int')
                       date = date + str(d[i])
                       if fount_first_sp and not fount_second_sp:
                           month_deg += 1
                       elif fount_first_sp and fount_second_sp:
                           day_deg += 1
                   except:
                       try:
                           str(d[i])
                           date_structure.append('char')
                           if not fount_first_sp:
                               fount_first_sp = True
                           elif fount_first_sp:
                               fount_second_sp = True
                       except:
                           return -1
   
               #Number separators:
               sp = sum(map(lambda x: x == 'char', date_structure))
               if sp != 0 and sp != 2:
                   return -1
               else:
                   return str(date), month_deg, day_deg
   
           except:
               return -1
       
       # Start of the main function: -----------------------------------------------------------------
       #d_temp_int = 0
       d_temp_str = ''
       d_result = dt.date
       #current_year = 0
       error = False
       d_alpha_cleaned = 0
       d_without_sp = 0
       d_fixed = ''
       month_deg = 0
       day_deg = 0
       
       if len(century) > 2:
           error = True
       else:
           
           #Remove separators and perform format cleaning:
           d = d.replace(" ", "").lower()
           
           #alphabitical month cleaning:
           d_alpha_cleaned = date_alpha_cleaning(d)
           
           if d_alpha_cleaned == -1:
               d_without_sp, month_deg, day_deg = remove_date_separators(d)
               
               if d_without_sp == -1:
                   error = True
               else:
                   d_fixed = str(d_without_sp)
           else:
               d_fixed = str(d_alpha_cleaned)
           
           #Check if error reported from format cleaning function:
           if error != True or len(d_fixed) <= 10:
               #Check if the string can be converted into a number
               try:
                   d_temp_str = str(d_fixed)
   
                   if len(d_fixed) == 4:                    
                       d_result = datetime.date(int(century + d_temp_str[:2]), int(d_temp_str[2]), int(d_temp_str[3]))
                   elif len(d_fixed) == 5:
                       if day_deg == 2:
                           d_result = datetime.date(int(century + d_temp_str[:2]), int(d_temp_str[3]), int(d_temp_str[-2:]))
                       else:
                           d_result = datetime.date(int(century + d_temp_str[:2]), int(d_temp_str[2:4]), int(d_temp_str[-1:]))
                   elif len(d_fixed) == 6: 
                       d_result = datetime.date(int(century + d_temp_str[:2]), int(d_temp_str[2:4]), int(d_temp_str[4:]))
                   elif len(d_fixed) == 7:
                       d_result = datetime.date(int(d_temp_str[:4]), int(d_temp_str[4]), int(d_temp_str[-2:]))
                   elif len(d_fixed) == 8:
                       d_result = datetime.date(int(d_temp_str[:4]), int(d_temp_str[4:6]), int(d_temp_str[6:]))
                   else:
                       error = True
   
                   if not error:  
                       #print(d_result)
                       return d_result
               except:
                   error = True
   
       if error:
           return -1 #Error
       
        
       
   def date_diff(self,d1,d2,unit = 'days'):
       '''
        This function calculates the difference between two dates, it cleans it up first using a custom fucntion 
        "date_formattting" and then returns the difference based on user's request in days, months or years
        
        Parameters
        ----------
         d1 : date
             the 'from' date
         d2 : date
             tthe 'to' date 
        
        unit: str   Default: days
            the unit to use 'days' or 'months' or 'years'
        
        Returns
        -------
        duration
            the difference based on user's request in days, months or years
       '''
       try:
           #Variables:
           duration = 0
           
           #Perform Date validation and cleaning:
           d1 = self.date_formatting(d1)
           d2 = self.date_formatting(d2)
           
           if d1 == -1 or d2 == -1:
               raise -1 #Error
           
           #Perform Duration Calculation:
           if unit == 'days': 
               duration = (d2-d1).days
           elif unit == 'months': 
               duration = (d2-d1).days/30
           elif unit == 'years': 
               duration = (d2-d1).days/365.25
           else:
               return -1 #Invalid duration unit
           
           return duration
       except:
           return -1
       
        
       
       
   def unix_time(self,d1): 
       '''
       This function to clean and convert datetime to a unix timestamp
       This function is needed to be called from date_transform
       '''
       return time.mktime(self.date_formatting(d1).timetuple()) #as unix timesstamp
   
   
   
   def time_diff_unix(self,d1,d2): 
       '''
       compares the difference between two dates in unix timestamp
       example use of function: 
       time_diff_unix('30 nov 2022',1735506000)
       '''
       return (self.unix_time(d1)-d2)
   
    
   
    
   def date_transform(self,d1,d2=None,unit = 'days',time_zone = "America/Los_Angeles"):
       '''
       

       Parameters
       ----------
       d1 : TYPE
           DESCRIPTION.
       d2 : TYPE, optional
           DESCRIPTION. The default is None.
       unit : TYPE, optional
           DESCRIPTION. The default is 'days'.
       time_zone : TYPE, optional
           DESCRIPTION. The default is "America/Los_Angeles".

       Returns
       -------
       TYPE
           DESCRIPTION.

       '''
       
       #checking what version of the polymorphic function to use 
       if d2 is  None : #one column provided
           return np.vectorize(self.unix_time)(d1) #return unittime 
       
       elif isinstance(d2,pd.Series) : #two columns version
           return np.vectorize(self.date_diff)(d1.astype(str),d2.astype(str),unit) #change this 
       
       elif isinstance(d2, int) : #compared to a static number (unix timestamp)
           return np.vectorize(self.time_diff_unix)(d1.astype(str),d2) #returns difference in unixtimestamp   
       
       elif isinstance(d2,str)  : #compare to a static date inserted as string
           return np.vectorize(self.date_diff)(d1.astype(str),d2,unit)
       else :
           return 'idk'

#End of Date function:--------------------------------------------------------------------------------------    

   def validate_saudi_national_id(self,snid):
       '''
       This function takes a national id and verifies if it is a valid number for Saudis

       Parameters
       ----------
       snid : str
           national id.

       Returns
       -------
       message
           returns a message that either the national id is valid or not.

       '''
       if type(snid) not in [str, int]:
               raise TypeError("The ID must be either a string of numbers or an integer")
       temp = ''
       total = 0
       try:
           snid = str(snid)
   
           if snid[0] != '1' and snid[0] != '2':
               return 'Error'
   
           if len(snid) != 10:
               return 'Error'
   
           for i in range(1,len(snid)):
               if i % 2 != 0:
                   temp = str(int(snid[i-1]) * 2)
                   if len(str(temp)) == 1:
                       temp = str(str('0') + str(int(int(snid[i-1]) * 2)))
   
                   total = total + int(temp[0]) + int(temp[1])
               else:
                   total = total + int(snid[i-1])
                   
           if str(total)[1] == snid[-1:] or int(snid[-1:]) == ( 10 - int(str(total)[1])):
               return 'Valid ID'
           else:
               return 'Not Valid ID'
           
       except:
           return 'Error'
       



   def categorical_regrouping(self, df, thresh=0.03, name= 'Other'):
       '''
       This function takes all object type columns and checks for values that have occurance less than the specified threshold and group these values into one value
       The function is helpful for ML preparation to avoid having rare values appearing only on training after the train-test split
       It also helps reducing the number of columns in case of OHE for a categorical variable
       It takes 3 parameters:
           1- df = dataframe name
           2- thresh = the percentage of how frequent the values occurance that should be regrouped (optional) with default value as 0.03
           3- name = the name where the values under the threshold will be changed to (optional) with default value as 'Other'
       '''
       regrouped = []
        
       cat_features = df.select_dtypes(include=np.object).columns.tolist()
       for col in cat_features:
            check_values= df[col].value_counts(normalize=True).reset_index()
            check_values.columns=[col, 'count percentage']
            
            for i in range(len(check_values)):
                if(check_values['count percentage'][i] < thresh):
                    regrouped.append(check_values[col][i])
            df[col] = np.where(df[col].isin(regrouped),name,df[col])
       return df
            
#### End of Manipulator

class Scaler(Manipulator):
     def __init__(self,df,metadataO): 
       #print('Scaler')
       metadata=metadataO.copy()
       metadata = super().metadata_verifier(df,metadata)
       tmp_metadata=self.remove_no_actions_per_type(metadata,'scaling')
       super().__init__(df,metadata)
       keys = metadata.keys()
       # initialization of class variables
       self.scalers_dict = {x:tmp_metadata[x]['scaling'] for x in keys}
       self.df=df
       self.fitted_scaler={}
       self.is_fit = False

       
     def fit(self):
        '''
         This function fits the data for each scaler type of the allowed scalers in this package. 
         The allowed scalers are ['RobustScaler','StandardScaler','MaxAbsoluteScaler','MinMaxScaler']

         Manages
         -------
         is_fit : bool
            This flag confirms if all the fits were completed successfuly or there was an issue. 

        '''               
        try:
            self.is_fit=True
            # check data type

            if super().check_type(self.df[self.scalers_dict.keys()],'Numerical')==True:
                
                avaliable_transformations=['RobustScaler','StandardScaler','MaxAbsoluteScaler','MinMaxScaler']
                # check transformation availability
                if super().check_transformation(avaliable_transformations,self.scalers_dict.values(),'scaling')==True:
                    # check columns availability
                   if  super().check_columns(self.df.columns,self.scalers_dict.keys()) ==True:
                       
                       for x, y in self.scalers_dict.items():
                           
                           # check scaler type and fit
                           if y == 'RobustScaler':
                               scaler = RobustScaler()
                               self.fitted_scaler[x]= scaler.fit(self.df[[x]])
                               
                           elif y == 'MaxAbsoluteScaler':
                               scaler = MaxAbsScaler()
                               self.fitted_scaler[x]= scaler.fit(self.df[[x]])
                               
                           elif y == 'MinMaxScaler':
                               scaler = MinMaxScaler()
                               self.fitted_scaler[x]= scaler.fit(self.df[[x]])
                               
                           else:
                               scaler = StandardScaler()
                               self.fitted_scaler[x]= scaler.fit(self.df[[x]])
                               
                   else:
                       self.is_fit=False 
            
                else:
                    self.is_fit=False  
                    print("This is not one of the available scaling options")
                    
            else:
                self.is_fit=False
                print("Not all the data you are scaling are numerical or no scaling was requested")
                
            # return scaler_flag       
        except:
            print('an error occurs while fitting proposed scalers, please ensure the fitted data are compatible with the available scalers in this package')
            self.is_fit=False
            # return scaler_flag
        
        
        
           
     def transform(self,X_test,keep_original=False):
         '''
         This function transfomrs the data by performing the recomended scaling approach
         
         Parameters
         ----------
         X_test:  DataFrame 
             The dataframe that needs to be fitted
         keep_original : bool Default=False
             This variable decides if the orignial column should be kept or deleted. The original column is deleted by default. 

         Returns
         -------
         df:    DataFrame
             It returns the updated and scaled dataframe

         '''
         if(self.is_fit):
             try:
                 self.df = X_test

                 if(keep_original):
                     for t,y in self.fitted_scaler.items():
                         self.df[t+"_scaled"] = y.transform(self.df[[t]])
                 else:
                     for t,y in self.fitted_scaler.items():
                         self.df[t] = y.transform(self.df[[t]])
                         
                 return self.df
             except:
                 raise Exception('an error occurs while performing scaling, please refit the data and apply scalers again')
         else:
            raise Exception ("You need to fit the scaler first")
##### End of Scaler()





class Imputer(Manipulator):
     def __init__(self,df,metadataO):
       metadata=metadataO.copy()
       metadata = super().metadata_verifier(df,metadata)
       tmp_metadata=self.remove_no_actions_per_type(metadata,'impute')
       super().__init__(df,metadata)
       keys = metadata.keys()
       
       # initialization class variables
     
       self.df=df
       self.fitted_imputer={}
       self.imputer_dict = {x:tmp_metadata[x]['impute'] for x in keys}
       self.is_fit = False
      
               
         
     def fit(self):
            '''
             This function fits the data for each imputer type of the allowed imputers in this package. 
             The allowed imputers are ['ConstantImputer','MostFrequentImputer','MeanImputer','MedianImputer']
             
             Manages
             -------
             is_fit : bool
                 This flag confirms if all the fits were completed successfuly or there was an issue. 
    
            '''        
        # fit all imputer
            try:
                self.is_fit=True # to indicate if fit function completed
                # for transformation, for constant imputer : 'ConstantImputer_20'
                avaliable_transformations=['ConstantImputer','MostFrequentImputer','MeanImputer','MedianImputer']
                # check transformation availability
                if super().check_transformation(avaliable_transformations,self.imputer_dict.values(),'imputation')==True:
                    # check columns availability 
                   if  super().check_columns(self.df.columns,self.imputer_dict.keys()) ==True:
                       
                       for x, y in self.imputer_dict.items():
                           # check imputer type and fit
                           if y.split('_')[0] == 'ConstantImputer': 
                              
                               if super().is_float(y.split('_')[1])==True and super().check_type(self.df[[x]],'Numerical')==True:  
                                   imputer = SimpleImputer(missing_values=np.nan, strategy='constant',fill_value=int(y.split('_')[1]))
                                   self.fitted_imputer[x]= imputer.fit(self.df[[x]])
                               
                               elif super().is_float(y.split('_')[1])!=True and super().check_type(self.df[[x]],'Categorical')==True: 
                                   imputer = SimpleImputer(missing_values=np.nan, strategy='constant',fill_value=y.split('_')[1])
                                   self.fitted_imputer[x]= imputer.fit(self.df[[x]])
    
                               else:
                                   self.is_fit=False
                                   print('The constant value is not matching  ',x,'column type')
                                   
                                   
                           elif y == 'MostFrequentImputer':
                               imputer = SimpleImputer(missing_values=np.nan, strategy='most_frequent')
                               self.fitted_imputer[x]= imputer.fit(self.df[[x]])
                               
                           elif y == 'MeanImputer':
                               # check data type
                               if super().check_type(self.df[x],'Numerical')==True: # only for 'Mean Imputer','Median Imputer'
                                   imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
                                   self.fitted_imputer[x]= imputer.fit(self.df[[x]])
                                   
                               else:
                                   self.is_fit=False
                                   print('There was an issue in Mean Imputer')
                                   
                           else:
                               # check data type
                               if super().check_type(self.df[x],'Numerical')==True: # only for 'Mean Imputer','Median Imputer'
                                   imputer = SimpleImputer(missing_values=np.nan, strategy='median')
                                   self.fitted_imputer[x]= imputer.fit(self.df[[x]])
                                   
                               else:
                                   self.is_fit=False
                                   print('There was an issue in Median Imputer Imputer')

                                   
                   else:
                        self.is_fit=False
                        
                else:
                   self.is_fit=False
                   print("This imputation type is not allowed or no imputation was proposed")
                   
                #return Imputer_flag
            except:
                print('an error occurs while fitting proposed imputers, please ensure the fitted data are compatible with the available imputers in this package')
                self.is_fit=False
                #return Imputer_flag
            
            
            
     # Transform all imputer       
     def transform(self,X_test,keep_original=False):
         '''
         This function transfomrs the data by performing the recomended imputation approach
         
         Parameters
         ----------
         X_test:  DataFrame 
             The dataframe that needs to be fitted
         
         keep_original : bool Default=False
             This variable decides if the orignial column should be kept or deleted. The original column is deleted by default.  

         Returns
         -------
         df:    DataFrame
             It returns the updated and imputed dataframe

         '''
         # loop through fitted scaler
         if(self.is_fit):
             try:
                 self.df = X_test

                 for t,y in self.fitted_imputer.items():
                     if(keep_original):
                         self.df[t+"_imputed"] = y.transform(self.df[[t]])
                     else:
                         self.df[t] = y.transform(self.df[[t]])
                     
                 return self.df
             except:
                  raise Exception ('an error occurs while performing imputation, please refit the data and apply imputers again')
         else:
             raise Exception ("You need to fit the imputer first")       



class Encoder(Manipulator):
     def __init__(self,df,metadataO):
       metadata=metadataO.copy()
       metadata = super().metadata_verifier(df,metadata)
       super().__init__(df,metadata)
       keys = metadata.keys()
       tmp_metadata=self.remove_no_actions_per_type(metadata,'encoding')
       # initialization class variables
       
       self.df=df
       self.fitted_encoder={}
       self.encoder_dict = {x:tmp_metadata[x]['encoding'] for x in keys}
       self.is_fit = False
       
       
     # fit all Encoder
     def fit(self,y):
            '''
             This function fits the data for each encoder type of the allowed encoders in this package. 
             The allowed encoders are ['OHE','FREQ','WOE']
             
             Parameters
             ----------
             y : array of bools
                 y is the target that we need to check against. This is expected to be an array of bool 
    
             Manages
             -------
             is_fit : bool
                 This flag confirms if all the fits were completed successfuly or there was an issue. 
    
            '''               
            try:
                self.is_fit=True # to indicate if fit function is completed successfully 
               
                avaliable_transformations=['OHE','FREQ','WOE']
                # check transformation availability
                if super().check_transformation(avaliable_transformations,self.encoder_dict.values(),'encoding')==True:
                   # check columns availability 
                   if  super().check_columns(self.df.columns,self.encoder_dict.keys()) ==True:
                       for x, t in self.encoder_dict.items():
                           # check imputer type and fit
                           if t == 'OHE':
                               
                               encoder = OneHotEncoder(handle_unknown='ignore')
                               self.fitted_encoder[x]= encoder.fit(self.df[[x]])
                                
                           elif t == 'FREQ':
                               try:
                                   encoder = ce.CountEncoder(cols=[x])
                                   self.fitted_encoder[x]= encoder.fit(self.df[[x]])
                               except ValueError as e:
                                   print("Frequency encoder")
                                   print(e)
                                   self.is_fit=False
                               except KeyError as ke:
                                   print("Frequency encoder")
                                   print(ke)
                                   self.is_fit=False
                             
                           elif t == 'WOE':
                               try:
                                   encoder = ce.WOEEncoder(cols=[x])
                                   self.fitted_encoder[x]= encoder.fit(self.df[[x]],y)
                               except ValueError as e:
                                   print("WOE")
                                   print(e)
                                   self.is_fit=False
                               except KeyError as ke:
                                   print("WOE")
                                   print(ke)
                                   self.is_fit=False
    
                   else:
                        self.is_fit=False
                        
                else:
                   self.is_fit=False
                   print("This is not an allowed encoder in this package yet or no transformation was proposed")
                   
                # return Encoder_flag
            except:
                print('an error occurs while fitting proposed encoders, please ensure the fitted data are compatible with the available encoders in this package')
                self.is_fit=False
                # return Encoder_flag
        
     # Transform all Encoder       
     def transform(self,X_test,keep_original=False):
         '''
         This function transfomrs the data by performing the recomended encoding approach
         
         Parameters
         ----------
         X_test:  DataFrame 
             The dataframe that needs to be fitted
             
         keep_original : bool Default=False
             This variable decides if the orignial column should be kept or deleted. The original column is deleted by default. 

         Returns
         -------
         df:    DataFrame
             It returns the updated and encoded dataframe

         '''
         # loop through fitted encoders
         if(self.is_fit):
             try:
                 self.df = X_test

                 # apply all transformation and append to the original data frame
                 for t,y in self.fitted_encoder.items():
                     
                     
                     if(keep_original):
                         if isinstance(y, sklearn.preprocessing.OneHotEncoder):
                             tmp_df=np.transpose(y.transform(self.df[[t]]).toarray())
                             counter=0
                             
                             for col in tmp_df:
                                 self.df[t+"_encoded"+str(counter)]=col
                                 counter=counter+1
                                 
                         else:    
                             self.df[t+"_encoded"] = y.transform(self.df[[t]])
                             
                             
                     else:
                         if isinstance(y, sklearn.preprocessing.OneHotEncoder):
                             tmp_df=np.transpose(y.transform(self.df[[t]]).toarray())
                             counter=0
                             
                             for col in tmp_df:
                                 self.df[t+"_encoded"+str(counter)]=col
                                 counter=counter+1
                                 
                             self.df = self.df.drop(t,axis=1)
                                 
                         else:    
                             self.df[t] = y.transform(self.df[[t]])
              
                 return self.df
             except:
                 raise Exception('an error occurs while performing encoding, please refit the data and apply encoders again')
         else:
             raise Exception("You need to fit the encoder first")

#### End of Encoder()



class Transformer(Manipulator):
     def __init__(self,df,metadataO):
       metadata=metadataO.copy()
       metadata = super().metadata_verifier(df,metadata)
       tmp_metadata=self.remove_no_actions_per_type(metadata,'transformation')
       super().__init__(df,metadata)
       keys = metadata.keys()
       # initialization class variables
       
       self.df=df
       self.transformation_dict = {x:tmp_metadata[x]['transformation'] for x in keys}
       
       
               
      
     def transform(self,X_test,keep_original=False):
            '''
             This function transfomrs the data by performing the recomended transformation approach

             The allowed transformers are ['reciprocal','log X','squared']
             
             Parameters
             ----------
             X_test:  DataFrame 
                 The dataframe that needs to be fitted
             keep_original : bool Default=False
                 This variable decides if the orignial column should be kept or deleted. The original column is deleted by default.  
    
             Returns
             -------
             transform_flag : bool
                 This flag confirms if all the transformation were completed successfuly or there was an issue.
                 
             df:    DataFrame
                 It returns the updated and transformed dataframe
            '''    
        # fit all numerical transformations
            try:
                transform_flag=True # to indicate if transform is completed successfully  
                self.df = X_test
                
                avaliable_transformations=['reciprocal','log X','squared']
                # check transformation availability
                if super().check_transformation(avaliable_transformations,self.transformation_dict.values(),'transformation')==True:
                # check columns availability
                   if  super().check_columns(self.df.columns,self.transformation_dict.keys()) ==True:
                       
                       for x, y in self.transformation_dict.items():
                           if super().check_type(self.df[[x]],'Numerical')==True:
                               
                               if(keep_original):
                                   # check numerical transformations and fit
                                   if y == 'reciprocal':
                                      self.df[x+"_reciprocal"] = np.reciprocal((self.df[x].replace(0,1)))
        
                                   elif y == 'log X':
                                       self.df[x+"_logX"] = np.log(self.df[x].replace(0,1))
                                       
                                   elif y == 'squared':
                                      self.df[x+"_squared"] = np.power((self.df[x]),2)                              
                                          
                                   else:
                                       transform_flag=False
                                       print("the tnrasformation is not of an allowed type")
                               #drop the original column
                               else:
                                    # check numerical transformations and fit
                                    if y == 'reciprocal':
                                       self.df[x] = np.reciprocal((self.df[x].replace(0,1)))
         
                                    elif y == 'log X':
                                        self.df[x] = np.log(self.df[x].replace(0,1))
                                        
                                    elif y == 'squared':
                                       self.df[x] = np.power((self.df[x]),2)                              
                                           
                                    else:
                                        transform_flag=False
                                        print("the tnrasformation is not of an allowed type")
                                      
                           else:
                               transform_flag=False
                               print("The column is not of numerical type")
                          
                   else:
                        transform_flag=False
                else:
                   transform_flag=False
                   print("This trasformation type is not allowed")
                   return transform_flag, self.df 
            except:
                print('an error occurs while performing numerical transformation, please ensure the fitted data are compatible with the available transformation in this package')
                transform_flag=False
                return transform_flag, self.df          
            
### End of Transformation()            

class Pyroar:
    
    def __init__(self ):
        pass
        self.df = None
        self.metadata= {}
        self.is_fit = False
        
        self.manipulator = None
        self.transformer = None
        self.encoder = None
        self.imputer = None
        self.scaler = None
        
        
    # End of __init__
        
    """
    ============================
    DF Exploratory Data Analysis
    ============================
    Easy and quick way to get the most important statistics for
    a dataframe with a single command showing several metrics.
    """
    def scan(self, df, target, dropThreshold=0.5, catsLblEncodeThreshold=20, catsDropThreshold=100, outlier_scale_lim = 1.5, outlier_scale_frac=0.005, outlier_drop_lim=3.0, pvalue=0.05):
        """
        
        Applies a number of checks over the dataframe and returns different statistics and recommendations
        for a number of transformations for different columns in the dataframe.

        Parameters
        ----------
        df : string, dataframe name 
            Python pandas dataframe.
        target : string, target column name in dataframe
            Binary classification target column name in the dataframe (column must exist in the dataframe)
        dropThreshold : float, optional
            Threshold of missing values percentage over which to recommend dropping a column from the dataframe.
            The default is 0.3.
        catsLblEncodeThreshold : integer, optional
            Threshold of catagorical variables catagories count over which to recommend applying label encoding.
            Must be lower than the value in 'catsDropThreshold'.
            Catagorical variables lowwer than the threshold will be recommended to be one-hot encoded.
            The default is 20.
        catsDropThreashold : integer, optional
            Threshold of catagorical variables catagories count over which to recommend dropping a column from the dataframe.
            The default is 100.
        outlier_scale_lim : float, optional
            Number of Interquartile Range statistical measure (IQR) over which outliers are identified using Interquartile Range statistical measure (IQR).
            The identified outliers will be recommended to be treated by applying robust scaler
            or will be ignored depending on the fraction specified in 'outlier_scale_frac'
            The default is 1.5.
        outlier_scale_frac : float, optional
            Fraction of outliers over which to recommend applying robust scaler based on the limit specified in 'outlier_scale_lim'
            If fraction of outliers is below this fraction, outliers will not be treated (ignored).
            The default is 0.005.
        outlier_drop_lim : float, optional
            Number of Interquartile Range statistical measure (IQR) over which outliers are identified using Interquartile Range statistical measure (IQR).
            Those outliers will be recommended to be dropped.
            The default is 3.0.
        pvalue : float, optional
            Probability value for null-hypothesis significance testing used in statistical tests used in this function.
            The default is 0.05.

        Returns
        -------
        dictionary
            Dictionary of all recommendations of the function for each column to be applied in other functions.

        """
        
        self.num_features = df.select_dtypes(include=np.number).columns.tolist()
        self.cat_features = df.select_dtypes(include=np.object).columns.tolist()
        
        
        self.df = df
        dropThreshold = dropThreshold
        catsLblEncodeThreshold = catsLblEncodeThreshold
        catsDropThreshold = catsDropThreshold
        outlier_scale_lim = outlier_scale_lim
        outlier_scale_frac = outlier_scale_frac
        outlier_drop_lim = outlier_drop_lim
        pvalue = pvalue
        
        for col in df.columns:
            self.metadata.update({col: {}})
            
        print("Head of dataframe:\n")
        print(df.head())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nTail of dataframe:\n")
        print(df.tail())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nNames of existing columns:\n")
        print(df.columns)
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nData types of the existing columns:\n")
        print(df.info())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nNumbers of columns with same data type:\n")
        print(df.dtypes.value_counts())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nMemory usage of each column:\n")
        print(df.memory_usage())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nShape of the dataframe (rows/columns):\n")
        rows = df.shape[0]
        cols = df.shape[1]
        print("There are " + str(rows) + " rows and " + str(cols) + " columns in this dataframe.")
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        
        print("\nNumber of occuring duplicates in the dataframe:\n")
        dupRows = df.duplicated().sum()
        print("There are " + str(dupRows) + " duplicated rows in the dataframe.")
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nGernalized Auto Plots:\n")
        self.plot()
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\Correlation Plot:\n")
        self.correlation_plot()
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nCheck the Missing Values per column:\n")
        self.scan_missing_values(dropThreshold)
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        

        #### Note: This section should be applied to categorical Variables ONLY ************
        print("\nCheck Unique Classes per Categorical Features")    
        #self.scan_catorical_classes(catsDropThreshold, catsLblEncodeThreshold )
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
               
        ######################  IMPLEMENT OUTLIER DETECTION  ####################
        #### Note: This section should be applied to numerical Variables ONLY ************
        print("\nCheck Unique Classes per Categorical Features")  
        self.scan_outliers( outlier_scale_lim, outlier_scale_frac, outlier_drop_lim)
        outlier_scale_lim, outlier_scale_frac, outlier_drop_lim
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        print("\nStandard statistics for each column:\n")
        print(df.describe())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
           
        print("\nCorrelations between columns:\n")
        print(df.corr())
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
                       
        for var in self.num_features:
            print(df[var])
            self.df[var] = pd.to_numeric(self.df[var], errors='coerce')
            self.df[var] = self.df[var].fillna(0)
        
        ########################### STATS #######################    
        #### Statistical Testing for Numerical Features 
        print("\nStatistical Test for Numerical Features using Shapiro and arque-Bera")
        self.stat_test_numerical( pvalue)
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        #### Statistical Testing for Categorical Features 
        print("\nStatistical Tests for Categorical Features using Chai-square")
        self.stat_test_categorical( pvalue, target)
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
        
        return self.metadata
         
        
    # End of scan()
    
    
    def prep(self):
        """
        This funcgtion handles the missing values, outliers, and 
        categorical variables with a large nubmer of unique values

        Parameters
        ----------
        None.
        Returns
        -------
        None.
        """
        # cleaning
        print("\n\n ==== Preperation function started =====")
        for col in self.metadata:
           print('\nColumn Name:', col ,  ' ** values:', self.metadata[col])
           # implement your fit methods here
           
           trans = self.metadata[col]
           
           # Treating Missing Values by Dropping
           # {'Drop': 'DropColumn'}   ==> Too many missing values
           key = 'drop'
           if key in trans:
                print(trans[key])
                if trans[key] == 'DropColumn':
                    if col in self.df.columns:
                        self.df.drop([col], axis=1, inplace=True)
           
            # {'Encoding': 'DropColumn'} ==> too many class for cat variables
           key = 'missingvalues'
           if key in trans:
                if trans[key] == 'DropColumn':
                    if col in self.df.columns:
                        self.df.drop([col], axis=1, inplace=True)
                    
            
           # {'DropExtermeOutliersValues': outlier_drop_lim} ==> Drop Extreme outliers
           key = 'DropExtermeOutliersValues'
           if key in trans:
                if trans[key][0] < 1.5 :
                    raise Exception("Sorry, You cannot set limit below 1.5 IQR")
                    
                elif col in self.df.columns:
                    # Calculate Q3 and Q1
                    # calculate the IQR
                    print(self.df[col], trans[key])
                    
                    # # find outliers extreme_upper_bound
                    extreme_upper_bound = trans[key][1]
                    # # find outliers extreme_lower_bound
                    extreme_lower_bound = trans[key][2]
                    
                    # drop rows with values <lower_bound or values >upper_bound
                    #self.df = self.df[self.df[col] != np.nan and ( self.df[col] > extreme_upper_bound or self.df[col] < extreme_lower_bound)  ]
                    self.df = self.df[ (self.df[col] > extreme_upper_bound) | (self.df[col] < extreme_lower_bound) ]
                    
    # End of prep()      
    
    
    def fit(self,X,y):
        """
        Applies fit methods for a number of recommended transformations given in the 'scan' function
        for different columns in the dataframe.        

        Parameters
        ----------
        X : {array-like, sparse matrix} of shape (n_samples, n_features)
            The data used for later transformation (e.g for scaling or categories of each feature for one-hot encoder)
        y : series-like of shape (n_samples,)
            Binary target values (class labels) as integers used for Weight of Evidence (WoE) transformation.
        
        """
        
        # print("Inside the fit funciton of pyroar =========================")
        # print(self.df)
        # print(self.metadata)
        
        self.manipulator = Manipulator(self.df,self.metadata)  
        self.transformer = Transformer(self.df,self.metadata)
        self.encoder = Encoder(self.df,self.metadata)
        self.imputer = Imputer(self.df,self.metadata)
        self.scaler = Scaler(self.df,self.metadata)
        encoder_flag = True
        imputer_flag = True
        scaler_flag = True
    
        try:
            if isinstance(X, pd.DataFrame):
                try:            
                   self.encoder=Encoder(X,self.metadata)
                   self.encoder.fit(y)
                   if self.encoder.is_fit==True:
                       # encoder.transform()
                       # print(' encoding operations were completed successfully')
                       pass
                   else:
                       print('an error occured while fitting encoder')
                       encoder_flag = False
                   
                   self.imputer=Imputer(X,self.metadata)
                   self.imputer.fit()
                   if self.imputer.is_fit == True:
                       # imputer.transform()
                        # print(' imputation operations were completed successfully')
                        pass
                   else:
                       print('an error occured while fitting imputers')
                       imputer_flag = False
                       
                    
                   self.scaler=Scaler(X,self.metadata)
                   self.scaler.fit()
                   if self.scaler.is_fit==True:
                       # scaler.transform()
                       # print(' imputation operations were completed successfully')
                       pass
                   else:
                       print('an error occured while fitting scalers')
                       scaler_flag = False
                   
                   
                   if(encoder_flag or imputer_flag or scaler_flag):
                       self.is_fit = True
                       print("fit was completed successfuly")
                except Exception as e:
                    print("The fit wasn't completed successfully. An Error has occured")
                    print(e)
            else:
                raise Exception("X needs to be of type DataFrame")
        except Exception as e:
            print(e)
            
    def transform(self,X_test):
        """   

         Perform transformations for the fitted transformers given in the 'fit' function
         for different columns in the dataframe.        

         Parameters
         ----------
         keep_original: bool Default: False
                This bool variable deiced to either keep the transformed values in seperate columns or replace the exisitng column
                

         Returns
         -------         
         The funciton doesn't reaturn anything though it updates the self.df value for this object. The result can be accessed using object.df

        """
        try:
            imputer_flag = True
            trans_flag = True
            scaler_flag = True
            encoder_flag = True
            
            if(self.is_fit):
                
                try:
                    self.df = self.imputer.transform(X_test)
                except Exception as e:
                    imputer_flag = False
                    print("There was an error in the Imputer class")
                    print(e)
                    
                    
                try:
                   self.transformer=Transformer(self.df,self.metadata)
                   trans_flag, self.df = self.transformer.transform(X_test)     
                except Exception as e:
                    trans_flag = False
                    print("There was an error in the Transformer class")
                    print(e)
        
        
                try:
                    self.df = self.scaler.transform(X_test)
                except Exception as e:
                    scaler_flag = False
                    print("There was an error in the Scaler class")
                    print(e)
        
        
                try:
                    self.df = self.encoder.transform(X_test)
                except Exception as e:
                    encoder_flag = False
                    print("There was an error in the Encoder class")
                    print(e)
                
                if(imputer_flag or trans_flag or scaler_flag or encoder_flag):
                    print("Transform was completed successfully")
            else:
                raise Exception ("You can't transform before you fit. Please run the fit() function first")
            
            
        except Exception as e:
            print(e)
            
            
    def get_recommendad_feature_engineering(self,df_format=False):
        '''
         This function is intended to print the metadata in dataframe format to make it easier for user to see the feature engineering that will 
         be done to the data.
         
        Parameters
        ----------
        df_format : bool, optional
            it checks if we want to return the recommeneded the feature engineering in DataFrame format or not. The default is False.

        Returns
        -------
        df or dict
            Recommended feature engineering in DataFrame format or in dict format.
        '''
        try:
            if(df_format):
                tmp_df = self.manipulator.get_recommendad_feature_engineering(metadata = self.metadata)
                print("Here are the recommended feature engineering for the fit and transform")
                print(tmp_df)
                return tmp_df
                
            else:
                print("Here are the recommended feature engineering for the fit and transform")
                print(self.metadata)
                return self.metadata
        except Exception as e:
            print("There was an issue in getting recommended feature engineering")
            print(e)
        
    
    
    def modify_recommended_feature_engineering(self,modified_metadata,metadata=None,inplace=False):
        '''
        This function is used to allow the user to modify the recommended feature engineerings that were given by the scan funciton. 
        Using this function the user can pass a dictionary that will modify only the parts specified in the modified dictionary and use the modified types if allowed 
        in the following fit and transform calls. 
        
        This funciton will could overwrite the metadata based on the inplace flag and return an updated metadata

        Parameters
        ----------
        modified_metadata : dict
            his is the dictionary containing the metadata that the user would like to change in the metadata.
            
            The expected format is as follows:
                {ColumnName:{TransformationType:Tranformation}}
         e.g.
                {'Gender':{'scaling':'RobustScaler'}} 
                
        metadata : dict, optional
            This is the metadata that would be changed. The deafult is to modify the metadata stored already in the object.  The default is None.
            
        inplace : bool, optional
            This bool is used to either replace the metadata stored in the object or just return the new metadata to the user. The default is False.

        Returns
        -------
        None.

        '''
        
        
        try:
            if(inplace):
                self.metadata = self.manipulator.modify_recommended_feature_engineering(modified_metadata,metadata)
            else:
                self.manipulator.modify_recommended_feature_engineering(modified_metadata,metadata)
        except Exception as e:
            print("There was an issue in modifying the recommended feature engineering metadata")
            print(e)

    
    def count_outlier_numircal(self, x, limLow, limHigh):
        """
        
        Counts the number of outliers in numerical columns in the dataframe
        
        Parameters
        ----------
        x : {array-like, sparse matrix} of shape (n_samples, n_features)
            The data in the numerical columns.
        limLow : float
            Number of Interquartile Range statistical measure (IQR) over which outliers are identified using Interquartile Range statistical measure (IQR).
            The identified outliers to be treated later by applying robust scaler
            or will be ignored depending on the scan fraction as specified in 'outlier_scale_frac'
        limHigh : float
            Number of Interquartile Range statistical measure (IQR) over which outliers are identified using Interquartile Range statistical measure (IQR).
            Those outliers will be dropped later.
        Returns
        -------
        outliers_normal : integer
            count of normal outliers to be treated later by applying robust scaler or to be ignored depending on the scan fraction as specified in 'outlier_scale_frac'.
        extreme_outliers : integer
            count of extreme outliers to be removed later.

        """
        
        #Q1 = np.percentile(self.df[x], 25, interpolation = 'midpoint')
        Q1 = np.quantile(self.df[x], q=0.25)
        #Q3 = np.percentile(self.df[x], 75, interpolation = 'midpoint')
        Q3 = np.quantile(self.df[x], q=0.75)
        IQR = Q3 - Q1
            
        #Old_length=len(x)
        #print("Old length: ", Old_length)
        
        # Upper bound for Exetreme outliers
        upper_extreme = len(np.where(self.df[x] >= (Q3+limHigh*IQR)))
        # Lower bound for Exetreme outliers
        lower_extreme = len(np.where(self.df[x] <= (Q1-limHigh*IQR)))
        extreme_outliers = upper_extreme + lower_extreme
        
        
        # Upper bound for Exetreme outliers
        upper = len(np.where(self.df[x] >= (Q3+limLow*IQR)))
        # Lower bound for Exetreme outliers
        lower = len(np.where(self.df[x] <= (Q1-limLow*IQR)))
        outliers_normal =  upper + lower - extreme_outliers
        
        print(Q1, Q3, IQR, outliers_normal, extreme_outliers, Q1-limHigh*IQR, Q3+limHigh*IQR)
        return outliers_normal, extreme_outliers, Q1-limHigh*IQR, Q3+limHigh*IQR
    # End of count_outlier_numircal()
    
    def detect_outliers_zscore(self, data):
        """
        This function detects outliers for features with normal distribution.
        Standard zscore is used to determine the outliers
        if we have a normal distribution we use a standard zscore

        Parameters
        ----------
        data : TYPE
            DESCRIPTION.

        Returns
        -------
        outliers : TYPE
            DESCRIPTION.

        """
        # threshhold for the outliers detection limit is taken to be equal to 3
        outliers =[]
        threshold = 3
        mean = np.mean(data)
        std = np.std(data)
        
        for x in data:
            zscore = (x-mean)/std
            if np.abs(zscore)> threshold:
                outliers.append(x)
        return outliers
    # End of detect_outliers_zscore()
    
    
    
    def detect_outliers_Mzscore(self, data):
        """
        This function returns the non-normal distribution we use a modified zscore

        Parameters
        ----------
        data : TYPE
            DESCRIPTION.

        Returns
        -------
        outliers : TYPE
            DESCRIPTION.

        """
        # threshhold for the outliers detection limit is taken to be equal to 3
        outliers =[]
        threshold = 3
        # compute modified z
        Med = np.median(data)
        MAD = robust.mad(data)
        
        for x in data:
            Mzscore = stats.norm.ppf(.75)*(x-Med) / MAD
            if np.abs(Mzscore)> threshold:
                outliers.append(x)
        return outliers
    # End of detect_outliers_Mzscore()
    
    
    def plot(self):
        """
        Correlation plots

        Returns
        -------
        None.

        """
        numeric=self.df.select_dtypes(include=['float64'])
        plt.plot(numeric)
        #plt.display()
    # End of plot()
    
    def correlation_plot(self, triangle = True, shrink = 0.5, orientation = "vertical", my_palette = None):
        """
        

        Parameters
        ----------
        data : TYPE
            DESCRIPTION.
        method : TYPE, optional
            DESCRIPTION. The default is "pearson".
        triangle : TYPE, optional
            DESCRIPTION. The default is True.
        shrink : TYPE, optional
            DESCRIPTION. The default is 0.5.
        orientation : TYPE, optional
            DESCRIPTION. The default is "vertical".
        my_palette : TYPE, optional
            DESCRIPTION. The default is None.

        Returns
        -------
        corr_mat : TYPE
            DESCRIPTION.
        TYPE
            DESCRIPTION.

        """
        """
        Function to obtain correlation matrix and associated correlation plot.
        :param data: pandas dataframe - data set to calculate correlations from.
        :param method: Default "pearson". Type of correlation to compute. See pandas.DataFrame.corr() for more information.
        :param triangle: Either True or False; default is True, Whether to plot the full heatmap of correlations or only the lower triangle.
        :param shrink: Governs the size of the color bar legend. See matplotlib.pyplot.colorbar() for more information.
        :param orientation. Either "vertical" or "horizontal"; default is "vertical". Governs where the color bar legend is plotted. See matplotlib.pyplot.colorbar() for more information.
        :return: tuple of (corr_mat, ax.figure). corr_mat is a pandas.DataFrame() holding the correlations. ax.figure is the plot-object of the heatmap.
        """
        corr_mat = self.df.corr(method="pearson")
    
        if triangle == True:
          mask = np.zeros_like(corr_mat)
          mask[np.triu_indices_from(mask)] = True
        else:
          mask = None
    
        with sns.axes_style("white"):
            plt.figure(figsize=(15,15))
            ax = sns.heatmap(corr_mat, vmin = -1,vmax= 1, square=True, cmap = my_palette, cbar_kws={"shrink": shrink, "orientation": orientation}, mask=mask)
            ax.set_xticklabels(ax.get_xmajorticklabels(), fontsize = 6)
            ax.set_yticklabels(ax.get_ymajorticklabels(), fontsize = 6)
        return corr_mat, ax.figure
    # End of correlation_plot()
        
    
    def scan_missing_values(self, dropThreshold):
        """
        This functions scans the missing values and gives recommendation either
        to drop the column, use specific imputation.
        Parameters
        ----------
        dropThreshold : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        print("\nNumber of occuring NULL/NA values per column:\n")
        print(self.df.isnull().sum())
        print("\nPercentage of occuring NULL/NA values per column:\n")
        missing_perentage = self.df.isnull().sum()/self.df.isnull().count() * 100
        print( missing_perentage)
        for col, val in zip(self.df.columns , missing_perentage):
            if(val >= dropThreshold):
                 # drop the column
                 print('Column: {} , metadata: Drop Column.  Too many missing values {}%'.format(col, val))
                 self.metadata[col].update(  {'missingvalues': 'DropColumn'})
            elif val>0:
                 print('Column: {} , metadata: Imputation for Missing Values is required.  Number of missing values {}%'.format(col, val))
                 self.metadata[col].update(  {'impute': 'MeanImputer'})
            else: # zero missing values
                 print('Column: {} , metadata: No imputation is required.  Number of missing values {}%'.format(col, val))
                 #self.metadata[col].update(  {'Imputation', 'Mean'})
        print("- - - - - - - - - - - - - - - - - - - - - - - -")
    
    
    def scan_catorical_classes(self, catsDropThreshold,catsLblEncodeThreshold ):
        """
        

        Parameters
        ----------
        catsDropThreshold : TYPE
            DESCRIPTION.
        catsLblEncodeThreshold : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        print("\nNumber of occuring unique values per column:\n")
        n_unique = self.df.nunique()
        print(""+n_unique)
        for col, val in zip(self.df.columns , n_unique):
             if(val > catsDropThreshold):
                 # drop the column
                 print('Column: {} , metadata: Drop.  Too many unique values {}'.format(col, val))
                 self.metadata[col].update(  {'drop': 'DropColumn'})
             elif val >catsLblEncodeThreshold:
                 # label encoder
                 print('Column: {} , metadata: Use FrequancyEncoder.  Moderate number of unique values {}'.format(col, val))
                 self.metadata[col].update(  {'encoding': 'FREQ'})
             else:
                 #one hot encoding
                 print('Column: {} , metadata: Use OneHotEncoder.  Limitted number of unique values {}'.format(col, val))
                 self.metadata[col].update(  {'encoding': 'OHE'})
                 
    def scan_outliers(self, outlier_scale_lim, outlier_scale_frac, outlier_drop_lim):
        """
        

        Parameters
        ----------
        outlier_drop_lim : TYPE
            DESCRIPTION.
        outlier_scale_frac : TYPE
            DESCRIPTION.
        outlier_scale_lim : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        num_out_low_lim = {}
        num_out_high_lim = {}
        num_out_lower_bound = {}
        num_out_upper_bound = {}
        for col in self.num_features:
           low, high, lower_bound, upper_bound =  self.count_outlier_numircal(col, outlier_scale_lim, outlier_drop_lim)
           num_out_low_lim[col] = int(low)
           num_out_high_lim[col] = int(high)
           num_out_lower_bound[col] = lower_bound
           num_out_upper_bound[col] = upper_bound
        print(num_out_low_lim)
        
        #metadata['OutlierValuesDropLimit'].update(outlier_drop_lim )
        ## Drop the outlier values that are greater than upper limit (e.g. 3 IQR )
        print("print the dictionarty 547")
        print(self.metadata)
        for col, val in num_out_high_lim.items():
             if int(val) > 0 :  
                 print('Column: {} , metadata: Drop Outlier Value.  There are {} outlier values that are more than {} IQR'.format(col, val, outlier_drop_lim))
                 
                 self.metadata[col].update(  {'DropExtermeOutliersValues': [outlier_drop_lim, num_out_lower_bound[col], num_out_upper_bound[col] ]})
                 #{ 'Age': { 'DropExtermeOutliersValues': 5 , 'scaling': 'StandardScaler' },          }
        ## use robustScalaer if the column has 3% or more of outliers that are more
        ## the lower outliers limit (e.g. 1.5 IQR)
        for col, val in  num_out_low_lim.items():
             if( (val/ len(self.df)) > outlier_scale_frac ):  # more than e.g 0.1% are outliers ==> Robust Scaler
                 print('Column: {} , metadata: Use RobustScaler.  There are {:0.2f} % outlier values that are more than {} IQR'.format(col, (val/len(self.df)) , outlier_scale_lim))
                 self.metadata[col].update(  {'scaling': 'RobustScaler'})
                 
                 
    def stat_test_numerical(self, pvalue):
        """
        

        Parameters
        ----------
        pvalue : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        for var in self.num_features:
            print(self.df[var])
            self.df[var] = pd.to_numeric(self.df[var], errors='coerce')
            self.df[var] = self.df[var].fillna(0)
            
        
        
        # To perform the Jarque-Bera goodness, first of all, it is needed to check that the sample is above 2000 (n>2000) data points.
        # Otherwise it is recommended to use the Shapiro-Wilk tests to check for normal distribution of the sample.
        
        
            ### test for normality Shapiro and Jarqu-Bera)
            for col in self.num_features:
                      
                
                if len(self.df) <=2000: # use shapiro
                    statistic, pval = stats.shapiro(self.df[col])
                else:   # use jarque_bera
                    statistic, pval = stats.jarque_bera(self.df[col])
                
                if pval > pvalue:
                    print("Dataset df has a normal distribution on var {}, as the null hyposthesis was not rejected for having a {:.4f} p-Value".
                         format(col, pval))
                    self.metadata[col].update(  {'scaling': 'StandardScaler'})
                else:
                    print("Dataset df does not have a normal distribution on var {}, as the pvalue is {:.4f}".
                          format(col,pval))
                    print("Try different transformations on var {}".format(col))
                    #
                    ### test transformations   1/X    log x    x^2
                    # 1/X transofrmation
                    #X = pd.map(lambda i: 1/i, df[col])
                    x = 1/self.df[col]
                    if len(self.df) <=2000: # use shapiro
                        statistic, pval = stats.shapiro(x)
                    else:   # use jarque_bera
                        statistic, pval = stats.jarque_bera(x)
                    if pval > pvalue:
                        print("Dataset df has a normal distribution on var 1 / {}, as the null hyposthesis was not rejected for having a {:.4f} p-Value".
                         format(col, pval))
                        
                        print("Recommendation: Transfor feature to 1/x")
                        self.metadata[col].update(  {'transformation': 'reciprocal'})
                        self.metadata[col].update(  {'scaling': 'StandardScaler'})
                    else:
                        # print("Dataset df does not have a normal distribution on var {}, as the pvalue is {:.4f}".
                        #       format(col,pval))
                        # Check log x transformation
                       
                        x = np.log(self.df[col].replace(0,1))
                        if len(self.df) <=2000: # use shapiro
                            statistic, pval = stats.shapiro(x)
                        else:   # use jarque_bera
                            statistic, pval = stats.jarque_bera(x)
                        if pval > pvalue:
                            print("Dataset df has a normal distribution on var log({}), as the null hyposthesis was not rejected for having a {:.4f} p-Value".
                             format(col, pval))
                            
                            print("Recommendation: Transfor feature to 1/x")
                            self.metadata[col].update(  {'transformation': 'log X'})
                            self.metadata[col].update(  {'scaling': 'StandardScaler'})
                        else:
                            ##  Chekc X^2 transofrmation
                            x = self.df[col]**2
                            if len(self.df) <=2000: # use shapiro
                                statistic, pval = stats.shapiro(x)
                            else:   # use jarque_bera
                                statistic, pval = stats.jarque_bera(x)
                            if pval > pvalue:
                                print("Dataset df has a normal distribution on var {}**2, as the null hyposthesis was not rejected for having a {:.4f} p-Value".
                                 format(col, pval))
                                
                                print("Recommendation: Transfor feature to 1/x")
                                self.metadata[col].update(  {'transformation': 'squared'})
                                self.metadata[col].update(  {'scaling': 'StandardScaler'})
                            else:
                                # none of the transformations worked ==> Appy MinMaxScaler
                                self.metadata[col].update(  {'scaling': 'MinMaxScaler'})
    # End of stat_test_numerical()
      
    def stat_test_categorical(self, pvalue, target):
        """
        

        Parameters
        ----------
        pvalue : TYPE
            DESCRIPTION.
        target : TYPE
            DESCRIPTION.

        Returns
        -------
        None.

        """
        ########################### Stat_3. IMPLEMENT ChaiSquare-Test for categorical nominal variables
        ### PROBLEM: we do not have the population to perform Chai-Square test
        # Source: https://towardsdatascience.com/chi-square-test-for-feature-selection-in-machine-learning-206b1f0b8223
        
        label_encoder = LabelEncoder()
        
        for col in self.cat_features:
            self.df[col] = label_encoder.fit_transform(self.df[col])


        
        print("chi squared test here",self.cat_features)
        X = self.df[self.cat_features]
        print(X.head())
        y = self.df[target] # we have to ask the user to specify the target variable at the beginning and then make it binary 1,0

        chi_scores = chi2(X,y)
        
        p_values = pd.Series(chi_scores[1],index = X.columns)
        p_values.sort_values(ascending = False , inplace = True)
        #p_values<0.05
        i = 0
        for pval in p_values:
            col = p_values.index[i]
            if pval >= pvalue:   
                print( " The variable {} is recommended to be removed since it is independent from the target variable. We fail to reject the null hypothesis as p-value >= 5%: {} ".format(col,pval))
                self.metadata[col].update(  {'drop': 'DropColumn'}) #the recommendation is to drop the column. Also the 5% shouldn't be hard-coded
            else:
                print( " The variable {} is recommended to be kept since it is dependent on the target variable. We reject the null hypothesis as p-value < 5%: {} ".format(col,pval))
            i = i+1
    # End of stat_test_categorical()           
            
    def printDf(self):
         print(self.df)
         print(self.metadata)
        
   # End of printDf()
    
    def getDf(self):
         return self.df
         
        
   # End of printDf()
    
    
   