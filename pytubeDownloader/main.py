	
import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
	try:
		ytLink = link.get()
		ytObject = YouTube(ytLink)
		video =ytObject.streams.get_hightest_resolution()
		video.download(filename='C:/Documents') # should add user prompted location then check box to open with vlc
		
	except:
		print("Yt link is invalid")
		finishLabel.configure(text= "Yt link is invalid, Download Error", text_color="red")
		return

	finishLabel.configure(text= "Downloaded")


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Donwloader")

# Adding UI Elememts
title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10 , pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height= 40)
link.pack()	

#Finished Downloading
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack()

#Download Button
download = customtkinter.CTkButton(app, text="Donwload", command=startDownload)
download.pack(padx=10 , pady=10)

# Running the app
app.mainloop()

