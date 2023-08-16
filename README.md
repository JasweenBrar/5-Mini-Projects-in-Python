# 5-Mini-Projects-in-Python
Practicing Python by developing small projects.

* [Project 1: Grocery Store Calculator and Receipt Generator](#project-1)

### <a name="project-1"></a> 💠 Project 1: Grocery Store Calculator and Receipt Generator

A bill calculator and receipt generator for a general store


*Explanation*-

We are using a while loop which runs till the user hits the Enter key. We've initialized the sum variable as 0, and every time the user inputs a new price(integer), the value gets added to the previous value of the sum. Once the user hits the enter key, the while loop is stopped with the help of a break statement.

**Code:**
```
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
```


**Output:**
```

```

---

### 💠 Project 2: Currency Converter</b>

We store the exchange rates of different currencies in a text file. After this, we're reading the data from the text file. Then, we're iterating over the text file's data (currencyData.txt), which is stored in the lines variable using a for loop and parsing the data to a dictionary variable named currencyDict.

We're done with the data fetching part. Now, we take the input of the amount that the user wants to convert. Once the user inputs some amount, the list of all different currencies is displayed to the user. In the end, we convert the amount entered by the user to the selected currency for exchange. 

**Code:**
```
with open('currencyData.txt') as f:
	lines = f.readlines()

currencyDict = {}
for line in lines:
	parsed = line.split("\t")
	currencyDict[parsed[0]] = parsed[1]

amount = int(input("Enter amount:\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
```

**Output:**
```

```

---

### 💠 Project 3: Password Generator</b>

**Code:**
```

```

**Output:**
```

```

---

### 💠 Project 4: Secure My Passwords through Python

**Code:**
```

```

**Output:**
```

```

---

### 💠 Project 5: Hangman Game

A basic command-line program: Hangman! The game will allow for user input, and will also output a visual of the hangman alongside the word that’s being guessed. 

**Code:**
```

```

**Output:**
```

```

----
