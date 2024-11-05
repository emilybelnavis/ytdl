import os
import subprocess
import pandas as pd

csv_file_path = './musicdb.csv'
ytdlp_config = './ytdl-config'
storage_location = '/Volumes/SSD-0024/MusicDownloads/'

def main():
    columns = ['album', 'artist', 'ytlink', 'downloaded']
    df = pd.read_csv(csv_file_path, usecols=columns)
    
    dl_list = df[df['downloaded'] == 'no']
    for index, entry in dl_list.iterrows():
        album = entry['album']
        artist = entry['artist']
        yt_link = entry['ytlink']
        
        album_directory = f"{artist}/{album}"

        full_path = os.path.join(storage_location, album_directory)
        if not os.path.exists(full_path):
            print(f"Creating directory at{full_path}")
            os.makedirs(full_path)

        cmd = f'yt-dlp --config {ytdlp_config} -o "{full_path}/%(title)s.%(ext)s" {yt_link}'
        subprocess.call(cmd, shell=True)



if __name__ == "__main__":
    main()