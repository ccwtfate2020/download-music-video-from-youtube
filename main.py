from pytube import YouTube
from sys import argv
import time
import subprocess
import os

warning="\033[93m"
error="\033[31m"
msg="\033[34m"
default="\033[0m"

music_dir = '~/Downloads'
video_dir = music_dir
output_dir = '/app/output'
youtube_link_filename="youtubeLink.txt"

try:
    choice = argv[1]
except:
    exit(f"Please input as following: \n{warning}python3 {argv[0]} (mp3/mp4){default}\n")

# Function
def download_mp3(mp4_filename):
    try:
        mp3_filename = os.path.splitext(mp4_filename)[0] + '.mp3'
        print(f"{msg}Covert \"{mp4_filename}\" to \"{mp3_filename}\" ...{default}")
        # ffmpeg man page
        # https://linux.die.net/man/1/ffmpeg

        # -i input file name
        # -y Overwrite output files
        # Generate mp3 and mp4 file
        subprocess.run([
            'ffmpeg',
            '-y',
            '-i', os.path.join(output_dir, mp4_filename),
            os.path.join(output_dir, mp3_filename)
        ])
        #Remove mp4 file
        subprocess.run([
            'rm',
            os.path.join(output_dir, mp4_filename)
        ])
    except:
        raise Exception
        #exit(f"Failed to download MP3")


def download_mp4(link,retry = 0):
    
    # filter mp4 streams from object
    while retry < 3:
        try:
            # yt = YouTube(link, use_oauth=True, allow_oauth_cache=True)
            yt = YouTube(link)
            video = yt.streams.get_by_resolution(resolution="720p")
            mp4_filename = video.default_filename
            print(f"{msg}Download \"{mp4_filename}\" ...{default}")
            video.download(output_dir)
            return mp4_filename
        except:
            retry += 1
            time.sleep(3)
            print(f"{warning}{retry} retry to download mp4 from {link} {default}")
    else:
        exit(f"{error}Failed to download mp4 from {link} {default}")

#Using readlines()
file = open(youtube_link_filename, 'r')
lines = file.readlines()

if not lines:
    exit(f"{error}\"{youtube_link_filename}\" is empty. Please input youtube link in \"{youtube_link_filename}\"{default}")

if(choice=="mp3"):
    for link in lines:
        mp4_filename = download_mp4(link)
        download_mp3(mp4_filename)
    print(f"{msg}Please check directory \"{music_dir}\"{default}")
elif(choice=="mp4"):
    for link in lines:
        download_mp4(link)
    print(f"{msg}Please check directory \"{video_dir}\"{default}")
else:
    exit(f"Please input as following: \n{warning}python3 {argv[0]} (mp3/mp4){default}\n")
