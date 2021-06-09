"""
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n
"""

def shapeArea(n):
    lateral = n + (n - 1)
    soma = lateral
    while lateral > 1:
        lateral = lateral - 2
        soma = soma + 2 * lateral
    return soma


# Testes
print(shapeArea(1)) # 1
print(shapeArea(2)) # 5    
print(shapeArea(3)) # 13
print(shapeArea(4)) # 25
