import streamlit as st
from genetico import run_genetico
from test_chess import chess_board, imscatter
import matplotlib.pyplot as plt
import numpy as np
import time

st.set_option('deprecation.showPyplotGlobalUse', False)

st.set_page_config(
        page_title='Problema delle regine',
        # layout='wide',
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

st.markdown("""<p>Il <b>problema delle regine</b> 👑 è un problema che consiste 
nel trovare il modo di posizionare <i>N</i> donne (pezzo degli scacchi ♟) su 
una scacchiera <i>N</i>x<i>N</i> tali che nessuna di esse possa catturarne un'altra, usando i 
movimenti standard della regina. Perciò, una soluzione dovrà prevedere che 
nessuna regina abbia una colonna, traversa o diagonale in comune con un'altra 
regina.<br><br><b>Inserisci il numero di regine e scopri la soluzione</b></p>""", unsafe_allow_html=True)


regine = st.number_input('REGINE', min_value=4 ,step=1)


zoom = (regine/regine**2) * 0.4
a =st.button('Play')

if a is True:

    start_time = time.time()
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
    st.write(time.time() - start_time)