n=input("Enter String")
x=len(n)
y=input("Enter char")
if n[0]==y:
     print("Valid")
elif n[x-1]==y:
       print("Valid")
else:
     print("Invalid:")