preço = float(input('Digite o preço do produto: R$ '))
desconto = preço * 0.05
preço_com_desconto = preço - desconto
print(f'O preço do produto com 5% de desconto é: R$ {preço_com_desconto:.2f}')