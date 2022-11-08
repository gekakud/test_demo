import streamlit as st
from streamlit_option_menu import option_menu

from pages.camera_stream import app_loopback


def main():
    st.sidebar.image("logo.png", use_column_width=True)
    with st.sidebar:
        # https://github.com/victoryhb/streamlit-option-menu
        s = option_menu("Main menu", ["Video stream", "Image preview", "Video filter", "Upload", "Code editor"],
                        icons=['file-earmark-code', 'check2-circle', 'cpu-fill'], menu_icon="cast", default_index=0)
    if s == "Video stream":
        app_loopback()

if __name__ == "__main__":
    main()