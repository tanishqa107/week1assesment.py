"""
#ARITHMETIC OPERATOR

    # "+" = Add
    # "-" = minus
    # "/" = divide
    # "*" = multiply
    # "%" = mod
    # "+" = Add
    # "//" = floor division
    # "**" = to the power of
"""

print(10+3)
print(10-3)
print(10/3)
print(10*3)
print(10%3)
print(10//3)
print(10**3)

print(int(10/3))
print("shivang"+"agrawal")
print("shivang" " " "agrawal")
print("sa"*2)

"""#COMPARISION OPERATOR

#'==' = True, if equal
#'!=' = True,if not equal
#'<' =less than
#'>' =greater than
#'<=' = less than equal to
#'>=' = greater than equal to
"""

print(1==1)
print(1!=1)
print(1<2)
print(1>2)
print(1<=1)
print(1>=1)
print("ab"<"z")
#lexicographical comparision
print("a"<"A")

"""#logical operator
 # not ,  or , and
"""

print(True and False)
print(True or False)
print(True and 1 )
print(1 and 0)
print(1 and 5)

print(isinstance(True,int))
print(type(True))

#print(True = 2)

"""#TRUTHY AND FALSY VALUE
#0,NULL SET ARE SAID TO BE FALSY VALUE
#ALL NON ZERO , SET ARE SAID TO BE TRUTHY
"""

print(bool(0))
print(bool(1))
print(bool(""))
print(bool([1,2,3]))

"""# true or b=true
#false or b=b 
#true and b=b
#false and b=false

"""

## SHORT CIRCUITING
#a or b=b(if a is truthy)
#a or b=a(if a is falsy)
#a and b=a(if a is truthy)
#a and b=b(if a is falsy)
print("jatin" and 6)
print("" and 6)
(print(" "and 6))
print(1 or 0)
print(1 and 0)
print(1.6 or "")
print(""or 2.5)
print("" and 0)
