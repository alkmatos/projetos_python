import pandas as pd
file_path="C:\\Users\\Andre.matos\\Documents\\MJV\\PROJETOS_CLOUD_AZURE\\medallia\\arqs_hist_faltantes\\medallia1.csv"
delimiter="|"

with open(file_path,'r') as file:
    next(file)  # * pular a primeira linha
    for i, line in enumerate(file,start=2):
        delimiter_count=line.count(delimiter)
        print(f"Linha {i}: {delimiter_count} delimiters")
        print(f"{line}")