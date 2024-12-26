import pandas as pd
import numpy as np
import warnings
import re
import sys

warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('display.max_columns', None)

#*********** Entrada
SISTEMA_ORIGEM="LEXW"
dicOrigem="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\LEXW\\dicionario\\HOLDG_LEXW_ORA.xlsx"
natureza="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\LEXW\\dicionario\\THESAURUS_BIDH_NATUREZAS.xlsx"

#* SE NÃO POSSUI TABELAS SELECIONADAS, PASSAR A VARIAVEL COMO VAZIA.
#  NO CASO DO CAPD TINHAMOS UM EXCEL COM A LISTA DE TABELAS QUE DEVERIAM SER CONTEMPLADAS
#listadetabelas="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\CADP_DB2 - Tabelas e descrição_Selecionadas.xlsx"
listadetabelas=""
#**************************************************************************************************************************

#* Saida
SAIDA="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\LEXW\\dicionario\\DICIONARIO_{}.xlsx".format(SISTEMA_ORIGEM)

dfDic = pd.read_excel(dicOrigem, sheet_name=0, engine='openpyxl', dtype=str)
dfNatureza=pd.read_excel(natureza, sheet_name=1, engine='openpyxl', dtype=str)
if listadetabelas == "":
    print("NAO TEM")
else:
    dfTabelas=pd.read_excel(listadetabelas, sheet_name=0, engine='openpyxl', dtype=str)


#* Definindo condicoes para pk
condicoes=[
    (dfDic['É PK?'] == 'Yes') & (dfDic['É FK?'] == 'Yes'),
    (dfDic['É PK?'] == 'Yes') & (dfDic['É FK?'] == 'No'),
    (dfDic['É PK?'] == 'No') & (dfDic['É FK?'] == 'Yes'),
    (dfDic['É PK?'] == 'No') & (dfDic['É FK?'] == 'No')
]
#* Define os resultados correspondentes a PK
#* Solicitaram quando for estrangeira e primaria nao manter as duas, neste caso manter somente primaria
#resultados=['Estrangeira e Primaria','Primaria','Estrangeira','Não se Aplica']
resultados=['Primaria','Primaria','Estrangeira','Não se Aplica']

def retornaAtributoSensivel(descricao, confirmacao):
    valor = (str(descricao)).lower()
    if re.search(r'\bcpf\b',valor) and re.search(r'\brg\b',valor) and re.search(r'\bcnpj\b',valor):
        return confirmacao
    elif re.search(r'\bcpf\b',valor) and re.search(r'\brg\b',valor):
        return confirmacao
    elif re.search(r'\bcpf\b',valor):
        return confirmacao
    elif re.search(r'\brg\b',valor):
        return confirmacao
    elif re.search(r'\bcnpj\b',valor):
        return confirmacao
    elif re.search(r'\bcep\b',valor):
        return confirmacao
    elif re.search(r'\bendereço\b',valor) or re.search(r'\bendereco\b',valor):
        return confirmacao
    elif re.search(r'\bbairro\b',valor):
        return confirmacao
    else:
        return ''
def dadosDeMenor(valor):
    valor = (str(valor)).lower()
    if re.search(r'\bcpf\b',valor) and re.search(r'\brg\b',valor):
        return 'Sim'
    elif re.search(r'\bcpf\b',valor):
        return 'Sim'
    elif re.search(r'\brg\b',valor):
        return 'Sim'
    else:
        return ''
def dadosSensiveis(valor):
    valor = (str(valor)).lower()
    if re.search(r'\bcpf\b',valor) and re.search(r'\brg\b',valor) and re.search(r'\bcnpj\b',valor):
        return 'Sim'
    elif re.search(r'\bcpf\b',valor) and re.search(r'\brg\b',valor):
        return 'Sim'
    elif re.search(r'\bcpf\b',valor):
        return 'Sim'
    elif re.search(r'\brg\b',valor):
        return 'Sim'
    elif re.search(r'\bcnpj\b',valor):
        return 'Sim'
    elif re.search(r'\bcep\b',valor):
        return 'Sim'
    elif re.search(r'\bendereço\b',valor) or re.search(r'\bendereco\b',valor):
        return 'Sim'
    elif re.search(r'\bbairro\b',valor):
        return 'Sim'
    else:
        return ''
def precisao(valor):
    valor=(str(valor)).lower()
    if 'decimal' in valor:
        return str(valor[7:]).replace("(",'').replace(")",'')
    elif 'varchar2' in valor:
        return str(valor[8:]).replace("(", '').replace(")", '')
    elif 'varchar' in valor:
        return str(valor[7:]).replace("(",'').replace(")",'')
    elif 'number' in valor:
        return str(valor[6:]).replace("(", '').replace(")", '')
    elif 'char' in valor:
        return str(valor[4:]).replace("(",'').replace(")",'')
    elif 'integer' in valor:
        return '10'
    elif 'smalint' in valor:
        return '4'
    elif 'int' in valor:
        return '10'
    elif 'boolean' in valor:
        return ''
    elif 'date' in valor:
        return '10'
    elif 'timestamp' in valor:
        return '21'
    else:
        return 'variavel nao definida'

