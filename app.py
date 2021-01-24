import streamlit as st
from genetico import run_genetico


regine = st.number_input('REGINE', min_value=4 ,step=1)



a =st.button('RUN')

if a is True:
    soluzione = run_genetico(regine, 100)
    st.text(soluzione)