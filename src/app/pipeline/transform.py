"""Transformação de dados para o pipeline de ETL."""

import pandas as pd
from typing import List


def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    """função para ler arquivos Excel de uma pasta específica.

    Após leitura a função concatena os arquivo em um único DataFrame.
    """
    return pd.concat(data_frame_list, ignore_index=True)
