# This one works

# file_ = open("/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/giphy.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()


# st.markdown(
#     f'<img src="data:image/gif;base64,{data_url}" alt="cat gif">',
#     unsafe_allow_html=True,
# )
        # background-size: 1600px 700px;
        # background-repeat: no-repeat




# Doesn't work #1

# page_bg_img = '''
# <style>
# body {
# background-image: url("https://images.unsplash.com/photo-1542281286-9e0a16bb7366");
# background-size: cover;
# }
# </style>
# '''

# st.markdown(page_bg_img, unsafe_allow_html=True)



# Doesn't work #2

# file_ = open("/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/Ocean - 21175.mp4", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode()
# file_.close()


# video_html = """
# 		<style>

# 		#myVideo {
# 		  position: fixed;
# 		  right: 0;
# 		  bottom: 0;
# 		  min-width: 100%;
# 		  min-height: 100%;
# 		}

# 		.content {
# 		  position: fixed;
# 		  bottom: 0;
# 		  background: rgba(0, 0, 0, 0.5);
# 		  color: #f1f1f1;
# 		  width: 100%;
# 		  padding: 20px;
# 		}

# 		</style>
# 		<video autoplay muted loop id="myVideo">
# 		  f<source type="video/mp4" src="data:video/mp4;base64,{data_url}" alt="sea")>
# 		</video>
#         """

# st.markdown(video_html, unsafe_allow_html=True)
# st.title('Video page')



# Doesn't work #3

# file_ = open("/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/giphy.gif", "rb")
# contents = file_.read()
# data_url = base64.b64encode(contents).decode("utf-8")
# file_.close()


# page_bg_img = '''
# <style>
# body {
# background-image: url(f'data:image/gif;base64,{data_url}');
# background-size: cover;
# }
# </style>
# '''


# st.markdown(
#     page_bg_img,
#     unsafe_allow_html=True,
# )


# Doesn't work #4

# def get_base64(bin_file):
#     with open(bin_file, 'rb') as f:
#         data = f.read()
#     return base64.b64encode(data).decode("utf-8")


# def set_background(png_file):
#     bin_str = get_base64(png_file)
#     page_bg_img = '''
#     <style>
#     body {
#     background-image: url("data:image/png;base64,%s");
#     background-size: cover;
#     }
#     </style>
#     ''' % bin_str
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# set_background('/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/MPA.png')


# df_2 = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.dataframe(df)
# st.dataframe(df_2)





# video_file = open("/Users/lgrigaitis/code/lgrigaitis/nemo-website/raw_data/Ocean - 21175.mp4", "rb")
# video_bytes = video_file.read()
# st.video(video_bytes)

# st.markdown("![Alt Text](https://media.giphy.com/media/3ndAvMC5LFPNMCzq7m/giphy-downsized-large.gif)")



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
