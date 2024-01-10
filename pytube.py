#!/usr/bin/env python3

from pytube import YouTube

def download_video(video_url, save_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(video_url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Print video details
        print(f"Downloading: {yt.title}")
        print(f"Resolution: {video_stream.resolution}")
        print(f"File Size: {round(video_stream.filesize / (1024 * 1024), 2)} MB")

        # Download the video
        video_stream.download(output_path=save_path)

        print("Download complete!")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Replace the URL below with the YouTube video URL you want to download
    video_url = input("Enter the url\n ")

    # Replace the save_path with the directory where you want to save the downloaded video
    save_path = "/home/student/mycode/"

    download_video(video_url, save_path)

