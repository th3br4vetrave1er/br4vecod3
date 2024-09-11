def repeat(string, digit):
    print(string * digit)

spam = "Spam, "

def first_two():
    repeat(spam, 4)
    repeat(spam, 4)
    

def other_three():
    repeat(spam, 2)
    print("(Lovely Spam, Wonderful Spam!)")
    repeat(spam, 2)
    
def final():
    first_two()
    other_three()
    

for i in range(5):
    print("Repeat number ", i)
    final()