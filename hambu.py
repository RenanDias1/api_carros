numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    ehVegano = input().lower()
    
    if ehVegano == "s":
      ehVegano = True
      prato_vegano = f"Pedido {i}: {prato} (Vegano) - {calorias} calorias"
      print(prato_vegano)
      
    elif ehVegano == "n":
      ehVegano = False
      prato_naoVegano = f"Pedido {i}: {prato} (Nao-vegano) - {calorias} calorias"
      print(prato_naoVegano)