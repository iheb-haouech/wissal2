import tkinter as tk
import math
my_w = tk.Tk()
width,height=610,410
d=str(width)+"x"+str(height+40)
my_w.geometry(d)
c1=tk.Canvas(my_w,width=width-10,height=height-50,bg='#FFFFFF')
c1.grid(row=0,column=0)
arc_w=80
x1,y1,x2,y2=40,40,560,560
x,y,r=300,295,220
c1.create_arc(x1,y1,x2,y2,start=0,extent=45,outline='green',
            width=arc_w,style=tk.ARC)
c1.create_arc(x1,y1,x2,y2,start=45,extent=45,outline='blue',
            width=arc_w,style=tk.ARC)
c1.create_arc(x1,y1,x2,y2,start=90,extent=30,outline='yellow',
            width=arc_w,style=tk.ARC)
c1.create_arc(x1,y1,x2,y2,start=120,extent=60,outline='red',
            width=arc_w,style=tk.ARC)
c1.create_oval(x-10,y-10,x+10,y+10,fill='blue')
in_radian=math.radians(0)
pointer=c1.create_line(x,y,(x+r*math.cos(in_radian)),
                       (y-r*math.sin(in_radian)),width=6,arrow='last')
def my_upd(*args):
    global pointer
    in_radian=math.radians(my_scale.get())
    c1.delete(pointer)
    pointer=c1.create_line(x,y,(x+r*math.cos(in_radian)),
                       (y-r*math.sin(in_radian)),width=6,arrow='last')
my_scale=tk.Scale(my_w,from_=0,to=180 , orient='horizontal',
                length=300, command=my_upd)
my_scale.grid(row=1,column=0)

my_w.mainloop()