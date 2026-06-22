from datetime import date
nome = input('Qual é o seu nome?: ')
print('Olá', nome )
inicio = input('No que posso te ajudar hoje? (escolha algumas das seguintes tarefas para AI realizar: calcular números, falar a data de hoje, fazer a tabuada): ')
if inicio == 'contar numeros':
 numero = int(input('Digite um número: '))
 for i in range (1, numero + 1):
     print(i)
elif inicio == 'calcular numeros':
      num1 = float(input('Digite o primeiro numero: '))
      operador = input('Digite o operador (+,-,*,/): ')
      num2 = float(input('Digite o segundo numero: '))
    
      if operador == '+':
        print(num1 + num2)
      elif operador == '-':
        print(num1 - num2)
      elif operador == '*':
        print(num1 * num2)
      elif operador == '/':
         if num2 != 0:
          print(num1 / num2)
         else:
          print('Não é possivel dividir por 0 (Nem tente isso! >:(')
      else:
       print('operação inválida')
elif inicio == 'falar a data de hoje':
 hoje = date.today()
 print(f'{hoje.day}/{hoje.month}/{hoje.year}')
elif inicio == 'calcular minha idade atual':
    ano_nascimento = int(input('Digite o ano de seu nascimento: '))
    idade = 2026 - ano_nascimento
    print('Sua idade é: ', idade)
elif inicio == 'quero a tabuada':
    num = int(input('Digite um numero: '))
    
    for i in range (0,12):
     tabuada = num * i
     print(f'{num} X {i} é igual a: {tabuada}')
else:
    print('Ainda não aprendi essa função')