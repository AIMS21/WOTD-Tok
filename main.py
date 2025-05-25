# main.py

from gtts import gTTS
from moviepy import *
from dotenv import load_dotenv
import os
import random
import requests

load_dotenv()
pexels_api_key = os.getenv("PEXELS_API_KEY")
merriam_api_key = os.getenv("MERRIAM_API_KEY")

def fetch_random_word():
    random_word_response = requests.get("https://random-word-api.herokuapp.com/word")
    random_word = random_word_response.json()[0]

    # print(random_word)
    return random_word

def fetch_word_data(word):
    try:
        print(merriam_api_key)
        url = f"https://dictionaryapi.com/api/v3/references/learners/json/{word}?key={merriam_api_key}"
        response = requests.get(url)
        data = response.json()
        definitions = []
        # print(data, '\n')
        if isinstance(data, list):
            for ex in data:
                definitions.extend(ex['shortdef'])

            return definitions
    except:
        print("Invalid Word for Dictionary API")
        raise Exception("Word not found in Dictionary.")

def generate_audio(text, filename="output/audio.mp3"):
    tts = gTTS(text)
    tts.save(filename)

def generate_background(duration):
    headers = {"Authorization": pexels_api_key}
    pexels_url = f"https://api.pexels.com/videos/search?query={word}&orientation=portrait&size=large&per_page=10"
    res = requests.get(pexels_url, headers=headers)
    videos = res.json()['videos']
    try:
        video_url = random.choice(videos)['video_files'][0]['link']
    except:
        print("Invalid Word for Video API")
        raise Exception("Video not found for word.")

    # Download the video
    video_path = "assets/temp_background.mp4"
    with open(video_path, "wb") as f:
        f.write(requests.get(video_url).content)

    clip = VideoFileClip(video_path)

    if clip.duration >= duration:
        # Trim the video if it's longer than the desired duration
        final_clip = clip.subclipped(0, duration)
    else:
        # Loop the video until it reaches or exceeds the target duration
        clips = []
        total_duration = 0
        while total_duration < duration:
            clips.append(clip)
            total_duration += clip.duration
        looped = concatenate_videoclips(clips)
        final_clip = looped.subclipped(0, duration)
    return final_clip

def create_video(word, definitions):
    audio = AudioFileClip("output/audio.mp3")
    background = generate_background(audio.duration + 1)

    print(audio.duration, background.duration, background.size)

    # text = f"Word of the Day:\n {word}\n\nDefinition:\n{definitions}\n\n"
    text = f"Word of the Day:\n {word}\n\nDefinition:\n"
    xcount = 0
    for xdef in definitions:
        for xword in xdef.split():
            text += xword + ' '
            xcount += 1
            if xcount == 7:
                text += '\n'
                xcount = 0
            
    txt_clip = TextClip(text= text, color='white', size=background.size, method='caption', stroke_color="black", stroke_width=5, margin=(20, 10, 20, 10), text_align='center')
    txt_clip = txt_clip.with_duration(audio.duration).with_position("center")

    final = CompositeVideoClip([background, txt_clip]).with_audio(audio)
    final.write_videofile("output/video.mp4", codec="libx264", audio_codec="aac")



if __name__ == "__main__":
    
    while True:
        try:
            word = fetch_random_word()
            definitions = fetch_word_data(word)
            print(word, definitions)
            print("done")
            definitions = definitions[0:3]
            narration = f"Word of the day is {word}. It means: {definitions}."
            print(narration)
            generate_audio(narration)
            create_video(word, definitions)
            break
        except:
            continue

    

