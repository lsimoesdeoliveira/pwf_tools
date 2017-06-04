import pandas as pd

tradutor_estados = pd.DataFrame({
                         'estado':['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
                                   'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR',
                                   'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'],
                         'estado_cod':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                       23, 24, 25, 26, 27]
                                       })           
                                        
tradutor_regiao = pd.DataFrame({
                         'estado':['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
                                   'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR',
                                   'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'],
                         'estado_cod':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
                                       13, 14, 15, 16, 17, 18, 19, 20, 21, 22,
                                       23, 24, 25, 26, 27],
                         'regiao_get':['NORTE', 'NORDESTE', 'NORTE', 'NORTE',
                                       'NORDESTE', 'NORDESTE', 'CENTRO OESTE',
                                       'SUDESTE', 'CENTRO OESTE', 'NORTE', 'SUDESTE',
                                       'SUDESTE', 'CENTRO OESTE', 'NORTE', 'NORDESTE',
                                       'NORDESTE', 'NORDESTE', 'SUL', 'SUDESTE', 'NORDESTE',
                                       'NORTE', 'NORTE', 'SUL', 'SUL', 'NORDESTE', 'SUDESTE',
                                       'NORTE'],                                      
                         'regiao_get_cod':[1, 2, 1, 1, 2, 2, 3, 4, 3, 1, 4,
                                           4, 3, 1, 2, 2, 2, 5, 4, 2, 1, 1,
                                           5, 5, 2, 4,1 ]
                        })                                       
                                            
tradutor_tipo_geracao = pd.DataFrame({
                        'Sigla': ['CER','EOL','PCH','SIN','UHE','UNE','UTE', 'UFV'],
                        'Cod':   [  1,    2,    3,    4,    5,    6,    7,     8]
                        })
                                       
tradutor_tipo_PD = pd.DataFrame({
                        'cod' : [1,2,3,4,5,6,6,6,6,7,8,8,8,8,9,10,10,10,11],
                        'sigla' : ['B','C','D','DF','E','G','GL','GM','GP','GF',
                                   'H','HL','HM','HP','HF','NL','NM','NP','P'],
                        'desc' : ['Biomassa'       ,
                                'Diesel'            ,
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
