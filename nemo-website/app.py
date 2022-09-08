import streamlit as st
import requests
import geopandas as gpd
from PIL import Image
import folium
import pandas as pd
import numpy as np
import pydeck as pdk
import base64
from dataset import ex_df

# url = 'https://savenemoimage-mcwnbka6oq-ew.a.run.app'

# response = requests.get(url).json()

# st.json(response)

url = 'https://savenemoimage-mcwnbka6oq-ew.a.run.app/new_mpa'


with open("nemo-website/styles.css") as f:
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
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# padding = 0
# st.markdown(f""" <style>
#     .reportview-container .main .block-container{{
#         padding-top: {padding}rem;
#         padding-right: {padding}rem;
#         padding-left: {padding}rem;
#         padding-bottom: {padding}rem;
#     }} </style> """, unsafe_allow_html=True)

df = pd.DataFrame({'lat': [41.8931, 45.4669, 40.8333], 'lon': [12.4828, 9.1900, 14.2500]})


def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/gif;base64,{encoded_string.decode("utf-8")});
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/giphy2.gif')


st.title("Finiding the best Marine Protected Areas (MPA's)")


im1 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/marine1.jpg')
im2 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/marine2.jpg')
im3 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/marine3.jpg')
im4 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/marine4.jpg')

mpa_image = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/MPA.png')


with st.container():
    text_col, text_col_2, text_col_3,  text_col_4= st.columns((1,1,1,1))
    with text_col:
        st.subheader("MPA")
        st.image(im3)
        st.markdown("#### Geographically distinct zones with set protection objectives.")

    with text_col_2:
        st.subheader("Ecosystem")
        st.image(im2)
        st.markdown("#### The system of living and non-living components that coexist in the same area.")

    with text_col_3:
        st.subheader("Biodiversity")
        st.image(im1)
        st.markdown("#### The different kinds of life you’ll find in one area, from animals to microorganisms.")

    with text_col_4:
            st.subheader("Ecosystem service")
            st.image(im4)
            st.markdown("#### Any positive, quantifiable benefit that an healthy ecosystem provides to people.")


mpa_map = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/eu_mpa.jpg')
percentage_image = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/percentage.png')

st.markdown("## MPA's in Europe")
with st.container():
    mpscreenCol, textCol=st.columns((3, 2))

    with mpscreenCol:
        st.image(mpa_map)

    with textCol:
        st.image(percentage_image)
        st.markdown("### Although more than 10% of EU seas are now labelled as MPAs, \
                representing almost 625,000 km2, most of these areas are mere ‘paper parks’ \
                with little effective protection in place.")



image1 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/coral-icon.png')
image2 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/fish-icon.png')
image3 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/Travel-icon.png')
image4 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/protect-icon.png')
image5 = Image.open('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/water-icon.png')


st.markdown("## The benefits of MPA")
with st.container():
    iconCol_1, iconCol_2, iconCol_3, iconCol_4, iconCol_5=st.columns((1, 1, 1, 1, 1))

    with iconCol_1:
        st.image(image1)
        st.markdown("#### Increased resilience and maintenance of ecosystem services ")

    with iconCol_2:
        st.image(image2)
        st.markdown("#### Fisheries spill-over")

    with iconCol_3:
        st.image(image3)
        st.markdown("#### Increased recreational and tourism opportunities")

    with iconCol_4:
        st.image(image4)
        st.markdown("#### Protection of biodiversity and increased productivity")

    with iconCol_5:
        st.image(image5)
        st.markdown("#### Better shoreline stabilization")





st.markdown("## The predicted MPA's on the map")

