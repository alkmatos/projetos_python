import pandas as pd
import sys
import ast
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
ARQUIVO="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\AFLUENTES\\Afluentes_Prev_20240830\\FGBI_FGBI_CANCELAMENTO_20240830193000.txt"
ARQUIVO2="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\AFLUENTES\\Afluentes_Prev_20240830\\FGBI_FGBI_CANCELAMENTO_20241031092200.TXT"
dfPd=pd.read_csv(ARQUIVO,delimiter="|")#,encoding='latin-1')#latin-1
dfPd2=pd.read_csv(ARQUIVO2,delimiter="|")#,encoding='latin-1')#latin-1
#print(dfPd.head(8))
print("*********************************************")
colunas=list(dfPd.columns)
colunas2=list(dfPd2.columns)
colunas=[item.strip() for item in colunas]
colunas2=[item.strip() for item in colunas2]
print(len(colunas))
print(len(colunas2))
print(colunas)
print(colunas2)
sys.exit()

dicionario="""MCAN_CD_MOT_CANCEL
MCAN_DT_VIG_INI   
MCAN_DT_VIG_FIN   
MCAN_DESC_MOT_CANC
MCAN_CD_CANC_BEN1 
MCAN_CD_CANC_BEN2 
MCAN_CD_CANC_BEN3 
MCAN_CD_CANC_BEN4 
MCAN_CD_CANC_BEN5 
MCAN_TP_CONV_SQTA 
MCAN_INDR_CANC_AUT
MCAN_TP_PAGTO_CAB 
MCAN_DT_ULT_ALTER 
MCAN_CD_USUARIO   
MCAN_INTEGRIDADE  
MCAN_DESC_RES_MCAN
MCAN_INDR_CANC_PAD
CIDTFD_INDIC_CONF 
"""

linhas=dicionario.splitlines()
lista2=[]
for a in linhas:
    lista2.append(a)

print(colunas)
print(lista2)


if colunas != lista2: # and colunas != lista2:
    diferenca=list(set(lista2) - set(colunas))
    print(len(colunas))
    print(len(lista2))
    for dic,col in zip(lista2,colunas):
        print("Corrigir no dicionario de dados o nome fisico do campo de {} para {}".format(dic, col))


    print(diferenca)
    print("LAYOUT DIVERGENTE")
else:
    print("LAYOUT OK")


sys.exit()

