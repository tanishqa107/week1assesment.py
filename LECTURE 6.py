##CONTROL FLOW STATEMENTS
# CODITIONAL STATEMENT
# 1 indent = 2 spaces , 4 spapces , tab, 8 spaces
a = True
if True:
  print("the value is true")
  a = False
  if True:
    print("the value is true")
print("end")

a = False
if a :
    print("the value is true")
print("end")

a=True
if a:
  print("the value is True")
else:
  print("the value is False")

a=5
if a==3:
  print("the value is 3")
elif a==5:
  print("the value is 5")
else:
  print("the value is not 3 or 5")

#x=int(-inf,inf)
 #G->x

# a=x<0
 #b=x==0
 #c=x>0

 #a intersection b =b intersection c = c intersection a = phi(null set)
# condition are mutually exclusive
"""
q= can profile a acces profile b
a=isfriend
b=isblocked 
c=isadmin
d=isarkjukerberg
TRUTH TABLE-
a b c d q
0 0 0 0 0
0 0 0 1 1
0 0 1 0 1
0 0 1 1 1
0 1 0 0 0
0 1 0 1 1
0 1 1 0 0
0 1 1 1 1
1 0 0 0 1
1 0 0 1 1
1 0 1 0 1
1 0 1 1 1
1 1 0 0 0
1 1 0 1 1
1 1 1 0 0
1 1 1 1 1
"""