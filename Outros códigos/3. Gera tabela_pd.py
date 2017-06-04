# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:33:01 2016

@author: lucas-s.oliveira
"""


import pandas
import os

script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Arquivos Auxiliares\DESPACHO_21_01_16_NORTE EXPORTADOR_CVU_PESADA.xls"
abs_file_path = os.path.join(script_dir, rel_path)


tab_PD = pandas.read_excel(abs_file_path,
                          sheetname='USINAS',
                          header = 2,
                          parse_cols = 3,
                          index_col=None)

tab_PD = tab_PD[tab_PD['BARRA'].apply(lambda x: isinstance(x, (int, float)))]

tab_PD = tab_PD.drop_duplicates('BARRA')

tradutor_tipo_PD = pandas.DataFrame({
                        'cod' : [1,2,3,4,5,6,6,6,6,7,8,8,8,8,9,10,10,10,11],
                        'sigla' : ['B','C','D','DF','E','G','GL','GM','GP','GF',
                                   'H','HL','HM','HP','HF','NL','NM','NP','P'],
                        'desc' : ['Biomassa'       ,
                                'Disel'            ,
                                'Carvão'           ,
                                'Disel Fixo'       ,
                                'Eólica'           ,
                                'Gás'              ,
                                'Gás Leve'         ,
                                'Gás Média'        ,
                                'Gás Pesada'       ,
                                'Gás Fixo'         ,
                                'Hidráulica'       ,
                                'Hidráulica Leve'  ,
                                'Hidráulica Média' ,
                                'Hidráulica Pesada',
                                'Hidráulica Fixa'  ,
                                'Nuclear Leve'     ,
                                'Nuclear Média'    ,
                                'Nuclear Pesada'   ,
                                'PCH'              ]
                        })
                        
                        
                        
tab_PD = pandas.merge(tab_PD, tradutor_tipo_PD, left_on='TIPO', right_on='sigla', how='left')                       