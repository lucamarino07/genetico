import streamlit as st
from genetico import run_genetico
from test_chess import chess_board
import matplotlib.pyplot as plt
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

regine = st.number_input('REGINE', min_value=4 ,step=1)



a =st.button('RUN')

if a is True:

    soluzione = run_genetico(regine, 100)
    st.text(soluzione)
    plt.imshow(chess_board(regine=regine), cmap='binary')
    plt.axis('off')
    plt.scatter(np.array(soluzione[0])-1, range(0,regine))
    st.pyplot()