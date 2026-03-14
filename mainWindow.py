from customtkinter import*
import threading
import base64
import io
import os
from PIL import socket,AF_INET,SOCK_STREAM

class MainWindow(CTk):
    def __init__(self,sock, username):
        super().__init__()

        self.sock = self.sock
        self.username = self.username
        self.geometry('400x600')
        self.title("Chat Client")


        # Меню
        self.label = None
        self.menu_frame = CTkFrame(self, width=30, height=300)
        self.menu_frame.pack_propagate(False)
        self.menu_frame.place(x=0, y=0)
        self.is_show_menu = False
        self.speed_animate_menu = -20
        self.btn = CTkButton(self, text='▶️', width=30)
        self.btn.place(x=0, y=0)




        # Основне поле чату
        self.chat_field = CTkScrollableFrame(self)
        self.chat_field.place(x=0, y=0)




        # Поле введення та кнопки
        self.message_entry = CTkEntry(self, placeholder_text='Введіть повідомлення:', height=40)
        self.message_entry.place(x=0, y=0)
        self.send_button = CTkButton(self, text='>', width=50, height=40)
        self.send_button.place(x=0, y=0)




        self.open_img_button = CTkButton(self, text='📂', width=50, height=40)
        self.open_img_button.place(x=0, y=0)




        self.adaptive_ui()
       


    def adaptive_ui(self):
        self.menu_frame.configure(height=self.winfo_height())
        self.chat_field.place(x=self.menu_frame.winfo_width())
        self.chat_field.configure(width=self.winfo_width() - self.menu_frame.winfo_width() - 20,
                                    height=self.winfo_height() - 40)
        self.send_button.place(x=self.winfo_width() - 50, y=self.winfo_height() - 40)
        self.message_entry.place(x=self.menu_frame.winfo_width(), y=self.send_button.winfo_y())
        self.message_entry.configure(
            width=self.winfo_width() - self.menu_frame.winfo_width() - 110)
        self.open_img_button.place(x=self.winfo_width()-105, y=self.send_button.winfo_y())




        self.after(50, self.adaptive_ui)

    def toggle_menu(self):
        if self.is_show_menu:
            self.is_show_menu = False
            self.speed_animate_menu *= -1
            self.bth.configure(text = " 💬")
            self.show_menu()
        else:
            self.is_show_menu = True
            #self.
        
    def show_menu(self):
        #self.menu_frame.configure(with = 

    def send_massage(self):
        massage = self.massage_entry.get()
        data = f"TEXT@{self.username}@{massage}\n"
        try:
            self.sock.sendall(date.encode())
            except:
            pass
    self.massage_entry.delete(0, END)

    def recv_massage(self):
        buffer = ""
        while = True
            try:
            chunk = self.sock.recv(4096)
            if not chunk:
            break 
        buffer += chunk.decode(errors = 'ignore')

        while "\n" in buffer.splet('\n,1')
        self.handle_line(line.strip())
        except:
        break
    self.sock.close()
        
    def handle_line(self,line):
        if not line:
            return
        parts = line.split("@", 3)
        msg_type = parts[0]
        if msg_type == "TEXT":
            if len(parts) == 3:
                author = parts = [1]
                massage = parts = [2]
                self.add_massage(f"{author}:{massage}")
        elif msg_type == "IMAGE":
            if len(parts) >= 4:
                author = parts[1]
                filename =  parts[2] 
                b64_img = parts[3]
                try:
                    img_data = base64.b64code(b64_img)
                    pil_img = Image.open(io.bytesIO(img_data))
                    ctk_img = CTkImage(pil_img, size=(300,300))
                    self.add_massage(f"{author}надіслав(ла) зображення: {filename}",img=ctk_img)
                except Exception as e:
                    self.add_massage(f"помилка відображення зображення: {e}")
            else:
                self.add_massage(line)
            def open_image(self):
                file_name = filedialog.askopenFilename()
                if not file_name:
                    return
                try:
                    with open(file_name, "rb") as f:
                        b64_data = base64.b64encode(raw).decode()
                        short_name = os.path.basename(file_name)
                        data = f"IMAGE@{self.user_name}@{short_name}@{2+2}"
                except:
                    pass


 
main = MainWindow()
main.mainloop()

