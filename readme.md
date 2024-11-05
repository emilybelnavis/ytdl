# ytdl

a script that makes the yt-dlp process less painful

## disclaimer

What this tool is intended for:
- A way for you to download the music you listen to on Youtube Music so you can take it on the go on your iPod or something.

What this tool is not intended for:
- Piracy. (for all you mad dog lawyers out there)

### Requirements
- A valid Youtube music/premium subscription
- Python 3.13 (or higher)

## Configuration

### YT-DLP Specific 
YT-DLP specific configs can be set in the `ytdl-config` file **except for the file output*. 
See [YT-DLP Documentation](YT-DLP_Documentation) for more details on how to write your configs

### File location
Set the root folder destination in `ytdl.py` under the variable `storage_location`.

### Music link csv file
set up a csv/excel/google sheet (idgaf as long as the output will be a csv file). use this structure:

| album | artist | ytlink | downloaded |
| ----- | ------ | ------ | ---------- |
| album name goes here | artist name goes here  | link goes here | yes/no |

using this structure lets you reuse the csv file in future batches. it's written like this because:
1. i'm lazy

You don't actually need to use the whole link. Just the part

- for a single song only the string after `watch?v=` is needed. if the full link is 
`https://music.youtube.com/watch?v=lYBUbBu4W08`, you only need `lYBUbBu4W08`.

- for an album, only the string after `playlist?list=` is needed. if the full link is`https://music.youtube.com/playlist?list=OLAK5uy_nmDUsWOMoEcz0SsVqUwir0oxu-k1oUyXE`, you only need `OLAK5uy_nmDUsWOMoEcz0SsVqUwir0oxu-k1oUyXE`.

## FAQ
Q: "Why didn't you do [anything else] instead of [what i did]" <br />
A: I am lazy



[YT-DLP_Documentation]: https://github.com/yt-dlp/yt-dlp?tab=readme-ov-file#configuration

