import streamlit as st
import math
import requests
from bokeh.plotting import figure, show
from bokeh.tile_providers import get_provider, Vendors

url = "https://api.openweathermap.org/data/2.5/weather?lat={0}&lon={1}&units=metric&appid="
api_key = "8b502954a629d709d6ec5d52e5e54722"

left_col, right_col = st.columns(2)

with left_col:
    st.write("World Map with Airbase Location")
    st.number_input("Enter latitude:")    

tile_provider = get_provider(Vendors.CARTODBPOSITRON)

lats = [40.106972, 46.070461 , 40.680031, 37.149811, 49.985889, 52.385948, 35.97861]
lons = [32.520821, 12.58675 , 141.365311, 127.077225, 6.68025, 0.52984, 126.71139]

def coords2merc(lat, lon):
    RADIUS = 6378137.0
    merc_lat = math.log(math.tan(math.pi / 4 + math.radians(lat) / 2)) * RADIUS
    merc_lon = math.radians(lon) * RADIUS
    return merc_lat, merc_lon

merc_lats, merc_lons = [], []
for lat, lon in zip(lats, lons):
    merc_lat, merc_lon = coords2merc(lat, lon)
    merc_lats.append(merc_lat)
    merc_lons.append(merc_lon)

p = figure(x_range=(-20000000, 20000000), y_range=(-10000000, 10000000),
           x_axis_type="mercator", y_axis_type="mercator")
p.plot_width = 375
p.plot_height = 400
p.add_tile(tile_provider)
p.circle(x=merc_lons, y=merc_lats, size=10, color="blue")

st.bokeh_chart(p)

with right_col: 
    st.write('Weather and Distance Details')
    st.number_input('Enter longitude')
    st.write("Weather Description")
    


