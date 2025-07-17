# 🎵 MXL to MP3 Converter

Convert sheet music (`.mxl` MusicXML files) into playable `.mp3` audio with just a few clicks!  
This desktop app uses a simple Tkinter GUI and MuseScore’s powerful command-line tools to bring your sheet music to life.

---

## 📌 Features

- 🎼 Upload `.mxl` (compressed MusicXML) files
- 🎧 Convert them to `.mp3` format using MuseScore
- 🖥️ Easy-to-use desktop GUI built with Tkinter
- 🪶 Lightweight, beginner-friendly code structure

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/mxl-to-mp3-converter.git
cd mxl-to-mp3-converter
```
### 2. Install requirements
```bash
pip install -r requirements.txt
```
### 3. Install MuseScore
Download MuseScore from https://musescore.org

Add MuseScore to your system PATH
(e.g. mscore, mscore3, or mscore4, depending on version)

You can check if MuseScore is accessible using:

```bash
mscore -h
```
### 🧑‍💻 Usage
```bash
python main.py
```
Click "Browse" to select a .mxl (MusicXML) file

Click "Convert" to generate an .mp3 using MuseScore

The .mp3 will be saved in the same directory as the .mxl

📂 Project Structure
```bash
mxl-to-mp3-converter/
├── main.py                  # GUI logic (Tkinter)
├── converter.py             # MuseScore command integration
├── utils.py                 # Helper functions
├── requirements.txt         # Python dependencies
├── demo/
│   ├── sample.mxl
│   └── output.mp3
└── screenshots/
    ├── ui.png
    └── result.png
```
### 📸 Screenshots
<img width="1142" height="725" alt="Screenshot 2025-07-17 at 5 13 04 PM" src="https://github.com/user-attachments/assets/178b7141-d8a4-42a2-b707-f40874e25732" />
<img width="1208" height="710" alt="Screenshot 2025-07-17 at 5 13 35 PM" src="https://github.com/user-attachments/assets/35a5b5bf-043b-44fb-9a55-986f7c120496" />


### 🎧 Demo Output
Try converting the sample .mxl in the demo/ folder.
The .mp3 will appear as output.mp3 in the same folder.

###  What is .mxl?
.mxl is a compressed MusicXML format for digital sheet music.
This app lets users convert .mxl into listenable .mp3, perfect for those who don't read sheet music but want to hear the melody.

### License
This project is licensed under the MIT License.

### Credits
Made by Anoushka Gupta,
Built using Python, Tkinter, and MuseScore
