import streamlit as st
import pandas as pd
st.title("Super Store Sales Dashboard")
df =pd.read_excel(r"E:\Panda\Excel_ sheet_for _working\super-store-sales-dataset-main\super-store-sales-dataset-main\Orders.xlsx")
st.dataframe(df)
st.text("Total Rows:" + str(len(df)))
category = st.sidebar.selectbox("Category",
                        df["Category"].unique()
                       )
region = st.sidebar.selectbox("Region:",df["Region"].unique())
Selected_sales =st.sidebar.slider("Minimum Sales", 0, 10000) 
filtered_df=df[(df["Category"]==category) & (df["Sales"]>Selected_sales) & (df["Region"]==region)]
st.text("Total Rows:" + str(len(filtered_df)))
st.dataframe(filtered_df)
st.text("Total Sales:" + str(round(filtered_df["Sales"].sum(),2)))
st.text("Total Profit:" + str(round(filtered_df["Profit"].sum(),2)))
st.text("Average Sales:" + str(round(filtered_df["Sales"].mean(),2)))
st.text("Max Sales:" + str(round(filtered_df["Sales"].max(),2)))
st.bar_chart(filtered_df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False))
st.bar_chart(filtered_df.groupby("Sub-Category")["Profit"].sum().sort_values(ascending=False))
st.text("Top 5 Rows By Sales:")
st.dataframe(filtered_df.sort_values(by="Sales",ascending = False).head())
col1,col2, col3 = st.columns(3)
with col1:
   st.metric ("Total Sales:", round(filtered_df["Sales"].sum(),2))
with col2:
   st.metric ("Total Profit:", round(filtered_df["Profit"].sum(),2))
with col3:
   st.metric ("Average Sales:", round(filtered_df["Sales"].mean(),2))