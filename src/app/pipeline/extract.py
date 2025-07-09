"""Módulo de extração de dados do pipeline."""

import glob  # Biblioteca para listar arquivos.
import os  # Biblioteca uqe mnanipula arquivos e pastas.
from typing import List

import pandas as pd  # Biblioteca para manipulação de dados.


def extract_from_excel(path: str) -> List[pd.DataFrame]:
    """Função ler arquivos CSV e concatená-os em um único DataFrame.

    args:
    input_path(str): Caminho da pasta onde os arquivos CSV estão localizados.

    returns:
    DataFrame contendo os dados de todos os arquivos CSV.
    """
    # Validar se o caminho existe
    if not os.path.exists(path):
        raise FileNotFoundError(f"O caminho '{path}' não existe.")

    if not os.path.isdir(path):
        raise ValueError(f"'{path}' não é um diretório válido.")

    # Listar todos os arquivos Excel (.xlsx) no diretório especificado
    all_files = glob.glob(os.path.join(path, "*.xlsx"))

    # Verificar se há arquivos Excel
    if not all_files:
        raise ValueError(f"Nenhum arquivo Excel (.xlsx) encontrado em '{path}'.")

    data_frame_list = []

    for file in all_files:
        try:
            df = pd.read_excel(file)
            data_frame_list.append(df)
        except Exception as e:
            print(f"Erro ao ler o arquivo {file}: {e}")
            continue

    return data_frame_list


if __name__ == "__main__":
    try:
        data_frame_list = extract_from_excel("data/raw")
        print(data_frame_list)

    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
