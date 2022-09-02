import streamlit as st
import requests
from PIL import Image

# url = 'https://savenemoimage-mcwnbka6oq-ew.a.run.app'

# response = requests.get(url).json()

# st.json(response)


st.title("Let's find Nemo the best location!")

im = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/nemo_picture.png')
mpa_image = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/MPA.png')



with st.container():
    image_col, text_col = st.columns((1,2))
    with image_col:
        st.image(im)

    with text_col:
        st.subheader("What is an MPA?")
        st.write("These marine areas can come in many forms ranging from wildlife refuges to research facilities. MPAs restrict human activity for a conservation purpose, typically to protect natural or cultural resources.")


st.markdown("## What are the benefits of MPA's?")
st.image(mpa_image)
