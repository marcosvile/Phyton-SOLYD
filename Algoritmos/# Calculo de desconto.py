# Calculo de desconto
# Algoritmo que pretende calcular o desconto sobre o valor de compra de mercadorias, 
# seguindo o critério:
# Se  o cliente comprar entre R$500 e R$1000 ele ganha um desconto de 5% sobre o valor de compra.
# Caso o cliente compre mais do que R$1000 ele recebe um desconto de 10%.
# O algoritmo informa, o valor da compra com desconto, e troco.

# Açougue do python

print("###########################################")
print("CALCULADORA DE DESCONTO - AÇOUGUE DO PYTHON")
print("###########################################")

preco = float(input("qual o valor a ser pago: "))
pago = float(input("insira o pagamento: "))

cinco_per = preco - (preco*5/100)
dez_per = preco - (preco *10/10)

if preco >= 500:
    print("voce ganhou 5%" "de desconto: ")
    print("valor a pagar: ",cinco_per)
    print("seu troco é: ", pago - cinco_per)

    
elif preco >= 1000:
    print ("você ganhou 10%" "de desconto: ", dez_per)
    print("seu troco é: ", pago - dez_per)


else:
    print("valor a pagar: ", preco)
    print("seu troco é: ", pago - preco)
