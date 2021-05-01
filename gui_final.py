from tkinter import *
from tkinter.ttk import *
from graph import *
from PIL import Image, ImageTk


def Pistol():
	def func1():
		func(b1['text'])
	def func2():
		func(b2['text'])
	def func3():
		func(b3['text'])
	def func4():
		func(b4['text'])

	root.destroy()
	t1=Tk()
	t1.geometry("1200x1200")
	ph1=PhotoImage(file = r"H:\Projects\Skins\Images\usp.png")
	a1=ph1.subsample(1,1)
	ph2=PhotoImage(file = r"H:\Projects\Skins\Images\p250.png")
	a2=ph2.subsample(1,1)
	ph3=PhotoImage(file = r"H:\Projects\Skins\Images\glock.png")
	a3=ph3.subsample(1,1)
	ph4=PhotoImage(file = r"H:\Projects\Skins\Images\db.png")
	a4=ph4.subsample(1,1)
	Label(t1,image=a1).place(x=180,y=50)
	Label(t1,image=a2).place(x=650,y=50)
	Label(t1,image=a3).place(x=200,y=400)
	Label(t1,image=a4).place(x=600,y=400)
	b1=Button(t1,text="USP",command=func1)
	b1.place(x=250,y=225)
	b2=Button(t1,text="Five-Seven",command=func2)
	b2.place(x=700,y=225)
	b3=Button(t1,text="Glock",command=func3)
	b3.place(x=250,y=570)
	b4=Button(t1,text="Dual-Berettas",command=func4)
	b4.place(x=700,y=570)
	t1.mainloop()


def Rifle():
	def func1():
		func(b1['text'])
	def func2():
		func(b2['text'])
	def func3():
		func(b3['text'])
	def func4():
		func(b4['text'])
	root.destroy()
	t2=Tk()
	t2.geometry("1200x1200")
	r1=PhotoImage(file = r"H:\Projects\Skins\Images\ak47.png")
	s1=r1.subsample(1,1)
	r2=PhotoImage(file = r"H:\Projects\Skins\Images\awp.png")
	s2=r2.subsample(1,1)
	r3=PhotoImage(file = r"H:\Projects\Skins\Images\m4a1.png")
	s3=r3.subsample(1,1)
	r4=PhotoImage(file = r"H:\Projects\Skins\Images\sg553.png")
	s4=r4.subsample(1,1)
	Label(t2,image=s1).place(x=150,y=50)
	Label(t2,image=s2).place(x=600,y=50)
	Label(t2,image=s3).place(x=150,y=400)
	Label(t2,image=s4).place(x=600,y=400)
	b1=Button(t2,text="AK47",command=func1)
	b1.place(x=250,y=225)
	b2=Button(t2,text="AWP",command=func2)
	b2.place(x=700,y=225)
	b3=Button(t2,text="M4A1",command=func3)
	b3.place(x=250,y=570)
	b4=Button(t2,text="SSG553",command=func4)
	b4.place(x=700,y=570)
	t2.mainloop()


def SMG():
	def func1():
		func(b1['text'])
	def func2():
		func(b2['text'])
	def func3():
		func(b3['text'])
	def func4():
		func(b4['text'])
	root.destroy()
	t3=Tk()
	t3.geometry("1200x1200")
	q1=PhotoImage(file = r"H:\Projects\Skins\Images\ump.png")
	u1=q1.subsample(1,1)
	q2=PhotoImage(file = r"H:\Projects\Skins\Images\p90.png")
	u2=q2.subsample(1,1)
	q3=PhotoImage(file = r"H:\Projects\Skins\Images\pp.png")
	u3=q3.subsample(1,1)
	q4=PhotoImage(file = r"H:\Projects\Skins\Images\mac10.png")
	u4=q4.subsample(1,1)
	Label(t3,image=u1).place(x=180,y=50)
	Label(t3,image=u2).place(x=600,y=30)
	Label(t3,image=u3).place(x=170,y=400)
	Label(t3,image=u4).place(x=650,y=400)
	b1=Button(t3,text="MP9",command=func1)
	b1.place(x=250,y=225)
	b2=Button(t3,text="P90",command=func2)
	b2.place(x=700,y=225)
	b3=Button(t3,text="PP-Bizon",command=func3)
	b3.place(x=250,y=570)
	b4=Button(t3,text="Mac 10",command=func4)
	b4.place(x=700,y=570)
	t3.mainloop()


def Shotgun():
	def func1():
		func(b1['text'])
	def func2():
		func(b2['text'])
	def func3():
		func(b3['text'])
	def func4():
		func(b4['text'])
		
	root.destroy()
	t4=Tk()
	t4.geometry("1200x1200")
	# b1=PhotoImage(file = r"mag7.png")

	b1=PhotoImage(file = r"H:\Projects\Skins\Images\mag7.png")
	c1=b1.subsample(1,1)

	b2=PhotoImage(file = r"H:\Projects\Skins\Images\nova.png")
	c2=b2.subsample(1,1)

	b3=PhotoImage(file = r"H:\Projects\Skins\Images\sawed.png")
	c3=b3.subsample(1,1)

	b4=PhotoImage(file = r"H:\Projects\Skins\Images\xm.png")
	c4=b4.subsample(1,1)

	Label(t4,image=c1).place(x=170,y=50)
	Label(t4,image=c2).place(x=600,y=50)
	Label(t4,image=c3).place(x=170,y=400)
	Label(t4,image=c4).place(x=600,y=375)

	b1=Button(t4,text="Mag 7",command=func1)
	b1.place(x=250,y=225)
	b2=Button(t4,text="Nova",command=func2)
	b2.place(x=700,y=225)
	b3=Button(t4,text="Sawed-off",command=func3)
	b3.place(x=250,y=570)
	b4=Button(t4,text="XM1014",command=func4)
	b4.place(x=700,y=570)

	t4.mainloop()

root=Tk()
root.geometry("1200x1200")

photo1=PhotoImage(file = r"H:\Projects\Skins\Images\pist.png")
p1=photo1.subsample(2,2)

photo2=PhotoImage(file = r"H:\Projects\Skins\Images\rif.png")
p2=photo2.subsample(2,2)

photo3=PhotoImage(file = r"H:\Projects\Skins\Images\smg.png")
p3=photo3.subsample(3,3)

photo4=PhotoImage(file = r"H:\Projects\Skins\Images\shot.png")
p4=photo4.subsample(3,2)

Label(root,image=p1).place(x=150,y=50)
Label(root,image=p2).place(x=600,y=50)
Label(root,image=p3).place(x=150,y=350)
Label(root,image=p4).place(x=600,y=350)

Button(root,text="Pistol",command=Pistol).place(x=250,y=225)
Button(root,text="Rifle",command=Rifle).place(x=700,y=225)
Button(root,text="SMG",command=SMG).place(x=275,y=570)
Button(root,text="Shotgun",command=Shotgun).place(x=700,y=580)

root.mainloop()


