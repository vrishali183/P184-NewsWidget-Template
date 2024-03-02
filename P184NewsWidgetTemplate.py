from tkinter import *
import requests
import json
root=Tk()
root.geometry("500x650")
root.configure(background="Light Blue")

t=Label(root,text="BBC News Update",font=("arial",20,"bold"))
t.place(relx=0.5,rely=0.1,anchor=CENTER)
h1=Label(root)
h1.place(relx=0.1,rely=0.175,anchor=W)
d1=Label(root)
d1.place(relx=0.1,rely=0.25,anchor=W)
h2=Label(root)
h2.place(relx=0.1,rely=0.3,anchor=W)
d2=Label(root)
d2.place(relx=0.1,rely=0.375,anchor=W)
h3=Label(root)
h3.place(relx=0.1,rely=0.45,anchor=W)
d3=Label(root)
d3.place(relx=0.1,rely=0.525,anchor=W)
h4=Label(root)
h4.place(relx=0.1,rely=0.6,anchor=W)
d4=Label(root)
d4.place(relx=0.1,rely=0.675,anchor=W)
h5=Label(root)
h5.place(relx=0.1,rely=0.85,anchor=W)
d5=Label(root)
d5.place(relx=0.1,rely=0.925,anchor=W)

def getit():  
    api_request=requests.get(" " + "d49274990f6b415a980e15a5e4f5630a")
    api_output_json = json.loads(api_request.content)
    gh1=api_output_json['articles'][ ]['title']
    h1["text"]=gh1
    gd1=api_output_json['articles'][ ]['description']
    d1["text"]=gd1
    gh2=api_output_json['articles'][ ]['title']
    h2["text"]=gh2
    gd2=api_output_json['articles'][ ]['description']
    d2["text"]=gd2
    gh3=api_output_json['articles'][ ]['title']
    h3["text"]=gh3
    gd3=api_output_json['articles'][ ]['description']
    d3["text"]=gd3
    gh4=api_output_json['articles'][ ]['title']
    h4["text"]=gh4
    gd4=api_output_json['articles'][ ]['description']
    d4["text"]=gd4
    gh5=api_output_json['articles'][ ]['title']
    h5["text"]=gh5
    gd5=api_output_json['articles'][ ]['description']
    d5["text"]=gd5
getit()

root.mainloop()
