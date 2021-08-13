colors=['red','blue' , 'yellow']
for index , color in enumerate(colors):
    print(index+1,':',color)


def asal(num):
    if int(num)%2==0:
        return num



for i in range(20):
    print(asal(i))
def display(lst):
    while lst:
        print(lst.pop())
    while len(lst) >= 5:
        print('i am in')
        print( lst.pop())

def dis(lst):
    pass


print(',,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,')
ls=[1,2,3,5,6, 90,7,8,9]
display(ls)
print('***********************************')
for index , i in enumerate(ls):
    if index<4:
        print(index)
        continue
    else:
        print(i)



