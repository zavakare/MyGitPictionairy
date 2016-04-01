#!/usr/bin/env python

import socket
from Tkinter import *
        
def main(word):
	root = Tk()
	root.minsize(800, 400)
	prompt = Label(root, text="Draw this word:", font=("Helvetica", 50))
	prompt.pack()
        title = Label(root,text=word,font=("Helvetica", 76),fg="Black" )
        title.pack()
	root.after(10000, lambda: root.destroy())
	root.mainloop()


if __name__ == "__main__":
	main()
