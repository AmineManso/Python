from  math import sqrt
from tkinter import *
from time import sleep

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
list = []
cluster_1 = []
cluster_2 = []
temoin = 1
c1 = P(w/4, h/2, 0, 0)
c2 = P(w/4*3, h/2, 0, 0)
c01 = c02 = 0

def show_point(p, col):
    global radius, w, h, idx
    cercle = my_canvas.create_oval(p.x1 - radius, p.x2 - radius, p.x1 + radius, p.x2 + radius, fill=col)
    # print(p)

def show_all_points():
    my_canvas.delete('all')
    for p in list:
        if p in cluster_1:
            show_point(p, 'red')
        else:
            show_point(p, "blue")
    cercle1 = my_canvas.create_rectangle(c1.x1 - radius, c1.x2 - radius, c1.x1 + radius, c1.x2 + radius, fill='green', outline='cyan', width=3)
    cercle2 = my_canvas.create_rectangle(c2.x1 - radius, c2.x2 - radius, c2.x1 + radius, c2.x2 + radius, fill='yellow', outline='magenta', width=3)





def display_coordinates(event):
    global idx, list

    my_label['text'] = f'x={event.x}  y={event.y}'
    ### create ponts:
    if event.num == 1:
        w_class = 1
        col = 'gray' #'red'
        point = P(event.x, event.y, 0, idx)
        list.append(point)
        idx += 1
        show_point(point, col)
        show_point(c1, 'green');     show_point(c2, 'yellow')
    if event.num == 3:
        run()

###############################################
def dist(P, sample):
   return sqrt( (P.x1 - sample.x1)*(P.x1 - sample.x1) + (P.x2 - sample.x2)*(P.x2 - sample.x2) )


def distances():
    global list
    cls_1 = []
    cls_2 = []

    for p in list:
        d1 = dist(p, c1)
        d2 = dist(p, c2)
        if d1 < d2:
            p.w = 1
            p.d = d1
            cls_1.append(p)
        else:
            p.w = 2
            p.d = d2
            cls_2.append(p)
    print( 'cls_1 & cls_2 : ', len(cls_1), len(cls_2))
    return cls_1, cls_2

def centroides():
    global c1, c2, c01, c02
    global cluster_2, cluster_1
    c1_avg = [0, 0]
    c2_avg = [0, 0]
    number_point = 0

    for p in cluster_1:
        c1_avg[0] += p.x1
        c1_avg[1] += p.x2
        number_point += 1

    print('numeber points', number_point)

    c1_avg[0] = c1_avg[0] / number_point
    c1_avg[1] = c1_avg[1] / number_point

    number_point = 0
    for p in cluster_2:
        c2_avg[0] += p.x1
        c2_avg[1] += p.x2
        number_point += 1

    c2_avg[0] = c2_avg[0] / number_point
    c2_avg[1] = c2_avg[1] / number_point

    return c1_avg, c2_avg




############################### run
def run():
    global cluster_2, cluster_1
    iteration = 1
    while(True): # temoin
        K = 2  # number of classes , we can use the elbow methode
        cluster_1, cluster_2 = distances();
        print( 'number in clusters : ', len(cluster_1), len(cluster_2))

        c1_avg, c2_avg = centroides()

        if [c1.x1, c1.x2] == c1_avg and [c2.x1, c2.x2] == c2_avg:
            print('work done !!!\nnumber of iteration of the program: ', iteration)
            break   # temoin = 0
        else:
            c1.x1, c1.x2 = c1_avg[0], c1_avg[1]
            c2.x1, c2.x2 = c2_avg[0], c2_avg[1]

        iteration += 1
        show_all_points()


###############################################  GUI
my_windows = Tk()
my_canvas = Canvas(my_windows, width=w, height=h, background='white')
#############################label, mouse:
my_label = Label(bd=4, relief="solid", font="Times 22 bold", bg="black", fg="white")
my_canvas.bind("<Button-1>", display_coordinates)
my_canvas.bind("<Button-3>", display_coordinates)
my_canvas.bind("<Button-2>", display_coordinates)
my_windows.geometry('500x500')
# ############################# grids
my_canvas.grid(row=0, column=0)
my_label.grid(row=1, column=0)
# my_canvas.pack()
my_windows.mainloop()


#############################################
# import cv2
#
# im = cv2.imread('road.PNG')
# im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
# im_blur = cv2.GaussianBlur(im_gray, (7, 7), 0)
# im_canny = cv2.Canny(im_blur, 50, 50)
# cv2.imshow('canny detection', im_canny)
#
# cv2.waitKey(0)