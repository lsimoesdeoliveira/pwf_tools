# -*- coding: utf-8 -*-
"""
Created on Mon Apr 17 19:43:47 2017

@author: lucas
"""

import pandas as pd
from leitor import read_pwf
       
arquivosComparar = ['1.pwf', '2.pwf', '3.pwf', '4.pwf', '5.pwf', '6.pwf']

#==============================================================================
# res[0] = res[0][['De', 'Para', 'Nc', 'R', 'X', 'Mvar']]
# res[1] = res[1][['De', 'Para', 'Nc', 'R', 'X', 'Mvar']]
#==============================================================================
                    
res = []

for file in arquivosComparar:
    res.append(read_pwf(file)['DLIN'])
    
for i in range(len(res)):
    #res[i] = res[i][['De', 'Para', 'Nc', 'R', 'X', 'Mvar', 'Tap', 'Cn', 'Ce']]
    res[i] = res[i][['De', 'Para', 'Nc', 'R', 'X', 'Mvar', 'Tap']]
    res[i]['TITU'] = arquivosComparar[i]
    
                    
#==============================================================================
#                     
# merge = res[0].merge(res[1], how='outer', indicator=True)
# merge = merge[merge['_merge'] != 'both']
# merge = merge.sort_values(['De', 'Nc'])
# 
# #Problema de comparar reatâncias é o ANAT0 dos trafos 
# #merge = merge[pd.notnull(merge['R'])]
# 
# #merge = merge [merge['Tap']]
# merge = merge.sort_values(['De','Para', 'Nc'])
# 
# 
#==============================================================================

TUDO = pd.DataFrame({})

for i in range(len(res)):
    try:
        if i == 0:
            temp = res[i].merge(res[i+1], how='outer', indicator=True)
            temp = temp[temp['_merge'] != 'both']
            temp = temp.drop('_merge', axis=1)
        elif i < len(res)-1:
            temp = temp.merge(res[i+1], how='outer', indicator=True)
            temp = temp[temp['_merge'] != 'both']
            temp = temp.drop('_merge', axis=1)
        elif i == len(res):
            #temp = temp.merge(res[i], how='outer', indicator=True)
            temp = temp[temp['_merge'] != 'both']
            #temp = temp.drop('_merge', axis=1)
    except IndexError:
        print("Erro index " + str(i))
    TUDO = TUDO.append(res[i])  
        
temp = temp[~pd.notnull(temp['Tap'])]        
temp = temp.sort_values(['De','Para', 'Nc'])         




b = list(TUDO.columns)
b.remove('TITU')

TUDO_no_dup = TUDO.drop_duplicates(subset=b, keep='first')
TUDO_no_dup = TUDO_no_dup[~pd.notnull(TUDO_no_dup['Tap'])]
TUDO_no_dup = TUDO_no_dup.sort_values(['De','Para', 'Nc'])    
#==============================================================================
# 
# #==============================================================================
# # SEÇÃO DBAR
# #==============================================================================
# 
# 
# 
# 
# for i in range(len(bar)):
#     bar[i] = bar[i][['Num',  'Nome', 'Are']]
#     
#                     #'T', 'Gb',
# #==============================================================================
# #                     
# # merge = res[0].merge(res[1], how='outer', indicator=True)
# # merge = merge[merge['_merge'] != 'both']
# # merge = merge.sort_values(['De', 'Nc'])
# # 
# # #Problema de comparar reatâncias é o ANAT0 dos trafos 
# # #merge = merge[pd.notnull(merge['R'])]
# # 
# # #merge = merge [merge['Tap']]
# # merge = merge.sort_values(['De','Para', 'Nc'])
# # 
# # 
# #==============================================================================
# 
# 
# 
# 
# 
# for i in range(len(bar)):
#     try:
#         if i == 0:
#             temp2 = bar[i].merge(bar[i+1], how='outer', indicator=True)
#             temp2 = temp2[temp2['_merge'] != 'both']
#             temp2 = temp2.drop('_merge', axis=1)
#         elif i < len(bar)-1:
#             temp2 = temp2.merge(bar[i+1], how='outer', indicator=True)
#             temp2 = temp2[temp2['_merge'] != 'both']
#             temp2 = temp2.drop('_merge', axis=1)
#         elif i == len(bar):
#             #temp2 = temp2.merge(bar[i], how='outer', indicator=True)
#             temp2 = temp2[temp2['_merge'] != 'both']
#             #temp2 = temp2.drop('_merge', axis=1)
#     except IndexError:
#         print("Erro index " + str(i))
#         
# #temp2 = temp2[~pd.notnull(temp2['Tap'])]        
# temp2 = temp2.sort_values(['Num'])       
# 
# 
# #temp = temp.drop_duplicates(subset='De', keep=False)
# 
# 
#==============================================================================


