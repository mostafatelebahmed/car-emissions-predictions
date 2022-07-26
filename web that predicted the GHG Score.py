from cProfile import label
from optparse import Option
from re import X
import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from pickle import FLOAT
from flask import render_template,request,Flask
from helpers.dummies import *
import joblib

# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="prediction", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

with st.container():
    st.subheader("Hi, I am Mostafa Teleb :wave:")
    st.title("And this is a project on car emissions prediction")


# ---- WHAT I DO ----
with st.container():
    st.write("---")
    st.title("Lets start with GHG Score")
    st.write("""Green House Gas just like the air pollution score, the greenhouse gas score is based on a scale of 1 to 10,
    and the higher your car scores, the less your car contributes to 
    global warming and climate change. Carbon emissions from various fuels will vary because every fuel type burns differently.""")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """A typical passenger vehicle emits about 4.6 metric tons of carbon dioxide per year. 
            This assumes the average gasoline vehicle on the road today has a fuel economy of about 22.0 miles per gallon 
            and drives around 11,500 miles per year.
             Every gallon of gasoline burned creates about 8,887 grams of CO2.""")
        st.write(
            """Among the three greenhouse gasses that are emitted by vehicles, carbon dioxide (CO2) 
            accounted for 98% while methane (CH4) and nitrous oxide (N2O) accounted for the balance""")
        st.write("[Learn More about this score >](https://auto.howstuffworks.com/fuel-efficiency/hybrid-technology/greenhouse-gas-score.htm)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.write({{X}})
    st.write("##")

    st.button(label="predict the GHG score")
