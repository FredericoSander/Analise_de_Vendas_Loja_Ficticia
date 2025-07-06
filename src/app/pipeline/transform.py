import pandas as pd
from Typing import List


"""
    função para ler arquivos Excel de uma pasta específica e concatená-los em um único DataFrame.
"""
def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    
    if not data_frame_list:
        raise ValueError("A lista de DataFrames está vazia.")
    
    return pd.concat(data_frame_list, ignore_index=True)