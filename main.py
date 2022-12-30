from pytube import YouTube

#Video details function
def detail_and_thumb():
    url1 = str(input("[*] Enter Video Link: "))
    data1 = YouTube(url1)
    print("Video Title is: ",data1.title)
    print("Video Thumbnail is: ",data1.thumbnail_url)
#detail_and_thumb()

#Video Download function
def video_down():
    url2 = str(input("[*] Enter Video Link: "))
    data2 = YouTube(url2)
    video = data2.streams.all()
    vid = list(enumerate(video))
   #for i in vid:
       #print(i)
    print()
    print(" Video Resolution : [1] 360p  [2] 480p ")
    res = int(input("[*] Choose Video Resolution: "))
    if res == 1:
        video[1].download()
    elif res == 2:
        video[11].download()
    else:
        print("You entered invalid number......")
    print()
    print("Working on it......")
    print("Start Download your video.....")
    print("Done")
    print()
#video_down()

#Videoa audio function
def audio():
    url3 = str(input("[*] Enter Video Link: "))
    data3 = YouTube(url3)
    video2 = data3.streams.filter(only_audio=True)
    vid2 = list(enumerate(video2))
    for j in vid2:
        print(j)
    print()
    ask2 = int(input("[*] Enter your choise: "))
    print("Working on it......")
    print("Start Download your Audio.....")
    video2[ask2].download()
    print("Done")
#audio()



ch = 0
#Graphical user interface
def main():
    print("")
    print('\033[0m'"██╗   ██╗ █████╗░██╗   ██╗'\033[1;31m'████████╗██╗   ██╗██████╗ ███████╗'\033[1;34m'      '\033[1;32m'██████╗  █████╗  ██╗       ██╗███╗  ██╗")
    print('\033[0m'"╚██╗ ██╔╝██╔══██╗██║   ██║'\033[1;31m'╚══██╔══╝██║   ██║██╔══██╗██╔════╝'\033[1;34m'      '\033[1;32m'██╔══██╗██╔══██╗ ██║  ██╗  ██║████╗ ██║")
    print('\033[0m'" ╚████╔╝ ██║  ██║██║   ██║'\033[1;31m'   ██║   ██║   ██║██████╦╝█████╗  '\033[1;34m'█████╗'\033[1;32m'██║  ██║██║  ██║ ╚██╗████╗██╔╝██╔██╗██║")
    print('\033[0m'"  ╚██╔╝  ██║  ██║██║   ██║'\033[1;31m'   ██║   ██║   ██║██╔══██╗██╔══╝  '\033[1;34m'╚════╝'\033[1;32m'██║  ██║██║  ██║  ████╔═████║ ██║╚████║")
    print('\033[0m'"   ██║   ╚█████╔╝╚██████╔╝'\033[1;31m'   ██║   ╚██████╔╝██████╦╝███████╗'\033[1;34m'      '\033[1;32m'██████╔╝╚█████╔╝  ╚██╔╝ ╚██╔╝ ██║ ╚███║")
    print('\033[0m'"   ╚═╝    ╚════╝  ╚═════╝ '\033[1;31m'   ╚═╝    ╚═════╝ ╚═════╝ ╚══════╝ '\033[1;34m'     '\033[1;32m'╚═════╝  ╚════╝    ╚═╝   ╚═╝  ╚═╝  ╚══╝")
    print("______________________________________________________________________________ᴄᴏᴅᴇᴅ ʙʏ Kᴀᴠɪɴᴅᴜ Sᴀɴᴅᴀʀᴜᴡᴀɴ")
    print("")
    print("        [1] Download video          [2] Video Thumbnail")
    print("        [3] Video Audio             [4] Follow on Github")
    print("        [5] Exit")
    print("")
    ch = int(input("[*] Enter Your Choise: "))

    if ch == 1:
        video_down()
    elif ch == 2:
        detail_and_thumb()
    elif ch == 3:
        audio()
    elif ch == 4:
        print("Follow me on Github: https://github.com/ImKavinduSandaruwan")
    elif ch == 5:
        print("Thank you for using")
    else:
        print("Invalid number:")
main()

