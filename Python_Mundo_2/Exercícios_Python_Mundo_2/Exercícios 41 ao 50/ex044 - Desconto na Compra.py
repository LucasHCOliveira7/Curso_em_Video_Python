# Crie um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Em até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

print('{:=^40}'.format(' \033[1;34mLOJA FERRAGENS MINEIRO\033[m '))

preço = float(input('Valor total da compra: '))
print('''FORMA DE PAGAMENTO
[1] À vista no dinheiro/cheque tem 10% de desconto!
[2] À vista no cartão tem 5% de desconto!
[3] Em até 2x no cartão o preço é normal!
[4] 3x ou mais no cartão terá um juros de 20%!''')
opção = int(input('Qual a forma de pagamento? '))

if opção == 1:
    total = preço - (preço * 10 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
elif opção == 2:
    total = preço - (preço * 5 / 100)
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
elif opção == 3:
    total = preço
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R$ {:.2f} \033[1;32mSEM JUROS!\033[m'.format(parcela))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
elif opção == 4:
    total = preço + (preço * 20 / 100)
    totalparc = int(input('Quantas parcelas: '))
    parcela = total / totalparc
    print('Sua compra será parcelada em {}x de R$ R$ {:.2f} \033[1;31mCOM JUROS!\033[m'.format(totalparc, parcela))
    print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final.'.format(preço, total))
else:
    total = 0
    print('\033[1;31mOpção inválida de pagamento! Tente novamente.\033[m')
