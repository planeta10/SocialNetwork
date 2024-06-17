from customtkinter import *
import Db
from tkinter import messagebox
#Profile
#Ponfiguration
#Post: Title, Description, (image)

class MainApplication():
    def __init__(self):
        #Variables
        self.Posts_list_data = []

        self.User_settings = {}


        #Creating the main lnterface

        self.main_window = CTk()
        #Creating frames to will have connect with interface
        self.Main_frame = CTkFrame(self.main_window)
        self.Profile_frame = CTkFrame(self.main_window)
        self.Post_frame = CTkFrame(self.Main_frame)
        self.Create_post_frame = CTkFrame(self.main_window)

        #Creating main buttons in main frame
        self.Add_post_button = CTkButton(self.Main_frame,command=self.Create_post,text="Create new post")
        self.User_profile = CTkButton(self.Main_frame,command=self.OpenUser_profile)

        #Creating widgets to create a post
        self.post_title_var = StringVar()
        self.post_title = CTkEntry(self.Create_post_frame,placeholder_text="Post title",textvariable=self.post_title_var)
        self.post_text = CTkTextbox(self.Create_post_frame)
        self.post_save = CTkButton(self.Create_post_frame,text="Post",command=self.Save_post)
        #Pack wigets in frames
        self.Add_post_button.pack(expand=True)
        self.Pack_widgets(self.post_title,self.post_text,self.post_save)
        #Pack_frames
        self.Main_frame.pack(expand=True)
        self.Post_frame.pack(expand=True)
        #Show all posts
        self.Post_show()
        self.main_window.mainloop()
    def Post_show(self):
        self.Posts_list_data = Db.read_posts()
        self.Post_list =[]
        for i,title in enumerate(self.Posts_list_data):
            frame = CTkFrame(self.Post_frame,border_width=0.5, border_color="gray50",bg_color="white")
            Title = title
            Text = self.Posts_list_data[Title]["Post_text"]
            label_Title= CTkLabel(frame,text=Title,text_color="red")
            label_text=CTkLabel(frame,text=Text,text_color="green")
            self.Pack_widgets(label_Title,label_text)
            self.Post_list.append(frame)
        for i in self.Post_list:
            i.pack(expand=True)

    def Pack_widgets(self,*args):
        for i in args:
            i.pack(expand=True)
    def Create_post(self):
        self.Main_frame.forget()
        self.Create_post_frame.pack(expand=True)
    def OpenUser_profile(self):
        self.Main_frame.forget()
        self.Profile_frame.pack(expand=True)
    def CloseUser_profile(self):
        ...
    def Save_post(self):
        title=self.post_title_var.get()
        text = self.post_text.get('1.0', END)
        self.post_title.delete(0,END)
        self.post_text.delete('1.0',END)
        if not Db.save_post(title=title,text=text): messagebox.showerror("","It was uncreatiable mistake")
        self.CloseCreate_post()

    def CloseCreate_post(self):
        self.Create_post_frame.forget()
        self.Main_frame.pack(expand=True)
        #Delete all posts to update tape
        for i in self.Post_list:
            i.destroy()
        del self.Post_list
        self.Post_show()

if __name__ == "__main__":
    app = MainApplication()

