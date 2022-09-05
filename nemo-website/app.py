import streamlit as st
import requests
import geopandas as gpd
from PIL import Image
import folium
import pandas as pd

# url = 'https://savenemoimage-mcwnbka6oq-ew.a.run.app'

# response = requests.get(url).json()

# st.json(response)


st.set_page_config(
     page_title="Home for Nemo",
     page_icon="🔎🏠🐠",
     layout="wide",
     menu_items={
         'Get Help': 'https://www.extremelycoolapp.com/help',
         'Report a bug': "https://www.extremelycoolapp.com/bug",
         'About': "# This is a header. This is an *extremely* cool app!"
     }
 )

st.title("Let's find Nemo the best location!")

# df = gpd.read_file("/Users/lgrigaitis/code/lgrigaitis/nemo-website/notebooks/mpa_poli_with_country.shp")
# df.crs = "EPSG:4326"
# # Plotting the map with Folium
# m = folium.Map(location=[53.0000, 9.0000], zoom_start=4)
# folium.Choropleth(
#     geo_data=df,
#     data=df,
#     columns=['PARENT_ISO', 'area'],
#     fill_color='RdYlBu',
#     fill_opacity=0.7,
#     line_opacity=0.2,
#     line_color='white',
#     line_weight=0,
#     highlight=False,
#     smooth_factor=1.0).add_to(m)

im = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/nemo_picture.png')
mpa_image = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/MPA.png')

map_data = pd.DataFrame({'lat': [53.0000], 'lon': [9.0000]})

with st.container():
    map_col, text_col, text_col_2 = st.columns((3,1,1))
    with map_col:
        st.map(map_data)

    with text_col:
        st.subheader("What is an MPA?")
        st.write("These marine areas can come in many forms ranging from wildlife refuges to research facilities. MPAs restrict human activity for a conservation purpose, typically to protect natural or cultural resources.")

    with text_col_2:
        st.subheader("What is an MPA?")
        st.write("These marine areas can come in many forms ranging from wildlife refuges to research facilities. MPAs restrict human activity for a conservation purpose, typically to protect natural or cultural resources.")


st.markdown("## What are the benefits of MPA's?")
st.image(mpa_image)
