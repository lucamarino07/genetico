import streamlit as st
from genetico import run_genetico
from test_chess import Checkerboard
import matplotlib.pyplot as plt

regine = st.number_input('REGINE', min_value=4 ,step=1)

chess_board = Checkerboard(regine**2, regine)


a =st.button('RUN')

if a is True:
    st.pyplot(plt.imshow(chess_board, cmap='gray'))
    soluzione = run_genetico(regine, 100)
    st.text(soluzione)