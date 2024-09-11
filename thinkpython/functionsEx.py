# 3.11.2. Exercise
# Write a function named print_right that takes a string named text as a parameter 
# and prints the string with enough leading spaces that the last letter 
# of the string is in the 40th column of the display.

# Hint: Use the len function, the string concatenation operator (+) 
# and the string repetition operator (*).

def print_right(text):
    length = len(text)
    final = " " * (40 - length) + text
    print(final)
    print(len(final))
    
print_right("traveler")

# 3.11.3. Exercise
# Write a function called triangle that takes a string and an integer and draws a pyramid 
# with the given height, made up using copies of the string. 

def triangle(text, digit):
    for i in range(digit + 1): # +1 cause last value of range doesn't count
        print(text * i)
   
        
triangle("D", 6)

# 3.11.4. Exercise
# Write a function called rectangle that takes a string and two integers 
# and draws a rectangle with the given width and height, 
# made up using copies of the string. 

def rectangle(text, num1, num2):
    for i in range(num2 +1):
        print(text * num1)
        
rectangle("A", 10, 6)

# 3.11.5. Exercise
# Write a function called bottle_verse that takes a number as a parameter 
# and displays the verse that starts with the given number of bottles.

# Hint: Consider starting with a function that can print the first, second, 
# or last line of the verse, and then use it to write bottle_verse.

def bottle_verse(num):
    for i in range(num + 1):
        print(f"{num} bottles of beer on the wall")
        print(f"{num} bottles of beer")
        print("Take one down, pass it around")
        print(f"{num - 1} bottles of beer on the wall")
        
bottle_verse(6)