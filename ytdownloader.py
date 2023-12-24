from pytube import YouTube
art = '''
 __     _________   _____   ______          ___   _ _      ____          _____  ______ _____  
 \ \   / /__   __| |  __ \ / __ \ \        / / \ | | |    / __ \   /\   |  __ \|  ____|  __ \ 
  \ \_/ /   | |    | |  | | |  | \ \  /\  / /|  \| | |   | |  | | /  \  | |  | | |__  | |__) |
   \   /    | |    | |  | | |  | |\ \/  \/ / | . ` | |   | |  | |/ /\ \ | |  | |  __| |  _  / 
    | |     | |    | |__| | |__| | \  /\  /  | |\  | |___| |__| / ____ \| |__| | |____| | \ \ 
    |_|     |_|    |_____/ \____/   \/  \/   |_| \_|______\____/_/    \_\_____/|______|_|  \_\
                                                                                          DEVGOLDEN1
                                                                                              
                                                                                              
'''
print(art)

def Download(link):
    youtubeOb= YouTube(link)
    youtubeOb = youtubeOb.streams.get_highest_resulation()
    try:
            youtubeOb.download()
    except:
        print("An error has occurred!! Try again.")
    print("Download is completed!")


link = input("Youtube video link: ")
Download(link)