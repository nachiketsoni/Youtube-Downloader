from pytube import YouTube

def YoutubeDownloader(link ,Type):
        print("Please Wait...")
        youtube_Output = YouTube(link)
        if Type == "1":
            result = youtube_Output.streams.filter(progressive = True)
        elif Type == "2":
            result = youtube_Output.streams.filter(only_audio=True)
        else:
            print("Error Wrong Input!!")
        resul = list(enumerate(result))
        for i in resul:
            print(f"Index : {i[0]} | {i[1]}")
        strm = int(input ("Select The Index Of The Quality  :  "))
        print("Please Wait...")
        result[strm].download()
        print("successfully downloaded")


    
link=input("Enter The Youtube Link: ")
Type = input("Press 1. Dowload as Video \nPress 2. Download as Audio \n")
YoutubeDownloader(link,Type)