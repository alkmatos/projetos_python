lista=['hextrc_hpu-timestamp','cppsta_ppriv-decimal(7,0)','cmatr_cli_ppriv-decimal(11,0)','dsdo_extrt_ppriv-date','cjunc_depdc-decimal(5,0)','ccta_cli-decimal(7,0)','ccpf_crrtt-decimal(11,0)','vsdo_atual_ppriv-decimal(17,2)','cfrmul_ppriv-decimal(3,0)','hprocm_reg-timestamp','vsdo_empr_ppriv-decimal(17,2)','vsdo_partc_ppriv-decimal(17,2)','cnro_contr_prevd-decimal(10,0)','cidtfd_envio_extrt-decimal(1,0)','cidtfd_emis_extrt-decimal(1,0)','dcontr_plano_prevd-date','cano_bloq_um-decimal(4,0)','cano_bloq_dois-decimal(4,0)','vbloq_um_partc-decimal(17,2)','vbloq_dois_partc-decimal(17,2)','vbloq_um_empr-decimal(17,2)','vbloq_dois_empr-decimal(17,2)']


print(len(lista))

i=1
for l in lista:
    print("{}-{}".format(i,l))
    i+=1