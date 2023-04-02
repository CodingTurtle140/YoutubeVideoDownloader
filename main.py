import pytube


choice = input("Would you like to download a \n Playlist \n Or a \n Video? ")


if choice == 'video':
    import pytube
    import time
    import os

    url = input("Enter the YouTube video URL: ")

    video = pytube.YouTube(url)

    folder_name = video.title.replace("/", "_")
    os.makedirs(folder_name, exist_ok=True)

    print(f"Downloading {video.title}...")
    video_stream = video.streams.get_highest_resolution()

    start_time = time.time()
    video_stream.download(output_path=folder_name, filename=f"{video.title}.mp4")
    end_time = time.time()

    download_time = round(end_time - start_time)

    with open(f"{folder_name}/{video.title}.txt", "w") as f:
        f.write(f"Video Title: {video.title}\n")
        f.write(f"Video Length: {video.length} seconds\n")
        f.write(f"Download Time: {download_time} seconds\n")

    print(f"Video and information file have been downloaded to folder '{folder_name}'.")






  
elif choice == 'playlist':
    import pytube
    import os
    import time

    playlist_url = input("Enter the YouTube playlist URL: ")
    playlist = pytube.Playlist(playlist_url)
    folder_name = playlist.title
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    with open(f"{folder_name}.txt", "w") as f:
        for video in playlist.videos:
            try:
                start = time.time()
                print(f"Downloading {video.title}...")
                video.streams.get_highest_resolution().download(output_path=folder_name)
                end = time.time()
                f.write(f"{video.title}: {end-start} seconds\n")
                f.write(f"Video Length: {video.length} seconds\n")
                time.sleep(10)  # Wait for 10 seconds before downloading the next video
            except:
                print(f"Failed to download {video.title}.")
                f.write(f"{video.title}: rejected\n")
        print("All videos have been downloaded.")



            



else:	
  print("Nah, XD")
