import yt_dlp
import os

URL = input("Enter Youtube Video Link : ")
DEFAULTQUALITY = "bestvideo+bestaudio/best"

HOME_DIR = os.path.expanduser("~")
DEFAULT_PATH = os.path.join(HOME_DIR, "Downloads", "%(title)s.%(ext)s")

def getformatid():
    with yt_dlp.YoutubeDL() as ydl:
        # Extract video info (no download)
        info = ydl.extract_info(URL, download=False)
        
        # Iterate over the available formats
        formats = info['formats']
        for f in formats:
            # Check if 'height' (resolution) is available
            
            if 'height' in f:
                print(f"Format ID: {f['format_id']} - Resolution: {f['height']}p - Codec: {f['ext']}")
            else:
                print(f"Format ID: {f['format_id']} - Audio only - Codec: {f.get('acodec', 'N/A')}")

def download_keep_vid_audio(quality = DEFAULTQUALITY, path = DEFAULT_PATH):
    ydl_opts = {
        'format': quality,
        'outtmpl': path,
        'merge_output_format': 'mp4',
        'keepvideo' : True
    }
    with yt_dlp.YoutubeDL(ydl_opts) as  ydl:
        ydl.download([URL])
    print(f"File saved at: {DEFAULT_PATH}")


def download_vid(quality = DEFAULTQUALITY, path = DEFAULT_PATH):
    ydl_opts = {
        'format': quality,
        'outtmpl': path,
        'merge_output_format': 'mp4',
            }
    with yt_dlp.YoutubeDL(ydl_opts) as  ydl:
        ydl.download([URL])
    print(f"File saved at: {DEFAULT_PATH}")

def change_quality(quality):
    global DEFAULTQUALITY
    if quality!="":
        DEFAULTQUALITY = quality

print("\nSELECT FROM BELOW :- \n1 : Get the format IDs \n2 : DOWNLOAD THE VIDEO\n3 : DOWNLOAD VIDEO+AUDIO, VIDEO, AUDIO\n")
choice = int(input("ENTER YOUR SELECTION : "))

match choice:
    case 1:
        getformatid()
    case 2:
        FormatIDs = input("Enter Quality Format(VidID+AudID) IDs or Click ENTER for the best quality : ")
        change_quality(FormatIDs)
        download_vid()
    case 3:
        FormatIDs = input("Enter Quality Format(VidID+AudID) IDs or Click ENTER for the best quality : ")
        change_quality(FormatIDs)
        download_keep_vid_audio()
    case _:
        print("INVALID SELECTION, TERMINATING...")
