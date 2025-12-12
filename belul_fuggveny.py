import numpy as np
def pontok_belul(pontok, kozep, hatar):
    kulonbseg = pontok - kozep
    tavolsagok = np.linalg.norm(kulonbseg, axis=1)
    belul = tavolsagok <= hatar
    return belul