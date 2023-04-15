#write a function that checks if a word is palindrome
#Returns true if it is and false if it is not 
#Words = 'Noon','Madam','Radar','Civic'

def palindrome(string):
    return string==string[::-1]
string= "Noon"
ans =palindrome(string)
if ans:
    print("true")
else:
    print("false")

print("My\nname\nis\nBond.", end=" ")
print("James Bond.")


#print(sep="&","fish","chips")


fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
print(fruits.count('apple'))
#counts the occurances of a particular element
print(fruits.index('banana'))
#finds the index of the first occurance of the element
print(fruits.copy())
#fruits.copy makes copy of the list but in a different memory location
# print(fruits[::-1])
fruits.reverse()
print (fruits)
print(fruits.pop())
#.pop removes and returns an item froma a list and also at a specified index
print(fruits.pop(2))
print(fruits)
print(fruits.sort())
print(fruits)
fruits.remove("apple")
print()
                                   #15/04/2023
                                   #OPEREATORS

def addittion(num1, num2):
    sum= num1+num2
    print(sum)

def substraction(num, num2):
    diff= num-num2
    print(diff)

#1. What is the output of the following code?
def calculate(a,b):
    c = a * b
    print(c)

#2. What is the output of the following code?
def division(d,e):
    f = d/e
    print(f)
    
 #2b.What is the output of the following code?
def divi(g,h):
    I = g // h
    print(I)

#3. What is the output of the following code?
# def logical():
def logic(j,k,):
    l = (j!= k)
    print(l)

#4. What is the output of the following code
def number(n):
  n=[1,2,3]
  not2 = 4 in n
  print(not2)

#5. What is the output of the following code?
def identical(q, p):
    value1 = q is p
    print(value1)
    
#6. What is the result of the following expression?
def modulus(num1, num):
    value = num1 % num
    print(value)

#7. What is the output of the following code?
def exponent(num3, num4):
    result = num3**num4
    print(result)

#8. What is the output of the following code?
def greater(numb,numb1):
    great= numb<numb1 and numb!= numb1
    print(great)

#9. What is the output of the following code
def notnumber(n):
  n=[1,2,3]
  not2 = 4 not in n
  print(not2)
 
#10. What is the output of the following code 
def compare2(y,z):
    comp = y == z
    print(comp)


