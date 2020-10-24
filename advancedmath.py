import math
from graphics import *
import matplotlib.pyplot as pl
import numpy as np
#array
# Calcultes magnitute of vector
def magnitudeVector(vectors):
    total=0
    for v in vectors:
        total+=v*2
    magnitude=total**0.5
    return magnitude

def quadratic(a,b,c):
    try :
        x1=(-b+math.sqrt((b**2-4*a*c)))/(2*a)
        x2=(-b-math.sqrt((b**2-4*a*c)))/(2*a)
        print(x1,x2)
    except Exception as e:
        print(str(e))
        
def trig_derivatives(d):
    trig={"sin(u)":"cos(u)*u'",
          "cos(u)":"-sin(u)*u'",
          "tan(u)":"sec(u)*sec(u)*u'",
          "csc(u)":"-cot(u)*csc(u)*u'",
          "sec(u)":"sec(u)*tan(u)*u'",
          "cot(u)":"-csc(u)*csc(u)*u'"
          }
    print(str(d)+" : "+trig[d])
    
def average_list(d):
    s=sum(d)
    print(s/len(d))

def area_circle(radius):
    print(radius*radius*math.pi)
    
def area_triangle(base,height):
    print((base*height)/2)
    
def area_rectangle(a,b):
    print(2*a*b)
    
def area_poly(length,sides):
    print(length*sides)
    
def vol_sphere(r):
    print(4*r**3*pi/3)
    
def vol_cube(length):
    print(length**3)
    
def vol_cylinder(radius,height):
    print(pi*radius*radius*height)

def vol_pyramid(base,height):
    print(base*height/3)

def vol_cone(radius,height):
    print(pi*radius*radius*height/3)

def sufrace_area_cube(length):
    print(6*length)
def slope(x1,y1,x2,y2):
    print((y2-y1)/(x2-x1))

def list_sum(list):
    b=0
    for r in list :
        b=b+r
    print(b)
    
def distance_point(x1,y1,x2,y2):
    a=(x2-x1)**2+(y2-y1)**2
    print(math.sqrt(a))

def speed(v0,a,t):
    print(v0+a*t)

def sin_formula(angle_a,side_a,angle_b,side_b,angle_c,side_c):
    a=math.sin(angle_a)/side_a
    b=math.sin(angle_b)/side_b
    c=math.sin(angle_c)/side_c
    if(a==b and b==c and a==c):
        print("True")
    else:
        print("Flase")

def mean(Listofnumbers):
    total=0
    counter=0
    for r in Listofnumbers:
        counter+=1
        total+=r
    return total/counter

def det_matrix_22(matrix):
    result=matrix[0]*matrix[3]-matrix[1]*matrix[2]
    return result

def det_matrix_33(matrix):
    result=matrix[0]*det_matrix_22([matrix[4],matrix[5],matrix[7],matrix[8]])-matrix[1]*det_matrix_22([matrix[3],matrix[5],matrix[6],matrix[8]])+matrix[2]*det_matrix_22([matrix[3],matrix[4],matrix[6],matrix[7]])
    return result

def plot_sin(n=1):
    x = np.linspace(-np.pi*n, np.pi*n, 512, endpoint=True)
    y1 = np.sin(x)
    pl.plot(x, y1)
    pl.show()
    
def plot_cos(n=1):
     x = np.linspace(-np.pi*n, np.pi*n, 512, endpoint=True)
     y = np.cos(x)
     pl.plot(x,y)
     pl.savefig('cos'+str(n)+'.png')
     pl.show()
   
def draw_circle():
    win = GraphWin("My Circle", 500, 500)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
    
def help():
    print("Format your file like this")
    print("Create a text file with any name you like")
    print("In the first line type the number of lines of your program")

def read_savefile(name_file_to_read,name_file_to_save=""):
    try:
        file1 = open(name_file_to_read,"r+")
        file2 = open(name_file_to_save,"w+")
    except:
        print("File not found")
    n_lines= 0
    for line in file1:
        result=0
        n_lines += 1
        linex= line.strip().split()
        x,y,n=0,0,0
        for i in linex:
          
            if(i.isdigit()):
                
                if(n%2==0):
                    x= int(i)
                   
                if(n%2==1):
                    y=float(i)
                    
                n=n+1
            elif(i=="+"):
                result=result+(x+y)
                
            elif(i=="-"):
                result=result+(x-y)
                
            elif(i=="*"):
                result=result+(x*y)
                
            elif(i=="/"):
                result=result+(x/y)
        
            elif(i=="="):
               print(result)
               file2.writelines(str(result)+'\n')
               result=0
    file1.close()
    file2.close()
  
read_savefile("saman.txt","answer.txt")

