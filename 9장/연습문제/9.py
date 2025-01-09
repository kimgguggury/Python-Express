# from tkinter import *

# window = Tk()


# name = Label(window, text="이름", width=10)
# name.grid(row=0,column=0,columnspan=2)

# work = Label(window, text="직업", width=10)
# work.grid(row=1,column=0,columnspan=2)

# contry = Label(window, text="국적", width=10)
# contry.grid(row=2, column=0,columnspan=2)

# nameEntry = Entry(window,width=33)
# nameEntry.grid(row=0,column=2)

# workEntry = Entry(window,width=33)
# workEntry.grid(row=1,column=2)

# contryEntry = Entry(window,width=33)
# contryEntry.grid(row=2,column=2)

# showButton = Button(window,text="show")
# showButton.grid(row=3, column=0)

# quitButton = Button(window,text="quit")
# quitButton.grid(row=3, column=1)
# window.mainloop()

from tkinter import *
fields = '이름', '직업', '국적'
def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text)) 
      
def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field)
      ent = Entry(row)
      row.pack(side=TOP, fill=X)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

root = Tk()
ents = makeform(root, fields)
root.bind('<Return>', (lambda event, e=ents: fetch(e)))   
b1 = Button(root, text='Show',
      command=(lambda e=ents: fetch(e)))
b1.pack(side=LEFT, padx=5, pady=5)
b2 = Button(root, text='Quit', command=root.quit)
b2.pack(side=LEFT, padx=5, pady=5)
root.mainloop()
