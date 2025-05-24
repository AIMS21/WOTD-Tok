# main.py
import requests
from gtts import gTTS
from moviepy import *


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

def create_video(word, definition, example):
    audio = AudioFileClip("output/audio.mp3")
    background = VideoFileClip("assets/background.mp4").subclipped(0, audio.duration)
    

    # audio_duration = audio.duration
    # print(f"Audio duration: {audio_duration}")

    text = f"Word: {word}\n\nDefinition:\n{definition}\n\nExample:\n{example}"
    txt_clip = TextClip(text= text, font_size=40, color='white', size=background.size, method='caption')
    txt_clip = txt_clip.with_duration(audio.duration).with_position("center")

    final = CompositeVideoClip([background, txt_clip]).with_audio(audio)
    final.write_videofile("output/video.mp4", fps=24, codec="libx264", audio_codec="aac")


if __name__ == "__main__":
    word, definition, example = fetch_word_data()
    print(word, definition, example)

    narration = f"Word of the day is {word}. It means: {definition}. Example: {example}"
    generate_audio(narration)
    create_video(word, definition, example)

