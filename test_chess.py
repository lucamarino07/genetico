import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def chess_board(regine):
    chessboard = np.zeros((regine,regine))
    chessboard[1::2, 0::2] = 1
    chessboard[0::2, 1::2] = 1

    return chessboard