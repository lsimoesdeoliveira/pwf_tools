# -*- coding: utf-8 -*-
"""
Created on 28/05/2017

@author: lucas-s.oliveira
"""


import pandas as pd
import numpy as np
import io


def read_pwf(path_to_file):

    # DEFINIÇÃO LARGURAS ======================================================

    TITUw = (80,)
    DOPCw = (4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1,
             1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1, 1, 4, 1, 1)
    DCTEw = (4, 1, 6, 1, 4, 1, 6, 1, 4, 1, 6, 1, 4, 1, 6, 1, 4, 1, 6, 1, 4,
             1, 6)
    DBARw = (5, 1, 1, 1, 2, 12, 2, 4, 4, 5, 5, 5, 5, 6, 5, 5, 5, 3, 4, 1, 3, 3,
             3, 3, 3, 3, 3, 3, 3, 3)
    DLINw = (5, 1, 1, 1, 1, 1, 5, 2, 1, 1, 1, 6, 6, 6, 5, 5, 5, 5, 6, 4, 4, 2,
             4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
    DCSCw = (5, 1, 1, 1, 1, 5, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 6, 6, 6, 1, 1, 6,
             1, 5, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3)
    # DBSHw =
    DSHLw = (5, 1, 1, 1, 1, 5, 2, 1, 6, 6, 1, 2, 1, 2)
    # DCARw =
    DCERw = (5, 1, 1, 1, 2, 1, 2, 1, 5, 1, 6, 1, 5, 5, 5, 1, 1, 1, 1)
    DCTRw = (5, 1, 1, 1, 5, 1, 2, 1, 4, 1, 4, 1, 1, 1, 1, 1, 6, 1, 6, 1, 1, 1,
             6, 1, 5, 1, 2)
    DGLTw = (2, 1, 5, 1, 5, 1, 5, 1, 5)
    DAREw = (3, 1, 1, 1, 1, 6, 1, 1, 1, 1, 1, 36, 1, 6, 1, 6)
    DTPFw = (5, 1, 5, 1, 2, 1, 5, 1, 5, 1, 2, 1, 5, 1, 5, 1, 2, 1, 5, 1, 5, 1,
             2, 1, 5, 1, 5, 1, 2, 1, 1)
    DELOw = (4, 1, 1, 1, 5, 1, 5, 1, 20, 1, 1, 1, 1)
    DCBAw = (4, 1, 1, 1, 1, 1, 12, 2, 5, 38, 5, 4)
    DCLIw = (4, 1, 1, 1, 1, 4, 2, 1, 1, 1, 6, 6, 31, 4)
    DCNVw = (4, 1, 1, 1, 5, 1, 4, 1, 4, 1, 1, 1, 1, 1, 5, 1, 5, 1, 5, 1, 5, 1,
             5, 1, 5, 1, 5, 1, 2)
    DCCVw = (4, 1, 1, 1, 1, 1, 1, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1, 5, 1,
             5, 1, 2, 1, 4, 1, 5, 1, 5)
    DGBTw = (2, 1, 5)
    DCMTw = (80, )

    # DEFINIÇÃO NOMES COLUNAS =================================================

    TITUc = ('Titulo', )
    DOPCc = ('Opc', 'Spc', 'E', 'Spc', 'Opc', 'Spc', 'E', 'Spc', 'Opc', 'Spc',
             'E', 'Spc', 'Opc', 'Spc', 'E', 'Spc', 'Opc', 'Spc', 'E', 'Spc',
             'Opc', 'Spc', 'E', 'Spc', 'Opc', 'Spc', 'E', 'Spc', 'Opc', 'Spc',
             'E', 'Spc', 'Opc', 'Spc', 'E', 'Spc', 'Opc', 'Spc', 'E')
    DCTEc = ('Mn', 'Spc', 'Val', 'Spc', 'Mn', 'Spc', 'Val', 'Spc', 'Mn', 'Spc',
             'Val', 'Spc', 'Mn', 'Spc', 'Val', 'Spc', 'Mn', 'Spc', 'Val',
             'Spc', 'Mn', 'Spc', 'Val')
    DBARc = ('Num', 'O', 'E', 'T', 'Gb', 'Nome', 'Gl', 'V', 'A', 'Pg', 'Qg',
             'Qn', 'Qm', 'Bc', 'Pl', 'Ql', 'Sh', 'Are', 'Vf', 'M', 'A1', 'A2',
             'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10')
    DLINc = ('De', 'Dde', 'Spc', 'O', 'Spc', 'Dpara', 'Para', 'Nc', 'E', 'P',
             'Spc', 'R', 'X', 'Mvar', 'Tap', 'Tmn', 'Tmx', 'Phs', 'Bc', 'Cn',
             'Ce', 'Ns', 'Cq', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8',
             'A9', 'A10')
    DSHLc = ('De', 'Spc', 'O', 'Spc', 'Spc', 'Para', 'Nc', 'Spc', 'Shde',
             'Shpa', 'Spc', 'Ed', 'Spc', 'Ep')
    DCSCc = ('De', 'Spc', 'O', 'Spc', 'Spc', 'Para', 'Nc', 'E', 'P', 'B',
             'Spc', 'Spc', 'Spc', 'Spc', 'Spc', 'Spc', 'Xmin', 'Xmax', 'Xv',
             'C', 'Spc', 'Vsp', 'Spc', 'Ext', 'Nst', 'A1', 'A2', 'A3', 'A4',
             'A5', 'A6', 'A7', 'A8', 'A9', 'A10')
    DCERc = ('Num', 'Spc', 'O', 'Spc', 'Gr', 'Spc', 'Un', 'Spc', 'Kb', 'Spc',
             'Incl', 'Spc', 'Qg', 'Qn', 'Qm', 'Spc', 'C', 'Spc', 'E')
    DCTRc = ('De', 'Spc', 'O', 'Spc', 'Para', 'Spc', 'Nc', 'Spc', 'Vmin',
             'Spc', 'Vmax', 'Spc', 'C', 'Spc', 'M', 'Spc', 'Fmin', 'Spc',
             'Fmax', 'Spc', 'C', 'Spc', 'Vsp', 'Spc', 'Ext', 'Spc', 'Ns')
    DGLTc = ('G', 'Spc', 'Vmn', 'Spc', 'Vmx', 'Spc', 'Vmne', 'Spc', 'Vmxe')
    DAREc = ('Ar', 'Spc', 'Spc', 'Spc', 'Spc', 'Xchg', 'Spc', 'Spc', 'Spc',
             'Spc', 'Spc', 'Nome', 'Spc', 'Xmin', 'Spc', 'Xmax')
    DTPFc = ('De', 'Spc', 'Para', 'Spc', 'Nc', 'Spc', 'De', 'Spc', 'Para',
             'Spc', 'Nc', 'Spc', 'De', 'Spc', 'Para', 'Spc', 'Nc', 'Spc', 'De',
             'Spc', 'Para', 'Spc', 'Nc', 'Spc', 'De', 'Spc', 'Para', 'Spc',
             'Nc', 'Spc', 'O')
    DELOc = ('Num', 'Spc', 'O', 'Spc', 'V', 'Spc', 'P', 'Spc', 'Id', 'Spc',
             'M', 'Spc', 'E')
    DCBAc = ('Num', 'Spc', 'O', 'Spc', 'T', 'P', 'Nome', 'Gl', 'Vd', 'Tab',
             'Rs', 'Elo')
    DCLIc = ('De', 'Spc', 'O', 'Spc', 'Spc', 'Para', 'Nc', 'Spc', 'P', 'Spc',
             'R', 'L', 'Tab', 'Cn')
    DCNVc = ('Num', 'Spc', 'O', 'Spc', 'Ca', 'Spc', 'Cc', 'Spc', 'El', 'Spc',
             'T', 'Spc', 'P', 'Spc', 'Ino', 'Spc', 'Xc', 'Spc', 'Vfs', 'Spc',
             'Snt', 'Spc', 'Rra', 'Spc', 'Lra', 'Spc', 'Ccc', 'Spc', 'Fr')
    DCCVc = ('Num', 'Spc', 'O', 'Spc', 'F', 'M', 'C', 'Spc', 'Vsp', 'Spc',
             'Marg', 'Spc', 'Imax', 'Spc', 'Dsp', 'Spc', 'Dtn', 'Spc', 'Dtm',
             'Spc', 'Tmn', 'Spc', 'Tmx', 'Spc', 'S', 'Spc', 'Vmn', 'Spc',
             'Tmh', 'Spc', 'Ttr')
    DGBTc = ('G', 'Spc', 'Kv')
    DCMTc = ('Comentario', )

    # DEFINIÇÃO DICIONARIOS ===================================================

    dictDADOS = {
        'TITU': [],
        'DOPC': [],
        'DCTE': [],
        'DBAR': [],
        'DLIN': [],
        'DCSC': [],
        # 'DBSH': [],
        'DSHL': [],
        'DCAR': [],
        'DCER': [],
        'DCTR': [],
        'DGLT': [],
        'DARE': [],
        'DTPF': [],
        'DELO': [],
        'DCBA': [],
        'DCLI': [],
        'DCNV': [],
        'DCCV': [],
        'DGBT': [],
        'DCMT': []
    }

    dictWidth = {
        'TITU': TITUw,
        'DOPC': DOPCw,
        'DCTE': DCTEw,
        'DBAR': DBARw,
        'DLIN': DLINw,
        'DCSC': DCSCw,
        # 'DBSH': DBSHw,
        'DSHL': DSHLw,
        'DCER': DCERw,
        'DCTR': DCTRw,
        'DGLT': DGLTw,
        'DARE': DAREw,
        'DTPF': DTPFw,
        'DELO': DELOw,
        'DCBA': DCBAw,
        'DCLI': DCLIw,
        'DCNV': DCNVw,
        'DCCV': DCCVw,
        'DGBT': DGBTw,
        'DCMT': DCMTw,

    }

    dictNomesColunas = {
        'TITU': TITUc,
        'DOPC': DOPCc,
        'DCTE': DCTEc,
        'DBAR': DBARc,
        'DLIN': DLINc,
        'DCSC': DCSCc,
        # 'DBSH': DBSHc,
        'DSHL': DSHLc,
        'DCER': DCERc,
        'DCTR': DCTRc,
        'DGLT': DGLTc,
        'DARE': DAREc,
        'DTPF': DTPFc,
        'DELO': DELOc,
        'DCBA': DCBAc,
        'DCLI': DCLIc,
        'DCNV': DCNVc,
        'DCCV': DCCVc,
        'DGBT': DGBTc,
        'DCMT': DCMTc
    }

    codExec = (
        'TITU',
        'DOPC',
        'DCTE',
        'DBAR',
        'DLIN',
        'DCSC',
        'DBSH',
        'DSHL',
        'DCAR',
        'DCER',
        'DCTR',
        'DGLT',
        'DARE',
        'DTPF',
        'DELO',
        'DCBA',
        'DCLI',
        'DCNV',
        'DCCV',
        'DGBT',
        'DCMT')

    execAtual = False

    with open(path_to_file, 'r') as file:
        for line in file:
            line = line.strip('\n')
            if line[:4] in codExec:
                execAtual = line[:4]
                buffer = io.StringIO()
                continue

            if line != '99999' and line != 'FIM' and execAtual in codExec:
                try:
                    buffer.write(line + '\n')
                except:
                    print('falha durante a escrita no buffer do CodExec ' +
                          execAtual)
                    break
            if line == '99999' or (line[:4] in codExec):
                try:
                    buffer.seek(0)
                    dictDADOS[execAtual] = pd.read_fwf(
                        buffer,
                        widths=dictWidth[execAtual],
                        names=dictNomesColunas[execAtual],
                        comment='(')
                    buffer.close()
                except:
                    pass
    file.close()

    return dictDADOS


def gen_agregadores(dbar, dlin, regioes=False, geracao=False, gera_dlin=True):

    tradutor_estados = pd.DataFrame({
        'estado': ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO',
                   'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR',
                   'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'],
        'estado_cod': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,
                       16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27],
        'regiao_get': ['N', 'NE', 'N', 'N', 'NE', 'NE', 'CO', 'SE', 'CO',
                       'N', 'SE', 'SE', 'CO', 'N', 'NE', 'NE', 'NE', 'S',
                       'SE', 'NE', 'N', 'N', 'S', 'S', 'NE', 'SE', 'N'],
        'regiao_get_cod': [1, 2, 1, 1, 2, 2, 3, 4, 3, 1, 4, 4, 3, 1, 2,
                           2, 2, 5, 4, 2, 1, 1, 5, 5, 2, 4, 1]
    })

    tradutor_tipo_geracao = pd.DataFrame({
        'Sigla': ['CER', 'EOL', 'PCH', 'SIN', 'UHE', 'UNE', 'UTE', 'UFV'],
        'Cod': [1, 2, 3, 4, 5, 6, 7, 8]
    })

    # dbar_estados contem todas as barras que possuem nos espaços 7 e 8 do
    # Nome valoes contidos em tradutor_estados
    dbar_estados = dbar[dbar['Nome'].str[7:9].isin(tradutor_estados['estado'])]

    dbar_estados.loc[:, 'A1'] = dbar_estados.loc[:, 'Nome'].str[7:9]

    dbar_estados = pd.merge(dbar_estados,
                            tradutor_estados,
                            how='inner',
                            left_on='A1',
                            right_on='estado')

    dbar_estados['A1'] = dbar_estados['estado_cod']

    # Removendo o agregador de UF das barras que tem CAP e TAP no nome
    # Capacitores e Tapes estavam sendo marcadas no Amapá
    dbar_estados.loc[dbar_estados['Nome'].str[6:9] == 'CAP', 'A1'] = np.nan
    dbar_estados.loc[dbar_estados['Nome'].str[6:9] == 'TAP', 'A1'] = np.nan

    dbar_estados = dbar_estados[['Num', 'A1']]
    dbar = pd.merge(dbar, dbar_estados, how='outer', on='Num')

    dbar['A1_x'] = dbar['A1_y']

    dbar = dbar.rename(columns={'A1_x': 'A1'})
    del dbar['A1_y']

    # PROCURANDO NA VIZINHANÇA - BARRA DE ======================================

    dbar_restante = dbar[pd.isnull(dbar['A1'])]

    match_de = pd.merge(dbar_restante,
                        dlin, left_on='Num',
                        right_on='De',
                        how='inner')

    match_de = match_de[['Num', 'De', 'Para']]
    match_de = match_de[match_de['Para'] > 0]
    match_de = match_de.merge(dbar, left_on='Para', right_on='Num', how='left')
    match_de = match_de[['De', 'A1']]

    dbar_temp = pd.merge(dbar,
                         match_de,
                         left_on='Num',
                         right_on='De',
                         how='left')

    # combine_first onde houver NaN em A1_x ele atualiza com os valores de A1_y
    dbar_temp['A1_x'] = dbar_temp['A1_x'].combine_first(dbar_temp['A1_y'])

    dbar_temp = dbar_temp.rename(columns={'A1_x': 'A1'})
    del dbar_temp['A1_y']
    del dbar_temp['De']

    dbar_temp = dbar_temp.sort_values(by=['Num', 'A1'], ascending=[True, True])

    dbar_temp = dbar_temp.drop_duplicates(subset='Num',
                                          keep='first',
                                          inplace=False)

    dbar = dbar_temp

    dbar_restante = dbar[pd.isnull(dbar['A1'])]

    # PROCURANDO NA VIZINHANÇA - BARRA PARA ====================================

    match_para = pd.merge(dbar_restante,
                          dlin, left_on='Num',
                          right_on='Para',
                          how='inner')

    match_para = match_para[match_para['De'] > 0]
    match_para = match_para[['Num', 'De', 'Para']]
    match_para = match_para.merge(dbar, left_on='De', right_on='Num', how='left')
    match_para = match_para[['Para', 'A1']]

    dbar_temp = pd.merge(dbar, match_para, left_on='Num', right_on='Para', how='left')
    dbar_temp['A1_x'] = dbar_temp['A1_x'].combine_first(dbar_temp['A1_y'])

    dbar_temp = dbar_temp.rename(columns={'A1_x': 'A1'})
    del dbar_temp['A1_y']
    del dbar_temp['Para']

    dbar_temp = dbar_temp.sort_values(by=['Num', 'A1'], ascending=[True, True])
    dbar_temp = dbar_temp.drop_duplicates(subset='Num', keep='first', inplace=False)

    dbar = dbar_temp

    dbar_restante = dbar[pd.isnull(dbar['A1'])]

    # Atribuindo UF de barras CAP ao mesmo da barra com retância negativa
    # =======================================================================

    '''Match_de'''
    dbar_cap = dbar[dbar['Nome'].str[6:9] == 'CAP'][['Num', 'Nome', 'A1']]

    match_de = pd.merge(dbar_cap,
                        dlin,
                        left_on='Num',
                        right_on='De',
                        how='inner')

    match_de = match_de[['Num', 'De', 'Para', 'X']]
    match_de = match_de[match_de['X'] < 0]
    match_de = match_de.merge(dbar, left_on='Para', right_on='Num', how='left')
    match_de = match_de[['De', 'A1']]

    dbar_temp = pd.merge(dbar, match_de, left_on='Num', right_on='De', how='left')
    dbar_temp['A1_y'] = dbar_temp['A1_y'].combine_first(dbar_temp['A1_x'])
    dbar_temp['A1_x'] = dbar_temp['A1_y']
    dbar_temp = dbar_temp.rename(columns={'A1_x': 'A1'})

    del dbar_temp['A1_y']
    del dbar_temp['De']

    dbar = dbar_temp

    '''Match_Para'''

    dbar_cap = dbar[dbar['Nome'].str[6:9] == 'CAP'][['Num', 'Nome', 'A1']]

    match_para = pd.merge(dbar_cap,
                          dlin,
                          left_on='Num',
                          right_on='Para',
                          how='inner')

    match_para = match_para[['Num', 'De', 'Para', 'X']]
    match_para = match_para[match_para['X'] < 0]
    match_para = match_para.merge(dbar, left_on='De', right_on='Num', how='left')
    match_para = match_para[['Para', 'A1']]

    dbar_temp = pd.merge(dbar, match_para, left_on='Num', right_on='Para', how='left')
    dbar_temp['A1_y'] = dbar_temp['A1_y'].combine_first(dbar_temp['A1_x'])
    dbar_temp['A1_x'] = dbar_temp['A1_y']
    dbar_temp = dbar_temp.rename(columns={'A1_x': 'A1'})

    del dbar_temp['A1_y']
    del dbar_temp['Para']

    dbar = dbar_temp

    # Atribuindo UF das barras com TAP ao da barra com menor retância
    # ==========================================================================

    '''Match_De'''

    dbar_tap = dbar[dbar['Nome'].str[6:9] == 'TAP'][['Num', 'Nome', 'A1']]

    match_de = pd.merge(dbar_tap,
                        dlin,
                        left_on='Num',
                        right_on='De',
                        how='inner')

    match_de = match_de[['Num', 'De', 'Para', 'X']]
    match_de = match_de[match_de['Para'] > 0]
    match_de = match_de.merge(dbar, left_on='Para', right_on='Num', how='left')
    match_de = match_de[['De', 'A1', 'X', 'Nome']]

    # Retirando as ligações entre Duas barras TAP
    match_de = match_de[match_de['Nome'].str[6:9] != 'TAP']
    # Organizando pelos menores valores de Reatância, para escolher a barra eletricamente mais próxima
    match_de = match_de.sort_values(by=['De', 'X'], ascending=[True, True])
    match_de = match_de.drop_duplicates(subset='De', keep='first', inplace=False)

    dbar_temp = pd.merge(dbar, match_de, left_on='Num', right_on='De', how='left')
    dbar_temp['A1_x'] = dbar_temp['A1_y'].combine_first(dbar_temp['A1_x'])

    dbar_temp = dbar_temp.rename(columns={'A1_x': 'A1'})
    dbar_temp = dbar_temp.rename(columns={'Nome_x': 'Nome'})

    del dbar_temp['A1_y']
    del dbar_temp['De']
    del dbar_temp['Nome_y']
    del dbar_temp['X']

    dbar_temp = dbar_temp.drop_duplicates(subset='Num', keep='first', inplace=False)

    dbar = dbar_temp

    '''Match_Para'''

    dbar_tap = dbar[dbar['Nome'].str[6:9] == 'TAP'][['Num', 'Nome', 'A1']]

    match_para = pd.merge(dbar_tap,
                          dlin,
                          left_on='Num',
                          right_on='Para',
                          how='inner')

    match_para = match_para[['Num', 'De', 'Para', 'X']]
    match_para = match_para[match_para['De'] > 0]
    match_para = match_para.merge(dbar, left_on='De', right_on='Num', how='left')
    match_para = match_para[['Para', 'A1', 'X', 'Nome']]

    # Retirando as ligações entre Duas barras TAP
    match_para = match_para[match_para['Nome'].str[6:9] != 'TAP']
    # Organizando pelos menores valores de Reatância, (Objetivo: escolher a barra mais próxima)
    match_para = match_para.sort_values(['Para', 'X'], ascending=[True, True])
    match_para = match_para.drop_duplicates(subset='Para', keep='first', inplace=False)

    dbar_temp = pd.merge(dbar, match_para, left_on='Num', right_on='Para', how='left')
    dbar_temp['A1_x'] = dbar_temp['A1_y'].combine_first(dbar_temp['A1_x'])

    dbar_temp = dbar_temp.rename(columns={'A1_x': 'A1'})
    dbar_temp = dbar_temp.rename(columns={'Nome_x': 'Nome'})

    del dbar_temp['A1_y']
    del dbar_temp['Para']
    del dbar_temp['Nome_y']
    del dbar_temp['X']

    dbar_temp = dbar_temp.drop_duplicates(subset='Num', keep='first', inplace=False)

    dbar = dbar_temp

    # Atribuindo regiões (N, NE, CO, SE, S) às barras
    # ==========================================================================

    if regioes:
        dbar_restante = dbar[pd.isnull(dbar['A1'])]

        dbar_temp = pd.merge(dbar,
                             tradutor_estados,
                             how='outer',
                             left_on='A1',
                             right_on='estado_cod')

        dbar_temp.loc[:, 'A3'] = dbar_temp.loc[:, 'regiao_get_cod']

        del dbar_temp['estado']
        del dbar_temp['estado_cod']
        del dbar_temp['regiao_get']
        del dbar_temp['regiao_get_cod']

        dbar = dbar_temp

    # Atribuindo tipos barras - de acordo com os caracteres 7, 8 e 9 do campo Nome
    # ==========================================================================

    if geracao:
        dbar_temp = dbar

        dbar_tipo = dbar_temp[dbar_temp['Nome'].str[6:9].isin(tradutor_tipo_geracao['Sigla'])]
        dbar_tipo.loc[:, 'A4'] = dbar_tipo['Nome'].str[6:9]

        dbar_tipo = pd.merge(dbar_tipo,
                             tradutor_tipo_geracao,
                             how='inner',
                             left_on='A4',
                             right_on='Sigla')

        dbar_tipo['A4'] = dbar_tipo['Cod']
        dbar_tipo = dbar_tipo[['Num', 'A4']]

        dbar_temp = pd.merge(dbar_temp,
                             dbar_tipo,
                             how='outer',
                             left_on='Num',
                             right_on='Num')

        dbar_temp['A4_x'] = dbar_temp['A4_y']

        dbar_temp = dbar_temp.rename(columns={'A4_x': 'A4'})

        del dbar_temp['A4_y']

        dbar = dbar_temp

    # Agregadores para o DLIN
    # ==========================================================================

    if gera_dlin:
        temp = dlin

        match_de = pd.merge(dlin, dbar, left_on='De', right_on='Num', how='left')
        match_de['A1_x'] = match_de['A1_y']
        match_de = match_de.rename(columns={'A1_x': 'A1'})
        temp['A1'] = match_de['A1']

        match_para = pd.merge(dlin, dbar, left_on='Para', right_on='Num', how='left')
        match_para['A1_x'] = match_para['A1_y']
        match_para = match_para.rename(columns={'A1_x': 'A1'})
        temp['A2'] = match_para['A1']

        # Usando apenas as linhas que estão contidas dentro de um mesmo estado, para
        # não criar outro agregador

        temp2 = pd.merge(dlin, temp, on=['De', 'Para', 'Nc'], how='left')

        dlin['A1'] = temp2['A1_y']
        dlin['A2'] = temp2['A2_y']

    return dbar, dlin


