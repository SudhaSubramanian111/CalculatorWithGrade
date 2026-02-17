Total=0.0
Percentage= float(0.0)
def grade(TamilMark,EngMark,HindiMark):
  Total = TamilMark + EngMark + HindiMark
  Percentage= Total/300 * 100
  return Total,Percentage
  
Name= input("Enter the Name of the student:")    
TamilMark=float(input("Enter Tamil Mark:"))
EngMark=float(input("Enter English Mark:"))
HindiMark=float(input("Enter Hindi Mark:"))

total,per=grade(TamilMark,EngMark,HindiMark)
print(f"Name: {Name}")
print(f"Total: {total :.2f}/300" )
print(f"Percentage: {per :.2f} %" )
if(Percentage >=75 ):
    print("Grade A")
elif(Percentage >=60):
    print("Grade B")
elif(Percentage >= 50):
    print("Grade C")
elif(Percentage >= 40):
     print("Grade D")
else:
    print("Grade F")