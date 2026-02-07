import os
import streamlit as st

get_path=os.getcwd()
list_png=[t for t in os.listdir(get_path+r'/Album') if t.endswith('.png')]
def delet_img(name_):
    if os.path.exists(get_path+r'/Album' + fr'/{name_}'):
        os.remove(get_path+r'/Album' + fr'/{name_}')
        st.rerun()

for item in list_png:
    path = get_path + r'/Album' + rf'/{item}'
    st.image(path,caption=item.replace('.png',''))
    with st.popover('Delet'):
        st.warning('Are you sure you want to delete this molecule?')
        if st.button('Confirm'):
            delet_img(item)

