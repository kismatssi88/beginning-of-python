print('enter the marks of 5 subjects of 2nd semester')
math=int(input('enter the marks of math:'))
stats=int(input('enter the marks of stats:'))
microprocesor=int(input('enter the marks of microprocessor:'))
oop=int(input('enter the marks of oop:'))
Ds=int(input('enter the marks of Ds:'))
total=math+stats+microprocesor+oop+Ds
average=total/5
percentage=(total/500)*100
if percentage>=40:
   print('pass')
else:
    print('fail')
print('The total marks =',total)
print('The average marks =',average)    

