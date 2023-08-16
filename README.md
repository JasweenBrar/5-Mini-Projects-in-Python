# 5-Mini-Projects-in-Python
Practicing Python by developing small projects.

* [Project 1: Grocery Store Calculator and Receipt Generator](#project-1)
* [Project 2: Currency Converter](#project-2)
* [Project 3: Password Generator](#project-3)
* [Project 4: Secure My Passwords through Python](#project-4)
* [Project 5: Hangman Game](#project-5)

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
    print("---------------------------------")
    
print(f"Total          =       Rs.{sum}")    
```


**Output:**
```
Enter the item name or press q to quit: Milk
Enter the item price(in Rs.) 50
Order total so far: 50
Enter the item name or press q to quit: Chocolate
Enter the item price(in Rs.) 10
Order total so far: 60
Enter the item name or press q to quit: Bread
Enter the item price(in Rs.) 32
Order total so far: 92
Enter the item name or press q to quit: q
Your Bill total is 92. Thanks for shopping with us


---------------------------------
******* Final receipt is *******
Item Name      -       Item Price
---------------------------------
Milk                   Rs.50
---------------------------------
Chocolate              Rs.10
---------------------------------
Bread                  Rs.32
---------------------------------
Total          =       Rs.92
```

---

### <a name="project-2"></a> 💠 Project 2: Currency Converter</b>

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

amount = int(input("Enter amount (INR):\n"))
print("Enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in currencyDict.keys()]
currency = input("Please enter one of these values: \n")
print(f"{amount} INR is equal to {amount *float(currencyDict[currency])} {currency}")
```

**Output:**
```
Enter amount (INR):
100
Enter the name of the currency you want to convert this amount to? Available Options:

Argentine Peso
Australian Dollar
Bahraini Dinar
Botswana Pula
Brazilian Real
British Pound
Bruneian Dollar
Bulgarian Lev
Canadian Dollar
Chilean Peso
Chinese Yuan Renminbi
Colombian Peso
Croatian Kuna
Czech Koruna
Danish Krone
Emirati Dirham
Euro
Hong Kong Dollar
Hungarian Forint
Icelandic Krona
Indonesian Rupiah
Iranian Rial
Israeli Shekel
Japanese Yen
Kazakhstani Tenge
Kuwaiti Dinar
Libyan Dinar
Malaysian Ringgit
Mauritian Rupee
Mexican Peso
Nepalese Rupee
New Zealand Dollar
Norwegian Krone
Omani Rial
Pakistani Rupee
Philippine Peso
Polish Zloty
Qatari Riyal
Romanian New Leu
Russian Ruble
Saudi Arabian Riyal
Singapore Dollar
South African Rand
South Korean Won
Sri Lankan Rupee
Swedish Krona
Swiss Franc
Taiwan New Dollar
Thai Baht
Trinidadian Dollar
Turkish Lira
US Dollar
Venezuelan Bolivar
Please enter one of these values:
US Dollar
100 INR is equal to 1.3588 US Dollar
```

---

### <a name="project-3"></a> 💠 Project 3: Password Generator</b>

The code generates a random password of specified length using a mix of lowercase and uppercase letters, digits, and punctuation symbols, utilizing the string and random modules in Python. 

**Code:**
```
import string
import random

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    plen = int(input("Enter password length\n")) 
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    print("Your password is: ")
    print("".join(random.sample(s, plen)))
```

**Output:**
```
Enter password length
8
Your password is: 
4#y*5EZF
```

---

### <a name="project-4"></a> 💠 Project 4: Secure My Passwords through Python

The code defines a function to enhance password security by replacing certain characters with corresponding symbols, following a predefined set of character transformations.

**Code:**
```
SECURE = (('s', '$'), ('and', '&'), 
            ('a', '@'), ('o', '0'), ('i', '1'),
            ('I', '|'))

def securePassword(password):
    for a,b in SECURE:
        password = password.replace(a, b)
    return password

if __name__ == "__main__":
    password = input("Enter your password\n")
    password = securePassword(password)
    print(f"Your secure password is {password}")
```

**Output:**
```
Enter your password
Indians123
Your secure password is |nd1@n$123
```

---

### <a name="project-5"></a> 💠 Project 5: Hangman Game

The Python code creates a command-line hangman game where players attempt to guess a word from a predefined list. The code handles guessing, tracks attempts, and reveals the word progressively as players guess letters correctly.

**Code:**
```
import random

# List of words for the game
words = ["apple", "banana", "cherry", "grape",
         "orange", "strawberry", "watermelon"]


def choose_word(words):
    return random.choice(words)


def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def hangman():
    selected_word = choose_word(words)
    guessed_letters = []
    attempts = 6

    print("Welcome to Hangman!")
    print(display_word(selected_word, guessed_letters))

    while True:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess not in selected_word:
            attempts -= 1
            print(f"Wrong guess! You have {attempts} attempts left.")
            if attempts == 0:
                print("Sorry, you lost. The word was:", selected_word)
                break
        else:
            word_display = display_word(selected_word, guessed_letters)
            print(word_display)

            if "_" not in word_display:
                print("Congratulations, you won!")
                break


hangman()
```

**Output:**
```
Welcome to Hangman!
_____
Guess a letter: a
a____
Guess a letter: e
a___e
Guess a letter: b
Wrong guess! You have 5 attempts left.
Guess a letter: g
Wrong guess! You have 4 attempts left.
Guess a letter: p
app_e
Guess a letter: l
apple
Congratulations, you won!
```

----
