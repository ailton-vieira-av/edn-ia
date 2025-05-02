preco = 3890 #valor do produto
desconto = 10 #valor do desconto

valor_final = preco - (preco * desconto / 100) #formula do desconto
print(f"\nO preço do celular de Joana con {desconto}% de desconto é R$ {valor_final}")