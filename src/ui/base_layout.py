import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
        .stApp {
            background: #5865F2;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
            background: #E0E3FF;
        }
        </style>
        """,
        unsafe_allow_html=True
    )


def style_base_layout():
    st.markdown(
        """
        <style>

        /* Google Fonts */
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

        /* Hide Streamlit menu and footer */
        #MainMenu, footer, header {
            visibility: hidden;
        }

        /* Main container spacing */
        .block-container {
            padding-top: 1.5rem !important;
        }

        /* Heading styles */
        h1 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            margin-bottom: 0rem !important;
            color: white !important;
        }

        h2 {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2.5rem !important;
            line-height: 0.9 !important;
            margin-bottom: 0rem !important;
            color: black !important;
        }

        /* Text styles */
        h3, h4, h5, h6, p{
            font-family: 'Outfit', sans-serif !important;
        }

        /* Primary buttons */
        button {
            border-radius: 1.5rem !important;
            background: #5865F2 !important;
            color: white !important;
            padding: 10px 20px !important;
            border: none !important;
            transition: transform 0.25s ease-in-out !important;
            font-family: 'Outfit', sans-serif !important;
            font-weight: 600 !important;
        }

        /* Secondary button */
        button[kind="secondary"] {
            background: #EB459E !important;
            color: white !important;
        }

        /* Tertiary button */
        button[kind="tertiary"] {
            background: black !important;
            color: white !important;
        }

        /* Hover animation */
        button:hover {
            transform: scale(1.05);
        }

        </style>
        """,
        unsafe_allow_html=True
    )