layout=[
'e_bradescoseg_cx_survey_type_enum',
'e_bradescoseg_cx_segmentacaopesquisa_enum',
'e_bradescoseg_cx_ramo_enum',
'e_bradescoseg_cx_episodio_enum',
'e_bradescoseg_cx_cpf_cnpj_txt',
'e_bradescoseg_cx_nome_cliente_txt',
'e_bradescoseg_cx_apolice_txt',
'e_bradescoseg_cx_canal_utilizado_auto',
'e_bradescoseg_cx_carteirinha_txt',
'e_bradescoseg_cx_data_date',
'e_bradescoseg_cx_data_evento_saude_date',
'e_bradescoseg_cx_data_encerramento_date',
'e_bradescoseg_cx_data_liberacao_date',
'e_bradescoseg_cx_data_pedido_reembolso_date',
'e_bradescoseg_cx_motivo_encerramento_auto',
'e_bradescoseg_cx_especialidade_auto',
'e_bradescoseg_cx_genero_enum',
'e_bradescoseg_cx_id_cliente_txt',
'e_bradescoseg_cx_id_registro_txt',
'e_bradescoseg_cx_idade_txt',
'e_bradescoseg_cx_natureza_dano_auto',
'e_bradescoseg_cx_nome_fundo_txt',
'e_bradescoseg_cx_nome_segurado_vida_txt',
'e_bradescoseg_cx_serie_cap_txt',
'e_bradescoseg_cx_sinistro_txt',
'e_bradescoseg_cx_titulo_cap_txt',
'e_bradescoseg_cx_posse_auto_yn',
'e_bradescoseg_cx_posse_cap_yn',
'e_bradescoseg_cx_posse_dental_yn',
'e_bradescoseg_cx_posse_prev_yn',
'e_bradescoseg_cx_posse_re_yn',
'e_bradescoseg_cx_posse_saude_yn',
'e_bradescoseg_cx_posse_vida_yn',
'e_bradescoseg_cx_posse_totalizador_enum',
'e_bradescoseg_cx_prestador_txt',
'e_bradescoseg_cx_prestador_formatado_txt',
'e_bradescoseg_cx_tipo_reembolso_auto',
'e_bradescoseg_cx_tipo_seguro_auto',
'e_bradescoseg_cx_titularidade_enum',
'e_bradescoseg_cx_plano_prev_txt',
'e_bradescoseg_cx_valor_resgate_txt',
'e_bradescoseg_cx_valor_venda_txt',
'e_bradescoseg_cx_ctl_formulario_contato_yn',
'e_bradescoseg_cx_ctl_formulario_comentarios_positivos_cmt',
'e_bradescoseg_cx_ctl_formulario_comentarios_negativos_cmt',
'e_bradescoseg_cx_ctl_formulario_comentarios_adicionais_cmt',
'e_bradescoseg_cx_plano_descricao_auto',
'e_bradescoseg_cx_plano_codigo_auto',
'e_bradescoseg_cx_plano_validade_auto',
'e_bradescoseg_cx_titulo_situacao_auto',
'e_bradescoseg_cx_data_pagamento_date',
'e_bradescoseg_cx_data_implantacao_date',
'e_bradescoseg_cx_data_inicio_vigencia_date',
'e_bradescoseg_cx_evento_saude_auto',
'e_bradescoseg_cx_ramo_saude_auto',
'e_bradescoseg_cx_valor_pago_txt',
'e_bradescoseg_cx_valor_apresentado_txt',
'e_bradescoseg_cx_prazo_decorrido_auto',
'e_bradescoseg_cx_uf_medico_auto',
'e_bradescoseg_cx_uf_beneficiario_auto',
'e_bradescoseg_cx_tipo_pagamento_auto',
'e_bradescoseg_cx_tipo_endoso_auto',
'e_bradescoseg_cx_tipo_endoso_formatado_auto',
'e_bradescoseg_cx_codigo_sise_txt',
'e_bradescoseg_cx_codigo_produto_txt',
'e_bradescoseg_cx_cpf_segurado_bvp_txt',
'e_bradescoseg_cx_parentesco_vida_auto',
'e_bradescoseg_cx_tipo_fundo_prev_auto',
'e_bradescoseg_cx_cnpj_fundo_prev_txt',
'e_bradescoseg_cx_tipo_regime_auto',
'e_bradescoseg_cx_data_solicitacao_date',
'e_bradescoseg_cx_nome_estipulante_auto',
'e_bradescoseg_cx_coringa1_int',
'e_bradescoseg_cx_coringa2_int',
'e_bradescoseg_cx_coringa3_int',
'e_bradescoseg_cx_coringa4_int',
'e_bradescoseg_cx_coringa5_txt',
'e_bradescoseg_cx_coringa6_txt',
'e_bradescoseg_cx_coringa7_txt',
'e_bradescoseg_cx_coringa8_txt',
'e_bradescoseg_cx_coringa9_txt',
'e_bradescoseg_cx_coringa10_txt',
'e_bradescoseg_cx_coringa11_txt',
'e_bradescoseg_cx_coringa12_txt',
'e_bradescoseg_cx_coringa13_txt',
'e_bradescoseg_cx_coringa14_txt',
'e_bradescoseg_cx_coringa15_txt',
'e_bradescoseg_cx_coringa8_descricao_txt',
'e_bradescoseg_cx_coringa11_data_cancelamento_date',
'e_bradescoseg_cx_coringa2_numero_protocolo_int',
'e_bradescoseg_cx_segmento_cliente_auto',
'e_bradescoseg_cx_cidade_auto',
'e_bradescoseg_cx_produto_enum',
'e_bradescoseg_cx_agencia_txt',
'e_bradescoseg_cx_coringa14_classif_vulnerabilidade_enum',
'e_bradescoseg_cx_coringa8_frequencia_reembolso_enum',
'e_bradescoseg_cx_natureza_dano_formatado_auto',
'e_bradescoseg_cx_produto_txt',
'e_bradescoseg_cx_situacao_reembolso_auto',
'e_bradescoseg_cx_status_enum',
'e_bradescoseg_cx_coringa15_teste_ab_enum',
'e_bradescoseg_cx_episodio_testeab_enum',
'e_bradescoseg_cx_tipo_resgate_enum',
'e_bradescoseg_cx_proposta_prev_txt',
'e_bradescoseg_cx_faixa_valor_resgate_enum',
'e_bradescoseg_cx_faixa_valor_pago_enum',
'e_bradescoseg_cx_nome_ramo_enum',
'e_bradescoseg_cx_sucursal_auto',
'e_bradescoseg_cx_coringa5_sinistrado_enum',
'e_bradescoseg_cx_coringa8_descricao_produto_enum',
'e_bradescoseg_cx_coringa5_descricao_produto_auto',
'e_bradescoseg_cx_coringa9_descricao_produto_auto',
'e_bradescoseg_cx_regional_auto',
'e_bradescoseg_cx_coringa9_passagem_bac_yn',
'e_bradescoseg_cx_coringa13_canal_pesquisa_enum',
'e_bradescoseg_flag_ciclocompleto_yn',
'e_bradescoseg_cx_central_centraldeatendimento_enum',
'e_bradescoseg_cx_ouvid_finalizados_forma_retorno_auto',
'e_bradescoseg_cx_ouvid_finalizados_tipo_manifest_auto',
'e_bradescoseg_cx_ouvid_finalizados_resultado_manifest_auto',
'e_bradescoseg_cx_ouvid_finalizados_manifestacao_enum',
'e_bradescoseg_cx_ouvid_finalizados_grupo_manifest_auto',
'e_bradescoseg_cx_ouvid_finalizados_prod_assunto_auto',
'e_bp_digital_device_hardware_type_auto',
'e_bp_digital_device_os_name_auto',
'e_bp_digital_browser_name_auto',
'e_bp_digital_city_auto',
'e_bp_digital_itm_survey_alt',
'e_bp_digital_unit',
'e_bp_digital_region_auto',
'e_bp_digital_mobile_app_version_auto',
'e_bp_digital_browser_version_auto',
'e_bp_digital_mobile_sdk_version_auto',
'e_bp_digital_device_os_version_auto',
'e_bp_digital_mobile_os_version_auto',
'a_surveyid',
'a_topics_tagged_original',
'a_action_plan_themes_alts',
'a_action_plan_topics_alts',
'a_topics_sentiments_tagged_after_manual_updates',
'a_topics_sentiments_tagged_original',
'a_ipaddress',
'k_bp_timezone_creation_time',
'k_bp_timezone_response_time',
'k_bradescoseg_cx_fechamento_alerta_enum',
'k_bradescoseg_cx_regiao_medico_enum',
'k_bradescoseg_cx_ctl_formulario_ligacoes_auto',
'k_bradescoseg_cx_ctl_alerta_fechado_yn',
'k_bradescoseg_cx_alertas_fechados_por_txt',
'k_bradescoseg_cx_ctl_alerta_com_dono_yn',
'k_bradescoseg_cx_segmento_nps_enum',
'k_bradescoseg_cx_regiao_enum',
'k_bradescoseg_cx_faixa_etaria_enum',
'k_bradescoseg_cx_faixa_etaria75_enum',
'k_bradescoseg_cx_oficinasauto_yn',
'k_bradescoseg_cx_central_cpf_txt',
'k_bradescoseg_cx_central_ltr_na_txt',
'k_bradescoseg_cx_central_operador_nome_txt',
'k_bradescoseg_cx_central_pesquisa_respondida_yn',
'k_bp_survey_device_finished_on_alt',
'k_bp_survey_browser_auto',
'k_bp_survey_os_auto',
'k_bradescoseg_nota_geral_scale',
'q_bradescoseg_cx_episodio_ltr_scale',
'q_bradescoseg_cx_episodio_ltr_motivo_cmt',
'q_bradescoseg_cx_relacionamento_ltr_scale',
'q_bradescoseg_cx_rlc_cliente_ltr_scale',
'q_bradescoseg_cx_rlc_cliente_ltr_motivo_cmt',
'q_bradescoseg_cx_reembolso_atendimento_particular_enum',
'q_bradescoseg_cx_episodio_agilidade_processo_scale',
'q_bradescoseg_cx_episodio_orientacoes_recebidas_scale',
'q_bradescoseg_cx_episodio_cordialidade_regulador_scale',
'q_bradescoseg_cx_episodio_documentacao_solicitada_scale',
'q_bradescoseg_cx_episodio_acionamento_seguro_scale',
'q_bradescoseg_cx_central_ltr_scale',
'q_bradescoseg_cx_central_solicitacao_atendida_scale',
'q_bradescoseg_cx_ouvid_finalizados_csat_1to10_scale',
'q_bradescoseg_cx_ouvid_finalizados_csat_motivo_cmt',
'q_bradescoseg_cx_ouvid_finalizados_solicitacao_resolvida_yn',
'q_bradescoseg_cx_ouvid_finalizados_solicitacao_resolvida_cmt',
'q_md_17497_ces_abertura_de_sinistro',
'q_md_17497_motivo_da_nota_ces_abertura_de_sinistro',
'q_md_17496_perfil_do_usu_rio',
'q_bradescoseg_digital_pi_ltr_scale',
'q_bradescoseg_digital_pi_ltr_reason_ctm'
]


