import streamlit as st
from streamlit_option_menu import option_menu

from pages.camera_filter import app_video_filters
from pages.camera_stream import app_loopback
from pages.code_edit import code_edit
from pages.upload_files import upload_files
from pages.image_preview import preview

def main():
    st.sidebar.image("logo.png", use_column_width=True)
    with st.sidebar:
        # https://github.com/victoryhb/streamlit-option-menu
        s = option_menu("Main menu", ["Video stream", "Image preview", "Video filter", "Upload", "Code editor"],
                        icons=['file-earmark-code', 'check2-circle', 'cpu-fill'], menu_icon="cast", default_index=0)
    if s == "Video stream":
        app_loopback()
    elif s == "Image preview":
        preview()
    elif s == "Video filter":
        app_video_filters()
    elif s == "Code editor":
        code_edit()
    else:
        upload_files()

if __name__ == "__main__":
    main()