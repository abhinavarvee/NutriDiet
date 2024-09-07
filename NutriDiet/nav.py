import streamlit as st
from home import show_home
from bmi import bmi_calculator
from chatcopy import show_chat
from story import share_story
def nav(user):
    st.title("NutriDiet")


    page = st.sidebar.selectbox("Choose a page", ["Home", "BMI Calculator", "Chat","story","log out"])

    if page == "Home":
        show_home()
    elif page == "BMI Calculator":
        bmi_calculator()
    elif page == "Chat":
        show_chat(user)
    elif page=="story":
        share_story()
    elif page=="log out":
        st.session_state.logged_in = False
        st.success("You have been logged out.")
        page = "login"
      


        
       

