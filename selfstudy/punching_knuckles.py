csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']

# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise
friends_list.pop()
csv = csv.replace(",", " ")
csv = csv.replace(":", " ")
csv = csv.replace(";", " ")
csv = csv.split()
print(csv)
print(friends_list)