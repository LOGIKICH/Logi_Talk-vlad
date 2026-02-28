from typing import Tuple
from customtkinter import*

class Mainwindow(CTk):
    def() __init__()
    super(). __init__() 
    self.geometry("700x500")
    self.title("Logtalk")

    #-----------------ВІДЖЕТИ----------------
    self.menu_bth = CTkButton(self,width=200,text="menu",corner_radius=0)
    self.menu_bth.place(x=0, y=0)

    self.menu_frame = CTkFrame(self,width=200,height=500,corner_radius=0)
    self.menu_frame.place(x=0, y=0)

    self.send_frame = CTkFrame(self)
    self.chat_frame.place(x=0, y=0)

    self.send_frame = CTkScrollableFrame(self)
    self.send_frame.place(x=0, y=0)
    #---------------АДАПТИВНІСТЬ---------------
    self.adaptive_ui()

def adaptive_ui(self):
    self.menu_frame.place(x= 0 , y = self.menu_bth.winfo