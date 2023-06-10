# Download Music video from Youtube
N/A

## Getting Started

1. Build a docker image<br>
```docker build -t download-yt-container .```

   
2. Download music<br>
```docker compose run download-yt mp3```<br>
   <br>OR<br><br>
   Download video<br>
```docker compose run download-yt mp4```<br>

If you don't want to create a duplicated container, but download a new youtube video
1. Add yt link into youtubeLink.txt
2. ```docker run <container ID>``` (Please notice the container only run one command. Double check the command in your container)


### Dependencies
N/A

## Version History

| Version | Date | Description
| --- | --- | ---
| v1.0.0 | 11 May 2023 | Initial version
| v1.0.1 | 27 May 2023 | 1. Change the output path in docker-compose.yaml and main.py<br>2. Update the download music and download video function in main.py|
| v1.0.2 | 10 Jun 2023 | 1. Add ENTRYPOINT in Dockerfile<br>2. Update docker-compose.yaml|

## Reference
N/A



