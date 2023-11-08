# -- PIP PACKAGES -- #
import streamlit as st
from streamlit_option_menu import option_menu
from isoweek import Week

#---BUILT-IN PYTHON MODULES
from datetime import datetime, date
import calendar
from pprint import pprint
import uuid

#---IMPORT THE DATABASE PYTHON FILE db.py---#
import db as db

#---STREAMLIT SETTINGS---#
page_title = "Weekly dinner and shopping app"
page_icon = ":pouch:"
layout = "centered"

#---STREAMLIT PAGE CONFIG---#
st.set_page_config(page_title=page_title, page_icon=page_icon, layout=layout)
st.title(f"{page_title} {page_icon}")

#---STREAMLIT CONFIG HIDE---#
hide_st_style = """<style>
                #MainMenu {visibility : hidden;}
                footer {visibility : hidden;}
                header {visibility : hidden;}
                </style>
                """
st.markdown(hide_st_style, unsafe_allow_html=True)
