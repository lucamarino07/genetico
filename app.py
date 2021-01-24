import streamlit as st
from genetico import run_genetico
from test_chess import chess_board, imscatter
import matplotlib.pyplot as plt
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
        page_title='Problema delle regine',
        layout='wide',
        initial_sidebar_state='auto',
        page_icon='♟',
    )

hide_streamlit_style = """
<style>
MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

regine = st.number_input('REGINE', min_value=4 ,step=1)


zoom = (regine/regine**2) * 0.4
a =st.button('RUN')

if a is True:

    soluzione = run_genetico(regine, 100)

    x = np.array(soluzione[0])-1
    y = range(0,regine)
    image_path = 'queen.png'
    imscatter(x, y, image_path, zoom=zoom)
    plt.imshow(chess_board(regine=regine), cmap='binary')
    # plt.axis('off')
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    st.pyplot()