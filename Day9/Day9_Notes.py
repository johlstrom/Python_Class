programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.", 
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again.",
}

#print(programming_dictionary["Bug"])

#Adding new item to dictionary.
programming_dictionary["Word"] = "Just a word"

#print(programming_dictionary)

#Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])