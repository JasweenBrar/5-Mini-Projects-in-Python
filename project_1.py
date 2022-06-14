sum = 0
listName = []
listPrice = []
while (True):
    userInputName = input("Enter the item name or press q to quit: ")    
	
    if (userInputName != 'q'):
        userInputPrice = input("Enter the item price(in Rs.) ")
        listName.append(userInputName)
        listPrice.append(userInputPrice)
		
        sum = sum + int(userInputPrice)
		
        print(f"Order total so far: {sum}")
	
    else:
		
        print(f"Your Bill total is {sum}. Thanks for shopping with us")
		
        break
        
print()
print()
print("---------------------------------")        
print("******* Final receipt is *******")
print("Item Name      -       Item Price")
print("---------------------------------")
for i in range(len(listPrice)):
    print(listName[i],end="")
    for j in range(23-len(listName[i])):
        print(" ",end="")
    print(f"Rs.{listPrice[i]}")    
    #print(f"{listName[i]}           {listPrice[i]}")
    print("---------------------------------")
    
print(f"Total          =       Rs.{sum}")    
