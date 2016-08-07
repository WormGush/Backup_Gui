import sys, shutil, os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread
from datetime import *
import time



def create_threads(destination,source,mode,name):
    t = Thread(target=timing_routine, kwargs={"d":destination, "s": source, "mode": mode, "name": name})
    t.start()

def timing_routine(d,s,mode,n):  #should be executed on its own thread
    #MODES:
    #1 = 2 minutes
    #2 = 5 minutes
    #3 = 10 minutes
    if mode == 1:
        copying = True
        mhello(d,s,n)
        copying = False
        time.sleep(120) #2 mins
    elif mode == 2:
        copying = True
        mhello(d,s,n)
        copying = False
        time.sleep(300) #5 mins
    elif mode == 3:
        copying = True
        mhello(d,s,n)
        copying = False
        time.sleep(600) #10 mins
    e = True
    while e:
        copying = True
        mhello(d,s,n)
        copying = False
        time.sleep(mode * 60)
        



def mhello(dst, src, name):
    #src = msrc.get()
    if e == None:
        name = mdst.get()
    #print(name)

    if len(dst) <= 0 or len(name) <=0:
        messagebox.showwarning("YO YOU MADE A MISTAKE $$$", "Your destination folder has to have a name!")
    elif os.path.exists(dst + "\\" + name):
        e = True
        i = 1
        while e:
            if os.path.exists(dst+ "\\" +name+"(" + str(i) +")"):
                i = i + 1
            else:
                e = False
        if messagebox.askokcancel("Ya dingus!", "That folder already exists! \nRename to " + name + "("+ str(i) +")?"):
            name = name + str(i)
            print(name)
            e == None
    else:
        #print("Copying from: "+ src + " To: "+ dst+ "\\" + name)
        dst = dst + "\\" + name
        try:
            shutil.copytree(src, dst)
            messagebox.showwarning("Alert", "Your backup has completed")
        except:
            messagebox.showwarning("Lazy error message", """Your folder name was invalid idk why lol,
try avoiding \"/ \ * ? < > | \" ya dingus """)

def browse(srcordst):
    global dest, source
    #print(srcordst)
    if srcordst == 2:    #2 = User Selected Destination
        greet = "Select The Folder You Are Backing Up To"
    elif srcordst == 1:  #1 = user selected source
        greet = "Select The Folder You Are Backing Up From"
    mGui.withdraw()
    tempdir = filedialog.askdirectory(parent = mGui, title= greet, initialdir = os.getcwd())
    mGui.deiconify()
    if srcordst == 2:    #2 = User Selected Destination
        dest = tempdir
        dstPrev = dest
        if len(dest) > 25:
            length = len(dest)
            dstPrev = dest[:3] + "..." + dest[length - 17:]
            #print(dstPrev)
        #lbldstPreview = Label(text=str(dstPrev)).place(x=110,y= (ypos + 50))
        lbldstPreview.config(text = str(dstPrev))
        #print(tempdir)
    elif srcordst == 1:  #1 = user selected source
        source = tempdir
        srcPrev = source
        if len(source) > 25:
            length = len(source)
            srcPrev = source[:3] + "..." + source[length - 17:]
            #print(srcPrev)
        #lblsrcPreview = Label(text=str(srcPrev)).place(x=110,y= (ypos + 20))
        lblsrcPreview.config(text = str(srcPrev))
        #print(tempdir)

def close():
    #height = mGui.winfo_height()
    #print(height)
    quit()
    sys.exit

mGui = Tk()
path, dest, source = "","",""
#srcordst = 0
ypos = 50

mdst = StringVar()


mGui.geometry("250x350+10+10")
mGui.resizable(width=False, height = False)
mGui.title("Backup Program 0.1")


mlabel3 = Label(text="Back up every...").place(x = 15, y = (ypos + 120))
lblsrcPreview = Label(text="")
lblsrcPreview.place(x=110,y= (ypos + 20))
lbldstPreview = Label(text="")
lbldstPreview.place(x=110,y= (ypos + 50))

mlabel4 = Label(text="Destination Folder Name:").place(x=15,y= (ypos + 80))
mentdst = Entry(mGui,textvariable = mdst,width = 30).place(x=15, y= (ypos + 100))

mlabel = Label(text="Josh's Backup Program",fg = "Black").grid(row=0,column=0,sticky=W) #W meaning west (left)

#~~~~~SORT OUT COMMANDS FOR TIME INTERVALS~~~~~~~#
mbuttstrt = Button(mGui,text="Start",command= lambda: mhello(dest, source)).place(x= 15, y=(ypos + 170))
mbutt2min = Button(mGui,text="2min",command= lambda: create_threads(dest, source, 1)).place(x= 15, y=(ypos + 140))
mbutt5min = Button(mGui,text="5min",command= lambda: create_threads(dest, source, 2)).place(x= 55, y=(ypos + 140))
mbutt10min = Button(mGui,text="10min",command= lambda: create_threads(dest, source, 3)).place(x= 95, y=(ypos + 140))
#~~~~~~#                                  #~~~~~~~#

mbuttBrowse = Button(mGui,text="Back Up From...",command= lambda: browse(1)).place(x= 15, y=(ypos + 20))
mbuttBrowse2 = Button(mGui,text="Back Up To...",command= lambda: browse(2)).place(x= 15, y= (ypos + 50))

mbutclose = Button(mGui,text="Close",font = ("","9","bold"), fg = "Black",command=close).place(x= (250/2-30), y=ypos+200)

mGui.iconbitmap('rainbowfrog.ico')

mGui.mainloop()