def saida_pwf_agregadores(dbar, nome):

    a = dbar[['Num', 'O', 'A1', 'A2', 'A3', 'A4', 'A5', 'A6']]
    a = a.sort_values(by='Num')

    a['O'] = 'M'
    a['O'] = a['O'].map('{:.1s}'.format)
    a['A1'] = a['A1'].map('{:.0f}'.format)
    a['A2'] = a['A2'].map('{:.0f}'.format)
    a['A3'] = a['A3'].map('{:.0f}'.format)
    a['A4'] = a['A4'].map('{:.0f}'.format)
    a['A5'] = a['A5'].map('{:.0f}'.format)
    a['A6'] = a['A6'].map('{:.0f}'.format)

    a = a.replace(to_replace='nan', value='   ')

    o_espacos = '%1s''                                                                           '

    np.savetxt(nome + '.pwf',
               a,
               fmt=('%5.f', o_espacos, '%3s', '%3s', '%3s', '%3s', '%3s', '%3s'),
               header='dbar\n(Num)OETGb(   nome   )Gl( V)( A)( Pg)( Qg)( Qn)( Qm)(Bc  )( Pl)( Ql)( Sh)Are(Vf)M(1)(2)(3)(4)(5)(6)(7)(8)(9)(10',
               footer='99999',
               comments='',
               delimiter='')
    return


def write_excel(dict_dataframes, path_to_file='Resultado.xlsx'):
    writer = pd.ExcelWriter(path_to_file, engine='xlsxwriter')
    for key in dict_dataframes:
        if len(dict_dataframes[key]) > 0:
            dict_dataframes[key].to_excel(writer, sheet_name=key)
    writer.save()
    return 0
