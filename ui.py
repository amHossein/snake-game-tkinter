import tkinter as tk

class GameWindow(tk.Tk):
    def __init__(self,master):
        tk.Tk.__init__(self)  
        self.master = master
        self.walls = []
        
    def create_map(self):
        map_size = 26
        for house in range(map_size):
            # left-side
            tk.Label(self.master,bg="black",width=3).grid(column=0,row=house)

            # right-side
            tk.Label(self.master,bg="black",width=3).grid(column=map_size-1,row=house)

            # top-side
            tk.Label(self.master,bg="black",width=3).grid(column=house,row=0)

            # top-side
            tk.Label(self.master,bg="black",width=3).grid(column=house,row=map_size-1)

            
            
            
        
        
    def show(self):
        self.create_map()