import random, string
x= ''.join(random.choices(string.ascii_letters + string.digits, k=32))
print(x)