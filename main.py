import moviepy.editor as mp
import sys
 
def convert(video_file_name, audio_file_name=None):
    if audio_file_name is None:
        audio_file_name = video_file_name + '.mp3'
    try:
        clip = mp.VideoFileClip(video_file_name)
        clip.audio.write_audiofile(audio_file_name)
        print('success')
    except Exception as e:
        print(e)
