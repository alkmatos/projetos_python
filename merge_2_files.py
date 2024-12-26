import pandas as pd
import warnings
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('display.max_columns', None)

dicionario = "C:\\Users\\Andre.matos\\Downloads\\Dicionario de Dados_CADP_184_tabelasv6.xlsx"
arqEscopo  = "C:\\Users\\Andre.matos\\Downloads\\Cópia de Escopo Ingestão CADP.xlsx"
SAIDA="C:\\Users\\Andre.matos\\Downloads\\resultado.xlsx"

dfDic = pd.read_excel(dicionario, sheet_name=0)
dfEscopo = pd.read_excel(arqEscopo, sheet_name=0)

resultado = dfEscopo.merge(dfDic, on=['tabela','campo'], how="left")

resultado.to_excel(SAIDA,index=False)