def substituirTipo(valor):
    valor=valor.lower()
    if "varchar2" in valor:
        return "Varchar"
    elif "varchar" in valor:
        return "Varchar"
    elif "char" in valor:
        return "Varchar"
    elif "integer" in valor:
        return "Int"
    elif "date" in valor:
        return "Date"
    elif "timestamp" in valor:
        return "Timestamp"
    elif "boolean" in valor:
        return "Boolean"
    elif "number" in valor:
        return "Decimal"
    elif "double" in valor:
        return "Double"
    elif "float" in valor:
        return "Float"
    else:
        return "TIPO NAO DEFINIDO"


#* Pandas DF
dfDic.insert(0,'Nome do Sistema Origem','{}'.format(SISTEMA_ORIGEM))
dfDic.insert(1,'Nome Fisico da Tabela',dfDic['Table Name'])
dfDic.insert(2,'Nome Logico da Tabela',dfDic['Entity Name'])
dfDic.insert(3,'Descricao Tabela',dfDic['Definição lógica entidade'])

dfDic.insert(4,'Nome Fisico do Campo',dfDic['Column Name'])
dfDic.insert(5,'Nome Logico do Campo',dfDic['Attribute Name'])
dfDic.insert(6,'CODIGO','')
dfDic.insert(7,'Natureza','')
dfDic['CODIGO']=dfDic['Nome Logico do Campo'].str[:2]
#* merge
df_merged=pd.merge(dfDic,dfNatureza,left_on='CODIGO',right_on='INATUZ_ABREV',how='left')
#* Atualiza a coluna natureza
dfDic['Natureza']=df_merged['INATUZ']
dfDic.insert(8,'Descricao do Campo',dfDic['Definição lógica atributo'])
dfDic.insert(9,'Tipo',dfDic['Datatype físico'])
dfDic.insert(10,'Precisao','')
dfDic['Precisao']=dfDic['Datatype físico'].apply(precisao)
dfDic.insert(11,'É CHAVE PK',dfDic['É PK?'])
dfDic.insert(12,'É CHAVE FK',dfDic['É FK?'])
dfDic.insert(13,'É CHAVE','')
dfDic['É CHAVE']=np.select(condicoes,resultados,default='Não se Aplica')
dfDic.insert(14,'Periodicidade de atualizacao','Diária (dias corridos)')
dfDic.insert(15,'Plataforma de Origem','{}'.format(SISTEMA_ORIGEM))
dfDic.insert(16,'Dominio',dfDic['Column Default Value'])
dfDic.insert(17,'Descricao do Dominio',dfDic['Column Validation Value'])
dfDic.insert(18,'Contem Dados Pessoais (PII)','')
dfDic['Contem Dados Pessoais (PII)']=dfDic['Descricao do Campo'].apply(dadosSensiveis)
dfDic.loc[dfDic['Contem Dados Pessoais (PII)'] == '', 'Contem Dados Pessoais (PII)']='Nao'
dfDic.insert(19,'Contem Dados de Menores','')
dfDic['Contem Dados de Menores']=dfDic['Descricao do Campo'].apply(dadosDeMenor)
dfDic.loc[dfDic['Contem Dados de Menores'] == '', 'Contem Dados de Menores']='Nao'
dfDic.insert(20,'Tipo de Dados Critico','')
dfDic['Tipo de Dados Critico']=dfDic.apply(lambda row: retornaAtributoSensivel(row['Descricao do Campo'],row['Nome Logico do Campo']), axis=1)
dfDic['Nome Logico do Campo']=dfDic['Nome Logico do Campo'].str.replace(r'^[^_]*_', '', regex=True)
dfDic['Tipo']=dfDic['Tipo'].apply(substituirTipo)
dfDic = dfDic.iloc[:,0:21]
dfDic = dfDic.drop(['CODIGO', 'É CHAVE PK', 'É CHAVE FK'], axis=1)


if listadetabelas == "":
    dfDic.to_excel(SAIDA, index=False)
else:
    #* Lista de tabelas contempladas para montar o dicionario
    tabelas2=dfTabelas['Nome de Tabela'].tolist()

    dfDicSelecionados = dfDic[dfDic['Nome Fisico da Tabela'].isin(tabelas2)]

    dfDicSelecionados=dfDicSelecionados.drop(['CODIGO','É CHAVE PK','É CHAVE FK'],axis=1)

    dfDicSelecionados.to_excel(SAIDA,index=False)