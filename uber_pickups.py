# Source: https://docs.streamlit.io/library/get-started/create-an-app

import streamlit as st
import pandas as pd
import numpy as np

st.header("Uber Pickups 🚕")
st.title("Uber Pickups in NYC")

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    # Rename the name of columns
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Done! (using st.cache)')


# ### Inspect the raw data
# st.subheader("Raw data")
# st.write(data)
### Usa a button to toggle data
if st.checkbox("Show raw data"):
    st.subheader("Raw data")
    st.write(data)

### Draw a histogram
st.subheader("Number of pickups by hour")
hist_values= np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)


### Plot data on a map
# # Normal Map
# st.subheader("Map of all pickups")
# st.map(data)
# Drawing the map to show the concertration of pickups at 17:00
hour_to_filter = 17
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f"Map of all pickups at {hour_to_filter}:00")
st.map(filtered_data)