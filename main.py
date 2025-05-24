# main.py

from gtts import gTTS
from moviepy import *
import random
import requests

PEXELS_API_KEY = "iUcGhDwSYhLEgvb6LpN4HJ3D3PCVCnj1VXD9iLllWGPU3ugnbOvM3r9s"


def fetch_word_data(word="hello"):
    url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
    response = requests.get(url)
    data = response.json()
    # print(data, '\n')
    if isinstance(data, list):
    #     for x in data:
    #         for key1 in x: 
                
    #             dict1 = x[key1]
    #             if isinstance(dict1, str):
    #                 print(key1, ":", x[key1])
    #             else: 
    #                 print(key1, ":")
    #             if isinstance(dict1, list):   
    #                 for index, y in enumerate(dict1): 
    #                     if isinstance(y, dict): 
    #                         for key2 in y:
    #                             print('\t', index, key2, ":", y[key2], '\n')
    #                     elif isinstance(y, list):    
    #                         for z in y:
    #                             print('HEEEEEEERE', z) 
    #             elif isinstance(dict1, dict):
    #                 for key3 in dict1:
    #                     print('\t', key3, ":", dict1[key3])
    #             print()
        meaning = data[0]['meanings'][0]['definitions'][0]['definition']
        example = data[0]['meanings'][0]['definitions'][0].get('example', '')
        return word, meaning, example
    else:
        raise Exception("Word not found.")

def generate_audio(text, filename="output/audio.mp3"):
    tts = gTTS(text)
    tts.save(filename)

def generate_background(duration):
    headers = {"Authorization": PEXELS_API_KEY}
    #Grabs videos related to the word
    # "https://api.pexels.com/videos/search?query=nature&per_page=10"
    pexels_url = "https://api.pexels.com/videos/search?query=" + word + "&orientation=portrait&size=large&per_page=10"
    res = requests.get(pexels_url, headers=headers)
    videos = res.json()['videos']
    video_url = random.choice(videos)['video_files'][0]['link']

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

def create_video(word, definition, example):
    audio = AudioFileClip("output/audio.mp3")
    background = generate_background(audio.duration + 1)

    print(audio.duration, background.duration)

    text = f"Word: {word}\n\nDefinition:\n{definition}\n\nExample:\n{example}"
    txt_clip = TextClip(text= text, font_size=40, color='white',size=background.size, method='caption', stroke_color="black", stroke_width=10)
    txt_clip = txt_clip.with_duration(audio.duration).with_position("center")

    final = CompositeVideoClip([background, txt_clip]).with_audio(audio)
    final.write_videofile("output/video.mp4", codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    word, definition, example = fetch_word_data()
    print(word, definition, example)

    narration = f"Word of the day is {word}. It means: {definition}. Example: {example}"
    generate_audio(narration)
    create_video(word, definition, example)

