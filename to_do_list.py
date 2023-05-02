import tkinter
from tkinter import *

root=Tk()
root.title("To-Do-List")
root.geometry("400x550+500+100")
root.resizable(False,False)

task_list=[]

def addTask():
    task=task_entry.get()
    task_entry.delete(0,END)
    if task:
        with open ("tasklist.txt","a") as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)

def deleteTask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open ("tasklist.txt","w") as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')
    listbox.delete(ANCHOR)

def openTaskfile():
    try:
        global task_list
        with open ("tasklist.txt",'r') as taskfile:
            tasks=taskfile.readlines()
        for task in tasks:
            if task!='\n':
                task_list.append(task.strip())
                listbox.insert(END,task.strip())
    except:
        file=open('tasklist.txt','w')
        file.close()

    

frame1=Frame(root,bd=1,width=300,height=200,bg='darkblue')
frame1.place(x=5,y=170)

listbox=Listbox(frame1,font=('times 15 bold'),width='36',bg='#27408B',fg='white',cursor='hand2',selectbackground='lightblue')
listbox.pack(side=LEFT,fill=BOTH,padx=2)

scrollbar=Scrollbar(frame1)
scrollbar.pack(side=RIGHT,fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskfile()

#------delete button-------#

del_button=Button(root,text="Delete",font=("times 15 bold"),fg='blue',command=deleteTask)
del_button.place(x=170,y=440)



topframe=Frame(root,bd=3,bg='#27408B',height=80,width=500)
topframe.place(x=0,y=0)

heading=Label(root,text="To Do List",font=('times 30 bold'),fg='white',bg='#27408B')
heading.place(x=110,y=15)

#------text entry-------#
task=StringVar()
task_entry=Entry(root,font=('times 20 bold'),bd=0,bg='lightgray')
task_entry.place(x=5,y=120,width=300)

#------add button-------#
button=Button(root,text='ADD',font=('times 20 bold'),bg='#27408B',width='6',fg='white',bd=0,command=addTask)
button.place(x=310,y=120,width='70',height='32')
root.mainloop()