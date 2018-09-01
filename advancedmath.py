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
    
    

