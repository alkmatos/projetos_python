import pandas as pd
import numpy as np
import warnings
import re
import sys
import os

pd.options.mode.chained_assignment = None  # default='warn'
warnings.simplefilter(action='ignore', category=UserWarning)
pd.set_option('display.max_columns', None)

#*********** Entrada
dicOrigem="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\DICIONARIO.xlsx"
variaveis="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\variaveis.xlsx"

#* Saida
SAIDA="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\CADP\\dicionario\\PARAMETRIZACAO.txt"


#** Deletar arquivo antes de gerar um novo de parametrizacao
if os.path.exists(SAIDA):
    os.remove(SAIDA)

#* Carrega as variaveis
dfVariaveis=pd.read_excel(variaveis, sheet_name=0, engine='openpyxl', dtype=str)
dfVariaveis['PROJETO']=dfVariaveis['PROJETO'].str.upper()
dfVariaveis['BASE']=dfVariaveis['BASE'].str.upper()
dfVariaveis['CARGA']=dfVariaveis['CARGA'].str.upper()
dfVariaveis['TRUNCATE']=dfVariaveis['TRUNCATE'].str.lower()
dfVariaveis['CONECTOR_BANCO']=dfVariaveis['CONECTOR_BANCO'].str.lower()
dfVariaveis['OWNER']=dfVariaveis['OWNER'].str.upper()
dfVariaveis['DATALAKE']=dfVariaveis['DATALAKE'].str.lower()
dfVariaveis['DATABRICKS']=dfVariaveis['DATABRICKS'].str.lower()
dfVariaveis['AMBIENTE']=dfVariaveis['AMBIENTE'].str.upper()
PROJETO = dfVariaveis['PROJETO'].iloc[0]
BASE= dfVariaveis['BASE'].iloc[0]
CARGA= dfVariaveis['CARGA'].iloc[0]
TRUNCATE= dfVariaveis['TRUNCATE'].iloc[0]
CONECTOR_BANCO= dfVariaveis['CONECTOR_BANCO'].iloc[0]
OWNER= dfVariaveis['OWNER'].iloc[0]
DATALAKE= dfVariaveis['DATALAKE'].iloc[0]
DATABRICKS= dfVariaveis['DATABRICKS'].iloc[0]
AMBIENTE= dfVariaveis['AMBIENTE'].iloc[0]


#* Carrega dicionario
dfDic = pd.read_excel(dicOrigem, sheet_name=0, engine='openpyxl', dtype=str)

dfSelecionados = dfDic[['Nome Fisico da Tabela','Nome Logico do Campo','Tipo']]

dfSelecionados['Tipo']=dfSelecionados['Tipo'].str.lower()
dfSelecionados['Tipo']=dfSelecionados['Tipo'].str.replace(r'^char.*','string',regex=True)
dfSelecionados['Tipo']=dfSelecionados['Tipo'].str.replace(r'^varchar.*','string',regex=True)
dfSelecionados['Tipo']=dfSelecionados['Tipo'].str.replace(r'^smallint','integer',regex=True)
dfSelecionados['Tipo']=dfSelecionados['Tipo'].str.replace(r'^bigint','integer',regex=True)

dfSelecionados=dfSelecionados.rename(columns={
                                   'Nome Fisico da Tabela':'tabela',
                                   'Nome Logico do Campo':'campo',
                                   'Tipo':'tipo'
})

dfSelecionados = dfSelecionados.dropna()

contadorIncremental=1
strCamposTabela=""
contadorTabela=1


