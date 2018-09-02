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
def circle_area(radius):
    print(radius*radius*math.pi)
def area_triangle(base,height):
    print((base*height)/2)
def vol_cube(length):
    print(length**3)
