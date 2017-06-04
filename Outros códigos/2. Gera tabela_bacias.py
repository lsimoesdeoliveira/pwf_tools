# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 14:33:01 2016

@author: lucas-s.oliveira
"""

#Estão presentes dois métodos de atribuição das bacias:
# 1 - tradutor_bacias usa a Aba 'Usinas' da planilha de redespacho, varrendo todas as barras e 
#     encontrado as bacias correspondentes.
#     limitações: Bacias que não possuem nenhuma barra atribuida não aparecerão no tradutor, causando uma
#                 numeração descontínua.
#     vantagem: método automatizado, independente da adição de novas bacias ou de mudanças de nomenclatura
# 2 - tradutor_bacias2 usa a lista entrada manualmente (também originada da planilha de redespacho),
#     limitações: A atualização é manual e pode ficar desatualizada, causando erros de nomentclaturas e 
#                 atribuições
#     vantagem: segue uma numeração lógica e com código de formação 'NXX'
#                'N' tipo de fonte geradora - 1 Hidro (PCH E UHE), 2 Eólica, 3 Solar, 4 Nuclear
#                'XX' numero da bacia ou região
   
# Para alternar o método de seleção, escolher qual par das ultimas 4 linhas comentar

import pandas
import numpy
import os
import subprocess



script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
rel_path = "Arquivos Auxiliares/plan_redespacho_v3.1.xlsm"
abs_file_path = os.path.join(script_dir, rel_path)


tab_bacias = pandas.read_excel(abs_file_path,
                          sheetname='Usinas',
                          header = 2,
                          parse_cols = 5)
                          
                         
tab_bacias = tab_bacias.rename(columns={'Unnamed: 4': 'TipoBacia',
                                        'Unnamed: 5': 'Bacia'})    
                                        
tab_bacias['Num_bacia'] = numpy.nan
                                        
tab_bacias['Num_bacia'] = tab_bacias['Bacia'].str[:2].replace(' ', '').astype(float)
tab_bacias['Num_bacia'] = pandas.to_numeric(tab_bacias['Num_bacia'])
tab_bacias['TipoBacia'] = tab_bacias['TIPO'].str[:1].map(str) + tab_bacias['Bacia'].str[:2]

tab_bacias['TIPO'] = tab_bacias['TIPO'].str[:1]


tab_bacias['TIPO'] = tab_bacias['TIPO'].str[:1]

#Filtrando as barras 99999 do arquivo redespacho
#tab_bacias = tab_bacias[tab_bacias['BARRA']<99999]

########################################################################################################

#tradutor_bacias = tab_bacias[['TipoBacia', 'Bacia']]
tradutor_bacias = tab_bacias
tradutor_bacias = tradutor_bacias.drop_duplicates('TipoBacia')
tradutor_bacias = tradutor_bacias[tradutor_bacias['TipoBacia']>0]


tradutor_bacias = tradutor_bacias.sort_values(['TIPO','Num_bacia'], ascending=[True,True])


tradutor_bacias['Num_agregador'] = range(len(tradutor_bacias['TipoBacia']))
tradutor_bacias['Num_agregador'] = tradutor_bacias['Num_agregador'] +1

tradutor_bacias = tradutor_bacias[['Bacia', 'TIPO', 'TipoBacia', 'Num_bacia','Num_agregador']]

########################################################################################################

tradutor_bacias2 = pandas.DataFrame({'Bacia': [
                                    u'1 - Jacuí(RS)',
                                    u'2 - Uruguai(SC)(RS)',
                                    u'3 - Itajaí-Capivari(SC)',
                                    u'4 - Iguaçu(PR)(SC)',
                                    u'5 - Paraná(MS)(SP)(PR)',
                                    u'6 - Paranapanema(SP)(PR)',
                                    u'7 - Tietê(SP)',
                                    u'8 - Grande (MG)(SP)',
                                    u'9 - Paranaíba (MG)(GO)',
                                    u'10 - Paraíba do Sul (SP)(MG)(RJ)',
                                    u'11 - Paraguai(MT)(MS)',
                                    u'12 - Doce-Mucuri (MG)(ES)',
                                    u'13 - Atlântico Leste (MG)(BA)',
                                    u'14 - São Francisco (MG)(BA)(AL)(PE)',
                                    u'15 - Parnaíba (PI)',
                                    u'16 - Tocantins-Araguaia(GO)(TO)(PA)',
                                    u'17 - Teles Pires-Juruena(MT)(PA)',
                                    u'18 - Madeira(RO)(AM)',
                                    u'19 - Amazonas (AM)(PA)(AP)',
                                    u'20 - Araguari (AP)',
                                    u'21 - Atlântico NE Oriental (CE)(RN)(PB)',
                                    u'22 - Atlântico NE Ocidental (MA)',
                                    u'23 - Itaipu 60 Hz (PR) (Bacia do Paraná)',
                                    u'24 - Itaipu 50 Hz (PR) (Bacia do Paraná)',
                                    u'25 - Complexo Madeira (Jirau + S. Ant.)',
                                    u'1 – Delta do Parnaíba (PI)(MA)',
                                    u'2 – Oeste do Ceará (CE)',
                                    u'3 – Leste do Ceará (CE)',
                                    u'4 – João Câmara (RN)',
                                    u'5 – Lagoa Nova (RN)',
                                    u'6 – Campina Grande (PB)(PE)',
                                    u'7 – Angelim (PE)',
                                    u'8 – Caldeirão Grande (PI)(CE)(PE)',
                                    u'9 – Jardim (SE)(BA)',
                                    u'10 – Central da Bahia (BA)',
                                    u'11 – Igaporã (BA)',
                                    u'12 - Coxilha de Santana (RS)',
                                    u'13 - Planalto das Missões (RS)',
                                    u'14 - Serra Gaúcha (RS)',
                                    u'15 - Lagoa dos Patos (RS)',
                                    u'16 - Litoral Sul (RS)',
                                    u'17 - Escudo Rio-Grandense (RS)',
                                    u'18 - Santa Catarina (SC)',
                                    u'19 - Rio de Janeiro (RJ)',
                                    u'1 - Sobral (CE)',
                                    u'2 - Crateús (CE)(PI)',
                                    u'3 - Milagres (CE)(PB)',
                                    u'4 - Mossoró (RN)(CE)',
                                    u'5 - João Câmara (RN)',
                                    u'6 - Natal (RN)',
                                    u'7 - Lagoa Nova (RN)',
                                    u'8 - Campina Grande (PB)',
                                    u'9 - Angelim (PE)(AL)',
                                    u'10 - Bom Nome (PE)',
                                    u'11 - Curral Novo do Piauí (PI)(CE)',
                                    u'12 - São João do Piauí (PI)',
                                    u'13 - Sobradinho (PE)(BA)',
                                    u'14 - Irecê (BA)',
                                    u'15 - Bom Jesus da Lapa (BA)',
                                    u'16 - Igaporã (BA)',
                                    u'17 - Gilbués (PI)',
                                    u'18 - Colinas (TO)',
                                    u'19 - Miracema (TO)',
                                    u'20 - Gurupi (TO)',
                                    u'21 - Dianópolis (TO)',
                                    u'22 - Janaúba (MG)',
                                    u'23 - Pirapora (MG)',
                                    u'24 - Paracatu (MG)',
                                    u'25 - Triângulo (MG)',
                                    u'26 - Goiás (GO)',
                                    u'27 - Oeste de São Paulo (SP)',
                                    u'1 - Angra 1 (RJ)',
                                    u'2 - Angra 2 (RJ)',
                                    u'3 - Angra 3 (RJ)'],

                                    'TipoBacia' : [
                                    'H1',
                                    'H2',
                                    'H3',
                                    'H4',
                                    'H5',
                                    'H6',
                                    'H7',
                                    'H8',
                                    'H9',
                                    'H10',
                                    'H11',
                                    'H12',
                                    'H13',
                                    'H14',
                                    'H15',
                                    'H16',
                                    'H17',
                                    'H18',
                                    'H19',
                                    'H20',
                                    'H21',
                                    'H22',
                                    'H23',
                                    'H24',
                                    'H25',
                                    'E1',
                                    'E2',
                                    'E3',
                                    'E4',
                                    'E5',
                                    'E6',
                                    'E7',
                                    'E8',
                                    'E9',
                                    'E10',
                                    'E11',
                                    'E12',
                                    'E13',
                                    'E14',
                                    'E15',
                                    'E16',
                                    'E17',
                                    'E18',
                                    'E19',
                                    'S1',
                                    'S2',
                                    'S3',
                                    'S4',
                                    'S5',
                                    'S6',
                                    'S7',
                                    'S8',
                                    'S9',
                                    'S10',
                                    'S11',
                                    'S12',
                                    'S13',
                                    'S14',
                                    'S15',
                                    'S16',
                                    'S17',
                                    'S18',
                                    'S19',
                                    'S20',
                                    'S21',
                                    'S22',
                                    'S23',
                                    'S24',
                                    'S25',
                                    'S26',
                                    'S27',
                                    'N1',
                                    'N2',
                                    'N3'],
                    'Num_agregador' : [
                                    101,
                                    102,
                                    103,
                                    104,
                                    105,
                                    106,
                                    107,
                                    108,
                                    109,
                                    110,
                                    111,
                                    112,
                                    113,
                                    114,
                                    115,
                                    116,
                                    117,
                                    118,
                                    119,
                                    120,
                                    121,
                                    122,
                                    123,
                                    124,
                                    125,
                                    201,
                                    202,
                                    203,
                                    204,
                                    205,
                                    206,
                                    207,
                                    208,
                                    209,
                                    210,
                                    211,
                                    212,
                                    213,
                                    214,
                                    215,
                                    216,
                                    217,
                                    218,
                                    219,
                                    301,
                                    302,
                                    303,
                                    304,
                                    305,
                                    306,
                                    307,
                                    308,
                                    309,
                                    310,
                                    311,
                                    312,
                                    313,
                                    314,
                                    315,
                                    316,
                                    317,
                                    318,
                                    319,
                                    320,
                                    321,
                                    322,
                                    323,
                                    324,
                                    325,
                                    326,
                                    327,
                                    401,
                                    402,
                                    403]}
)







#dbar_bacias = pandas.merge(tab_bacias, tradutor_bacias, how='inner', left_on='TipoBacia', right_on='TipoBacia')
#
#dbar_bacias = dbar_bacias[['BARRA', 'Num_agregador']]

dbar_bacias = pandas.merge(tab_bacias, tradutor_bacias2, how='inner', left_on='Bacia', right_on='Bacia')

dbar_bacias = dbar_bacias[['BARRA', 'Num_agregador']]