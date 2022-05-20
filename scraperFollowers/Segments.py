import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv(r'C:\Users\chris\Desktop\surveyNormalized.csv')

pmf_df = pd.DataFrame()

for index, row in df.iterrows():
    if row['pmf_scale'] > 3:
        pmf_df = pmf_df.append(row)

pmf_df = pmf_df.reset_index()
pmf_df = pmf_df.drop(columns=['index'])
pmf_df.to_csv('pmf_df.csv')

# dems_df = pmf_df.drop(columns=['pmf_scale', 'expensive_price', 'bargain_price'])

# uniques_df = pd.DataFrame()


# for index, row in dems_df.iterrows():
#     if(uniques_df.empty):
#         uniques_df = uniques_df.append(row)
#         uniques_df['count'] = 1
#     else:
#         print(row)
#         for idx, rw in uniques_df.iterrows():
#             if row['age'] == rw['age']:
#                 if row['marital_status'] == rw['marital_status']:
#                     if row['ethnicity'] == rw['ethnicity']:
#                         if row['dependents'] == rw['dependents']:
#                             if row['region'] == rw['region']:
#                                 if row['income'] == rw['income']:
#                                     if row['advisor'] == row['advisor']:
#                                         rw['count'] += 1
#                                     else:
#                                         uniques_df = uniques_df.append(row)
#                                 else:
#                                     uniques_df = uniques_df.append(row)
#                             else:
#                                 uniques_df = uniques_df.append(row)
#                         else:
#                             uniques_df = uniques_df.append(row)
#                     else:
#                         uniques_df = uniques_df.append(row)
#             else:
#                 uniques_df = uniques_df.append(row)
                
# print(uniques_df)