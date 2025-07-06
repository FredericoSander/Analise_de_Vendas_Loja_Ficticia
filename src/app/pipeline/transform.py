import pandas as pd
from typing import List

"""
    função para ler arquivos Excel de uma pasta específica e concatená-los em um único DataFrame.
"""
def concat_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index=True)

