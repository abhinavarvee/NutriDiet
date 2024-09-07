import streamlit as st
from login import login_user
from registration_page import register_user
from db import init_db
from nav import nav
st.set_page_config(page_title='NutriDiet',page_icon="🍎")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
    
    body {
        background-color: #f0f2f6;
        color: #333;
        font-family: 'Roboto', sans-serif;
    }
    .container {
        max-width: 500px;
        margin: auto;
        padding: 20px;
        background-color: #fff;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
        text-align: center;
    }
    
    .container h1 {
        margin-bottom: 20px;
    }
    
    .container input[type="text"],
    .container input[type="password"] {
        width: calc(100% - 40px); 
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 5px;
        font-family: 'Roboto', sans-serif;
        font-size: 14px;
        box-sizing: border-box;
    }
    
    .container button {
        background-color: #4CAF50;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        cursor: pointer;
        transition: 0.3s;
        font-family: 'Roboto', sans-serif;
        font-size: 14px;
    }
    
    .container button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)
def login_page():
    st.markdown("<h1>NutriDiet</h1>", unsafe_allow_html=True)
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
    .stApp {
             background: url("https://www.artofliving.org/in-en/app/uploads/2023/11/healthy-food-habits-to-maintain-wellness-scaled.jpg");
             background-size: cover
         }
                 </style>
    """, unsafe_allow_html=True)
    st.markdown("<h3>Login</h3>", unsafe_allow_html=True)
    login_username = st.text_input("Username", key="login_username")
    login_password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login"):
        result, message = login_user(login_username, login_password)
        if result:
            st.success(message)
            st.session_state.logged_in = True
            st.session_state.username = login_username 
        else:
            st.warning(message)
    
    st.markdown("Don't have an account? ")
    if st.button("Register"):
        st.session_state.page = "register"
    

def register_page():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Roboto:wght@400;700&display=swap');
            
    .stApp {
             background: url("https://www.artofliving.org/in-en/app/uploads/2023/11/healthy-food-habits-to-maintain-wellness-scaled.jpg");
             background-size: cover
         }
                 </style>
    """, unsafe_allow_html=True)
    st.markdown("<h1>NutriDiet</h1>", unsafe_allow_html=True)
    st.markdown("<h3>Register</h3>", unsafe_allow_html=True)
    register_username = st.text_input("Username", key="register_username")
    register_password = st.text_input("Password", type="password", key="register_password")
    if st.button("Register"):
        result, message = register_user(register_username, register_password)
        if result:
            st.success(message)
        else:
            st.warning(message)

    st.markdown("Already have an account? ")
    if st.button("Login"):
        st.session_state.page = "login"

def main():
    init_db()

    if "page" not in st.session_state:
        st.session_state.page = "login"
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        if st.session_state.page == "login":
            login_page()
        elif st.session_state.page == "register":
            register_page()
    else:
        
        nav(st.session_state.username)
            

if __name__ == "__main__":
    main()
