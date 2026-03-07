# Assignment 07 
name_one = "Osama"
name_two = "Osama_Elzero"

x = "@@@@@@@"
print(f"{x}{name_one}")

# rjust()
my_name = "atif"
new_name = my_name.center(10, '-')
print(new_name)

def build_chars(name, length, char):
    rest_chars = length - len(name)
    return f"{(rest_chars // 2) * char}{name}{(rest_chars // 2) * char}"

user_name = "Ahmed"
width = 30
char = '%' 

print(build_chars(user_name, width, char))

# Solution
print(name_one.rjust(20, "@"))
print(name_two.rjust(20, "@"))
 
 
