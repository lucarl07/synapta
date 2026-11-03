# ==:== Utilidades Miscelâneas ==:==

import pandas as pd

def startsAt1Index(bd: pd.Series | pd.DataFrame, name: str = "N°"):
    """
    Retorna um índice que começa a partir do número 1, e tem como limite o tamanho da estrutura de 
    dados inserida.
    """

    return pd.RangeIndex(start=1, stop=len(bd) + 1, name=name)

