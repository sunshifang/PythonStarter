import tkinter


'''
top=tkinter.Tk()
top.mainloop()
'''

root=tkinter.Tk()
li=['c','python','php','html','sql','java']
movie=['css','jQuery','Bootstrap']
listb=ListBox(root)
listb2=Listbox(root)

for item in li:
    listb.insert(0,item)

for item in movie:
    listb2.insert(0,item)

listb.pack()
listb2.mainloop()
