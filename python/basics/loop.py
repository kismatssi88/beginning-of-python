sub=['math','physics','chem']
for index ,course in enumerate(sub,start=1):
    print(course,index)
    sub=['math','physics','chem']
    new=','.join(sub)
    print(new)
    new_str=new.split(',')
    print('new_str')