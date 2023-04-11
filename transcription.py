import os
import moviepy.editor as mp
import whisper

model = whisper.load_model("base")

folder_path = 'videos/'

for video_file_path in os.listdir(folder_path):
    if video_file_path.endswith('.mp4'):

        # Extract audio from video and save it as a WAV file
        audio_file_path = os.path.splitext(folder_path + video_file_path)[0] + ".wav"
        clip = mp.VideoFileClip(folder_path + video_file_path)
        clip.audio.write_audiofile(audio_file_path)
        os.remove(folder_path + video_file_path)

        result = model.transcribe(audio_file_path)
        final_transcript = result["text"]
        os.remove(audio_file_path)

        print()
        print()
        print(video_file_path)
        print(final_transcript)
        