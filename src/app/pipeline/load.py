"""esse é o arquivo load.py, que salva os DataFrames em um arquivo Excel."""

import os

import pandas as pd


def load_excel(data_frame: pd.DataFrame, processed_path: str, file_name: str) -> str:
    """Recebe a list of DataFrames and salva no arquivo excel.

    Args:
    data_frame (pd.DataFrame): DataFrames a ser salvo como excel.
    output_file (str): Caminho do arquivo de saída.
    file_name (str): nome do arquivo a ser salvo.

    return:
    DataFrame contendo os dados de todos os arquivos CSV.
    """

    if not os.path.exists(processed_path):
        os.makedirs(processed_path)

    data_frame.to_excel(f"{processed_path}/{file_name}.xlsx", index=False)
    return "Arquivo salvo com sucesso"
