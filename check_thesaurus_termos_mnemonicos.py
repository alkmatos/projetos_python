import pandas as pd
import numpy as np
import sys
import warnings

warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('display.max_columns', None)

#* LOAD ATRIBUTOS
#atributos="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\medallia\\ATRIBUTOS_MEDALIA_NATUREZA.xlsx"
atributos="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CRM\\ID_226\\ATRIBUTOS_CRM_NATUREZA.xlsx"
dfAtributos = pd.read_excel(atributos, sheet_name=0, engine='openpyxl', dtype=str)
dfAtributos.fillna(value="NULO" ,inplace=True)


#** VALIDANDO ATRIBUTOS E NATUREZA, SE FALTA INFORMAÇÃO DE NATUREZA
check_quant_atributo = dfAtributos['ATRIBUTO'] != 'NULO'
countAt = len(dfAtributos[check_quant_atributo])
check_quant_natureza = dfAtributos['NATUREZA'] != 'NULO'
countNat = len(dfAtributos[check_quant_natureza])

if countAt != countNat:
    print("******** EXISTEM ATRIBUTOS SEM NATUREZA!!!! ********\n")
else:
    print("******** TODOS OS ATRIBUTOS POSSUEM NATUREZA ********\n")


dfAtributos['AT_NAT']=dfAtributos['ATRIBUTO']+'-'+dfAtributos['NATUREZA']
listAtributosNaturezas = list(dfAtributos['AT_NAT'])


#* LOAD TERMOS
termos="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CRM\\ID_226\\THESAURUS_BIDH_TERMOS.xlsx"
dfTermos = pd.read_excel(termos, sheet_name=1, engine='openpyxl', dtype=str)
dfTermos.fillna(value="SEM_MN" ,inplace=True)
dfTermos['MN_FINAL'] = np.where((dfTermos['MNEMONICO'] == 'SEM_MN') & (dfTermos['MNEMONICO2'] != 'SEM_MN'), \
                                dfTermos['MNEMONICO2'], dfTermos['MNEMONICO'])
dfTermos['TERMO_MNEMONICO']=dfTermos['TERMO']+'-'+dfTermos['MN_FINAL']
listaTermos = list(dfTermos['TERMO'])

#* VALIDA SE OS ATRIBUTOS POSSUEM TERMOS
count=1
ausenciaDeTermo=1
atributoSemTermo=0
for at_nat in listAtributosNaturezas:
    ausenciaDeTermo = 1
    atributo,natureza = at_nat.split("-")
    for colunaSplitada in atributo.split("_"):
        if colunaSplitada.strip() in listaTermos:
            ausenciaDeTermo = 0
        else:
            ausenciaDeTermo = 1
        if ausenciaDeTermo == 1:
            atributoSemTermo=1
            print('******** ATRIBUTO [{}] COM AUSENCIA DE TERMO [{}]'.format(atributo,colunaSplitada.strip()))
    count += 1
if atributoSemTermo == 0:
    print('******** TODOS OS ATRIBUTOS POSSUEM TERMOS ********')


#** VALIDANDO MNEMONICOS NOS TERMOS
mask = dfTermos['MN_FINAL'] == 'SEM_MN'
count = len(dfTermos[mask])
if count == 0:
    print("\n******** TODOS OS TERMOS POSSUEM MNEMONICOS ********")
else:
    print("\n******** EXISTEM AUSENCIAS DE MNEMONICOS PARA OS TERMOS:\n")
    print(dfTermos.loc[dfTermos['MN_FINAL'] == 'SEM_MN'])
    
#* MONTA INFORMACOES SE TUDO OK COM A DOCUMENTACAO TERMOS E MNEMONICOS
if atributoSemTermo == 1 or count > 0 or countAt != countNat:
    sys.exit()

#* LOAD ATRIBUTOS
#atributos="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\medallia\\THESAURUS_BIDH_NATUREZAS.xlsx"
atributos="C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CRM\\ID_226\\THESAURUS_BIDH_NATUREZAS.xlsx"
dfNatCodig = pd.read_excel(atributos, sheet_name=1, engine='openpyxl', dtype=str, usecols= 'A,C')
dfNatCodig.rename(columns={"INATUZ": "NATUREZA","INATUZ_CODIF": "CODIF"}, inplace=True)


#* CARREGA ATRIBUTOS COM SEUS CODIFS
dfAtributoCodif=pd.merge(dfAtributos,dfNatCodig, on='NATUREZA',how='left')
dfAtributoComCodif=dfAtributoCodif
dfAtributoCodif['ATRIBUTO_CODIF'] = dfAtributoCodif['ATRIBUTO'] + "-" + dfAtributoCodif['CODIF']
dfAtributoCodif=dfAtributoCodif[['ATRIBUTO_CODIF']]
listaAtributoCodif = list(dfAtributoCodif['ATRIBUTO_CODIF'])

#* CARREGA TERMOS
dfTermos=dfTermos[['TERMO','MN_FINAL']]
dfTermos['TERMO_MNEMONICO']=dfTermos['TERMO']+"-"+dfTermos['MN_FINAL']
listaTermos = list(dfTermos['TERMO_MNEMONICO'])


layoutFinal=[]
for atributo_codif in listaAtributoCodif:
    stringFinal=""
    strAtributo, strCodif = atributo_codif.split("-")
    for tempAtributo in strAtributo.split("_"):
        for termo_mnemonico in listaTermos:
            strTermo,strMnemonico = termo_mnemonico.split("-")
            if tempAtributo == strTermo:
                strAtributo=strAtributo.replace(tempAtributo, strMnemonico)
    strAtributo=strCodif+strAtributo
    layoutFinal.append(strAtributo)
dfAtributoComCodif['COL_THESAURUS']=layoutFinal
#dfAtributoComCodif.to_excel("C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\medallia\\ATRIBUTOS_PADRAO_THESAURUS.xlsx",index = False)
dfAtributoComCodif.to_excel("C:\\Users\\andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CRM\\ID_226\\ATRIBUTOS_PADRAO_THESAURUS.xlsx",index = False)











