from pytube import YouTube

loop = True
verified = False
valid_link = False

while loop == True:
    while not valid_link:
        link = input("Paste the video link here:  ")
        try:
            yt = YouTube(link)
            valid_link = True
        except:
            print("INVALID LINK. Please Try Again.")
            valid_link = False

    print("Title: ", yt.title)
    print(f"RunTime: ~{round(yt.length / 60)} minutes.")
    verification = input("Correct Video?  Y/N   ")

    if verification == 'Y':
        verified = True
        loop = False
    elif verification == 'N':
        print("Bummer. Let's try again.")
        valid_link = False
    else:
        print("INVALID INPUT: Please Try Again.")
        valid_link = False

print("Your video is now downloading")

video = yt.streams.get_highest_resolution()

# edit for the quotations to contain the file path you would like videos downloaded to
video.download('')

print("DOWNLOAD COMPLETE")




