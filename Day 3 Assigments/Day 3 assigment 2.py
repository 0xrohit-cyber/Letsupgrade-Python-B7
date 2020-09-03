start = 1
end = 200

print("Printing the Prime numbers between", start, "and", end, "are:")

for i in range(start, end + 1):
   if i  > 1:
       for j in range(2, i):
           if (i % j) == 0:
               break
       else:
           print(i)
