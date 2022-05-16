import os

import pandas as pd
import streamlit as st
from sqlalchemy import create_engine

pwd = os.getcwd()
file_path = os.path.join(pwd, "data/clean_data.csv")

# conn = create_engine('mysql+pymysql://root:root@127.0.0.1/tellco')

st.title("User Overview analysis")
st.header("Overall Handset Manufacturers and Type Data")


# query = "SELECT * FROM satisfaction_scores LIMIT 10"

# df = pd.read_sql(query, conn)


df = pd.read_csv(file_path, parse_dates=["Start", "End"])

top_10_handsets = df["Handset Type"].value_counts().nlargest(10)

st.header("Top 10 Handsets used by customers")
st.write(top_10_handsets)

top_3_handset_manufacturers = (
    df["Handset Manufacturer"].value_counts().nlargest(3)
)

st.header("Top 3 Handsets Manfacturers")
st.write(top_3_handset_manufacturers)

top_5_apple_handsets = (
    df[df["Handset Manufacturer"] == "Apple"][
        ["Handset Manufacturer", "Handset Type"]
    ]
    .groupby("Handset Type")
    .count()
    .nlargest(n=5, columns="Handset Manufacturer")
)

st.header("Top 5 Handsets Made By Apple")
st.write(top_5_apple_handsets)

top_5_samsung_handsets = (
    df[df["Handset Manufacturer"] == "Samsung"][
        ["Handset Manufacturer", "Handset Type"]
    ]
    .groupby("Handset Type")
    .count()
    .nlargest(n=5, columns="Handset Manufacturer")
)

st.header("Top 5 Handsets Made By Samsung")
st.write(top_5_samsung_handsets)

top_5_huawei_handsets = (
    df[df["Handset Manufacturer"] == "Huawei"][
        ["Handset Manufacturer", "Handset Type"]
    ]
    .groupby("Handset Type")
    .count()
    .nlargest(n=5, columns="Handset Manufacturer")
)

st.header("Top 5 Handsets Made By Huawei")
st.write(top_5_huawei_handsets)

st.sidebar.title("TellCo User Analytics")
