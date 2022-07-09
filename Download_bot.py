from pytube import YouTube,Playlist
import requests
# https://file2linktsbot553.herokuapp.com/227557
DownloadPath = "/home/harrypotter/Downloads/Py _Downloads/"
def job():
    ItemsToDownload={
        'video': "https://youtube.com/shorts/qmZIqVYL5F0?feature=share",
        'playlist': "https://youtube.com/playlist?list=PL4cUxeGkcC9jsz4LDYc6kv3ymONOKxwBU",
        'movie': "https://file2linktsbot553.herokuapp.com/227557",
    }

    def download_file(url):
        local_filename = "/home/harrypotter/Downloads/Py _Downloads/"+url.split('/')[-1]
        print(local_filename)
        # NOTE the stream=True parameter
        r = requests.get(url, stream=True)
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
                    #f.flush() commented by recommendation from J.F.Sebastian
        print("completed")
        return local_filename


    def video_download(url,path=DownloadPath):
        yt_video=YouTube(url)
        print(yt_video.title)
        stream=yt_video.streams.get_highest_resolution()
        stream.download(path)
        print("completed!!")


    def playlist_download(url):
        p_list=Playlist(url)
        path = DownloadPath+p_list.title
        print(p_list.title)
        for url in p_list.video_urls:
            print(url)
            video_download(url,path)

    for key in ItemsToDownload.keys():
        print(key)
        if key =="video":
            print(" its a video")
            video_download(ItemsToDownload["video"])
        elif key == "playlist":
            print("its a playlist")
            playlist_download(ItemsToDownload["playlist"])
        elif key =="movie":
            print("its a movie")
            download_file(ItemsToDownload["movie"])


if __name__ =="__main__":
    job()
