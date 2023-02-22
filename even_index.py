# Exercise Statement:
# Write a program to accept a string from the user and display characters that
# are present at an even index number.
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.

def iterator(string):
    for i in range(len(string)):
        if i % 2 == 0:
            print(string[i])
        else:
            pass


original_string = input("Give me a string: ")
print("Original String is  " + original_string)
print("Printing only even index chars.")
print("Remember that computers count from 0.")

iterator(original_string)
