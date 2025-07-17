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
├── mxl-to-mp3-converter.py                
├── config.json          
├── README.md             
├── LICENSE               
├── .gitignore            
├── screenshots/          
│   └── ui.png
```
### 📸 Screenshots

![Screenshot 1](demo/upload%20file.png)  
![Screenshot 2](demo/mp3%20produced.png)


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
