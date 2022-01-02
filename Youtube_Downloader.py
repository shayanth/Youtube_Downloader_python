import requests
import youtube_dl


API_KEY = 'Put your API code in here'

def playlist_downloader():
    PlayList_id = input("Enter the playlist id: ")
    res = requests.get(f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&maxResults=50&playlistId={PlayList_id}&key={API_KEY}').json()
    v_ids =[]
    for item in range(len(res['items'])):
        v_ids.append(res['items'][item]['snippet']['resourceId']['videoId'])

    NP_Token = res["nextPageToken"]
    res = requests.get(f'https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet&pageToken={NP_Token}&maxResults=50&playlistId={PlayList_id}&key={API_KEY}').json()
    
    for item in range(len(res['items'])):
        v_ids.append(res['items'][item]['snippet']['resourceId']['videoId'])

    video = []
    for vid in range(len(v_ids)):
        video.append(f"https://www.youtube.com/watch?v={v_ids[vid]}")

    try:
        youtube_dl.YoutubeDL({}).download(video)
    except Exception as e:
        print("error: ",e)

def Single_video_downloader():
    video = []
    video.append(input("enter the link of video:"))
    print(video)
    try:
        youtube_dl.YoutubeDL({}).download(video)
    except Exception as e:
        print("error: ",e)

if __name__ == "__main__":

    print("#########################")
    print("1.Playlist Downloader.")
    print("2.Single video Downloader.")
    print("#########################")
    choice = int(input("choose proper option: "))
    if(choice == 1):
        playlist_downloader()
    elif(choice == 2):
        Single_video_downloader()


