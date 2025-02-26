import tkinter as tk
from ui import *

class StartWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        
        self.geometry("500x500+500+200") # change later
        
    
    def create_widget(self):
        self.button_play = tk.Button(self,text="Play",command=self.open_game)
        
        
    def locate_widget(self):
        self.button_play.place(x=200,y=200) # change later 
        
    def open_game(self):
        all_widgets = self.winfo_children()
        
        for widget in all_widgets:
            widget.destroy()  
            
        GameWindow(master=self).show() 
    
    def show(self):
        self.create_widget()
        self.locate_widget()
        self.mainloop()
        
        
        
if __name__ == "__main__":
    StartWindow().show()