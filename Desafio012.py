print('========================================Desafio012============================================')
preco = float(input('Digite o preço do produto: '))
desc = preco*0.05
novoPreço = preco - desc

print('O preço é R${} e com desconto de 5% é R${:.2f}'.format(preco, novoPreço))