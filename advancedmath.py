import math

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
