#string demo
print("this is a string msg.\nAnd now this line is printed in \"new line\".")

# string variable
phrase_1 = "Hello" 
phrase_2 = " World"
print(phrase_1+phrase_2)

# string function
print(phrase_1.upper())     # Upper function
print(phrase_1.upper().isupper())

print(phrase_2.lower())     # Lower function
print(phrase_2.lower().islower())

print(len(phrase_1))     # Lenght function ->  Find the length

# index
print(phrase_1.index("llo"))

# replace
print(phrase_1.replace("H","h"))

# ascii check
print(phrase_1.isascii())