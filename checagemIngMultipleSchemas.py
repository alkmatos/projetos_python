#***************************************************
# Arquivo de entrada -> tabelas.txt
# Contendo: nome_arquivo;nome_tabela
#***************************************************

strCentroCusto="GERAL"
strSchema = "{0}_ING".format(strCentroCusto)
script="C:\\scripts\\CHECAGEM_{0}.txt".format(strCentroCusto)
tabelas = "C:\\scripts\\tabelas2.txt"

open(script, 'w').close()
new_script=open(script, 'w')

open(script, 'w').close()
strPartitions="show partitions "
strCount="select count(*) as quant, dt_ingtao_ptcao from "
strCount2="select count(*) from "

# Using readlines()
arquivo = open(tabelas, 'r')
registro = arquivo.readlines()

for tabela in registro:
    print(tabela)
    #tabela  = tabela.split(";")[1]
    strSh="!sh echo '{0}';".format(tabela.strip())
    new_script.write("{}\n".format(strSh))
    countTotal="select count(*) as quantTotal from {};".format(tabela.strip())
    new_script.write("{}\n".format(countTotal))
    strDistinct = "select count(*) as quant, dt_ingtao_ptcao from (select distinct * from {0}) as {0} group by dt_ingtao_ptcao order by dt_ingtao_ptcao".format(tabela.strip())
    #comando="{2}{0}.{1};\n{5}{0}.{1};\n{4};\n{3}{0}.{1} group by dt_ingtao_ptcao;".format(strSchema,tabela.strip(),strPartitions,strCount,strDistinct,strCount2)
    #* PARA COLETA DE INFORMAÇÕES NO HIVE
    #comando2 = "select * from {} limit 10;".format(tabela.strip());
    comando = "{1} {0};\n{2} {0} group by dt_ingtao_ptcao order by dt_ingtao_ptcao;\n{4} {0};".format( tabela.strip(),
                                                                                            strPartitions, strCount,
                                                                                            strDistinct, strCount2)
    print(comando);
    new_script.write("{}\n\n".format(comando))
    #* PARA COLETA DE INFORMAÇÕES NO HIVE
    #new_script.write("{}\n\n".format(comando2))

#LOGS AUDIT
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