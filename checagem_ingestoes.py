#***************************************************
# Arquivo de entrada -> tabelas.txt
# Contendo: nome_arquivo;nome_tabela
#***************************************************

strCentroCusto="ALTA"
strSchema = "{0}_ING".format(strCentroCusto)
script="C:\\scripts\\CHECAGEM_{0}.txt".format(strCentroCusto)
tabelas = "C:\\scripts\\tabelas.txt"

open(script, 'w').close()
new_script=open(script, 'w')
new_script.write('echo "#** HDFS"\n'.format(strCentroCusto))
new_script.write('echo "Validando /hadoop/staging/bradesco/{1}/processado_com_falha" \n'.format(strSchema,strCentroCusto))
strHdfs1="if [ `hdfs dfs -ls /hadoop/staging/bradesco/{0}/processado_com_falha |wc -l` == 0 ]; then echo 'Nao existem processamentos com falha no {0}'; else echo 'Processamentos com falha no {0}:';hdfs dfs -ls /hadoop/staging/bradesco/{0}/processado_com_falha ; fi".format(strCentroCusto)
new_script.write("{}\n".format(strHdfs1))
new_script.write('echo "Validando /hadoop/ingestao/bradesco/{1}"\n'.format(strSchema,strCentroCusto))
strHdfs2="if [ `hdfs dfs -ls /hadoop/ingestao/bradesco/{0} |wc -l` == 0 ]; then echo 'Nao existem ingestoes pendentes na raiz do {0}'; else echo 'Arquivos pendentes para ingestao {0}:';hdfs dfs -ls /hadoop/ingestao/bradesco/{0}; fi".format(strCentroCusto)
new_script.write("{}\n".format(strHdfs2))
new_script.write('echo "Validando /hadoop/archiving/bradesco/{1}"\n'.format(strSchema,strCentroCusto))
strHdfs3="if [ `hdfs dfs -ls /hadoop/archiving/bradesco/{0} |wc -l` == 0 ]; then echo 'Nao existem arquivos processados com sucesso no centro de custo {0}'; else echo 'Ultimos 30 arquivos processados para o centro de custo {0}:';hdfs dfs -ls -t /hadoop/archiving/bradesco/{0} |head -30; fi".format(strCentroCusto)
new_script.write("{}\n".format(strHdfs3))
new_script.write('echo "Validando /hadoop/archiving/bradesco/backup_zip"\n'.format(strSchema,strCentroCusto))
strHdfs4="if [ `hdfs dfs -ls /hadoop/archiving/bradesco/backup_zip |grep {0}  |wc -l` == 0 ]; then echo 'Nao existem arquivos zipados processados com sucesso no centro de custo {0}'; else echo 'Ultimos 30 arquivos zip processados para o centro de custo {0}:';hdfs dfs -ls -t /hadoop/archiving/bradesco/backup_zip |grep {0} |head -30; fi".format(strCentroCusto)
new_script.write("{}\n\n".format(strHdfs4))


strPartitions="show partitions "
strCount="select count(*) as quant, dt_ingtao_ptcao from "
strCount2="select count(*) from "

# Using readlines()
arquivo = open(tabelas, 'r')
registro = arquivo.readlines()

#** Ver quando as tabelas foram atualizadas no hive/warehourse
# for tabela in registro:
#     gerarComando = "hdfs dfs -ls /hadoop/apps/hive/warehouse/ingestion/{}.db/{} |tail -n 20".format(strSchema,tabela)
#     new_script.write("{}\n".format(gerarComando))
# new_script.write("\n\n")

new_script.write("#** Checagem no HIVE para o schema {0}\n".format(strSchema))
new_script.write("use {};\n".format(strSchema))
new_script.write("!sh echo '{0}';\n\n".format(strSchema))
for tabela in registro:
    tabela  = tabela.split(";")[1]
    strSh="!sh echo '{0}';".format(tabela.strip())
    new_script.write("{}\n".format(strSh))
    countTotal="select count(*) as quantTotal from {}.{};".format(strSchema, tabela.strip())
    new_script.write("{}\n".format(countTotal))
    strDistinct = "select count(*) as quant, dt_ingtao_ptcao from (select distinct * from {0}.{1}) as {1} group by dt_ingtao_ptcao order by dt_ingtao_ptcao".format(strSchema, tabela.strip())
    #comando="{2}{0}.{1};\n{5}{0}.{1};\n{4};\n{3}{0}.{1} group by dt_ingtao_ptcao;".format(strSchema,tabela.strip(),strPartitions,strCount,strDistinct,strCount2)
    #* PARA COLETA DE INFORMAÇÕES NO HIVE
    #comando2 = "select * from {} limit 10;".format(tabela.strip());
    comando = "{2}{0}.{1};\n{3}{0}.{1} group by dt_ingtao_ptcao order by dt_ingtao_ptcao;\n{4};".format(strSchema, tabela.strip(),
                                                                                            strPartitions, strCount,
                                                                                            strDistinct, strCount2)
    print(comando);
    new_script.write("{}\n\n".format(comando))
    #* PARA COLETA DE INFORMAÇÕES NO HIVE
    #new_script.write("{}\n\n".format(comando2))

#LOGS AUDIT
strSh="\n\n!sh echo 'Verifica trava do centro de custo {0}';\n".format(strCentroCusto)
new_script.write("{}\n".format(strSh))
comando="use audit;"
new_script.write("{}\n".format(comando))
for tabela in registro:
    tabela = tabela.split(";")[0]
    #Abaixo para copybook
    #comando01="select dt_ingestion, file_name, table_name, status, history from audit.ext_ingestion_error_control where copybook like '%{0}%';".format(strCentroCusto)
    comando01="select dt_ingestion, file_name, table_name, status, history from audit.ext_ingestion_manager where table_name like '%{}%' order by dt_ingestion desc limit 600;".format(tabela.strip())
    new_script.write("{}\n".format(comando01))
    comando02= "select dt_ingestion, file_name, table_name, status, history from audit.ext_ingestion_manager where table_name like '%{}%' and status = 'DIFFERENT_SCHEMA' order by dt_ingestion desc limit 600;".format(
        tabela.strip())
    new_script.write("{}\n".format(comando02))

new_script.close()