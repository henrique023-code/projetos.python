num1 = float(input("Digite o primeiro numero: "))
operacao = input('Digite a operação(+, -, *, /): ')
num2 = float(input("Digite o segundo número: "))

if operacao == '+':
  print(num1 + num2)
elif operacao == '-':
  print(num1 - num2)
elif operacao == '*':
  print(num1 * num2)
elif operacao == '/'
 if num2 != 0:
    print(num1 / num2)
 else:
    print('Não é possivel dividir por zero')
else:
    print('operação inválida')