with open(SAIDA,'a') as arquivo:
    for tabela in dfSelecionados['tabela'].unique():
        STR_PARAM_FAST=""
        #print("*************{}".format(tabela))
        dfTemp=dfSelecionados[dfSelecionados['tabela'] == tabela]
        contadorIncremental=1
        strCamposTabela=""
        #print(len(dfTemp))
        for index,row in dfTemp.iterrows():
            if contadorIncremental < len(dfTemp):
                #print("{} {},".format(row['campo'],row['tipo']))
                strCamposTabela=strCamposTabela + "{} {},".format(row['campo'],row['tipo'])
            else:
                #print("{} {}".format(row['campo'], row['tipo']))
                trCamposTabela = strCamposTabela + "{} {}".format(row['campo'], row['tipo'])
            contadorIncremental+=1
        #print(trCamposTabela)

        #* ABAIXO FIXADO PAARA TESTAR PARAMETRIZAÇÃO DO CRM
        #trCamposTabela="CPF_CNPJ INTEGER, CPF_CNPJ_HASH STRING, DS_STATUS STRING, SEGMENTO_BANCO STRING, QTD_PROD_TOT INTEGER, CAPI BOOLEAN, BARE STRING, AUTO STRING, RE STRING, BILHETE STRING, RESIDENCIAL STRING, SAUDE STRING, INDIVIDUAL STRING, SPG STRING, EMPRESARIAL STRING, DENTAL STRING, DENTAL_INDIVIDUAL STRING, DENTAL_SPG STRING, DENTAL_EMPRESARIAL STRING, BSD STRING, VIDA STRING, VIDA_GRUPO_I STRING, PRESTAMISTA STRING, PREVI STRING, BVP STRING, CAPI_FUNC STRING, CORRENTISTA_ATIVO STRING, SUPERPROTEGIDO STRING, PRIMEIRA_PROTECAO STRING, SEGURO_VIAGEM STRING, PRESTAMISTA_ANALISE STRING, FLAG_TOP_TIER STRING, FLAG_COTITULAR STRING, FLAG_POUPANCISTA STRING, NOME STRING, SEXO STRING, DATA_NASCIMENTO DATE, NACIONALIDADE STRING, DESCRICAO_ESTADO_CIVIL STRING, PROFISSAO STRING, CIDADE STRING, UF STRING, PAIS STRING, CEP STRING, AGENCIA_PRINCIPAL STRING, CONTA_PRINCIPAL STRING, CD_OPTIN_EMAIL STRING, CD_OPTIN_SMS STRING, CARTAO_BS STRING, FLG_FUNCIONARIO STRING, FLG_PPE STRING, FLG_AGENCIA_001 STRING, DS_IND_CLI_ESP STRING, DS_IND_OBITO STRING, DS_IND_CEL_BVP STRING, DS_IND_LGPD STRING, FLAG_NAO_PERTURBE STRING, SF_POSSUI_CAMPANHA STRING, SF_ENGAJADO STRING, EMAIL STRING, ORIGEM STRING, DATA_REF_ORIGEM STRING, NR_DDD1 STRING, NR_TEL1 STRING, NR_DDD_MLH_TEL_MOVEL STRING, NR_MLH_TEL_MOVEL STRING, DT_REF_POSSE STRING, DT_REF_CRM STRING"
        #tabela="TB_CRM_CADASTRO_POSSE_PF"

        if contadorTabela < len(dfSelecionados['tabela'].unique()):
            STR_PARAM_FAST = "('1','EXTERNO','HOLDING','{0}','LIBERADO','0','LIBERADO','01:20:32','05:20:00','{1}','SELECT * FROM {7}.{2}','nao_utilizar','{3}','12/10/2023 09:33:22','10/10/2023 02:45:12','/TRANSIENT/DADOS_CORPORATIVOS/EXTERNAL/{0}/{2}','abfss://bronze@{8}{{0}}001.dfs.core.windows.net/TRANSIENT/DADOS_CORPORATIVOS/EXTERNAL/{0}/{2}'.format(AMBIENTE),'abfss://bronze@{8}{{0}}001.dfs.core.windows.net/DADOS_CORPORATIVOS/EXTERNAL/{0}/{2}'.format(AMBIENTE),'{8}{{0}}001'.format(AMBIENTE),'bronze','{9}_{{0}}'.format(AMBIENTE),'bronze','{2}','{4}','DMOVT_CTRL','nao_utilizar','nao_utilizar','nao_utilizar','{5}','{0}','{2}','{6}','2024-10-10','2024-10-15','','','','','','','','','','','','','','',''),".format(
                PROJETO, BASE, tabela, CARGA,trCamposTabela,TRUNCATE,CONECTOR_BANCO,OWNER,DATALAKE,DATABRICKS)
            arquivo.write(STR_PARAM_FAST + '\n\n')
            #print(STR_PARAM_FAST)
        else:
            STR_PARAM_FAST = "('1','EXTERNO','HOLDING','{0}','LIBERADO','0','LIBERADO','01:20:32','05:20:00','{1}','SELECT * FROM {7}.{2}','nao_utilizar','{3}','12/10/2023 09:33:22','10/10/2023 02:45:12','/TRANSIENT/DADOS_CORPORATIVOS/EXTERNAL/{0}/{2}','abfss://bronze@{8}{{0}}001.dfs.core.windows.net/TRANSIENT/DADOS_CORPORATIVOS/EXTERNAL/{0}/{2}'.format(AMBIENTE),'abfss://bronze@{8}{{0}}001.dfs.core.windows.net/DADOS_CORPORATIVOS/EXTERNAL/{0}/{2}'.format(AMBIENTE),'{8}{{0}}001'.format(AMBIENTE),'bronze','{9}_{{0}}'.format(AMBIENTE),'bronze','{2}','{4}','DMOVT_CTRL','nao_utilizar','nao_utilizar','nao_utilizar','{5}','{0}','{2}','{6}','2024-10-10','2024-10-15','','','','','','','','','','','','','','','')".format(
                PROJETO, BASE, tabela, CARGA, trCamposTabela, TRUNCATE, CONECTOR_BANCO, OWNER, DATALAKE, DATABRICKS)
            arquivo.write(STR_PARAM_FAST)
            #print(STR_PARAM_FAST)
        contadorTabela += 1