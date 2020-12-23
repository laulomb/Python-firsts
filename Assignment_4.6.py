#Assignment 4.6

hours = input("Enter Hours:")
rate = input('Enter rate:')
h=float(hours)
r=float(rate)

Pay=h*r

if h>40:
    hext=h-40
    rext=r*0.5
    Pay=(r*h)+(hext*rext)

def computepay(h,r):
    return Pay

P = computepay(h,r)
print("Pay",P)