with st.container():
   commentaryCol, spaceCol, chartCol=st.columns((2,1,6))
   # Description
   with commentaryCol:
      st.write("Input the minimum and maximum lantitude and longtitude in order \
          to get the MPA points on the map")
      form = st.form(key='my_form')
    #   min_lat=st.slider("Write the minimum latitude", min_value=-40.0000, max_value=24.0000, value=-40.0000, step=0.1000)
    #   min_lng=st.slider("Write the minimum longtude", min_value=0.0000, max_value=39.0000, value=0.0000, step=0.1000)
    #   max_lat=st.slider("Write the maximum latitude", min_value=25.0000, max_value=90.0000, value=40.0000, step=0.1000)
    #   max_lng=st.slider("Write the maximum longtude", min_value=40.0000, max_value=80.0000, value=40.0000, step=0.1000)

    #   min_lat=st.slider("Write the minimum latitude", min_value=30.0000, max_value=54.0000, value=30.0000, step=0.1000)
    #   min_lng=st.slider("Write the minimum longtude", min_value=-20.0000, max_value=9.0000, value=-20.0000, step=0.1000)
    #   max_lat=st.slider("Write the maximum latitude", min_value=55.0000, max_value=75.0000, value=55.0000, step=0.1000)
    #   max_lng=st.slider("Write the maximum longtude", min_value=10.0000, max_value=40.0000, value=10.0000, step=0.1000)

    #   minimum_lat=st.slider("Write the minimum latitude", min_value=30.0000, max_value=75.0000, value=30.0000, step=0.1000)
    #   minimum_lng=st.slider("Write the minimum longtude", min_value=-20.0000, max_value=40.0000, value=-20.0000, step=0.1000)
    #   maximum_lat=st.slider("Write the maximum latitude", min_value=minimum_lat, max_value=75.0000, value=minimum_lat, step=0.1000)
    #   maximum_lng=st.slider("Write the maximum longtude", min_value=minimum_lng, max_value=40.0000, value=minimum_lng, step=0.1000)

      minimum_lat=st.slider("Write the minimum latitude", min_value=-40.0000, max_value=90.0000, value=-40.0000, step=0.2500)
      maximum_lat=st.slider("Write the maximum latitude", min_value=minimum_lat, max_value=90.0000, value=minimum_lat, step=0.2500)
      minimum_lng=st.slider("Write the minimum longtude", min_value=-20.0000, max_value=80.0000, value=-20.0000, step=0.2500)
      maximum_lng=st.slider("Write the maximum longtude", min_value=minimum_lng, max_value=80.0000, value=minimum_lng, step=0.2500)

      submit_button = form.form_submit_button(label='Submit')
    #   if submit_button:
      if submit_button:
        params = {
            "min_lat": minimum_lat,
            "max_lat": maximum_lat,
            "min_lon": minimum_lng,
            "max_lon": maximum_lng
            }
        response = requests.get(url, params=params).json()
        print(response)

        df_4 = pd.DataFrame.from_dict(response["key"])
        input_2 = gpd.GeoDataFrame(df_4, geometry=gpd.points_from_xy(df_4.lat, df_4.lon))

        # set the new coordinates system and drop the old lat and lon columns
        # input = input.set_crs('WGS84', allow_override=True)
        # input = input.drop(columns=['lat', 'lon'])

        # recreate lat and lon in the new coordinates systems and drop the old geometry to go back to a normal dataframe
        # input['lat'] = input['geometry'].x
        # input['lon'] = input['geometry'].y
        # df_5 = input.drop(columns='geometry')

    #   lat=st.slider("Write the latitude", min_value=30.0000, max_value=75.0000, value=54.5260, step=0.1000)
    #   lng=st.slider("Write the longtude", min_value=-20.0000, max_value=40.0000, value=15.2551, step=0.1000)
   #Chart
        with chartCol:
                st.pydeck_chart(pdk.Deck(
                    map_style=None,
                    initial_view_state=pdk.ViewState(
                        latitude=54.0000,
                        longitude=15.2551,
                        zoom=3,
                        pitch=50,
                    ),
                    layers=[
                        pdk.Layer(
                            'GeoJsonLayer',
                            data=input_2,
                            # get_position='[lat, lon]',
                            # radius=10000,
                            # auto_highlight=True,
                            # elevation_scale=500,
                            # elevation_range=[0, 1000],
                            # pickable=True,
                            # extruded=True,
                        ),
                        pdk.Layer(
                            'ScatterplotLayer',
                            data=input_2,
                            pickable=True,
                            opacity=1,
                            stroked=True,
                            filled=True,
                            radius_scale=50,
                            radius_min_pixels=1,
                            radius_max_pixels=100,
                            line_width_min_pixels=1,
                            get_position="geometry.coordinates",
                            get_radius=1000,
                            get_fill_color=[255, 140, 0],
                            get_line_color=[0, 0, 0],
                        ),
                    ]
                ))


        # st.dataframe(df_4)


# url = 'https://savenemoimage-mcwnbka6oq-ew.a.run.app/new_mpa'

# params = {
#     "min_lat": min_lat,
#     "max_lat": max_lat,
#     "min_lon": min_lng,
#     "max_lon": max_lng
# }


# if submit_button:
#     response = requests.get(url, params=params).json()
#     df_2 = pd.read_json(response)
