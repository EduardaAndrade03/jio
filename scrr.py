# q 1 

# peso = float(input("digite seu peso em Kg "))
# altura = float(input("digite sua altura em M "))
# IMC = peso / (altura*altura)

# if IMC<18.5:
#     print("abaixo do peso")
# elif IMC>=18.6 and IMC<=24.9:
#     print("peso normal")
# elif IMC>=25 and IMC<=29.9:
#     print("sobrepeso")
# elif IMC>30:
#     print("obesidade")

# q 2

# num = int(input("digite um numero"))
# for n in range(1, num+1):
#     if n%2==0:
#         print(f"{n} é par")
#     else:
#         print(f"{n} é impar")

# q 3 

# tabu=1
# num=int(input("fala um numero ai "))
# for n in range(1, 11):
#     tabu= num*n
#     print(f"{num}x{n}={tabu}")

# q 4

# cont=0
# num=int(input("digite um numero "))
# for n in range(1, num+1):
#     if num%n==0:
#         cont+=1
# if cont==2:
#     print(f"{num} é primo")
# else:
#     print(f"{num} não é primo")

# q 5

med=0
maior=0
menor=0
alunos=int(input("quantos alunos tem? "))
for a in range(1, alunos+1):
    nota=int(input(f"nota de {a}: "))
    med+=nota
    if nota>=6:
        maior+=1
    elif nota<6:
        menor+=1
med/=alunos
print(f"media geral: {med}")
print(f"alunos acima da média: {maior}")
print(f"alunos abaixo da média: {menor}")
