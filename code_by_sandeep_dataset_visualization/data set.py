import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


st.set_page_config(page_title="Iris Dataset Visualization")


@st.cache_data
def load_data():
    return sns.load_dataset("iris")

data = load_data()


st.title("🌸 Iris Dataset Visualization with Streamlit")
st.write("Explore the famous Iris flower dataset using Streamlit charts and plots.")


if st.checkbox("Show raw data"):
    st.subheader("Raw Iris Data")
    st.dataframe(data)


plot_type = st.selectbox("Select plot type", ["Line Chart", "Bar Chart", "Scatter Plot"])


numeric_columns = data.select_dtypes(include=['float64']).columns.tolist()
x_axis = st.selectbox("Select X-axis", options=numeric_columns)
y_axis = st.selectbox("Select Y-axis", options=numeric_columns)


st.subheader(f"{plot_type} between {x_axis} and {y_axis}")

if plot_type == "Line Chart":
    st.line_chart(data[[x_axis, y_axis]])

elif plot_type == "Bar Chart":
    st.bar_chart(data[[x_axis, y_axis]])

elif plot_type == "Scatter Plot":
    fig, ax = plt.subplots()
    sns.scatterplot(x=data[x_axis], y=data[y_axis], hue=data['species'], ax=ax)
    st.pyplot(fig)


sepal_min = st.slider("Minimum Sepal Length", float(data["sepal_length"].min()), float(data["sepal_length"].max()), float(data["sepal_length"].min()))
filtered_data = data[data["sepal_length"] >= sepal_min]

st.write(f"Filtered data (Sepal Length ≥ {sepal_min}):")
st.dataframe(filtered_data)
