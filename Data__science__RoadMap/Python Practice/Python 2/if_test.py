is_male = True
is_tall = False

if is_male and is_tall :
    print("you are a Tall male")
elif is_male and ~is_tall :
    print("you are a Short male")
elif ~is_male and is_tall :
    print("you are not a male but tall")
else:
    print("You are either not male.")

def max_num(n1,n2,n3):
    if n1>=n2 and n1>=n3:
        return n1
    elif n2>=n1 and n2>=n3:
        return n2
    else:
        return n3

max = max_num(10,25,60)
print(max)