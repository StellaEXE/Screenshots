lastName = input ("customer's last name")
numBathrooms = int(input ("number of bathrooms to be cleaned"))
numOtherRooms = int(input ("number of rooms to be cleaned"))
totalCostBathrooms = numBathrooms * 15
totalCostOtherRooms = numOtherRooms * 10
serviceCharge = totalCostBathrooms + totalCostOtherRooms + 40
print(lastName)
print(numBathrooms + totalCostBathrooms)
print(numOtherRooms + totalCostOtherRooms)
print(totalCostBathrooms + totalCostOtherRooms)
print("program complete")
