import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def Checkerboard(N,n):
    """N: size of board; n=size of each square; N/(2*n) must be an integer """
    if (N%(2*n)):
        print('Error: N/(2*n) must be an integer')
        return False
    a = np.concatenate((np.zeros(n),np.ones(n)))
    b=np.pad(a,int((N**2)/2-n),'wrap').reshape((N,N))
    x = (b+b.T==1).astype(int)
    return np.where(x == 0, 1, 0)

# B=Checkerboard(64,8)
# print(B[0].T)
# df = pd.DataFrame(B)
# plt.imshow(B)
# plt.show()