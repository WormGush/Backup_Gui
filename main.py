# ~~~~~Plans~~~~~~#
# event handling for cancel on name change
# change font size of title (label 1)
# add simple mode where user selects drive by a button
# 
#  http://effbot.org/tkinterbook/checkbutton.htm
#  http://www.tutorialspoint.com/python/os_open.htm
# http://stackoverflow.com/questions/2553886/how-can-i-bundle-other-files-when-using-cx-freeze?rq=1
# make into exe


import sys, shutil, os
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from threading import Thread
#from datetime import *
import time


mycomp_path="Z:\\"
#mycomp_path="::{323CA680-C24D-4099-B94D-446DD2D7249E}"


def create_threads(destination, source, mode):
    print("got here")
    t = Thread(target=timing_routine, kwargs={"d": destination, "s": source, "mode": mode})
    t.start()




def mhello(dst, src):

    name = mdst.get()
    for i in range(len(illegalchars)):
        name = name.replace(illegalchars[i],"_")
    print(name)
    if len(dst) <= 0 or len(name) <=0:
        messagebox.showwarning("YO YOU MADE A MISTAKE $$$", "Your destination folder has to have a path and name!")
    
    elif os.path.exists(dst + "\\" + name):
        e = True
        i = 1
        while e:
            if os.path.exists(dst+ "\\" +name+ str(i)):
                i = i + 1
            else:
                e = False
        if messagebox.askokcancel("Ya dingus!", "That folder already exists! \nRename to " + name + "("+ str(i) +")?"):
            name = name + str(i)
            print(name)
            #e = None
    #else:
        #print("Copying from: "+ src + " To: "+ dst+ "\\" + name)
    dst = dst + "\\" + name
    print(dst)
    try:
        shutil.copytree(src, dst)
        messagebox.showwarning("Alert", "Your backup has completed")
    except:
        messagebox.showwarning("Lazy error message", """Your folder name was invalid idk why lol,
try avoiding \"/ \ * ? : < > | \" ya dingus """)
    return


def timing_routine(d, s, mode):  #should be executed on its own thread
    #MODES:
    #1 = 2 minutes
    #2 = 5 minutes
    #3 = 10 minutes
    if mode == "0":
        copying = True
        mhello(d, s)
        copying = False        
    elif mode == "1":
        print("delay 1")
        copying = True
        mhello(d, s)
        copying = False
        time.sleep(12) #2 mins
    elif mode == "2":
        copying = True
        mhello(d, s)
        copying = False
        time.sleep(30) #5 mins
    elif mode == "3":
        copying = True
        mhello(d, s)
        copying = False
        time.sleep(60) #10 mins
    else:
        print("mode didnt match")
    #e = True
    #while e:
    #    copying = True
    #    mhello(d, s)
    #    copying = False
    #    time.sleep(mode * 60)
    print("routine done" + str(mode))


def start():

    print("v is " +str(v.get()))
    create_threads(dest, source, v.get())


def browse(srcordst):
    global dest, source
    if srcordst == 2:    #2 = User Selected Destination
        greet = "Select The Folder You Are Backing Up To"
    elif srcordst == 1:  #1 = user selected source
        greet = "Select The Folder You Are Backing Up From"
    mGui.withdraw()
    tempdir = filedialog.askdirectory(parent=mGui, title=greet, initialdir=mycomp_path)
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



def close():
    quit()

mGui = Tk()
path, dest, source = "", "", ""

ypos = 50

illegalchars = ["/", "\\", "*", "?", "<", ">", '"', "|", ":"]

mdst = StringVar()

mGui.geometry("250x350+10+10")
mGui.resizable(width=False, height=False)
mGui.title("Backup Program 0.3")


mlabel3 = Label(text="Back up every...").place(x = 15, y = (ypos + 120))
lblsrcPreview = Label(text="")
lblsrcPreview.place(x=110, y=(ypos + 20))
lbldstPreview = Label(text="")
lbldstPreview.place(x=110, y=(ypos + 50))

mlabel4 = Label(text="Destination Folder Name:").place(x=15,y= (ypos + 80))
mentdst = Entry(mGui, textvariable = mdst, width = 30).place(x=15, y= (ypos + 100))

mlabel = Label(text="Josh's Backup Program", fg = "Black").grid(row=0, column=0, sticky=W) #W meaning west (left)

# ~~~~~SORT OUT COMMANDS FOR TIME INTERVALS~~~~~~~#
mbuttstrt = Button(mGui,text="Start",command= start).place(x= 15, y=(ypos + 170))

MODES = [
    ("No Loop", "0", 0),
    ("2min", "1", 60),
    ("5min", "2", 100),
    ("10min", "3", 140),
]

v = StringVar()
# v.set("0")  # initialize

for text, mode, xmult in MODES:

    b = Radiobutton(mGui, text=text,
                    variable=v, value=mode, indicatoron=0)
    b.place(x=15 + xmult, y=(ypos + 140))

# ~~~~~~#                                  #~~~~~~~#
# test = Button(mGui, text = "test", command = lambda: timing_routine(dest, source, v.get())).place(x = 15, y=(ypos+ 190))
mbuttBrowse = Button(mGui, text="Back Up From...",command= lambda: browse(1)).place(x= 15, y=(ypos + 20))
mbuttBrowse2 = Button(mGui, text="Back Up To...",command= lambda: browse(2)).place(x= 15, y= (ypos + 50))
mbutclose = Button(mGui, text="Close", font=("", "9", "bold"), fg="Black", command=close).place(x=(250/2-30), y=ypos+200)

mGui.iconbitmap('rainbowfrog.ico')
mGui.mainloop()
