import random
print("Enter the word,letter,symbols from which the password will be genrrated")
password = input()
print("Enter the length of passsword")
pass_length = int(input())
a = "".join(random.sample(password,pass_length))
print("Your genrated password")
print(a)
