from pytube import YouTube
from sys import argv
import time
import subprocess
import os

warning="\033[93m"
default="\033[0m"

try:
    choice = argv[1]
except:
    exit(f"Please input as following: \n{warning}python3 {argv[0]} (mp3/mp4){default}\n")
# link = "https://www.youtube.com/watch?v=7jna9bvhdRE&list=PLdR7m7PFLzQ7RqOVfxk2Fr2F-a7iWzovn&index=3"

# music_dir = '/home/ccwtadmin/Music/temp'
# video_dir = '/home/ccwtadmin/Videos/temp'
music_dir = '/app/output'
video_dir = '/app/output'

# Function
def download_mp3(link,retry = 0):
    # yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
    yt = YouTube(link)
    while retry < 3:
        try:
            video = yt.streams.get_audio_only()
            break
        except:
            retry += 1
            time.sleep(3)
            print(f"{retry} retry")

    try:
        mp4_filename = video.default_filename
        mp3_filename = os.path.splitext(mp4_filename)[0] + '.mp3'

        print(f"Download \"{mp4_filename}\" into {music_dir}")
        video.download(music_dir)

        print(f"Covert \"{mp4_filename}\" to \"{mp3_filename}\"")
        # ffmpeg man page
        # https://linux.die.net/man/1/ffmpeg

        # -i input file name
        # -y Overwrite output files
        # Generate mp3 and mp4 file
        subprocess.run([
            'ffmpeg',
            '-y',
            '-i', os.path.join(music_dir, mp4_filename),
            os.path.join(music_dir, mp3_filename)
        ])
        #Remove mp4 file
        subprocess.run([
            'rm',
            os.path.join(music_dir, mp4_filename)
        ])
    except:
        raise Exception
        #exit(f"Failed to download MP3")


def download_mp4(link,retry = 0):
    yt = YouTube(link)
    # filter mp4 streams from object
    while retry < 3:
        try:
            video = yt.streams.get_by_resolution(resolution="720p")
            break
        except:
            retry += 1
            time.sleep(3)
            print(f"{retry} retry")

    while retry < 3:
        try:
            mp4_filename = video.default_filename
            print(f"Download \"{mp4_filename}\" into {video_dir}")
            video.download(video_dir)
            break
        except:
            retry += 1
            time.sleep(3)
            print(f"{retry} retry to download {mp4_filename}")
    else:
        exit(f"Failed to download {mp4_filename}")

#Using readlines()
file = open('youtubeLink.txt', 'r')
lines = file.readlines()


if(choice=="mp3"):
    for link in lines:
        download_mp3(link)
elif(choice=="mp4"):
    for link in lines:
        download_mp4(link)
    #download_mp4(lines[0])
else:
    print(f"Please input mp3 or mp4")
