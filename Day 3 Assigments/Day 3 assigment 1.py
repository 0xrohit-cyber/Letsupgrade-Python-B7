Altitude=int(input("Enter your altitude you are in : "))

if (Altitude <= 1000):
    print("Safe to Land")

elif (Altitude > 1000 ) and (Altitude <5000):
    print("Bring down to 1000")
else:
    print("Turn around")
                   
