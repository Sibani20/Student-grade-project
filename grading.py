name=input('Enter your name:')
a=int(input('Enter Maths mark:'))
b=int(input('Enter English mark:'))
c=int(input('Enter Science mark:'))
d=int(input('Enter Social mark:'))
e=int(input('Enter French mark:'))
Total=a+b+c+d+e
Average=Total/5
Percentage=(Total/500)*100
print(f'Hello,{name}!')
print(f'Total marks:{Total}')
print(f'Average marks:{Average}')
print(f'Percentage:{Percentage:.2f}%')
if (Average>=95):
    print('Grade=S')
elif(90<=Average<=94):
    print('Grade=A+')
elif(75<=Average<=89):
    print('Grade=A')
elif(60<=Average<=74):
    print('Grade=B')
elif(40<=Average<=59):
    print('Grade=C')
else:
    print('Fail')
print('Thank You,',name)