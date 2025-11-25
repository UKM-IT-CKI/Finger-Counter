# Hand Gesture & Audio Recognizer

Aplikasi pengenalan gestur tangan real-time yang dibangun menggunakan Streamlit dan Computer Vision. Proyek ini mendeteksi gestur tangan melalui webcam, menghitung jumlah jari yang diangkat, dan memberikan respons audio secara langsung.

Dikembangkan untuk kegiatan **UKM IT** guna mendemonstrasikan kemampuan AI dan Computer Vision.

## ✨ Fitur Utama

- **Pelacakan Tangan Real-time**: Mendeteksi tangan dan titik-titik jari dengan akurasi tinggi menggunakan MediaPipe.
- **Penghitung Jari**: Menghitung jumlah jari yang diangkat secara otomatis.
- **Umpan Balik Audio**: Menyebutkan jumlah jari yang terdeteksi menggunakan Text-to-Speech (TTS).
- **Antarmuka Web Interaktif**: Dibangun dengan Streamlit untuk tampilan yang bersih dan responsif.
- **Integrasi WebRTC**: Streaming video latensi rendah untuk performa yang lancar.

## 🛠️ Teknologi yang Digunakan

- **Python 3.x**
- **Streamlit**: Framework Frontend.
- **OpenCV & MediaPipe**: Pemrosesan citra dan deteksi tangan.
- **Streamlit-WebRTC**: Streaming video dan audio real-time.
- **gTTS (Google Text-to-Speech)**: Pembuatan audio.

## 🚀 Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/UKM-IT-CKI/Finger-Counter.git
   cd Finger-Counter
   ```

2. **Buat Virtual Environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 💻 Cara Penggunaan

Jalankan aplikasi Streamlit:

```bash
streamlit run app.py
```

Izinkan browser untuk mengakses kamera Anda saat diminta. Tunjukkan tangan Anda ke kamera untuk mulai berinteraksi!

## 📂 Struktur Proyek

```
├── modules/
│   ├── audio.py       # Logika audio dan TTS
│   ├── detector.py    # Logika deteksi tangan menggunakan MediaPipe
│   └── ui.py          # Komponen UI dan tata letak
├── audio_cache/       # File audio yang disimpan (cache)
├── app.py             # Titik masuk utama aplikasi
├── requirements.txt   # Daftar dependensi Python
└── README.md          # Dokumentasi proyek
```

---
Dibuat dengan ❤️ oleh Tim UKM IT.
