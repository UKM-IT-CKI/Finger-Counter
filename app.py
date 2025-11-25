import cv2
import streamlit as st
import os
import av
import time
from streamlit_webrtc import webrtc_streamer, WebRtcMode, RTCConfiguration
from modules.detector import HandDetector
from modules.audio import AudioManager
import modules.ui as ui

# ===========================================
# SETUP
# ===========================================
ui.setup_page()

# Initialize session state
if 'camera_active' not in st.session_state:
    st.session_state.camera_active = False
if 'last_number' not in st.session_state:
    st.session_state.last_number = None

# ===========================================
# SIDEBAR
# ===========================================
ui.render_sidebar()

# ===========================================
# MAIN CONTENT AREA
# ===========================================
ui.render_header()

class HandProcessor:
    def __init__(self):
        self.detector = HandDetector()
        self.current_fingers = None

    def recv(self, frame):
        img = frame.to_ndarray(format="bgr24")
        
        # Process frame
        # detector.process_frame returns (processed_frame, total_fingers)
        processed_img, count = self.detector.process_frame(img)
        self.current_fingers = count
        
        return av.VideoFrame.from_ndarray(processed_img, format="bgr24")

if st.session_state.camera_active:
    # Layout: 2 Columns (Video Feed | Stats Panel)
    col_video, col_stats = st.columns([2, 1], gap="large")
    
    audio_manager = AudioManager()
    
    with col_video:
        st.markdown('<div class="camera-frame">', unsafe_allow_html=True)
        
        # WebRTC Streamer configuration
        ctx = webrtc_streamer(
            key="hand-detection",
            mode=WebRtcMode.SENDRECV,
            rtc_configuration=RTCConfiguration(
                {"iceServers": [{"urls": ["stun:stun.l.google.com:19302"]}]}
            ),
            video_processor_factory=HandProcessor,
            media_stream_constraints={"video": True, "audio": False},
            async_processing=True,
            desired_playing_state=True
        )
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col_stats:
        stats_placeholder = st.empty()
        audio_placeholder = st.empty()
    
    # Real-time update loop
    if ctx.state.playing:
        while ctx.state.playing:
            if ctx.video_processor:
                fingers = ctx.video_processor.current_fingers
                
                if fingers is not None:
                    # Update Stats Panel
                    text_num = audio_manager.get_text_for_number(fingers)
                    with stats_placeholder.container():
                        ui.render_result_panel(fingers, text_num)
                    
                    # Audio Logic
                    if fingers != st.session_state.last_number:
                        st.session_state.last_number = fingers
                        if text_num:
                            audio_html = audio_manager.get_audio_html(text_num)
                            audio_placeholder.markdown(audio_html, unsafe_allow_html=True)
            
            # Small delay to prevent high CPU usage in the loop
            time.sleep(0.1)
            
else:
    ui.render_instructions()