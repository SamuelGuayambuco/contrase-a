import random
x =  "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("Escribe la longitud de tu contraseña (un numero)"))
password = ""
for i in range(longitud):
    password += random.choice(x)
print(password)
