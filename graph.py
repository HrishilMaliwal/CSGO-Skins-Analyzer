from tkinter import *


def func(fn):
    import csv
    from matplotlib import pylab as plt
    import matplotlib
    import numpy as np

    y1, y2, y3, y4 = 10, 10, 10, 10
    l1 = []
    l2 = []
    l3 = []
    l4 = []
    filename = "H:\Projects\Skins\Data\\" + fn + ".csv"
    filename = filename.replace(" ", "")

    with open(filename, 'r') as csvfile:
        rea = csv.reader(csvfile)

        for row in rea:
            l1.append(row[0])
            l2.append(row[1])
            l3.append(row[2])
            l4.append(row[3])

    t = Toplevel()
    t.geometry("1200x1200")
    for i in l1:
        Label(t, text=i).place(x=100, y=y1)
        y1 += 20
    for i in l2:
        Label(t, text=i).place(x=250, y=y2)
        y2 += 20
    for i in l3:
        Label(t, text=i).place(x=350, y=y3)
        y3 += 20
    for i in l4:
        Label(t, text=i).place(x=450, y=y4)
        y4 += 20


    fields=[]
    rows=[]
    xlabels=[]
    li=[]
    ylabels=[]

    d={'Industrial':'#5e98d9','Mil-Spec':'#4b69ff','Restricted':'#8847ff','Classified':'#d32ee6','Covert':'#eb4b4b','Consumer':'#b0c3d9'}

    with open(filename,'r') as f:
        csvreader =csv.reader(f)
        fields=next(csvreader)
        for row in csvreader:
            rows.append(row)
    for row in rows:
        li.append(row[1])
        xlabels.append(row[0])
        ylabels.append(row[2])
    npa = np.arange(len(xlabels))
    ylabels = list(map(int, ylabels))

    a=[]
    b=[]
    try:
        co=li.index("Covert")
    except:
        pass
    else:
        a.append(co)
        b.append("Covert")

    try:
        cl=li.index("Classified")
    except:
        pass
    else:
        a.append(cl)
        b.append("Classified")

    try:
        re=li.index("Restricted")
    except:
        pass
    else:
        a.append(re)
        b.append("Restricted")

    try:
        ind=li.index("Industrial")
    except:
        pass
    else:
        a.append(ind)
        b.append("Industrial")

    try:
        con=li.index("Consumer")
    except:
        pass
    else:
        a.append(con)
        b.append("Consumer")

    for i in range(0,len(a)-1):
        plt.tick_params(axis='x', labelsize=3)
        plt.bar(npa[a[i]:a[i+1]], ylabels[a[i]:a[i+1]], width=0.75, color=d[b[i]], align='center')
        plt.xticks(npa,xlabels)
    plt.tick_params(axis='x', labelsize=3)
    plt.bar(npa[a[-1]:],ylabels[a[-1]:],width=0.75,color=d[b[-1]],align='center')
    plt.show()

