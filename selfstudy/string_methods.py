# Capitalize - convert first character to upper and rest to lower
name = "dWIGHT"
print(name.capitalize())

# Encode - return encoded version of string. 
# Optional parameter encoding & errors specify encoding to use and error method
txt = "Mr. Ståle"
print(txt)
print(txt.encode("ascii", "ignore"))

# Format - format values in string
txt = "I {} The {}".format("love", "Office")
print(txt)
txt = "I {1} The {0}".format("Office", "love")
print(txt)

# Isalpha - return True if all string characters are in alphabet    
name = "Andy123"
print(name)
print(name.isalpha())

# Isidentifier - return True if string is identifier. 
# These can only contain alphanumeric chars & underscores & can't start with numbers.
txt = "2077Cyber"
print(txt)
print(txt.isidentifier())
txt2 = "Cyber2077"
print(txt2)
print(txt2.isidentifier())

# Isspace - return True if all characters are whitespaces
txt = "   "
print(txt.isspace())

# Istitle - Return True if string follows rules of a title. 
# (All words are lower except first letter of each word.)
txt = "I Like Tech Twitter"
print(txt.istitle())
txt2 = "I like tech twitter"
print(txt2.istitle())

# Ljust - Return string left justified. (needs to be len of string + len of characters in 2nd param)
# 2nd optional param specifies character to fill space. Default is space
txt = "JavaScript"
txt2 = txt.ljust(15, "@") 
print(txt2) 

# Partition - Return tuple with string parted in 3 parts. 
# Middle part is specified string. If not found, entire string stored in first part of tuple.
txt = "HTML is a programming language?"
print(txt.partition("programming"))