#=================================================================================================
# Atribuindo subtipos barras - de acordo com a classificação da Tabela de Despacho do PD
#=================================================================================================   

#Importado de outro aquivo
tab_PD = tab_PD[['BARRA','cod']]

temp = pandas.merge(dbar, tab_PD, left_on='Num', right_on='BARRA', how='left')

temp['A5'] = temp['cod']

del temp['BARRA']
del temp['cod']

dbar = temp


# Atribuindo bacias das barras - de acordo com a classificação da Planilha de Redespacho
temp = pandas.merge(dbar, dbar_bacias, left_on='Num', right_on='BARRA', how='left')
temp['A6'] = temp['Num_agregador']
temp = temp.drop_duplicates('Num')
del temp['BARRA']
del temp['Num_agregador']
dbar = temp
dbar['A6'] = numpy.nan
#=================================================================================================



# Gerando arquivos de saída
#=================================================================================================
funcoes.saida_pwf_agregadores(dbar, 'agregadores_'+ nome_arquivo[:-4])
#=================================================================================================   




#=================================================================================================
#Gerando arquivo saida para o DLIN
#=================================================================================================
a = dlin[['De','O','Pa','Nc','A1', 'A2']]
a = a.sort_values(by='De')

a['O'] = 'M'

a['O'] = a['O'].map('{:.1s}'.format)
a['A1'] = a['A1'].map('{:.0f}'.format)
a['A2'] = a['A2'].map('{:.0f}'.format)

a = a.replace(to_replace='nan', value='   ')

o_espacos ='  ''%1s''  '
nc_espacos ='%2.f''       '

#usando o f_handle para abrir o arquivo já existente - criado pelo dbar - e adicionar os dados do dlin
with open('agregadores_'+nome_arquivo,'ab') as f_handle:
    numpy.savetxt(f_handle,
                  a,
                  fmt=('%5.f',o_espacos ,'%5.f',nc_espacos,'%3s','%3s'),
                  header = 'dlin\n(De )d O d(Pa )NcEP ( R% )( X% )(Mvar)(Tap)(Tmn)(Tmx)(Phs)(Bc  )(Cn)(Ce)Ns(Cq)(1)(2)(3)(4)(5)(6)(7)(8)(9)(10',
                  footer = '99999\nFIM',
                  comments ='',
                  delimiter='')
#=================================================================================================