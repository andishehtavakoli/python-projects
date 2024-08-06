import streamlit as st

from linkedin_profile_viewer import get_linkedin_profile
from utils import read_json

st.header('Linkedin Profile Data')

usr = st.text_input("Enter Username")

linkedin_profile = get_linkedin_profile(usr)


st.button("Search", type="primary")

if st.button:
    st.write(linkedin_profile)
else:
    st.write("Unknown")
    