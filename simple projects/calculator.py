#sum,product ,division ,difference
a=float(input('enter first number:'))
b=float(input('enter second number'))
operator = (input('enter operattion +,-,*,/ or all'))
if operator == '+':
 sum=a+b
 print('the sum is',sum)
elif operator == '-': 
 difference=a-b
 print('result=',difference)
elif operator == '*':
 product=a*b
 print('result=',product)
elif  operator == '/':
  if b!=0:
   division=a/b
   print('result=',division)

elif operator == 'all':
 sum=a+b
 difference=a-b
 product=a*b
 division=a/b
 print('result=\n',sum,difference,product,division)

else:
 print('invalid')



