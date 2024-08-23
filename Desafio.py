#Entre com o nome do usuário
user = input("Digite seu nome:")
if user.isdigit():
    print("Você digitou o nome errado!")
    exit()
elif user.isspace():
    print("Verifique se seu nome foi digitado corretamente.")
    exit()
elif len(user) == 0:
    print("Verifique se seu nome foi digitado corretamente.")
    exit()
#elif user.isprintable():
    #print("Não é permitido caracter especial no nome.")
    #exit()

#Entre com o salário do usuário
salario = float(input("Digite seu salário:"))
try:
    if salario <= 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")
    exit()
#Entre com o bonus do usuário
bonus_user = float(input("Digite sue bônus:"))
try:
    if bonus_user <= 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")
    exit()

#Variável que será alterado anualmente
percent = 1000
#Cálculo do KPI final
bonus_final = percent + salario*bonus_user
try:
    if percent <= 0:
        print("Atenção, o valor da variável anual PERCENT deve ser maior que 0")
        exit()
except ValueError:
    exit()

#Mensagem final
print(f"Olá {user}, o seu bônus foi de {bonus_final}.")