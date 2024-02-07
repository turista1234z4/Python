p=0
im=0

for i in range(1,21):
    x=int(input("Digite um número"))
    if x%2==0:
        p+=1;
    else:
        im+=1;
print(f"Existem {p} números pares e {im} números ímpares")