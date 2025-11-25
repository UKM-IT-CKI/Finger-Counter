import streamlit as st
import os
from PIL import Image
from typing import Optional

def setup_page() -> None:
    st.set_page_config(
        page_title="Deteksi Angka Jari AI",
        page_icon="✋",
        layout="wide",
        initial_sidebar_state="expanded"
    )
    load_custom_css()

def load_custom_css() -> None:
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
        
        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
        }
        
        /* Sidebar Styling */
        [data-testid="stSidebar"] {
            background-color: #0e1117;
            border-right: 1px solid rgba(255, 255, 255, 0.1);
        }
        
        /* Logo Styling */
        .logo-container {
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .logo-img {
            filter: drop-shadow(0 0 10px rgba(255, 255, 255, 0.2));
            transition: transform 0.3s ease;
        }
        .logo-img:hover {
            transform: scale(1.05);
        }
        
        /* Sidebar Header Text */
        .sidebar-title {
            text-align: center;
            font-size: 1.5rem;
            font-weight: 700;
            margin-bottom: 5px;
            background: linear-gradient(90deg, #fff, #aaa);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .sidebar-subtitle {
            text-align: center;
            font-size: 0.8rem;
            color: #666;
            margin-bottom: 30px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        /* Status Badge */
        .status-badge {
            background: rgba(255, 255, 255, 0.05);
            border-radius: 12px;
            padding: 15px;
            margin-top: 20px;
            border: 1px solid rgba(255, 255, 255, 0.1);
            text-align: center;
        }
        .status-indicator {
            display: inline-block;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            margin-right: 8px;
        }
        .status-active {
            background-color: #00ff00;
            box-shadow: 0 0 10px #00ff00;
        }
        .status-inactive {
            background-color: #ff0000;
            box-shadow: 0 0 10px #ff0000;
        }
        
        /* Main Content Styling */
        .stCard {
            background: rgba(255, 255, 255, 0.05);
            border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 16px;
            padding: 20px;
            backdrop-filter: blur(10px);
        }
        
        .main-header {
            text-align: center;
            padding: 2rem 0;
            background: linear-gradient(90deg, #FF4B4B 0%, #FF914D 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-weight: 700;
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .number-display {
            font-size: 8rem;
            font-weight: 700;
            text-align: center;
            color: #FF4B4B;
            text-shadow: 0 0 20px rgba(255, 75, 75, 0.3);
            line-height: 1;
        }
        
        .text-display {
            font-size: 1.5rem;
            text-align: center;
            color: #a0a0a0;
            margin-top: 10px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        
        /* Camera Container */
        .camera-frame {
            border-radius: 16px;
            overflow: hidden;
            border: 2px solid rgba(255, 255, 255, 0.1);
            box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        }
        
        /* Button Styling */
        .stButton button {
            width: 100%;
            border-radius: 8px;
            font-weight: 600;
            padding: 0.5rem 1rem;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            transform: translateY(-2px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        }
        </style>
    """, unsafe_allow_html=True)

def render_sidebar(logo_path: str = os.path.join("Img", "Logo UKMIT.png")) -> None:
    with st.sidebar:
        # Logo Section
        if os.path.exists(logo_path):
            # Use columns to center the image perfectly
            _, col2, _ = st.columns([1, 2, 1])
            with col2:
                st.image(logo_path, use_container_width=True)
                
        # Brand Text
        st.markdown("""
            <div class='sidebar-title'>UKM IT</div>
            <div class='sidebar-subtitle'>Cipta Karya Informatika</div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Controls Section
        st.markdown("<h3 style='text-align: center;'>🎮 Panel Kontrol</h3>", unsafe_allow_html=True)
        
        # Status Indicator (Top of controls)
        is_active = st.session_state.get('camera_active', False)
        status_color = "status-active" if is_active else "status-inactive"
        status_text = "Kamera Aktif" if is_active else "Kamera Non-aktif"
        
        st.markdown(f"""
        <div class='status-badge'>
            <span class='status-indicator {status_color}'></span>
            <span style='font-weight: 500;'>{status_text}</span>
        </div>
        <br>
        """, unsafe_allow_html=True)
        
        # Action Buttons
        if st.button("📷 Mulai", type="primary", use_container_width=True):
            st.session_state.camera_active = True
            st.rerun()
            
        if st.button("⏹️ Stop", use_container_width=True):
            st.session_state.camera_active = False
            st.rerun()
            
        # Footer
        st.markdown("---")
        st.markdown(
            "<div style='text-align: center; color: #666; font-size: 0.8rem;'>"
            "© 2025 UKM IT<br>All Rights Reserved"
            "</div>", 
            unsafe_allow_html=True
        )

def render_header() -> None:
    st.markdown("<h2 class='main-header' style='padding-top: 0; margin-top: -40px;'>✋ AI Hand Detector</h2>", unsafe_allow_html=True)

def render_instructions() -> None:
    st.markdown("""
    <div style='text-align: center; padding: 2rem; background: rgba(255,255,255,0.03); border-radius: 20px; margin-top: 0;'>
        <h2>Selamat Datang!</h2>
        <p style='font-size: 1.2rem; color: #aaa; margin-bottom: 2rem;'>
            Program ini menggunakan Artificial Intelligence untuk mendeteksi jumlah jari<br>
            dan akan diucapkan secara otomatis.
        </p>
    </div>
    """, unsafe_allow_html=True)

def render_result_panel(number: Optional[int], text: Optional[str]) -> None:
    if number is not None:
        st.markdown(f"""
        <div class='stCard'>
            <div style='text-align: center; color: #888; margin-bottom: 10px;'>Terdeteksi</div>
            <div class='number-display'>{number}</div>
            <div class='text-display'>"{text}"</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Visual bar indicator
        progress = number / 10.0
        st.progress(progress)
    else:
        st.markdown("""
        <div class='stCard' style='text-align: center; padding: 40px 20px;'>
            <div style='font-size: 3rem; margin-bottom: 1rem; opacity: 0.3;'>✋</div>
            <div style='color: #666;'>Menunggu tangan...</div>
        </div>
        """, unsafe_allow_html=True)
