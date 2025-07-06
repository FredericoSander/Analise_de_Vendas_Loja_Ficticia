from pipeline.extract import extract_from_excel# Importa a função extract_from_excel do módulo analise_vendas_loja_ficticia

lista_de_data_frame = extract_from_excel("data/raw")
print(lista_de_data_frame) # Chama a função para extrair dados dos arquivos Excel na pasta especificada