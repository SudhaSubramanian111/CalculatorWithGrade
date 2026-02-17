# Online Python compiler (interpreter) to run Python online.

def calculator(x,y,operation):
  if(operation == '+'):
    return x+y
  elif(operation == '-'):
    return x-y
  elif(operation == '*'):
    return x*y
  elif(operation == '/'):
      if y==0:
         return "We can't devide by using 0. Please provide the valid divider"
      else:
        return x/y
  else:
    return "enter valid operator to proceed"
    
ip_x=float(input("Enter x:"))
ip_y=float(input("Enter y:"))
ip_operator=input("Enter operator:")

res=calculator(ip_x,ip_y,ip_operator)
print("Result=",res)
if(res== 0):
    print("Zero")
elif(res >0 ):
    print("Positive")
else:
    print("Negative")
