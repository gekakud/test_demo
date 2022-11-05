from streamlit_webrtc import webrtc_streamer


def app_loopback():
    """Simple video loopback"""
    webrtc_streamer(key="loopback")
    