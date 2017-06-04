#-*- coding: utf-8 -*-
   
def saida_pwf_agregadores(dbar, nome):
    
    a = dbar[['Num','O','A1', 'A2', 'A3', 'A4', 'A5', 'A6']]
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
    
    numpy.savetxt(nome +'.pwf',
                  a,
                  fmt=('%5.f',o_espacos ,'%3s','%3s','%3s','%3s','%3s','%3s'),
                  header = 'dbar\n(Num)OETGb(   nome   )Gl( V)( A)( Pg)( Qg)( Qn)( Qm)(Bc  )( Pl)( Ql)( Sh)Are(Vf)M(1)(2)(3)(4)(5)(6)(7)(8)(9)(10',
                  footer = '99999',
                  comments ='',
                  delimiter='')
    return