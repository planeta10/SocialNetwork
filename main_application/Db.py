from json import *
from os import remove
global PATH
PATH = r"C:\Users\Vladimir\PycharmProjects\SocialNet\main_data\Posts.json"
def save_post(title,text):

        with open(PATH,'r+') as file:
            read = file.read()
            data = loads(read)
            data[title] = {"Post_text":text}
        remove(PATH)
        with open(PATH,"w+") as file:
            dump(data,file)
        return True

def read_posts():
    with open(PATH,'r+') as file:
        read = file.read()
        data = loads(read)
    return data
if __name__=="__main__":
    data = save_post("TEXT","3343E")
    print(read_posts())