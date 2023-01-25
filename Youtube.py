from pytube import YouTube

def YoutubeDownloader(link ,check):
    def Download(require):
        print("Please Wait...")
        youtube_Output = YouTube(link)
        if require == 1:
            result = youtube_Output.streams.filter(progressive = True)
        elif require == 2:
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

    if check =="1":
        Download(1)
    elif check =="2":
        Download(2)
    
link=input("Enter The Youtube Link: ")
check = input("Press 1. Dowload as Video \nPress 2. Download as Audio \n")
YoutubeDownloader(link,check)