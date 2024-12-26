import pandas as pd
import numpy as np
import warnings
import re

warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('display.max_columns', None)

#*********** Entrada
dicOrigem="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\MDC_CADP_DB2.xlsx"
natureza="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\THESAURUS_BIDH_NATUREZAS.xlsx"
listadetabelas="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\CADP_DB2 - Tabelas e descrição_Selecionadas.xlsx"
#**************************************************************************************************************************

#* Saida
SAIDA="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\DICIONARIO.xlsx"

dfDic = pd.read_excel(dicOrigem, sheet_name=0, engine='openpyxl', dtype=str)
dfNatureza=pd.read_excel(natureza, sheet_name=1, engine='openpyxl', dtype=str)
dfTabelas=pd.read_excel(listadetabelas, sheet_name=0, engine='openpyxl', dtype=str)


#* Definindo condicoes para pk
condicoes=[
    (dfDic['É PK?'] == 'Yes') & (dfDic['É FK?'] == 'Yes'),
    (dfDic['É PK?'] == 'Yes') & (dfDic['É FK?'] == 'No'),
    (dfDic['É PK?'] == 'No') & (dfDic['É FK?'] == 'Yes'),
    (dfDic['É PK?'] == 'No') & (dfDic['É FK?'] == 'No')
]
#* Define os resultados correspondentes a PK
resultados=['Estrangeira e Primária','Primária','Estrangeira','Não se Aplica']

def retornaAtributoSensivel(,descricao, confirmacao):
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
        return valor[7:]
    elif 'varchar' in valor:
        return valor[7:]
    elif 'char' in valor:
        return valor[4:]
    elif 'integer' in valor:
        return ''
    elif 'smalint' in valor:
        return ''
    elif 'int' in valor:
        return ''
    elif 'boolean' in valor:
        return ''
    elif 'date' in valor:
        return '10'
    elif 'timestamp' in valor:
        return '21'
    else:
        return 'variavel nao definida'


#* Pandas DF
dfDic.insert(0,'Nome do Sistema Origem','CADP')
dfDic.insert(1,'Nome Fisico da Tabela',dfDic['Table Name'])
dfDic.insert(2,'Nome Logico da Tabela',dfDic['Entity Name'])
dfDic.insert(3,'Descricao Tabela',dfDic['Definição lógica entidade'])
dfDic.insert(4,'Nome Fisico do Campo',dfDic['Attribute Name'])
dfDic.insert(5,'Nome Logico do Campo',dfDic['Column Name'])
dfDic.insert(6,'CODIGO','')
dfDic.insert(7,'Natureza','')
dfDic['CODIGO']=dfDic['Nome Fisico do Campo'].str[:2]
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
dfDic.insert(15,'Plataforma de Origem','CADP')
dfDic.insert(16,'Dominio',dfDic['Column Default Value'])
dfDic.insert(17,'Descricao do Dominio',dfDic['Column Validation Value'])
dfDic.insert(18,'Contem Dados Pessoais (PII)','')
dfDic['Contem Dados Pessoais (PII)']=dfDic['Descricao do Campo'].apply(dadosSensiveis)
dfDic.insert(19,'Contem Dados de Menores','')
dfDic['Contem Dados de Menores']=dfDic['Descricao do Campo'].apply(dadosDeMenor)
dfDic.insert(20,'Tipo de Dados Critico','')
dfDic['Tipo de Dados Critico']=dfDic.apply(lambda row: retornaAtributoSensivel('dadosdemenor',row['Descricao do Campo'],row['Nome Logico do Campo']), axis=1)
dfDic = dfDic.iloc[:,0:21]

#* Lista de tabelas contempladas para montar o dicionario
tabelas2=dfTabelas['Nome de Tabela'].tolist()

dfDicSelecionados = dfDic[dfDic['Nome Fisico da Tabela'].isin(tabelas2)]

dfDicSelecionados=dfDicSelecionados.drop(['CODIGO','É CHAVE PK','É CHAVE FK'],axis=1)

dfDicSelecionados.to_excel(SAIDA,index=False)