if colunas != layout:
    print("LAYOUT DIVERGENTE")
else:
    print("LAYOUT OK")

sys.exit()



x="JOURNEYID|JOURNEYNAME|ACTIVITYNAME|JOURNEYACTIVITYOBJECTID|SUBSCRIBERKEY|EVENTDATE|dt_abert|BOUNCECATEGORY|bouncetime|EmailAddress|fl_entregue|fl_click|dt_click|fl_optout|dt_ref|optout_date"



listaX=[]
for c in x.split("|"):
    listaX.append(c)

dicionario=""" JOURNEYID
 JOURNEYNAME
 ACTIVITYNAME
 JOURNEYACTIVITYOBJECTID
 SUBSCRIBERKEY
 EVENTDATE
 DT_ABERT
 BOUNCECATEGORY
 BOUNCETIME
 EmailAddress
 FL_ENTREGUE
 FL_Click
 DT_CLICK
 FL_OPTOUT
 DT_REF
 OPTOUT_DATE"""

linhas=dicionario.splitlines()
lista2=[]
for a in linhas:
    lista2.append(a)

print(lista2)
print(listaX)
print(colunas)

if colunas != listaX and colunas != lista2:
    print("LAYOUT DIVERGENTE")
else:
    print("LAYOUT OK")
    print("Tamanho da lista [{}]".format(len(lista2)))
    print("Tamanho da lista [{}]".format(len(listaX)))

