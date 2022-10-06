import tkinter
import tkinter.messagebox


t=tkinter.Tk()
t.title('profile')
t.geometry('500x500')

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
                
f=tkinter.Button(text='Enter',bg="blue",fg='white',font=('times new roman',11,"bold"),command=n)
f.place(x=100,y=95)

t.mainloop()
