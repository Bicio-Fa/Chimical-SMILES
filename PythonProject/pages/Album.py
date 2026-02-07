import os
import streamlit as st

get_path=os.getcwd()
list_txt=[t for t in os.listdir(get_path+r'\Album') if t.endswith('.png')]

for item in list_txt:
    path = get_path + r'\Album' + rf'\{item}'
    st.image(path,caption=item.replace('.png',''))