# count=0
# for colunaLayout in layout:
#     for colunaArq in colunas:
#         print("[{}]-[{}]".format(colunaLayout[count], colunaArq[count]))
#     count=count+1
sys.exit()
layout=[
'e_bradescoseg_cx_survey_type_enum',
'e_bradescoseg_cx_segmentacaopesquisa_enum',
'e_bradescoseg_cx_ramo_enum',
'e_bradescoseg_cx_episodio_enum',
'e_bradescoseg_cx_cpf_cnpj_txt',
'e_bradescoseg_cx_nome_cliente_txt',
'e_bradescoseg_cx_apolice_txt',
'e_bradescoseg_cx_canal_utilizado_auto',
'e_bradescoseg_cx_carteirinha_txt',
'e_bradescoseg_cx_data_date',
'e_bradescoseg_cx_data_evento_saude_date',
'e_bradescoseg_cx_data_encerramento_date',
'e_bradescoseg_cx_data_liberacao_date',
'e_bradescoseg_cx_data_pedido_reembolso_date',
'e_bradescoseg_cx_motivo_encerramento_auto',
'e_bradescoseg_cx_especialidade_auto',
'e_bradescoseg_cx_genero_enum',
'e_bradescoseg_cx_id_cliente_txt',
'e_bradescoseg_cx_id_registro_txt',
'e_bradescoseg_cx_idade_txt',
'e_bradescoseg_cx_natureza_dano_auto',
'e_bradescoseg_cx_nome_fundo_txt',
'e_bradescoseg_cx_nome_segurado_vida_txt',
'e_bradescoseg_cx_serie_cap_txt',
'e_bradescoseg_cx_sinistro_txt',
'e_bradescoseg_cx_titulo_cap_txt',
'e_bradescoseg_cx_posse_auto_yn',
'e_bradescoseg_cx_posse_cap_yn',
'e_bradescoseg_cx_posse_dental_yn',
'e_bradescoseg_cx_posse_prev_yn',
'e_bradescoseg_cx_posse_re_yn',
'e_bradescoseg_cx_posse_saude_yn',
'e_bradescoseg_cx_posse_vida_yn',
'e_bradescoseg_cx_posse_totalizador_enum',
'e_bradescoseg_cx_prestador_txt',
'e_bradescoseg_cx_prestador_formatado_txt',
'e_bradescoseg_cx_tipo_reembolso_auto',
'e_bradescoseg_cx_tipo_seguro_auto',
'e_bradescoseg_cx_titularidade_enum',
'e_bradescoseg_cx_plano_prev_txt',
'e_bradescoseg_cx_valor_resgate_txt',
'e_bradescoseg_cx_valor_venda_txt',
'e_bradescoseg_cx_ctl_formulario_contato_yn',
'e_bradescoseg_cx_ctl_formulario_comentarios_positivos_cmt',
'e_bradescoseg_cx_ctl_formulario_comentarios_negativos_cmt',
'e_bradescoseg_cx_ctl_formulario_comentarios_adicionais_cmt',
'e_bradescoseg_cx_plano_descricao_auto',
'e_bradescoseg_cx_plano_codigo_auto',
'e_bradescoseg_cx_plano_validade_auto',
'e_bradescoseg_cx_titulo_situacao_auto',
'e_bradescoseg_cx_data_pagamento_date',
'e_bradescoseg_cx_data_implantacao_date',
'e_bradescoseg_cx_data_inicio_vigencia_date',
'e_bradescoseg_cx_evento_saude_auto',
'e_bradescoseg_cx_ramo_saude_auto',
'e_bradescoseg_cx_valor_pago_txt',
'e_bradescoseg_cx_valor_apresentado_txt',
'e_bradescoseg_cx_prazo_decorrido_auto',
'e_bradescoseg_cx_uf_medico_auto',
'e_bradescoseg_cx_uf_beneficiario_auto',
'e_bradescoseg_cx_tipo_pagamento_auto',
'e_bradescoseg_cx_tipo_endoso_auto',
'e_bradescoseg_cx_tipo_endoso_formatado_auto',
'e_bradescoseg_cx_codigo_sise_txt',
'e_bradescoseg_cx_codigo_produto_txt',
'e_bradescoseg_cx_cpf_segurado_bvp_txt',
'e_bradescoseg_cx_parentesco_vida_auto',
'e_bradescoseg_cx_tipo_fundo_prev_auto',
'e_bradescoseg_cx_cnpj_fundo_prev_txt',
'e_bradescoseg_cx_tipo_regime_auto',
'e_bradescoseg_cx_data_solicitacao_date',
'e_bradescoseg_cx_nome_estipulante_auto',
'e_bradescoseg_cx_coringa1_int',
'e_bradescoseg_cx_coringa2_int',
'e_bradescoseg_cx_coringa3_int',
'e_bradescoseg_cx_coringa4_int',
'e_bradescoseg_cx_coringa5_txt',
'e_bradescoseg_cx_coringa6_txt',
'e_bradescoseg_cx_coringa7_txt',
'e_bradescoseg_cx_coringa8_txt',
'e_bradescoseg_cx_coringa9_txt',
'e_bradescoseg_cx_coringa10_txt',
'e_bradescoseg_cx_coringa11_txt',
'e_bradescoseg_cx_coringa12_txt',
'e_bradescoseg_cx_coringa13_txt',
'e_bradescoseg_cx_coringa14_txt',
'e_bradescoseg_cx_coringa15_txt',
'e_bradescoseg_cx_coringa8_descricao_txt',
'e_bradescoseg_cx_coringa11_data_cancelamento_date',
'e_bradescoseg_cx_coringa2_numero_protocolo_int',
'e_bradescoseg_cx_segmento_cliente_auto',
'e_bradescoseg_cx_cidade_auto',
'e_bradescoseg_cx_produto_enum',
'e_bradescoseg_cx_agencia_txt',
'e_bradescoseg_cx_coringa14_classif_vulnerabilidade_enum',
'e_bradescoseg_cx_coringa8_frequencia_reembolso_enum',
'e_bradescoseg_cx_natureza_dano_formatado_auto',
'e_bradescoseg_cx_produto_txt',
'e_bradescoseg_cx_situacao_reembolso_auto',
'e_bradescoseg_cx_status_enum',
'e_bradescoseg_cx_coringa15_teste_ab_enum',
'e_bradescoseg_cx_episodio_testeab_enum',
'e_bradescoseg_cx_tipo_resgate_enum',
'e_bradescoseg_cx_proposta_prev_txt',
'e_bradescoseg_cx_faixa_valor_resgate_enum',
'e_bradescoseg_cx_faixa_valor_pago_enum',
'e_bradescoseg_cx_nome_ramo_enum',
'e_bradescoseg_cx_sucursal_auto',
'e_bradescoseg_cx_coringa5_sinistrado_enum',
'e_bradescoseg_cx_coringa8_descricao_produto_enum',
'e_bradescoseg_cx_coringa5_descricao_produto_auto',
'e_bradescoseg_cx_coringa9_descricao_produto_auto',
'e_bradescoseg_cx_regional_auto',
'e_bradescoseg_cx_coringa9_passagem_bac_yn',
'e_bradescoseg_cx_coringa13_canal_pesquisa_enum',
'e_bradescoseg_flag_ciclocompleto_yn',
'e_bradescoseg_cx_central_centraldeatendimento_enum',
'e_bradescoseg_cx_ouvid_finalizados_forma_retorno_auto',
'e_bradescoseg_cx_ouvid_finalizados_tipo_manifest_auto',
'e_bradescoseg_cx_ouvid_finalizados_resultado_manifest_auto',
'e_bradescoseg_cx_ouvid_finalizados_manifestacao_enum',
'e_bradescoseg_cx_ouvid_finalizados_grupo_manifest_auto',
'e_bradescoseg_cx_ouvid_finalizados_prod_assunto_auto',
'e_bp_digital_device_hardware_type_auto',
'e_bp_digital_device_os_name_auto',
'e_bp_digital_browser_name_auto',
'e_bp_digital_city_auto',
'e_bp_digital_itm_survey_alt',
'e_bp_digital_unit',
'e_bp_digital_region_auto',
'e_bp_digital_mobile_app_version_auto',
'e_bp_digital_browser_version_auto',
'e_bp_digital_mobile_sdk_version_auto',
'e_bp_digital_device_os_version_auto',
'e_bp_digital_mobile_os_version_auto',
'a_surveyid',
'a_topics_tagged_original',
'a_action_plan_themes_alts',
'a_action_plan_topics_alts',
'a_topics_sentiments_tagged_after_manual_updates',
'a_topics_sentiments_tagged_original',
'a_ipaddress',
'k_bp_timezone_creation_time',
'k_bp_timezone_response_time',
'k_bradescoseg_cx_fechamento_alerta_enum',
'k_bradescoseg_cx_regiao_medico_enum',
'k_bradescoseg_cx_ctl_formulario_ligacoes_auto',
'k_bradescoseg_cx_ctl_alerta_fechado_yn',
'k_bradescoseg_cx_alertas_fechados_por_txt',
'k_bradescoseg_cx_ctl_alerta_com_dono_yn',
'k_bradescoseg_cx_segmento_nps_enum',
'k_bradescoseg_cx_regiao_enum',
'k_bradescoseg_cx_faixa_etaria_enum',
'k_bradescoseg_cx_faixa_etaria75_enum',
'k_bradescoseg_cx_oficinasauto_yn',
'k_bradescoseg_cx_central_cpf_txt',
'k_bradescoseg_cx_central_ltr_na_txt',
'k_bradescoseg_cx_central_operador_nome_txt',
'k_bradescoseg_cx_central_pesquisa_respondida_yn',
'k_bp_survey_device_finished_on_alt',
'k_bp_survey_browser_auto',
'k_bp_survey_os_auto',
'k_bradescoseg_nota_geral_scale',
'q_bradescoseg_cx_episodio_ltr_scale',
'q_bradescoseg_cx_episodio_ltr_motivo_cmt',
'q_bradescoseg_cx_relacionamento_ltr_scale',
'q_bradescoseg_cx_rlc_cliente_ltr_scale',
'q_bradescoseg_cx_rlc_cliente_ltr_motivo_cmt',
'q_bradescoseg_cx_reembolso_atendimento_particular_enum',
'q_bradescoseg_cx_episodio_agilidade_processo_scale',
'q_bradescoseg_cx_episodio_orientacoes_recebidas_scale',
'q_bradescoseg_cx_episodio_cordialidade_regulador_scale',
'q_bradescoseg_cx_episodio_documentacao_solicitada_scale',
'q_bradescoseg_cx_episodio_acionamento_seguro_scale',
'q_bradescoseg_cx_central_ltr_scale',
'q_bradescoseg_cx_central_solicitacao_atendida_scale',
'q_bradescoseg_cx_ouvid_finalizados_csat_1to10_scale',
'q_bradescoseg_cx_ouvid_finalizados_csat_motivo_cmt',
'q_bradescoseg_cx_ouvid_finalizados_solicitacao_resolvida_yn',
'q_bradescoseg_cx_ouvid_finalizados_solicitacao_resolvida_cmt',
'q_md_17497_ces_abertura_de_sinistro',
'q_md_17497_motivo_da_nota_ces_abertura_de_sinistro',
'q_md_17496_perfil_do_usu_rio',
'q_bradescoseg_digital_pi_ltr_scale',
'q_bradescoseg_digital_pi_ltr_reason_ctm'
]


if colunas != layout:
    print("LAYOUT DIVERGENTE")
else:
    print("LAYOUT OK")