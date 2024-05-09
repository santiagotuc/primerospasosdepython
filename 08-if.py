mass = 78
height = 1.74
bmi= mass / (height ** 2)

print('Mi nombre es Santiago y mi IMC es', bmi)
Resultado = bmi

if Resultado >= 24:
    print("Usted esta gordito")

elif Resultado >= 18:
    print("Usted tiene un bmi normal")  

else:
    print("Usted tiene un bmi bajo")

print(Resultado)    

