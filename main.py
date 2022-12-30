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
    for i in vid:
        print(i)
    ask = int(input("[*] Enter your choice: "))
    print("Working on it......")
    print("Start Download your video.....")
    video[ask].download()
    print("Done")
#video_down()

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
        print("I'm still working on it")
    elif ch == 4:
        print("Follow me on Github: https://github.com/ImKavinduSandaruwan")
    elif ch == 5:
        print("Thank you for using")
    else:
        print("Invalid number:")
main()
