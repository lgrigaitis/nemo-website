import geopandas as gpd
import pandas as pd

explore_df = gpd.read_file('/Users/lgrigaitis/Desktop/df/Data-prediction-pred_kmeans_all_feat.shp')

only_pred = explore_df[explore_df['pred'] == 1]

only_pred.drop(columns=['pred', 'geometry'], inplace=True)

only_pred['lat'] = only_pred['lat'].map("{:.7f}".format)
only_pred['lon'] = only_pred['lon'].map("{:.7f}".format)

ex_df = pd.DataFrame(only_pred)
