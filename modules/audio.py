from gtts import gTTS
import os
import base64
import tempfile
from typing import Optional, Dict

class AudioManager:
    def __init__(self):
        self.angka_teks: Dict[int, str] = {
            0: "nol", 1: "satu", 2: "dua", 3: "tiga", 4: "empat",
            5: "lima", 6: "enam", 7: "tujuh", 8: "delapan", 9: "sembilan", 10: "sepuluh"
        }
        
        # Setup cache directory using system temp folder
        # This is safer for cloud environments (Hugging Face, etc) where write permissions 
        # to the app directory might be restricted
        self.cache_dir = os.path.join(tempfile.gettempdir(), "finger_counter_audio_cache")
        if not os.path.exists(self.cache_dir):
            try:
                os.makedirs(self.cache_dir)
            except OSError:
                # Fallback if creation fails, though tempdir usually works
                pass

    def get_text_for_number(self, number: int) -> Optional[str]:
        return self.angka_teks.get(number)

    def get_audio_html(self, text: str) -> str:
        """Generate HTML audio tag with base64 encoded audio"""
        try:
            filename = f"{text}.mp3"
            file_path = os.path.join(self.cache_dir, filename)

            # Generate audio if it doesn't exist
            if not os.path.exists(file_path):
                tts = gTTS(text=text, lang='id')
                tts.save(file_path)

            # Read file and encode to base64
            with open(file_path, "rb") as f:
                audio_bytes = f.read()
            
            audio_base64 = base64.b64encode(audio_bytes).decode()
            
            # HTML for autoplaying audio
            return f'<audio autoplay="true" src="data:audio/mp3;base64,{audio_base64}">'
        except Exception as e:
            print(f"Audio Error: {e}")
            return ""
