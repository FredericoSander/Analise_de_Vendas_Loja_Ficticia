"""Esse é o módulo de teste do pipeline."""

import pandas as pd

from app.pipeline.transform import concat_data_frames


df_1 = pd.DataFrame({"Col1": [1, 2], "Col2": [3, 4]})
df_2 = pd.DataFrame({"Col1": [5, 6], "Col2": [7, 8]})
df_3 = pd.DataFrame({"Col1": [9, 10], "Col2": [11, 12]})


def testar_a_concatenação_da_lista_de_dataframe():
    """Testa a concatenação de uma lista de DataFrames."""
    arrange = pd.concat([df_1, df_2, df_3], ignore_index=True)
    # Arrange: DataFrame esperado

    act = concat_data_frames([df_1, df_2, df_3])
    # Act:Chamada da função a ser testada

    assert arrange.equals(act)  # Testa a concatenação de uma lista de DataFrames
