sentence_one ="the Dog Breed is German Shepherd"
sentence_two ="Defeats for the Clinton forces, this was her moment of triumph"
print(sentence_one[8:23])
print(sentence_two[16:29])


o="JOHn ."
j=o.lower()[:4]
print(j)

k="6"
g="7"
z=k+g 
print(z)
f=int(k)+ int(g)
print(f)
temp=56.8926
temp2=round(temp,1)
temp2=str(temp2) + "0"
print(temp2)
s=2
r=4
x=(2%4)
print(x)
sentence_five="the lazy dog ran so fast it hit the wall"
print(sentence_five.split(';'))
numb=56.8926
numb2=round(numb,3)
print(numb2)
print((7>8 and 3>1) or(5>9 and 4!=9))
print((6>3 and 8<9 or 4>8) or(5==5 and 6>5) )
print((4>7 or 6<3 and 8>1) and(32 and 4<9 or 5>7))
print((5<3 and 6>2 or 6!=3) and (5>9 and 8>9 or 3>9))

#list&tuples
taskList = [ 23, "Jane", ["Lesson 23", 560, {"currency" : "KES"}], 987, (76,"John")]
print(type(taskList))
print(taskList[2][1])
print(taskList[2][2]["currency"])
print(len(taskList))
taskList[2][2]["amount"]=90
print(taskList)
print(taskList[4][0])

#new work
m=int(input("Enter marks:"))
try:
    m=int(m)
    if m < 0 or m > 100:
        print("marks out of range")
    else:
        print("passed.proceed to next grade")
except:
    print("Ensure you enter a number")

#extrawork
mtest="45.89"
mtest1=mtest[0]+mtest[1]
mtest2=int(mtest1)
print(mtest2)
print(type(mtest2))
lst1=list(range(0,10))
print(lst1)

for i in lst1:
    print(i)