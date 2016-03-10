#!/usr/bin/env python 
# http://stackoverflow.com/questions/10596988/making-a-countdown-timer-with-python-and-tkinter

import Tkinter as tk
import ChooseCat
#import NewMotion
#import threading
#from threading import Thread
#from multiprocessing import Pool
#p = Pool(2)
#p.map(__init__, range(app.mainloop, NewMotion.drawFunction)) 
class ExampleApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
	self.minsize(1780, 1080)
        self.label = tk.Label(self, text="", font=("Helvetica", 76))
        self.label.pack()
        self.remaining = 0
        self.countdown(45)
	
    def countdown(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="time's up!")
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdown)

if __name__ == "__main__":
	app = ExampleApp()
	#Thread(target = NewMotion.drawFunction).start()
	#Thread(target = app.mainloop).start()
	#NewMotion.drawFunction()
	#p.map(__init__, range(app.mainloop, NewMotion.drawFunction))

	app.mainloop()
