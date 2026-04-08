import random

password=int(input("Enter the length of the password: "))

c="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
output="".join(random.sample(c,password))
print(output)