import tkinter as tk
from tkinter import font
from tkinter import messagebox
from PIL import Image, ImageTk
from string import ascii_uppercase
import json
from spanzuratoarea import Spanzuratorea
from time import sleep
from random import randint

class SpanzuratoareaGUI:
    def __init__(self):
        self.sp = Spanzuratorea()
        self.count = 0
        self.tries = 1
        self.game_active = True
        filename = 'words.json'
        with open(filename) as f:
            self.words = json.load(f)
        print(self.words)
        self.get_word()


    def _check_letter(self,letter):
        if self.game_active:
            if letter in self.sp.aux_word:
                self.sp.fit_letter(letter)
            elif self.tries <= 5:
                self.tries += 1
                #hang_label['text'] = self.tries
                _create_part()
            print(self.tries)
            print(self.sp.word_displayed)
            label['text'] = self.sp.word_displayed
            self._check_win_lose()
            print(self.sp.word_displayed)
            print(self.sp.word)

    def _check_win_lose(self):
        if self.sp.word_displayed == list(self.sp.word.upper()):
            print(f"'{self.sp.word}' was the word.")
            label['text'] = spg.sp.word_displayed
            tk.messagebox.showinfo(title="Nice",message="You guessed the word")
            hang_label.config(image='')
            print(self.sp.word_displayed)
            self.get_word()
        if self.tries >= 5:
            tk.messagebox.showinfo(title="Game Over",message=f"'{self.sp.word}' was the word.")
            self.game_active = False

    def get_word(self):
        index = randint(self.count,3)
        self.sp.word = self.words[index]
        self.words.remove(self.words[index])
        #[randint(self.count,3)]
        self.sp.word_displayed = list(len(self.sp.word) * '_')
        self.sp.aux_word = list(self.sp.word.upper())
        self.sp._convert_spaces()
        if self.count:
            sleep(0.5)
            label['text'] = self.sp.word_displayed
            self.tries = 0
        self.count += 1


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

def _create_letter(letter_name,x,y):
    filename = f"images/Litere/{letter_name}.gif"
    loadimage = Image.open(filename)
    render = ImageTk.PhotoImage(loadimage)
    rounded_button = tk.Button(image=render,command= lambda letter = letter_name: spg._check_letter(letter))
    rounded_button.image = render
    rounded_button["bg"] = "white"
    rounded_button["border"] = "0"
    rounded_button.place(relwidth=0.065,relheight=0.11,relx=x,rely=y)
    letters[letter_name] = render

def _create_part():
    filename = f"images/parti/{spg.tries}.png"
    loadimage = Image.open(filename)
    render = ImageTk.PhotoImage(loadimage)
    hang_label.configure(image=render)
    hang_label.image = render


def win_message():
    top = tk.Toplevel()
    top.title('Nice')
    tk.Message(top, text="You guessed the word", padx=20, pady=20).pack()
    top.after(2000, top.destroy)

Height = 1200
Width = 1600
letters = {}
spg = SpanzuratoareaGUI()

root = tk.Tk()

font = font.Font(size=70)

canvas = tk.Canvas(root,height=Height,width=Width,bg="white")
canvas.pack()

frame = tk.Frame(root,bg="white")
frame.place(relx=0.5,rely=0.65,relwidth= 0.75,relheight=0.15,anchor='n')


i = 1
for c in ascii_uppercase[:13]:
    letter = _create_letter(c,0.04*i,0.01)
    i+=2
i = 1
for c in ascii_uppercase[12:]:
    letter = _create_letter(c,0.04*i,0.15)
    i+=2
letter = _create_letter("Y",0.4,0.3)
letter = _create_letter("Z",0.5,0.3)

label = tk.Label(frame,text=spg.sp.word_displayed,bg="white",font=font)
label.place(relwidth=1, relheight=1)

hang_label = tk.Label(root,image=None,bg="white")
hang_label.place(relwidth=0.3, relheight=0.3, relx=0.7, rely=0.35)


root.mainloop()