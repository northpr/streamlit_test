# Source: https://datarockie.com/blog/python-streamlit-web-app/

import streamlit as st
import pandas as pd

st.header("Hello World 👋")
st.write("Streamlit Testing")


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
# print(df.head())

df2 = df.groupby("species")["body_mass_g"].mean()
# print(df2.head())

st.bar_chart(df2)

genre = st.radio("What's your favorite movie genre", ("Comedy", "Drama", "Documentary"))
st.write(f"You selected {genre}")

# Run it with streamlit run <app-name>.py