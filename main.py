import math

threeVAR = (input("Y/N if it is 3 vars: ")).lower()
while (threeVAR != "y" and threeVAR != "n"):
  threeVAR = (input("Y/N if it is 3 vars: ")).lower()

print ("This is the format")
if threeVAR == "n":
  print ("ax+by=e\ncx+dy=f")

if threeVAR == "y":
  print ("ax+by+cz=j\ndx+ey+fz=k\ngx+hy+iz=l")

global a
global b
global c
global d
global e
global f

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))
d = float(input("d = "))
e = float(input("e = "))
f = float(input("f = "))

if threeVAR == "y":

  global g
  global h
  global i
  global j
  global k
  global l

  g = float(input("g = "))
  h = float(input("h = "))
  i = float(input("i = "))
  j = float(input("j = "))
  k = float(input("k = "))
  l = float(input("l = "))
print ("")

def BigA(whichisit):
  if whichisit == "n":
    BigA = (a*d)-(c*b)
  else:
    BigA = (a*e*i + b*f*g + c*d*h) - (g*e*c + h*f*a + i*d*b)
  return BigA
    
def solver(whichisit,BigA):
  if BigA == 0:
    print ("Does Not Exist")
  else:
    if whichisit == "n":
      X = ((e*d)-(f*b))/BigA
      Y = ((a*f)-(c*e))/BigA

      print ("(" + str(X) + ", " + str(Y) + ")")
    else:
      X = ((j*e*i + b*f*l + c*k*h)-(l*e*c + h*f*j + i*k*b))/BigA
      Y = ((a*k*i + j*f*g + c*d*l)-(g*k*c + l*f*a + i*d*j))/BigA
      Z = ((a*e*l + b*k*g + j*d*h)-(g*e*j + h*k*a + l*d*b))/BigA

      print ("(" + str(X) + ", " + str(Y) + ", " + str(Z) + ")")


solver(threeVAR,(BigA(threeVAR)))