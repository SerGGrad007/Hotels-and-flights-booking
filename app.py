import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Streamlit example")
st.header("Example 1")
st.header("Subexample 1.1")

df = pd.read_csv('train.csv')
st.write(df)

st.markdown("хз")

# st.badge("New")
# st.badge("Success", icon=":material/check:", color="green")

# st.markdown(
#     ":violet-badge[:material/star: Favorite] :orange-badge[⚠️ Needs review] :gray-badge[Deprecated]"
# )

# video_file = open("video_2025-04-20_18-34-09.mp4", "rb")
# video_bytes = video_file.read()

# st.video(video_bytes)

# color = st.color_picker("Pick A Color", "#00f900")
# st.write("The current color is", color)

# from numpy.random import default_rng as rng

# df = pd.DataFrame(
#     rng(0).standard_normal((1000, 2)) / [50, 50] + [37.76, -122.4],
#     columns=["lat", "lon"],
# )

# st.map(df)

st.bar_chart(df.groupby(['Pclass', 'Survived'],as_index=False).agg({'PassengerId':'count'}), horizontal=True, y = 'PassengerId', x = 'Pclass', color = 'Survived')




fig = px.scatter(df, y="Fare", x="Age")

st.plotly_chart(fig)