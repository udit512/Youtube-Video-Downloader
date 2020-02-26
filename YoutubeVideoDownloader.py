from pytube import YouTube
print("Enter the url")
url=input()
yt = YouTube(url)
res=yt.streams.filter(mime_type="video/mp4")
print("THe given url can be downloaded in these resolutions")
print("Itag\tType\tResolution\tFile Size")
print('*'*43)
for item in res:
	if(item.resolution!=None):
		streamk=yt.streams.get_by_itag(item.itag)
		filesize2=streamk.filesize/1000000
		print(f"{item.itag}\t{item.mime_type}\t{item.resolution}\t{filesize2}mb")
print("Enter the particular Itag")
res0=int(input())
streaml=yt.streams.get_by_itag(res0)
filesize=streaml.filesize/0.000001
print(f"Downloading {filesize}")
streaml.download()
	

