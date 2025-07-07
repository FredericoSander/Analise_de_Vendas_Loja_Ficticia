"""Este módulo contém a função principal do pipeline de ETL.

Esse é o arquivo main.py,
responsável por executar o pipeline de ETL para a análise de vendas.
"""

from pipeline.extract import extract_from_excel
# Importa a função extract_from_excel do módulo analise_vendas_loja_ficticia.
from pipeline.transform import concat_data_frames
# Importa a função concat_data_frames do módulo analise_vendas_loja_ficticia.
from pipeline.load import load_excel
# Importa a função save_to_excel do módulo analise_vendas_loja_ficticia.


if __name__ == "__main__":
    data_frame_list = extract_from_excel("data/raw")
    # Chama a função para extrair dados na pasta especificada.
    data_frame = concat_data_frames(data_frame_list)
    # Concatena os DataFrames extraídos em um único DataFrame.
    load_excel(data_frame, "data/processed", "vendas_consolidadas")
    # Salva o DataFrame consolidado em arquivo Excel na pasta especificada.
