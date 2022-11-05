from streamlit_webrtc import VideoProcessorBase, webrtc_streamer
import cv2
import streamlit as st
import av

def app_video_filters():
    class VideoTransformer(VideoProcessorBase):
        def __init__(self) -> None:
            self.threshold1 = 100
            self.threshold2 = 200

        def recv(self, frame: av.VideoFrame) -> av.VideoFrame:
            img = frame.to_ndarray(format="bgr24")
            # img = cv2.rotate(img, rotateCode = cv2.ROTATE_90_CLOCKWISE)
            img = cv2.cvtColor(cv2.Canny(img, self.threshold1, self.threshold2), cv2.COLOR_GRAY2BGR)
            return av.VideoFrame.from_ndarray(img, format="bgr24")

    ctx = webrtc_streamer(
            key="opencv-filter",
            video_processor_factory=VideoTransformer,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
        )


    if ctx.video_transformer:
        ctx.video_transformer.threshold1 = st.slider("Threshold1", 0, 1000, 100)
        ctx.video_transformer.threshold2 = st.slider("Threshold2", 0, 1000, 200)