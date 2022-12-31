import os

from tkinter import *
from tkinter import filedialog

from gtts import gTTS
from tika import parser

from sys import exit

TITLE_FONT = "Verdana"
TITLE_COLOR = "#aefaff"
WORD_FONT = "Montserrat"
WORD_COLOR = "#eeeeee"
BACKGROUND_COLOR = "#b1aeff"
BUTTON_BG_COLOR = "#d9aeff"

def open_pdf_file():
    pdf_file = filedialog.askopenfilename(
        initialdir="/",
        title="Select a PDF file",
        filetypes=(("pdf files", "*.pdf"), ("all files", "*."))
    )  
    raw = parser.from_file(pdf_file)
    raw_content = raw['content']
    print(raw_content)
    tts = gTTS(text=raw_content, lang = 'en')
    tts.save('pdf_to_audio.mp3')
    play_button.config(fg=TITLE_COLOR)

def play_audio():
    os.startfile('pdf_to_audio.mp3')

root = Tk()
root.title('PDF TO MP3')
root.config(padx=25, pady=25, bg= BACKGROUND_COLOR)

title_label = Label(text='PDF TO MP3', 
font=(TITLE_FONT, 45, "bold"),
fg = TITLE_COLOR,
bg=BACKGROUND_COLOR,)

title_label.grid(column=0, row=0, pady=40)
open_button = Button(text="Select PDF",
 font=(WORD_FONT, 35), 
 width=15, fg=WORD_COLOR,
  bg=BUTTON_BG_COLOR,
  command= open_pdf_file)

play_button = Button(text="Play Audio File",
  font=(WORD_FONT, 35), 
  width=15, fg=WORD_COLOR,
  bg=BUTTON_BG_COLOR,
  command= play_audio)

open_button.grid(column=0, row=1, pady=5)
play_button.grid(column=0, row=2, pady=5)

root.resizable(False,False)

root.mainloop()
