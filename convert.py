from moviepy.editor import *
import os

# Specify the path to the videos and audio folders
videos_folder = "custom"
audio_folder = "audio"

# Create the audio folder if it doesn't exist
if not os.path.exists(audio_folder):
    os.makedirs(audio_folder)

# Check if the videos folder exists
if os.path.exists(videos_folder) and os.path.isdir(videos_folder):
    # Get a list of all video files in the videos folder
    video_files = os.listdir(videos_folder)

    # Iterate over each video file
    for video_file in video_files:
        # Get the full path of the video file
        video_path = os.path.join(videos_folder, video_file)

        # Load the video file
        video = VideoFileClip(video_path)

        # Extract audio from video
        audio = video.audio

        # Set the output audio file path
        audio_file = os.path.splitext(video_file)[0] + ".mp3"
        audio_path = os.path.join(audio_folder, audio_file)

        # Write the audio file
        audio.write_audiofile(audio_path)

        # Close the video file
        video.close()

    print("Audio extraction completed.")
else:
    print("Videos folder not found.")
