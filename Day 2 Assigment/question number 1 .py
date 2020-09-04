#Question 1

#list and its default functions..................

#synatax of the list is varibale=[E1,E2,E3.....................]

number=[1,2,3,4,5,6,7,8,0]

print("the numbers are...................... ",number)

#5 functions used in list..................

#append() -used to add a element at the end of the existing list.............

name=["Rohit","Ram","Sam"]

#adding an element to yhe end of the list...........

name.append("Rakesh")

print("After appending an elemets...........",name)

#extend() - use dto add mulktiple element at the end of the list.....................

name.extend(["Rahul","Ramesh"])

print("After adding more elements at the end of the list..............",name)

#difference between append and extend is append is used to add only one element at the end of the list whereas extend is use dto add multiple element at the end of the list............

#insert() -used to add an element at the desired position

#syntax: list_varaibale.insert(position index,element)

name.insert(1,"Sanjay")

print("After inserting element sanjay in the index postion of 1............... ",name)

#remove() -to delete a particular element in the list

name.remove("Sanjay")

print("After removing sanjay from the lsit...............",name)

#clear()-deletes all the elements in the list and it only delete all the elements but the loist retains .............

name.clear()

print("Deleting all the elements in the list ..............",name)


