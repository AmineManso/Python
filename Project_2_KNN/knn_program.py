from  math import sqrt
from tkinter import *
#################################
class P:
    def __init__(self, x1, x2, w, idx):
        self.x1 = x1
        self.x2 = x2
        self.w = w
        self.idx = idx
        self.d = 0

    def __repr__(self):
        return '(x1:{}, x2:{}, w:{}, idx:{}, d:{})'.format(self.x1, self.x2, self.w, self.idx, self.d)
##########################


w, h, radius = 400, 400, 10  #  to draw the cercles
idx = 0 # used to index the list of points => list
list = []  # list or stack of the points

def show_line(p, sample):
    line = my_canvas.create_line(p.x1, p.x2,sample.x1,  sample.x2,  width=3    )

def show_point(p, col):
    global radius, w, h, idx
    cercle = my_canvas.create_oval(p.x1 - radius, p.x2 - radius, p.x1 + radius, p.x2 + radius, fill=col)
    print(p)

def show_point_sample(p, col, stroke):
    global radius, w, h, idx
    cercle = my_canvas.create_oval(p.x1 - radius, p.x2 - radius, p.x1 + radius, p.x2 + radius, fill=col, outline=stroke)
    print(p)


def predict(s_list, sample):
    k = 3  # 3 neibors are enough
    i, zw1, zw2 = 0, 0, 0  # index and counters zw1,2
    for p in s_list:
        if i < k:
            if p.w == 1:
                zw1 += 1
            else:
                zw2 += 1
            show_line(p, sample )
        else:
            break
        i += 1



    if zw1 > zw2:
        w_class = 1
        col = 'red'
    else:
        w_class = 2
        col = 'green'

    return w_class, col

def dist(P, sample):
   return sqrt( (P.x1 - sample.x1)*(P.x1 - sample.x1) + (P.x2 - sample.x2)*(P.x2 - sample.x2) )







def display_coordinates(event):
    global idx

    my_label['text'] = f'x={event.x}  y={event.y}'
    ### create ponts:
    if event.num == 1:
        w_class = 1
        col = 'red'
    elif event.num == 3:
        w_class = 2
        col = 'green'
    else:  ## new sample
        sample = P(event.x, event.y, 0, idx)
        list_2 = list.copy()
        for p in list_2:
            p.d = dist(p, sample)
        s_list = sorted(list_2, key=lambda e: e.d)
        ####
        w_class, col = predict(s_list, sample)

    if event.num != 2:
        pt = P(event.x, event.y, w_class, idx)
        list.append(pt)
        idx += 1
        show_point(pt, col)
    else:
        pt = P(event.x, event.y, w_class, idx)
        outline = 'yellow'
        show_point_sample(pt, col, outline)

###############################################  GUI

my_windows = Tk()

my_canvas = Canvas(my_windows,  width= w, height= h, bg= 'blue')
#############################label, mouse:
my_label = Label(bd=4, relief="solid", font="Times 22 bold", bg="black", fg="white")
my_canvas.bind("<Button-1>", display_coordinates)
my_canvas.bind("<Button-3>", display_coordinates)
my_canvas.bind("<Button-2>", display_coordinates)
my_windows.geometry('500x500')
############################# shapes
# my_windows.geometry('500x500')
# line = my_canvas.create_line(0, 0, w, h, width = 5)
# cercle = my_canvas.create_oval(w/2 - radius, h/2 - radius, w/2 + radius, h/2 + radius, fill='red')
# my_canvas.pack()
############################# grids
my_canvas.grid(row=0, column=0)
my_label.grid(row=1, column=0)


my_windows.mainloop()




