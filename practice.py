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









