
# Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
# Given:
# str1 = "James"
# Expected Output:
# Jms """

str1="James"
str1=str1 [0::2]
print(str1)

# Exercise 1B: Create a string made of the middle three characters
# Write a program to create a new string made of the middle three characters of an input string.
# Given:
# Case 1
# str1 = "JhonDipPeta"
# Output
# Dip 

str1 = "JhonDipPeta"
print(type(str1))
middle=len(str1)//2
output=str1[middle-1:middle+2]
print(output)

# Case 2
# str2 = "JaSonAy"
# Output
# Son

str2 = "JaSonAy"
output=str2[(len(str2)//2)-1:(len(str2)//2)+2]
print(output)

#Exercise 2A: Append new string in the middle of a given string
#Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
#Given:
#s1 = "Ault"
#s2 = "Kelly"
#Expected Output:
#AuKellylt
s1='Ault'
s2='Kelly'
a1=s1[len(s1)//2:]
print(a1)
a2=s1[0:len(s1)//2]
print(a2)
s3=a2+s2+a1
print(s3)

#Exercise 2B: Create a new string made of the first, middle, and last characters of each input string
#Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
#Given:
#s1 = "America"
#s2 = "Japan"
#Expected Output:
#AJrpan
d1 = "America"
d2 = "Japan"
w1=d1[0]+d2[0]
w2=d1[-1]+d2[-1]
w3=d1[len(d1)//2]+d2[len(d2)//2]
new=w1+w3+w2
print(new)

#Exercise3: Find all occurrences of a substring in a given string by ignoring the case
#Write a program to find all occurrences of “USA” in a given string ignoring the case.
#Given:
#str1 = "Welcome to USA. usa awesome, isn't it?"
#Expected Outcome:
#The USA count is: 2
str1 = "Welcome to USA. usa awesome, isn't it?"
str1=(str1.upper())
print(str1.count('USA'))

#Exercise4: Strings and console output
#Exercise4A: Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string. 
#Sample String : 'resource'
#Expected Result : 'rece'
#Sample String : 'tx'
#Expected Result : 'txtx'
ss1='resource'
e1=ss1[0:2]+ss1[-2:]
print(e1)
ss2='txtx'
e2=e1=ss2[0:2]+ss2[-2:]
print(e2)

#Exercise4B: Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$', except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'
ss3='restart'
first_symbol=ss3[0]
print(first_symbol)
print(ss3.count('r'))
ss4=ss3[1:]
print(ss4)
ss5=ss4.replace('r','$')
print(ss5)
newss3=first_symbol+ss5
print(newss3)

#Experience4C: Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.
#Sample String : 'abc', 'xyz'
#Expected Result : 'xyc abz'
ss6='abc'
ss7='xyz'
a6=ss7[0:2]+ss6[-1]
a7=ss6[0:2]+ss7[-1]
print(a6)
print(a7)
final=a6+" "+a7
print(final) 