"""
Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.
"""

def adjacentElementsProduct(inputArray):
    
    """ (list) -> numeric
    Retorna o maior produto entre dois umeros da lista
    """
    m = []
    for i in range(1, len(inputArray)):
        m.append( inputArray[i - 1] * inputArray[i] )
    
    return max(m)

    
# Testes
print(adjacentElementsProduct([3, 6, -2, -5, 7, 3]))        # 21
print(adjacentElementsProduct([2, 6, 10]))                  # 60
