x=0
p=0
i=0
p90=0
m=0
for i in range(1, 8):
    x=x+1
    p=int(input(f"Digite o peso da {x}ﾟ pessoa "))
    i=int(input(f"Digite a idade da {x}ﾟ pessoa "))
    m+=i
    if p >= 90:
        p90+=1
print(f"Existem {p90} pessoas com peso maior ou igual a 90")
