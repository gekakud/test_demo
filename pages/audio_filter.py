from streamlit_webrtc import AudioProcessorBase, webrtc_streamer
import av
import numpy as np
import pydub
import streamlit as st

def app_audio_filter():
    DEFAULT_GAIN = 1.0

    class AudioProcessor(AudioProcessorBase):
        gain = DEFAULT_GAIN

        def recv(self, frame: av.AudioFrame) -> av.AudioFrame:
            raw_samples = frame.to_ndarray()
            sound = pydub.AudioSegment(
                data=raw_samples.tobytes(),
                sample_width=frame.format.bytes,
                frame_rate=frame.sample_rate,
                channels=len(frame.layout.channels),
            )

            sound = sound.apply_gain(self.gain)

            channel_sounds = sound.split_to_mono()
            channel_samples = [s.get_array_of_samples() for s in channel_sounds]
            new_samples: np.ndarray = np.array(channel_samples).T
            new_samples = new_samples.reshape(raw_samples.shape)

            new_frame = av.AudioFrame.from_ndarray(new_samples, layout=frame.layout.name)
            new_frame.sample_rate = frame.sample_rate
            return new_frame

    webrtc_ctx = webrtc_streamer(key="audio-filter",
        audio_processor_factory=AudioProcessor,
        async_processing=True,
    )

    if webrtc_ctx.audio_processor:
        webrtc_ctx.audio_processor.gain = st.slider("Gain", -10.0, +20.0, DEFAULT_GAIN, 0.05)