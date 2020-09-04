#Question3

#Set and its default functions..........

#Syntax variable={E1,E2,E3,E4............................}

s={1,2,3,4,5}

print("printing the elements....",s)

#5 functions in set..........

#add()	Adds an element to the set

s.add(6)

print("After adding an element in the set........",s)

#len() returns the length of the items present in the list.

l=len(s)

print("Printing the length of the items present in the list...",l)

#union() - joing two sets

a={1,2,3}

b={3,4,5,6}

u=a.union(b)

print("Union of A and B is ",u)

#intersection() - common elements

i=a.intersection(b)

print("Intersection of A and B is ",i)

#difference -

d=a.difference(b)

print("DIfference of A and B is ",d)

