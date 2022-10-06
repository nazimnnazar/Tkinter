import tkinter
import tkinter.messagebox
from PIL import ImageTk,Image
from subprocess import call

t=tkinter.Tk()
t.title('profile')
t.geometry('500x500')

p=Image.open("C:\\Users\\nazim\\Desktop\\TKINTER s1\\pg.jpg")
p=p.resize((500,500))
p=ImageTk.PhotoImage(p)

pic=tkinter.Label(t,image=p)
pic.place(x=0,y=0)

a=tkinter.Label(text="profile making",bg="indigo",fg="white",font=('times new roman',20,"bold"))
a.place(x=190,y=0)

b=tkinter.Label(text=" Name :",fg="red",font=('time new roman',10,"bold"))
b.place(x=0,y=45)

c=tkinter.Entry(width=30)
c.place(x=100,y=45)

d=tkinter.Label(text="Place Name :",fg="blue",font=('times new roman',10,"bold"))
d.place(x=0,y=70)

e=tkinter.Entry(width=30)
e.place(x=100,y=70)

def n():
    name=c.get()
    place=e.get()
    if(name=="" or place==""):
      tkinter.messagebox.showerror('Alert','you are Hacked')
    else:
        
      import pymysql
      x=pymysql.connect(host='localhost',user='root',password='anjunazim1234#',db='nazim')
      cur=x.cursor()
      cur.execute("insert into profile values('"+name+"','"+place+"')")
      x.commit()
      x.close()
      tkinter.messagebox.showerror('Alert!','you are hacked')
      t.destroy()

      call(['python','next.s'])
      
f=tkinter.Button(text='Enter',bg="blue",fg='white',font=('times new roman',11,"bold"),command=n)
f.place(x=100,y=95)

t.mainloop()
