# 📚 WOTD-Tok

WOTD-Tok is a Python-based automation script that generates short, captioned videos for a word of the day. Each video features:
- A randomly chosen English word
- Its definition(s) from the Merriam-Webster Dictionary API
- Text-to-speech narration using gTTS
- A background video from Pexels based on the word
- Perfect for creating engaging vocabulary videos for TikTok, Instagram Reels, YouTube Shorts, or educational content.


https://github.com/user-attachments/assets/62f9749b-d532-4b1e-9a02-ae012b2048cd


  
  
## 🚀 How It Works

1. Random Word Generation
A random English word is selected using the Heroku Random Word API and internal logic.
2. Definition Lookup
The selected word is searched in the Merriam-Webster Dictionary API.
3. Validation & Retry
If the word is not found in the dictionary or lacks suitable video content, a new word is chosen and the process restarts.
4. Text-to-Speech
Using the gTTS (Google Text-to-Speech) library, the word and its definition are narrated and saved as audio.
5. Background Video Fetching
A relevant background video is fetched from the Pexels Video API using the word as a search keyword.
6. Caption Generation
A visual caption is created with the word and definition text overlaid.
7. Video Compilation
All components—background video, narration, and caption—are combined into a single video using moviepy.

## 🧪 Requirements

Python 3.8+
gTTS, requests, moviepy, python-dotenv, etc.
(See requirements.txt)

## 🔧 Setup & Usage

  1. Clone the repo

    `git clone https://github.com/yourusername/wotd-tok.git`

    `cd wotd-tok`

  2. Create and activate a virtual environment

    `python3 -m venv venv`

    `source venv/bin/activate  # For Mac/Linux`

    `# venv\Scripts\activate    # For Windows`

  3. Install dependencies
   
    `pip install -r requirements.txt`

  4. Set up your API keys
   
    `touch .env`

.env File Format

    `PEXELS_API_KEY=your_pexels_api_key`

    `MERRIAM_API_KEY=your_merriam_dictionary_api_key`

Run the Script

    `python main.py`

## 📦 Output

- Final video will be saved in the output/ directory.
- Example filename: output/video.mp4

## ❗ Error Handling

If a word is not:
- Found in the dictionary OR
- Matched with a background video on Pexels
...the script automatically retries with a new word.

## 📌 To-Do / Ideas for Improvement

 - Add CLI progress bar
 - Option to export subtitles
 - Add more dictionaries (Oxford, Wordnik, etc.)
 - Improve word selection (e.g., filter by frequency or part of speech)
 - Upload videos directly to TikTok or YouTube via API
 
## 🧠 Inspiration

Inspired by educational content creators using short-form video to make learning vocabulary fun and accessible.

## 📄 License

MIT License — feel free to fork, remix, or contribute!
