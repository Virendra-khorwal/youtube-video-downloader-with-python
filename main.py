import tkinter
import customtkinter
from pytube import YouTube

# Download Function
def start_download():
    
    try:
        url = url_var.get()
        yt = YouTube(url, on_progress_callback=on_progress)
        video = yt.streams.get_highest_resolution()
        title.configure(text=yt.title, text_color="green")
        title.update()
        finished.configure(text="")
        video.download()
        finished.configure(text="Download Completed!")

    except:
        finished.configure(text="Download Failed", text_color="red")

# Progress Function
def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    progress = bytes_downloaded / total_size * 100
    per = str(int(progress))
    percentage.configure(text=per + "%")
    percentage.update()
    progress_bar.set(float(progress)/100)
    progress_bar.update() 



# System Settings
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

# App Frame
app = customtkinter.CTk()
app.geometry("720x480")
app.title("YouTube Video Downloader")

# Adding UI Elements
title = customtkinter.CTkLabel(app, text="Insert a youtube video", font=("Lato", 20))
title.pack(padx=10, pady=10)

# Link Input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Finished Downloading Label
finished = customtkinter.CTkLabel(app, text="")
finished.pack()

# Progress percentage
percentage = customtkinter.CTkLabel(app, text="0%")
percentage.pack()

progress_bar = customtkinter.CTkProgressBar(app, width=350, height=10)
progress_bar.set(0)
progress_bar.pack(padx=10, pady=10)

# Download Button
download = customtkinter.CTkButton(app, text="Download", width=350, height=40, command=start_download)
download.pack(pady=10)


# Run App
app.mainloop()