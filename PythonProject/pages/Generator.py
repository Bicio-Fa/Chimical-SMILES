import  streamlit as st
from rdkit import Chem
from rdkit.Chem import Draw
import  os

path=os.getcwd()

if os.path.exists(path+r'\Album'):
    check=True
else:
    os.mkdir(path+r'\Album')


def save(name_,img_):
    if len(name_)>=5:
        path_to_save = f'Album/{name_}.png'
        img_.save(path_to_save)
        st.success('Saved in the Album!')

    else:
        st.warning('The name must be at least 5 characters long!')

smile=st.text_input(label='SMILE with me :)',placeholder='Insert SMILE...')
mol=Chem.MolFromSmiles(smile)

if smile:
    try:
        img= Draw.MolToImage(mol)

        st.image(img,width=500)
        name = st.text_input('Insert the images name...')

        if st.button('Save'):
            if os.path.exists(f'{name}.txt'):
                st.warning('The image has already been saved to the album!')
            else:
                save(name,img)
    except ValueError as ex:
        st.warning(f'{ex}')
else:
    st.warning('SMILE cannot be empty!')
