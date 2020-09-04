#Question 2

#Dictionary and its default functions..........

#syntax dic_name={key1:value1,key2:value2...............}

Details={"name":"rohit","rollno":10,"Subject":"Python"}

print("Printing the dictionary elements............",Details)

#5 functions in python.................

#copy()	Returns a copy of the dictionary

cop=Details.copy()

print("copying the values in the new variable using the copy()", cop)

#values()	Returns a list of all the values in the dictionary

print("Returning a list of all the values in the dictionary",Details.values())

#keys()	Returns a list containing the dictionary's keys

print("Returning a list containing the dictionary's keys",Details.keys())

#pop()	Removes the element with the specified key

Details.pop("rollno")

print("Removing the element with the specified key",Details)

#clear()	Removes all the elements from the dictionary
Details.clear()

print("Removing all the elements from the dictionary",Details)



