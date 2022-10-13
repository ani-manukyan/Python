#string is defined with '' or ""
#to understand the type we use type function
nm='my name is John'
num=25
print(type(nm), type(num))
#for example in this case it shows -- str and int
#print function ends with an "enter", so it starts with a new line
# if you want all your output to be in the same line you add "end" and a space " "
# we will add one more space in a separate print
print(type(nm),type(num),end='   ')
print("",end=' ')
print(type(nm),type(num))

#adding \ and smth to transfer to a new line
nm1='My name \n \t \t is John'
print(nm1)

#we can also use "sep" to separate output values. Will work the same with 3 variables
print('this is test','This is another test',sep='\n', end='\n\n')
print('this is test')

#defining a new string
sometxt='This is test'

#to see the last and first symbol
first_symbol=sometxt[0]
print(first_symbol)

last_symbol=sometxt[-1]
print(last_symbol)

#starting from some point, eg starting from the second value
point=sometxt[1:]
print(point)
#second value in the [] means it's not inclusive
point1=sometxt[1:3]
print(point1)
#will print only "hi" from "this"
# if we want to skip every one we say [::], will print "Ti sts"
point2=sometxt[0::2]
print(point2)
#we can do the same from the back, using [-1::-2]
#to write the word in the opposite way [-1::-1]
point3=sometxt[-1::-1]
print(point3)
#in this case it will take the values from [-1:-5] with the frequency of [-2] - will print "te"
point4=sometxt[-1:-5:-2]
print(point4)

#to add texts to each other
text1="James"
text2=25
text3='engineer'
#to add all to each other they need to have the same type
#change to str
person1=str(text1)+' '+str(text2)+' '+str(text3)
print(person1)

#formating string, adding f and {}
person1=f'{text1} {text2} {text3}'
print(person1)
#to define the variables
person1=f'Name: {text1}, age:{text2}, profession: {text3}'
print(person1)
#formating
person1='Name:{},age:{}, profession:{}'.format(text1, text2, text3)
print(person1)
#adding indexes, name is txt1 and is the first one (0)
person1='Name:{0},age:{1}, profession:{2}, Name:{0} is driving car'.format(text1, text2, text3)
print(person1)
#changing to decimals, adding 0.2f to show .00 value
person1='Name:{0},age:{1:0.2f}'.format(text1, text2)
print(person1)

#text - capitalize or count
text1.capitalize
print(text1)
#count the number of values, how many times we have the variable
print(person1.count(text1))
#len - length of the stirng
print(len(person1))
#finding middle value
print(person1[len(person1)//2])
#show characters after the middle
print(person1[len(person1)//2:])
#find the position (which character)
print(person1.find(text1))

#lst - multi values, lst[]
lst=[]
print(type(lst)) 
#add value - append
lst.append(12)
lst.append (15)
print(lst)
#change its value
lst[0]=11
lst[1]=12
print(lst)
#we can choose from where to print
print(lst[1:])
#find index (their position)
print(lst.index(12))
#append, in this case 11 is the1st element, 12 is the 2nd element, and [jack , jane] the 3rd elemnt
lst2=['Jack',"Jane"]
lst.append(lst2)
print(lst)
#extend - if you want the appending elements to be counted as their own
#now you have Jack as the 3rd element and Jane as the 4th
lst.extend(lst2)
print(lst)
#how to define the position of the adding text - give the order where you want and then value
lst.insert(1,'drivers')
print(lst)
#copy to ensure that changes in lst won't affect lst3
lst3=lst.copy()
#dropping last value
lst.pop()
lst.remove(12)
#tuple and st for multiple values
#tuple cannot be changed, can be done by changing to lst
#needs to be at least 2 elements
#this is why we wrote , - otherwise it would have understood as integer
tpl=(25, )
set={14, }
print(type(tpl))
print(type(set))
#changing types
lst_n=list(tpl)
lst_n.append(15)
print(lst_n)
print(type(lst_n))

lst_n=tuple(lst_n)
print(type(lst_n))

print(lst_n[1])
print(lst_n.count(12))
print(lst_n.index(15))